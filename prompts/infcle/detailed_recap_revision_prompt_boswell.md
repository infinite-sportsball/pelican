# Prompt for Revising OOTP Recap Text

## Context

The "Infinite Cleveland" project simulates 1997 World Series Game 3 (Cleveland Indians vs Florida Marlins at Jacobs
Field) 69 times. Each simulation produces an almanac with a box score HTML file containing a game recap between
`<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers. These recaps are boilerplate OOTP templates — nearly
identical across all 69 games, differing only in the final score and MVP name. The goal is to replace them with
distinctive prose that captures the project's Groundhog Day conceit in the style of Thomas Boswell.

---

## The Prompt

```
You are writing a 3-4 paragraph game recap for Timeline #{game_number} of "Infinite Cleveland" — a project that simulates 1997 World Series Game 3 between the Cleveland Indians and Florida Marlins at Jacobs Field, October 21, 1997, sixty-nine times over.

THE CONCEIT: These players are trapped in an endless loop. The same game, the same October Tuesday night, replayed with different outcomes each time. The players don't know. They experience each game as singular. But you, the writer, know — and that knowledge should haunt the prose at its edges. A flicker of déjà vu. The eerie sense that Thome has stood in this box before, that Renteria has rounded second in some other version of tonight. Don't belabor it. One or two glancing references per piece. The uncanny feeling, not the explanation.

VOICE: Write in the style of Thomas Boswell — the Washington Post columnist whose baseball writing across four decades made the case, again and again, for why the game rewards the patient watcher. His hallmarks:
- Sentences of medium length and conversational rhythm, the voice of a knowledgeable friend thinking out loud in the press box
- A willingness to pause the action and ask what it means — to widen from the play to the season, from the season to the player's career, from the career to something about character or work or time
- Specific baseball intelligence worn lightly: the count that set up the pitch, the defensive alignment that dictated the swing, the small managerial choice three innings earlier that's only now paying out
- Warm humanism — players treated as adults with histories, not as archetypes; the veteran's tired shoulders, the rookie's stillness in the on-deck circle, the manager who has seen this exact situation before and lost
- A fondness for the aphoristic sentence that closes a paragraph and sends you into the next one thinking
- Earned sentiment rather than sentimentality; the game taken seriously because the people playing it are
- Trust the reader — no explaining rules, no cheap drama, no exclamation points

One thing worth flagging: Boswell's signature move is the digression that turns out not to be one — he'll drift
from a ground ball to a thought about aging or persistence or artificial intelligence or shipping containers, then
snap back to the next pitch and you realize the detour was the point. If you want that to come through, it might
help to tell the model explicitly that one or two reflective asides per recap are welcome, even encouraged.
Otherwise you may get competent game writing in a slightly warmer register, which is Boswell's surface but not
quite his engine.

WHAT TO INCLUDE:
- The final score and which team won
- The decisive moment(s): the walk-off hit, the late rally, the key strikeout — whatever turned this particular version of the night. Be specific: name the pitch count, the fielder, the distance.
- At least 2-3 specific player names tied to what they actually did in THIS game
- The shape of the game: a blowout that was over by the 4th? A pitchers' duel cracked open in the 8th? A seesaw with lead changes every other inning?
- One vivid sensory detail grounded in the physical world of Jacobs Field
- A light reference to this being one iteration among many — "the sixty-ninth telling," "in this particular shuffling of the deck," "once more the lineup cards were exchanged" — but never more than a line or two

WHAT TO AVOID:
- Sports clichés ("gave 110%", "clutch performance", "wanted it more")
- The word "destiny"
- Direct player quotes (no one actually said anything — this is a simulation)
- Any mention of regular season records, franchise history, or "Simyou Lator Engine"
- Being heavy-handed about the simulation concept
- Exclamation points in the prose
- Headlines or titles — just the body text

FORMAT:
- 3-4 paragraphs of flowing prose
- Use <br/><br/> between paragraphs (no <p> tags — this lives inside an existing HTML table cell)
- Approximately 250-400 words total
- Do not include any HTML tags other than <br/> for line breaks

GAME DATA FOR THIS TIMELINE:
[Paste the extracted game data here — see extraction guide below]
```

---

## Data Extraction Guide

For each of the 69 games, you need to assemble a context block to paste into the prompt above. Here's what to pull and where to find it:

### 1. From the folder name
The folder name encodes the game number and final score:
```
infinite_cleveland_g{NN}_{winner_abbrev}{winner_runs}{loser_abbrev}{loser_runs}
```
Example: `infinite_cleveland_g01_cle15fla14` → Timeline 1, Cleveland 15, Florida 14

### 2. From `box_scores/game_box_1.html`
- **Inning-by-inning line score**: Found in the `<table class="data" width="630px">` near the top (lines ~64-204). Each `<td class="dc">` contains one inning's runs. The final three columns are R, H, E totals.
- **Winning team headline**: The `<td class="boxtitle">` inside `<!--RECAP_START-->` (e.g., "Cleveland Wins World Series!")
- **MVP name**: In the existing recap text, look for "who was named series MVP" — the name just before that phrase.

### 3. From `game_logs/log_1.html` (the play-by-play)
This is the richest source. Key sections to extract:

**Structure**: The HTML is organized by half-inning. Each half-inning starts with:
```html
<th class="boxtitle" colspan="2">
  BOTTOM OF THE 9TH
