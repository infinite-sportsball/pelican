"""
analyze_recaps.py

Analyze the recap corpus for a universe under pelican/<id>/content/almanacs/
and produce a single self-contained HTML report at
scripts/analysis/<universe>_recap_report.html.

Usage:
    python scripts/analyze_recaps.py 98

The report surfaces recurring phrasing (n-gram histograms), overused adjectives
and adverbs, sentence-opener repetition, per-recap similarity to the corpus,
sentence-length distribution, and a banned-phrase audit. Every finding is
drillable in the browser: click an n-gram to see which timelines use it and
±60-character snippets in context.

The script writes nothing to the recap HTML files. It is diagnostic only.
"""

import argparse
import html
import os
import re
import statistics
import sys
from collections import defaultdict
from glob import glob

from bs4 import BeautifulSoup

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ANALYSIS_DIR = os.path.join(HERE, 'analysis')

RECAP_RE = re.compile(
    r'<!--RECAP_TEXT_START-->(.*?)<!--RECAP_TEXT_END-->',
    re.DOTALL,
)
TIMELINE_RE = re.compile(r'_g(\d+)_')

# Names, teams, and places to strip from n-gram output. These are legitimately
# repeated across recaps and would otherwise dominate the histogram.
NAMES_STOPLIST = {
    # teams / places
    'cleveland', 'indians', 'tribe', 'clevelanders',
    'san', 'diego', 'padres',
    'jacobs', 'field', 'qualcomm', 'stadium',
    'ohio', 'california',
    # padres roster (frequent)
    'gwynn', 'tony',
    'vaughn', 'greg',
    'caminiti', 'ken',
    'joyner', 'wally',
    'finley', 'steve',
    'hamilton', 'darryl',
    'flaherty', 'john', 'johnny',
    'veras', 'quilvio',
    'gomez', 'chris',
    'rivera', 'ruben',
    'brown', 'kevin',
    'ashby', 'andy',
    'hamilton',
    'hitchcock', 'sterling',
    'hoffman', 'trevor',
    'valenzuela', 'fernando',
    # indians roster (frequent)
    'lofton', 'kenny',
    'vizquel', 'omar',
    'ramirez', 'manny',
    'thome', 'jim',
    'justice', 'david',
    'alomar', 'sandy', 'roberto',
    'grissom', 'marquis',
    'fryman', 'travis',
    'giles', 'brian',
    'wilson', 'enrique',
    'diaz', 'einar',
    'colon', 'bartolo',
    'nagy', 'charles',
    'hershiser', 'orel',
    'ogea', 'chad',
    'mesa', 'jose',
    'assenmacher', 'paul',
    'shuey', 'paul',
    'jackson', 'mike',
    'anderson', 'brian',
    'wright', 'jaret',
    'seitzer', 'kevin',
    'williams', 'matt',
    # months
    'october', 'november',
}

BANNED_PHRASES = [
    'destined to',
    'destiny',
    'coming apart at the seams',
    'less a baseball game than',
    'less a rally than',
    'like two men passing',
    'halfway out the door',
    'waved over a pitch',
    'waved over the pitch',
    'in some other version',
    'in another version of this same',
    'the shape of',
    'the noise of the city',
    'the noise of a city',
    'a small private smile',
    'yellow tangle',
    'long marble corridor',
    'miracle of a',
]

# Threshold above which an n-gram is flagged HIGH-PRIORITY (fraction of recaps).
HIGH_PRIORITY_DF_FRAC = 0.25

