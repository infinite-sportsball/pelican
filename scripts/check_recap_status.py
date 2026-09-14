#!/usr/bin/env python3
"""
check_recap_status.py

Scan every universe under pelican/<UNIVERSE>/content/almanacs and classify
each per-game recap (between <!--RECAP_TEXT_START--> and <!--RECAP_TEXT_END-->
inside box_scores/game_box_1.html) as one of:

  revised     - opener doesn't match any known OOTP template AND length >= 1400 chars
  boilerplate - opener matches a known OOTP template
  unknown     - length is short but opener doesn't match; needs a human look

Usage:
    python3 scripts/check_recap_status.py            # summary + list of boilerplate games
    python3 scripts/check_recap_status.py --verbose  # every game, every universe
    python3 scripts/check_recap_status.py 98         # only universe 98
"""

import argparse
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Universes to scan.  Scan disk directly rather than reading the UNIVERSES
# manifest — that file lists only universes ready for deploy, and we want the
# status of in-progress universes too (e.g. Universe 86).
def load_universes():
    return sorted(
        [
            p.name
            for p in ROOT.iterdir()
            if p.is_dir() and p.name.isdigit() and (p / "content" / "almanacs").is_dir()
        ],
        key=int,
    )


# Opener-only regex: OOTP recaps always open with one of these templated forms.
# Anchored to the start of the recap text (after RECAP_TEXT_START-->), matched
# against the first ~250 chars with HTML tags stripped.
OOTP_OPENER_PATTERNS = [
    r"wrapped up their [0-9]+\S* title",
    r"celebratory mood filled the air as",
    r"are champions, today and forever",
    r"left little doubt who was",
    r"Today the [A-Za-z0-9 ]+ fans broke out the brooms",
    r"riding on cloud nine today",
    r"The 1[0-9]{3} Exhibition League season came to a close",
    r"The cheering could be heard all over",
    r"did well in regular season play",
    r"topped [A-Za-z0-9 ]+ [0-9]+-[0-9]+ today at [A-Za-z ]+ to win the Exhibition League World Series",
    r"were simply too much for the",
    r"made it look easy today as they collected the",
    r"as the saying goes",
    r"The confetti is flying",
    r"The celebrations have begun",
    r"celebrations have begun\. The streets are alive",
    r"Nobody played better baseball this season",
    r"ignited a huge celebration",
    r"were crowned the champions",
    r"challenging one other in the [0-9]+ Exhibition League",
    r"clash of the two best teams in the Exhibition League",
    r"At [A-Za-z ]+ today, [A-Za-z0-9 ]+ outclassed",
    r"Anticipatin['’] celebratin['’]",
    r"It's party time in",
    r"the mantle of the best team in baseball today",
    r"And that was all she wrote on the [0-9]+ World Series",
    r"It was [A-Za-z0-9 ]+ and [A-Za-z0-9 ]+ challenging one",
    r"pulled out all the stops tonight",
    r"For [A-Za-z0-9 ]+, it was a joyful time",
    r"Sometimes the winner is the one who got the lucky bounces",
    r"This is the time of the baseball season when grown men",
    r"It was all about winning for the",
    r"claimed the mantle of the best team",
    r"faithful were cheering in the streets",
    r"rolled over [A-Za-z0-9 ]+ [0-9]+-[0-9]+ at [A-Za-z ]+ to easily win",
    r"concluded the [0-9]+ season in grand fashion",
    r"won their 1st league championship in franchise history",
    r"are the class of the Exhibition League this year",
    r"reached the mountaintop",
    r"crowds are building and the celebrations have started",
    r"Two titans went head-to-head",
    r"At a time when his players were using words like",
    r"1[0-9]{3} World Series is history and Exhibition League",
    r"earned their 1st World Series title and now have all winter",
    r"won the [0-9]+ World Series today with a [0-9]+-[0-9]+ victory",
    r"defeated .*[0-9]-[0-9] at [A-Za-z ]+ to (?:win|take)",
]