</th>
```

And ends with a summary line:
```html
<td class="datathbg" colspan="2">
  Top of the 9th over - 4 runs, 4 hits, 0 errors, 3 left on base; Florida 1997 14 - Cleveland 1997 13
</td>
```

**What to extract**:
- The **last 2-3 innings** (or more if the game was wild throughout). Focus on where the runs scored.
- **Scoring plays** are marked in bold: `<b>SINGLE</b>`, `<b>HOME RUN (427 ft)</b>`, `<b>Jim Thome scores</b>`
- **Key details per at-bat**:
  - Batter name: `Batting: LHB Jim Thome`
  - Pitch count progression: `0-0: Ball`, `1-0: Called Strike`, etc.
  - Result: `3-1: SINGLE (Flyball, 4MD, EV 93.1 MPH)`
  - Runner advancement: `Jim Thome to second`, `Tony Fernandez scores`
- **Home runs** include distance: `HOME RUN (Flyball, 7D, EV 96.2 MPH, 368 ft)`
- **Walk-off indicator**: If the game ends in the bottom of the 9th with the home team (Cleveland) winning, the final at-bat with a scoring bold line is the walk-off.

**Tip**: Search for `<b>` tags within the last 2 innings to quickly find all the dramatic moments — hits, home runs, scoring plays.

### 4. From CSV data (optional enrichment)
Located in `/Users/creid/golly/infinite/infinite-cleveland-data/`:

- **`games.csv`**: Columns include `winning_pitcher`, `losing_pitcher`, `save_pitcher` — useful for naming the pitchers involved.
- **`players.csv`**: Maps player IDs to names/positions if you need to confirm identity.
- **`players_at_bat_batting_stats.csv`**: Has WPA (Win Probability Added) per at-bat — the highest WPA play is statistically the most important moment of the game.

### Example extracted context block (Timeline 1):

```
TIMELINE: 1
FINAL SCORE: Cleveland 15, Florida 14
LINE SCORE:
  Florida:   2 0 0 2 1 4 1 0 4 — 14 H:18 E:1
  Cleveland: 3 1 1 0 0 0 1 7 2 — 15 H:20 E:1
MVP: Jim Thome

KEY LATE-GAME ACTION:

BOTTOM 8TH (Cleveland scores 7 runs, trailing 6-10):
- Sandy Alomar Jr: 2-run HOME RUN (7D, EV 96.2, 368 ft), score now 8-10
- Matt D Williams: 2-run HOME RUN (8RXD, EV 104.4, 433 ft), score now 13-10
- Bip Roberts: Double (78M, EV 104.4) scoring Grissom and Vizquel, 13-10

TOP 9TH (Florida scores 4, takes lead 14-13):
- Darren Daulton: Solo HOME RUN (8LXD, EV 100.0, 418 ft)
- Moises Alou: Triple (89XD) scoring Johnson
- Edgar Renteria: Single (56, EV 106.9) scoring Alou, ties game 13-13
- Gary Sheffield: Walk with bases loaded, forces in go-ahead run, 14-13

BOTTOM 9TH (Cleveland walk-off, down 13-14):
- Jim Thome: Single on 3-1 count (Flyball, 4MD, EV 93.1)
- Manny Ramirez: Fly out after 8-pitch battle
- Tony Fernandez: Walk on full count, Thome to second
- Matt D Williams: WALK-OFF DOUBLE on 2-2 (Flyball, 78XD, EV 100.0)
  → Jim Thome scores tying run
  → Tony Fernandez scores from third on throw to trailing runner — GAME OVER, 15-14

Winning pitcher: [from games.csv]
Losing pitcher: Livan Hernandez (pitching in the 9th)
```

---

## Verification Checklist

After generating each recap:
- Confirm it's 3-4 paragraphs, 250-400 words
- Check that specific game details (score, player names, key plays) match the actual game data
- Ensure the HTML will render properly (only `<br/>` tags, no unclosed elements)
- Read it aloud — does it sound like Angell? Long sentences, precise imagery, no clichés?
- Is the simulation conceit present but restrained (1-2 references max)?