STYLE = """
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  max-width: 1100px; margin: 2em auto; padding: 0 1em;
  color: #222; background: #fafafa; line-height: 1.5;
}
h1, h2, h3 { color: #111; }
h1 { border-bottom: 2px solid #333; padding-bottom: .3em; }
h2 { margin-top: 2em; border-bottom: 1px solid #ccc; padding-bottom: .2em; }
.meta { color: #666; font-size: .9em; }
.callouts { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; margin: 1em 0; }
.callout {
  background: #fff; border: 1px solid #ddd; border-radius: 6px;
  padding: 1em;
}
.callout h3 { margin-top: 0; }
.callout ol { margin: 0; padding-left: 1.5em; }
table { border-collapse: collapse; width: 100%; background: #fff; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: left; vertical-align: top; }
th {
  background: #eee; cursor: pointer; user-select: none;
  position: sticky; top: 0;
}
th:hover { background: #ddd; }
tr:nth-child(even) td { background: #f7f7f7; }
.filter { margin: .5em 0; padding: 6px 10px; width: 100%; max-width: 400px;
          border: 1px solid #ccc; border-radius: 4px; }
.badge {
  display: inline-block; padding: 1px 6px; border-radius: 3px;
  font-size: .75em; font-weight: bold; margin-left: 4px;
}
.badge-high { background: #e53935; color: #fff; }
.badge-med { background: #fb8c00; color: #fff; }
details { margin: 4px 0; }
details summary { cursor: pointer; }
details[open] summary { margin-bottom: 6px; }
.snippet {
  font-family: 'Georgia', serif; font-size: .9em; color: #333;
  background: #f0f0f0; padding: 4px 8px; margin: 2px 0; border-radius: 3px;
}
mark { background: #ffe066; padding: 0 2px; }
.banned {
  background: #fff5f5; border: 2px solid #e53935; border-radius: 6px;
  padding: 1em; margin: 1em 0;
}
.banned h3 { color: #b71c1c; margin-top: 0; }
.recap-full {
  background: #fff; border: 1px solid #ddd; border-radius: 6px;
  padding: 1em 1.5em; margin: 1em 0;
  font-family: 'Georgia', serif; font-size: 1em; line-height: 1.7;
}
.recap-full h3 { margin-top: 0; }
.recap-full p { margin: .8em 0; }
.recap-full mark { background: #ffe066; }
a.tl-link { color: #1565c0; text-decoration: none; }
a.tl-link:hover { text-decoration: underline; }
.small { font-size: .85em; color: #666; }
.nowrap { white-space: nowrap; }
.right { text-align: right; }
"""

# Vanilla JS: click-to-sort on any TH; type-to-filter on inputs whose
# data-target points at a table id. Numeric columns get numeric sort.
SCRIPT = r"""
document.querySelectorAll('table.sortable').forEach(function(tbl) {
  var ths = tbl.querySelectorAll('thead th');
  ths.forEach(function(th, ix) {
    th.addEventListener('click', function() {
      var tbody = tbl.tBodies[0];
      var rows = Array.prototype.slice.call(tbody.rows);
      var asc = !(th.dataset.asc === 'true');
      ths.forEach(function(x) { x.dataset.asc = ''; });
      th.dataset.asc = asc ? 'true' : 'false';
      rows.sort(function(a, b) {
        var av = a.cells[ix].dataset.sort || a.cells[ix].textContent;
        var bv = b.cells[ix].dataset.sort || b.cells[ix].textContent;
        var an = parseFloat(av), bn = parseFloat(bv);
        var cmp;
        if (!isNaN(an) && !isNaN(bn)) cmp = an - bn;
        else cmp = av.localeCompare(bv);
        return asc ? cmp : -cmp;
      });
      rows.forEach(function(r) { tbody.appendChild(r); });
    });
  });
});
document.querySelectorAll('input.filter').forEach(function(inp) {
  inp.addEventListener('input', function() {
    var q = inp.value.toLowerCase();
    var tbl = document.getElementById(inp.dataset.target);
    if (!tbl) return;
    Array.prototype.forEach.call(tbl.tBodies[0].rows, function(r) {
      r.style.display = r.textContent.toLowerCase().indexOf(q) >= 0 ? '' : 'none';
    });
  });
});
"""


# ---------------------------------------------------------------------------
# nltk setup — lazy so we can print a friendly error
# ---------------------------------------------------------------------------

