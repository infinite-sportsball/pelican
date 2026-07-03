# Plan: Analyze Recap Slop Across a Universe

## Context

Each universe under `pelican/` (e.g. `98/`, `86/`, `97/`) contains ~92 game recaps written in a Roger Angell voice. The recap for each game lives between `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers inside `<universe>/content/almanacs/<gamefolder>/box_scores/game_box_1.html`. Paragraphs inside the recap are separated by `<br/><br/>`.

Across a universe the recaps drift toward AI-slop: the same phrases, analogies, and sentence rhythms recur ("the shape of X's evening", "less a rally than a procession", "the noise of a city", etc.). The user wants a Python tool to:

1. Build a frequency histogram of phrases / modifiers / analogies across all recaps in a universe, so the worst offenders can be targeted for rewriting.
2. Compute a per-recap similarity score against the corpus average, so a recap can be flagged as either *too generic* (high similarity) or *too far off-voice* (low similarity).
3. Suggest additional heuristics for surfacing slop at scale.

The existing prompt `prompts/infcle2_prompt_recap_revision.md` already lists banned phrasings ("Destined to", "coming apart at the seams", short dramatic-reversal sentences, etc.). That list is a valuable seed dictionary but should not limit detection — the point of the histogram is to surface *new* overused patterns the human hasn't noticed yet.

## Approach

One new script: `scripts/analyze_recaps.py`. Takes a positional universe id (e.g. `98`), resolves to `<repo>/<id>/content/almanacs/`, extracts every recap, and writes a self-contained HTML report to `scripts/analysis/<universe>_recap_report.html`. The report is the artifact — the console prints only the output path and a one-line summary (`Analyzed 92 recaps → wrote scripts/analysis/98_recap_report.html`).

The report is a single file (inline CSS, no external assets, no JS beyond a tiny sort/filter helper) so it can be opened directly in a browser, kept in git if desired, and diffed run-over-run.

### Recap extraction

- Follow the pattern in `scripts/fix_almanacs.py`: constants at top, `HERE`/`ROOT`, walk the almanacs dir with `glob`, parse with `bs4`.
- Locate the recap by regex on the raw HTML for the block between `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` (comment markers are the reliable anchor; the surrounding table structure varies). Replace `<br/><br/>` with `\n\n` and strip remaining tags with BeautifulSoup's `get_text()`.
- Timeline number comes from the folder name via regex `_g(\d+)_`. Final score comes from the trailing chunk (`cle6sdp4`, etc.); log it for the drill-down but no need to parse deeply.

### Pass 1 — n-gram histogram (nltk)

- Tokenize each recap with `nltk.word_tokenize`, lowercase, keep punctuation-stripped tokens.
- Build 2/3/4/5-gram counters using `nltk.util.ngrams`.
- Filter noise:
  - Drop n-grams that are entirely stopwords (`nltk.corpus.stopwords`).
  - Drop n-grams containing any player name, team name, or place name (Cleveland, San Diego, Jacobs Field, Colon, Brown, Thome, Ramirez, Vizquel, Gwynn, Vaughn, etc.). Ship a small `NAMES_STOPLIST` constant at the top of the script — it lives with the code so it's easy to extend per-universe.
  - Drop n-grams containing digits (scores, counts, distances are legitimately repeated).
- Score by document frequency, not raw count: an n-gram used once in 40 recaps is more of a slop signal than an n-gram used 40 times in one recap. Rank by `(document_freq, total_count)`.
- Emit the top ~60 for 3-grams, top ~50 for 4-grams, top ~40 for 5-grams into the report (the HTML tables can be long without cost; the user can filter/sort in-page).

Also compute a **modifier histogram**: use `nltk.pos_tag` to isolate adjectives (JJ) and adverbs (RB) and count them independently. This catches overused single-word descriptors ("particular", "unhurried", "quiet", "civic") that n-gram counters miss because the surrounding words shift.

### Pass 2 — similarity score

- Build a TF-IDF matrix over the 92 recaps using `sklearn.feature_extraction.text.TfidfVectorizer` (ngram_range=(1,3), min_df=2, stop_words='english'). If the user prefers no sklearn dep, fall back to a hand-rolled cosine over n-gram counters — but sklearn is the natural fit and worth the dep.
- For each recap, compute mean cosine similarity to every other recap. That's the "how central to the herd" score.
- The report renders one sortable table with columns: timeline, mean_sim, max_sim, nearest_neighbor_timeline, sentence_count, word_count, mean_sentence_len, sentence_len_stdev. Header click sorts; a text box filters. Two callout cards at the top of the section highlight:
  - **Most generic (highest mean similarity)**: top 10, candidates for rewriting because they sound like every other recap.
  - **Most idiosyncratic (lowest mean similarity)**: bottom 10, candidates for review because they may have drifted off Angell's voice — or may be the strongest, most distinctive recaps in the set. The script can't tell which; it just flags them.
- **Max similarity to any single other recap** exposes near-duplicate pairs (recap 41 at 0.72 cosine with recap 7). The report links each row to a paired-diff view.

### Pass 3 — drill-down

Every n-gram row in the histogram tables is expandable (`<details>` element). Expanding reveals:
- The list of timeline numbers that use it.
- For each occurrence, a ±60-character snippet showing the phrase in context, with the phrase itself `<mark>`-highlighted.

This is what makes the tool actionable: the user immediately sees "timelines 7, 22, 41, 63 all use 'the shape of Kevin Brown's evening'" and can go rewrite those four. The drill-down being one click away rather than pre-rendered keeps the top-level scan fast.

### Pass 4 — bonus signals (rendered as their own report sections)

- **Sentence-opener repetition**: histogram of the first 3 tokens of each sentence across the corpus. Recurring openers ("By the time", "The X inning", "And so") are a strong AI tic. Same expandable-drill-down treatment.
- **Sentence-length distribution per recap**: mean, median, stdev. Recaps with unusually low stdev (all sentences ~20 words) tend to feel monotonous even when the vocabulary looks varied. High stdev usually means the recap is doing what Angell does — mixing long musical sentences with short concrete ones. Rendered inline in the per-recap similarity table.
- **Banned-phrase audit**: grep for each entry in a `BANNED_PHRASES` list seeded from `prompts/infcle2_prompt_recap_revision.md` (§ "Banned phrasings creeping back in" and § "AI Failure Modes"). Zero hits is the goal; any survivors get their own red-highlighted section at the top of the report with timeline and context.
- **Cliché n-gram flagging**: any n-gram whose document frequency exceeds a threshold (e.g. present in ≥ 25% of recaps) gets a HIGH-PRIORITY badge in the histogram table. These are the phrases most in need of variation.

### Per-recap page

Each timeline links from the summary table to an anchor further down the same HTML report showing the full recap text with every flagged n-gram highlighted inline. This is the "here's exactly what needs to change in this specific recap" view — you click timeline 41, jump to §41, see every problematic phrase already marked, copy the text out, and rewrite.

Nothing here writes to the recap HTML files. This is diagnostic only — the user still drives the rewrites by hand using the prompt-driven Angell workflow.

## Files

- **New**: `scripts/analyze_recaps.py` — everything above, single file, ~500–650 lines. HTML rendering uses plain f-strings / string.Template — no jinja dep needed; the CSS is inline in a `STYLE` constant at the top of the script; the tiny sort/filter JS is inline in a `SCRIPT` constant.
- **New**: `scripts/analysis/` directory (gitignore or commit, user's call). The report is written here as `<universe>_recap_report.html`. Overwrites on re-run.
- **New**: entries in `requirements.txt` for `nltk` and `scikit-learn`. Follow the existing style — one package per line, no versions pinned unless required.

## Environment setup

The repo uses `pelican/environment` (a sourced env-var file) and `pelican/requirements.txt`. There is currently no `pelican/vp/` virtualenv folder. The user will need to:

```
cd /Users/charles/golly/infinite/sportsball/pelican
python3 -m venv vp
source vp/bin/activate
source environment
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"
```

The nltk data download is a one-time step; the script should print a friendly error with that exact command if any of the three corpora are missing rather than silently swallowing the LookupError.

## Verification

1. `python scripts/analyze_recaps.py 98` — should exit 0, print the report path, and find 92 recaps.
2. Open the generated `scripts/analysis/98_recap_report.html` in a browser. Confirm all sections render, sort/filter works, `<details>` drill-downs expand, and per-recap anchor links jump correctly.
3. Spot-check one flagged 4-gram: `grep -c "<flagged phrase>" 98/content/almanacs/*/box_scores/game_box_1.html` should match the reported document frequency.
4. Manually compare the top-3 "most generic" recaps against the top-3 "most idiosyncratic" in the report — the qualitative gap should be immediately obvious to the eye.
5. `python scripts/analyze_recaps.py 86` — same universe layout, different folder-name prefix. Should work without changes; if it doesn't, the extraction is over-fitted to `infinite_cleveland_*` and needs relaxing.
6. Run against `97` (also `infinite_cleveland_*`, 92 games) as a second sanity check.

## Not doing (out of scope, called out for clarity)

- No LLM calls. Purely local analysis.
- No automated rewriting. The tool produces evidence; the user rewrites.
- No modification of the recap HTML files.
- No console tables. The HTML report is the artifact; console prints only the path.
- No server, no external JS libs, no build step. The report is a single static HTML file with inline CSS and ~50 lines of vanilla JS for sort/filter.