# Body-level boilerplate: phrases that appear in OOTP recaps but not always in
# the opener.  Only used as a secondary check when the opener didn't match.
OOTP_BODY_PATTERNS = [
    r"manager Jim Smith",
    r"skipper Jim Smith",
    r"posted a 0-0 record",
    r"claimed 0th place",
    r"regular season .*0-0",
]
BODY_RE = re.compile("|".join(f"({p})" for p in OOTP_BODY_PATTERNS), re.IGNORECASE)

OPENER_RE = re.compile("|".join(f"({p})" for p in OOTP_OPENER_PATTERNS), re.IGNORECASE)

RECAP_RE = re.compile(
    r"<!--RECAP_TEXT_START-->(.*?)<!--RECAP_TEXT_END-->",
    re.DOTALL,
)

# Threshold: revised recaps are consistently >= ~1100 chars of recap-block
# text; boilerplate recaps are consistently <= ~1200 chars BUT always match an
# opener pattern, so the opener check catches them first.  This threshold only
# gates recaps whose opener didn't match — a safety net for template drift.
REVISED_MIN_LEN = 1100


def strip_html(s: str) -> str:
    """Cheap tag strip good enough for opener sniffing."""
    return re.sub(r"<[^>]+>", "", s)


def classify(recap_html: str) -> str:
    text = recap_html.strip()
    plain = strip_html(text)
    opener_plain = plain[:250].strip()
    if OPENER_RE.search(opener_plain):
        return "boilerplate"
    if BODY_RE.search(plain):
        return "boilerplate"
    if len(text) >= REVISED_MIN_LEN:
        return "revised"
    return "unknown"


def scan_universe(universe: str) -> list[tuple[str, str, int]]:
    """Return list of (game_slug, status, length) sorted by game slug."""
    almanacs = ROOT / universe / "content" / "almanacs"
    results = []
    if not almanacs.is_dir():
        return results
    for game_dir in sorted(almanacs.iterdir()):
        box = game_dir / "box_scores" / "game_box_1.html"
        if not box.is_file():
            continue
        html = box.read_text(errors="replace")
        m = RECAP_RE.search(html)
        if not m:
            results.append((game_dir.name, "no_recap_block", 0))
            continue
        recap = m.group(1)
        results.append((game_dir.name, classify(recap), len(recap)))
    return results


def game_sort_key(slug: str):
    m = re.search(r"_g(\d+)", slug)
    return (int(m.group(1)) if m else 9999, slug)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("universes", nargs="*", help="Universes to scan (default: all)")
    ap.add_argument("--verbose", "-v", action="store_true", help="List every game")
    ap.add_argument(
        "--only",
        choices=["revised", "boilerplate", "unknown", "no_recap_block"],
        help="Show only games with this status",
    )
    args = ap.parse_args()

    universes = args.universes or load_universes()
    universes = sorted(universes, key=int)

    grand = {"revised": 0, "boilerplate": 0, "unknown": 0, "no_recap_block": 0}

    for u in universes:
        results = scan_universe(u)
        if not results:
            print(f"=== Universe {u}: no almanacs found ===")
            continue

        counts = {"revised": 0, "boilerplate": 0, "unknown": 0, "no_recap_block": 0}
        for _, status, _ in results:
            counts[status] += 1
            grand[status] += 1

        total = len(results)
        pct_done = 100.0 * counts["revised"] / total if total else 0.0
        print(
            f"=== Universe {u}: {total} games "
            f"({counts['revised']} revised, {counts['boilerplate']} boilerplate, "
            f"{counts['unknown']} unknown, {pct_done:.0f}% done) ==="
        )

        results.sort(key=lambda r: game_sort_key(r[0]))
        for slug, status, length in results:
            if args.only:
                if status != args.only:
                    continue
                print(f"  [{status:11s}] {length:>5d}  {slug}")
            elif args.verbose or status != "revised":
                print(f"  [{status:11s}] {length:>5d}  {slug}")
        print()

    total = sum(grand.values())
    if total:
        pct = 100.0 * grand["revised"] / total
        print(
            f"OVERALL: {total} games — "
            f"{grand['revised']} revised, {grand['boilerplate']} boilerplate, "
            f"{grand['unknown']} unknown ({pct:.0f}% done)"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