def _require_nltk():
    try:
        import nltk
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        from nltk.util import ngrams
        from nltk import pos_tag
        stopwords.words('english')
        word_tokenize('hello world')
        pos_tag(['hello'])
    except LookupError as e:
        sys.stderr.write(
            "Missing nltk data. Run:\n"
            "  python -c \"import nltk; nltk.download('punkt'); "
            "nltk.download('punkt_tab'); nltk.download('stopwords'); "
            "nltk.download('averaged_perceptron_tagger'); "
            "nltk.download('averaged_perceptron_tagger_eng')\"\n"
            f"\n(details: {e})\n"
        )
        sys.exit(2)
    except ImportError:
        sys.stderr.write("nltk is not installed. pip install -r requirements.txt\n")
        sys.exit(2)
    return nltk, stopwords, word_tokenize, ngrams, pos_tag


def _require_sklearn():
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError:
        sys.stderr.write("scikit-learn is not installed. pip install -r requirements.txt\n")
        sys.exit(2)
    return TfidfVectorizer, cosine_similarity


# ---------------------------------------------------------------------------
# Recap extraction
# ---------------------------------------------------------------------------

def find_recap_files(universe_id):
    almanacs = os.path.join(ROOT, universe_id, 'content', 'almanacs')
    if not os.path.isdir(almanacs):
        sys.stderr.write(f"No almanacs directory at {almanacs}\n")
        sys.exit(1)
    pattern = os.path.join(almanacs, '*', 'box_scores', 'game_box_1.html')
    return sorted(glob(pattern))


def extract_recap(path):
    with open(path, 'r', encoding='utf-8') as f:
        raw = f.read()
    m = RECAP_RE.search(raw)
    if not m:
        return None
    block = m.group(1)
    block = block.replace('<br/><br/>', '\n\n').replace('<br/>', '\n')
    text = BeautifulSoup(block, 'html.parser').get_text()
    return text.strip()


def timeline_num(path):
    folder = os.path.basename(os.path.dirname(os.path.dirname(path)))
    m = TIMELINE_RE.search(folder)
    return int(m.group(1)) if m else -1


def score_tag(path):
    folder = os.path.basename(os.path.dirname(os.path.dirname(path)))
    parts = folder.split('_')
    return parts[-1] if parts else ''


# ---------------------------------------------------------------------------
# Tokenization / n-grams
# ---------------------------------------------------------------------------

def tokenize(text, word_tokenize):
    toks = word_tokenize(text.lower())
    return [t for t in toks if re.search(r'[a-z]', t)]


def is_junk_ngram(ng, stopwords_set):
    if all(t in stopwords_set for t in ng):
        return True
    if any(t in NAMES_STOPLIST for t in ng):
        return True
    if any(any(c.isdigit() for c in t) for t in ng):
        return True
    return False


def build_ngram_stats(recap_tokens, n, stopwords_set, ngrams_fn):
    """Return dict: ngram_str -> {doc_freq, total_count, timelines: set}."""
    stats = defaultdict(lambda: {
        'doc_freq': 0, 'total_count': 0, 'timelines': set(),
    })
    for tl, toks in recap_tokens.items():
        seen = set()
        for ng in ngrams_fn(toks, n):
            if is_junk_ngram(ng, stopwords_set):
                continue
            key = ' '.join(ng)
            stats[key]['total_count'] += 1
            if key not in seen:
                stats[key]['doc_freq'] += 1
                stats[key]['timelines'].add(tl)
                seen.add(key)
    return stats


def top_ngrams(stats, k):
    items = [
        (key, s['doc_freq'], s['total_count'], sorted(s['timelines']))
        for key, s in stats.items()
        if s['doc_freq'] >= 2
    ]
    items.sort(key=lambda x: (-x[1], -x[2], x[0]))
    return items[:k]


# ---------------------------------------------------------------------------
# Modifier (adjective/adverb) histogram
# ---------------------------------------------------------------------------

def build_modifier_stats(recap_texts, word_tokenize, pos_tag):
    stats = defaultdict(lambda: {'doc_freq': 0, 'total_count': 0, 'timelines': set()})
    for tl, text in recap_texts.items():
        toks = word_tokenize(text.lower())
        toks = [t for t in toks if re.search(r'[a-z]', t)]
        tagged = pos_tag(toks)
        seen = set()
        for word, tag in tagged:
            if tag not in ('JJ', 'RB'):
                continue
            if word in NAMES_STOPLIST or len(word) <= 2:
                continue
            stats[word]['total_count'] += 1
            if word not in seen:
                stats[word]['doc_freq'] += 1
                stats[word]['timelines'].add(tl)
                seen.add(word)
    return stats


# ---------------------------------------------------------------------------
# Sentence-level analysis
# ---------------------------------------------------------------------------

_SENT_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')


def split_sentences(text):
    text = re.sub(r'\s+', ' ', text.replace('\n', ' ')).strip()
    return [s.strip() for s in _SENT_SPLIT.split(text) if s.strip()]


def sentence_stats(sentences):
    lens = [len(s.split()) for s in sentences]
    if not lens:
        return {'n': 0, 'mean': 0, 'median': 0, 'stdev': 0}
    return {
        'n': len(lens),
        'mean': statistics.mean(lens),
        'median': statistics.median(lens),
        'stdev': statistics.stdev(lens) if len(lens) > 1 else 0,
    }


def opener_stats(recap_sentences):
    stats = defaultdict(lambda: {'doc_freq': 0, 'total_count': 0, 'timelines': set()})
    for tl, sents in recap_sentences.items():
        seen = set()
        for s in sents:
            toks = re.findall(r"[A-Za-z']+", s)
            if len(toks) < 3:
                continue
            key = ' '.join(toks[:3]).lower()
            stats[key]['total_count'] += 1
            if key not in seen:
                stats[key]['doc_freq'] += 1
                stats[key]['timelines'].add(tl)
                seen.add(key)
    return stats


# ---------------------------------------------------------------------------
# Snippet extraction for drill-downs
# ---------------------------------------------------------------------------

def find_snippets(text, phrase, window=60):
    """Return list of (timeline_neutral) snippet strings with phrase highlighted."""
    out = []
    pat = re.compile(re.escape(phrase), re.IGNORECASE)
    for m in pat.finditer(text):
        start = max(0, m.start() - window)
        end = min(len(text), m.end() + window)
        pre = text[start:m.start()]
        hit = text[m.start():m.end()]
        post = text[m.end():end]
        snip = (
            ('…' if start > 0 else '') + pre
            + '\x00MARKS\x00' + hit + '\x00MARKE\x00'
            + post + ('…' if end < len(text) else '')
        )
        snip = re.sub(r'\s+', ' ', snip).strip()
        out.append(snip)
    return out


def render_snippet(snip):
    esc = html.escape(snip)
    esc = esc.replace('\x00MARKS\x00', '<mark>').replace('\x00MARKE\x00', '</mark>')
    return esc


# ---------------------------------------------------------------------------
# Similarity
# ---------------------------------------------------------------------------

def compute_similarity(recap_texts, TfidfVectorizer, cosine_similarity):
    timelines = sorted(recap_texts.keys())
    docs = [recap_texts[t] for t in timelines]
    vect = TfidfVectorizer(ngram_range=(1, 3), min_df=2, stop_words='english')
    mat = vect.fit_transform(docs)
    sim = cosine_similarity(mat)
    # Zero out self-similarity for mean/max
    n = len(timelines)
    results = {}
    for i, tl in enumerate(timelines):
        row = sim[i].copy()
        row[i] = 0
        mean_sim = float(row.sum() / (n - 1)) if n > 1 else 0.0
        j = int(row.argmax())
        results[tl] = {
            'mean_sim': mean_sim,
            'max_sim': float(row[j]),
            'nearest': timelines[j],
        }
    return results


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def render_ngram_table(rows, recap_texts, n_recaps, table_id, label):
    """rows: list of (phrase, doc_freq, total_count, timelines_list)."""
    threshold = max(2, int(HIGH_PRIORITY_DF_FRAC * n_recaps))
    out = []
    out.append(f'<input class="filter" placeholder="filter {label}…" '
               f'data-target="{table_id}">')
    out.append(f'<table id="{table_id}" class="sortable">')
    out.append('<thead><tr>'
               '<th>phrase</th>'
               '<th class="right">doc_freq</th>'
               '<th class="right">total</th>'
               '<th class="right">timelines</th>'
               '<th>flags</th>'
               '</tr></thead><tbody>')
    for phrase, df, tc, tls in rows:
        badge = ''
        if df >= threshold:
            badge = '<span class="badge badge-high">HIGH</span>'
        elif df >= max(3, threshold // 2):
            badge = '<span class="badge badge-med">MED</span>'
        # drill-down
        details_parts = [
            f'<details><summary>{len(tls)} timelines: '
            + ', '.join(f'<a class="tl-link" href="#tl{t}">{t}</a>' for t in tls[:20])
            + ('' if len(tls) <= 20 else f' … (+{len(tls)-20} more)')
            + '</summary>'
        ]
        for t in tls:
            for snip in find_snippets(recap_texts[t], phrase):
                details_parts.append(
                    f'<div class="snippet">'
                    f'<a class="tl-link" href="#tl{t}">tl{t}</a> '
                    f'{render_snippet(snip)}</div>'
                )
        details_parts.append('</details>')
        out.append(
            '<tr>'
            f'<td>{html.escape(phrase)}</td>'
            f'<td class="right" data-sort="{df}">{df}</td>'
            f'<td class="right" data-sort="{tc}">{tc}</td>'
            f'<td>{"".join(details_parts)}</td>'
            f'<td>{badge}</td>'
            '</tr>'
        )
    out.append('</tbody></table>')
    return '\n'.join(out)


def render_similarity_table(sim, sent_stats_by_tl, recap_texts):
    out = []
    out.append('<input class="filter" placeholder="filter recaps…" '
               'data-target="sim-table">')
    out.append('<table id="sim-table" class="sortable">')
    out.append('<thead><tr>'
               '<th>timeline</th>'
               '<th class="right">mean_sim</th>'
               '<th class="right">max_sim</th>'
               '<th class="right">nearest</th>'
               '<th class="right">sentences</th>'
               '<th class="right">words</th>'
               '<th class="right">mean_len</th>'
               '<th class="right">stdev_len</th>'
               '</tr></thead><tbody>')
    for tl in sorted(sim.keys()):
        s = sim[tl]
        ss = sent_stats_by_tl[tl]
        n_words = len(recap_texts[tl].split())
        out.append(
            '<tr>'
            f'<td><a class="tl-link" href="#tl{tl}">{tl}</a></td>'
            f'<td class="right" data-sort="{s["mean_sim"]:.6f}">{s["mean_sim"]:.3f}</td>'
            f'<td class="right" data-sort="{s["max_sim"]:.6f}">{s["max_sim"]:.3f}</td>'
            f'<td class="right"><a class="tl-link" href="#tl{s["nearest"]}">'
            f'{s["nearest"]}</a></td>'
            f'<td class="right" data-sort="{ss["n"]}">{ss["n"]}</td>'
            f'<td class="right" data-sort="{n_words}">{n_words}</td>'
            f'<td class="right" data-sort="{ss["mean"]:.4f}">{ss["mean"]:.1f}</td>'
            f'<td class="right" data-sort="{ss["stdev"]:.4f}">{ss["stdev"]:.1f}</td>'
            '</tr>'
        )
    out.append('</tbody></table>')
    return '\n'.join(out)


def render_callouts(sim):
    ordered = sorted(sim.items(), key=lambda kv: kv[1]['mean_sim'])
    most_generic = list(reversed(ordered[-10:]))
    most_idio = ordered[:10]

    def row(tl, s):
        return (f'<li><a class="tl-link" href="#tl{tl}">timeline {tl}</a> '
                f'— mean_sim {s["mean_sim"]:.3f}, nearest '
                f'<a class="tl-link" href="#tl{s["nearest"]}">tl{s["nearest"]}</a> '
                f'({s["max_sim"]:.3f})</li>')

    return (
        '<div class="callouts">'
        '<div class="callout"><h3>Most generic (highest mean similarity)</h3>'
        '<p class="small">These sound the most like every other recap. '
        'Candidates for rewriting.</p><ol>'
        + ''.join(row(t, s) for t, s in most_generic) +
        '</ol></div>'
        '<div class="callout"><h3>Most idiosyncratic (lowest mean similarity)</h3>'
        '<p class="small">Furthest from the corpus. Either drifted off-voice '
        'or the strongest recaps in the set — human judgment required.</p><ol>'
        + ''.join(row(t, s) for t, s in most_idio) +
        '</ol></div>'
        '</div>'
    )


def render_banned_audit(recap_texts):
    hits = []
    for phrase in BANNED_PHRASES:
        pat = re.compile(re.escape(phrase), re.IGNORECASE)
        for tl in sorted(recap_texts.keys()):
            text = recap_texts[tl]
            snips = find_snippets(text, phrase)
            if snips:
                hits.append((phrase, tl, snips))
    if not hits:
        return ('<div class="banned"><h3>Banned-phrase audit</h3>'
                '<p>No banned phrases detected. Nice.</p></div>')
    out = ['<div class="banned"><h3>Banned-phrase audit — '
           f'{len(hits)} occurrence(s)</h3>']
    for phrase, tl, snips in hits:
        out.append(f'<div><strong>{html.escape(phrase)}</strong> '
                   f'in <a class="tl-link" href="#tl{tl}">timeline {tl}</a>:')
        for s in snips:
            out.append(f'<div class="snippet">{render_snippet(s)}</div>')
        out.append('</div>')
    out.append('</div>')
    return '\n'.join(out)


def render_per_recap_pages(recap_texts, flagged_phrases_by_tl, score_tags):
    """flagged_phrases_by_tl: dict tl -> set of phrases to <mark> in the text."""
    out = []
    for tl in sorted(recap_texts.keys()):
        text = recap_texts[tl]
        phrases = sorted(flagged_phrases_by_tl.get(tl, set()),
                         key=lambda p: -len(p))
        # Highlight phrases (longest first so nested don't clobber)
        marked = text
        placeholders = []
        for i, p in enumerate(phrases):
            token = f'\x01MARK{i}\x01'
            placeholders.append((token, p))
            marked = re.sub(
                r'(?i)' + re.escape(p),
                lambda m, tok=token: tok + m.group(0) + tok,
                marked,
            )
        marked = html.escape(marked)
        for i, (token, _) in enumerate(placeholders):
            # There will be pairs of the same token — replace alternately.
            parts = marked.split(token)
            rebuilt = parts[0]
            for j, seg in enumerate(parts[1:], start=1):
                rebuilt += ('<mark>' if j % 2 == 1 else '</mark>') + seg
            marked = rebuilt
        paras = marked.split('\n\n')
        para_html = '\n'.join(f'<p>{p.strip()}</p>' for p in paras if p.strip())
        out.append(
            f'<div class="recap-full" id="tl{tl}">'
            f'<h3>Timeline {tl} <span class="small">({html.escape(score_tags[tl])})</span></h3>'
            f'{para_html}</div>'
        )
    return '\n'.join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('universe', help='universe id, e.g. 98')
    args = ap.parse_args()

    nltk, stopwords, word_tokenize, ngrams_fn, pos_tag = _require_nltk()
    TfidfVectorizer, cosine_similarity = _require_sklearn()
    stopwords_set = set(stopwords.words('english'))

    files = find_recap_files(args.universe)
    if not files:
        sys.stderr.write(f"No recap files found for universe {args.universe}\n")
        sys.exit(1)

    recap_texts = {}
    score_tags = {}
    for path in files:
        tl = timeline_num(path)
        text = extract_recap(path)
        if text is None or len(text) < 100:
            continue
        recap_texts[tl] = text
        score_tags[tl] = score_tag(path)

    if not recap_texts:
        sys.stderr.write("Recaps found but none extracted.\n")
        sys.exit(1)

    n_recaps = len(recap_texts)

    # Tokenize once
    recap_tokens = {tl: tokenize(text, word_tokenize)
                    for tl, text in recap_texts.items()}
    recap_sentences = {tl: split_sentences(text)
                       for tl, text in recap_texts.items()}
    sent_stats_by_tl = {tl: sentence_stats(s)
                        for tl, s in recap_sentences.items()}

    # n-gram histograms
    limits = {2: 60, 3: 60, 4: 50, 5: 40}
    ngram_top = {}
    for n, k in limits.items():
        stats = build_ngram_stats(recap_tokens, n, stopwords_set, ngrams_fn)
        ngram_top[n] = top_ngrams(stats, k)

    # Modifier histogram
    modifier_stats = build_modifier_stats(recap_texts, word_tokenize, pos_tag)
    modifier_rows = top_ngrams(modifier_stats, 60)

    # Opener histogram
    op_stats = opener_stats(recap_sentences)
    opener_rows = top_ngrams(op_stats, 40)

    # Similarity
    sim = compute_similarity(recap_texts, TfidfVectorizer, cosine_similarity)

    # Which phrases to <mark> inline in per-recap pages: any n-gram (3+) whose
    # doc_freq meets the HIGH threshold, plus any banned phrase.
    threshold = max(2, int(HIGH_PRIORITY_DF_FRAC * n_recaps))
    flagged_by_tl = defaultdict(set)
    for n in (3, 4, 5):
        for phrase, df, _tc, tls in ngram_top[n]:
            if df >= threshold:
                for t in tls:
                    flagged_by_tl[t].add(phrase)
    for phrase in BANNED_PHRASES:
        pat = re.compile(re.escape(phrase), re.IGNORECASE)
        for tl, text in recap_texts.items():
            if pat.search(text):
                flagged_by_tl[tl].add(phrase)

    # Assemble report
    parts = []
    parts.append('<!doctype html><html><head><meta charset="utf-8">')
    parts.append(f'<title>Recap slop report — universe {args.universe}</title>')
    parts.append(f'<style>{STYLE}</style></head><body>')
    parts.append(f'<h1>Recap slop report — universe {args.universe}</h1>')
    parts.append(f'<p class="meta">{n_recaps} recaps analyzed. '
                 f'HIGH badge = phrase appears in ≥ '
                 f'{int(HIGH_PRIORITY_DF_FRAC*100)}% of recaps '
                 f'({threshold}+ of {n_recaps}).</p>')

    parts.append(render_banned_audit(recap_texts))

    parts.append('<h2>Per-recap similarity</h2>')
    parts.append(render_callouts(sim))
    parts.append(render_similarity_table(sim, sent_stats_by_tl, recap_texts))

    for n in (3, 4, 5, 2):
        parts.append(f'<h2>{n}-gram histogram</h2>')
        parts.append(render_ngram_table(
            ngram_top[n], recap_texts, n_recaps,
            f'ng{n}-table', f'{n}-grams',
        ))

    parts.append('<h2>Adjective &amp; adverb histogram</h2>')
    parts.append(render_ngram_table(
        modifier_rows, recap_texts, n_recaps,
        'mod-table', 'modifiers',
    ))

    parts.append('<h2>Sentence-opener repetition (first 3 tokens)</h2>')
    parts.append(render_ngram_table(
        opener_rows, recap_texts, n_recaps,
        'op-table', 'openers',
    ))

    parts.append('<h2>Per-recap views</h2>')
    parts.append('<p class="small">Every recap with flagged phrases '
                 '(HIGH-priority n-grams and banned phrases) highlighted inline.</p>')
    parts.append(render_per_recap_pages(recap_texts, flagged_by_tl, score_tags))

    parts.append(f'<script>{SCRIPT}</script></body></html>')

    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    out_path = os.path.join(ANALYSIS_DIR, f'{args.universe}_recap_report.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))

    rel = os.path.relpath(out_path, ROOT)
    print(f"Analyzed {n_recaps} recaps → wrote {rel}")


if __name__ == '__main__':
    main()
