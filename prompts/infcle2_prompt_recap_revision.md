# Prompt for Revising OOTP Recap Text — Infinite Cleveland 2

## Context

The "Infinite Cleveland 2" project simulates 1998 World Series Game 7 (Cleveland Indians vs San Diego Padres at Jacobs Field) 92 times. Each simulation produces an almanac with a box score HTML file containing a game recap between `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers. These recaps are boilerplate OOTP templates — nearly identical across all 92 games, differing only in the final score and Player of the Game name. The goal is to replace them with distinctive prose that captures the project's Groundhog Day conceit in Roger Angell's voice.

Unlike the original Infinite Cleveland prompt, this version uses a **two-pass approach**: a data-digestion pass that extracts and structures the game's key moments, followed by a narrative-generation pass that writes the Angell prose from that digest. This separation keeps the analytical and literary tasks from competing for the model's attention, and compensates for the loss of numerical WPA data in this OOTP version.

---

## Two-Pass Overview

**Why two passes?**

1. The play-by-play HTML for a single game runs 860–1,000+ lines. Parsing that while simultaneously crafting literary prose degrades both tasks.
2. This OOTP version no longer exports per-at-bat WPA (Win Probability Added) data in CSV form. Identifying the game's pivotal moments now requires analyzing game state from the play-by-play and the WPA chart image — an analytical task best done separately from prose generation.
3. A structured intermediate digest makes factual errors easier to catch before they get baked into polished prose.

**Pass 1 (Game Digest):** Analytical. Reads the raw HTML play-by-play, box score, and WPA chart image. Produces a structured text summary of the game: score, shape, key moments, decisive turning point, notable performances.

**Pass 2 (Narrative):** Literary. Reads only the Pass 1 digest (no HTML, no images). Writes 3–4 paragraphs of Roger Angell–style prose.

---

## Pass 1: Game Digest Prompt

```
You are a baseball data analyst preparing a structured game summary. Your job is to extract facts from the provided game data — no literary embellishment, no opinions, no invented details. Include ONLY information that can be verified from the provided sources.

You will be given:
1. A WPA (Win Probability Added) chart image showing the game flow and 4 annotated key moments
2. The full play-by-play HTML game log
3. The box score HTML with line score, batting/pitching tables, and game notes
4. The game folder name (encoding timeline number and final score)

From these sources, produce the following structured output:

TIMELINE: {number}
GAME: 1998 World Series Game 7
DATE: October 27, 1998
VENUE: Jacobs Field

FINAL SCORE: {Winner} {runs}, {Loser} {runs}
INNINGS: {number}

LINE SCORE:
  San Diego:   {inning scores separated by spaces} — {R} H:{H} E:{E}
  Cleveland:   {inning scores separated by spaces} — {R} H:{H} E:{E}

PLAYER OF THE GAME: {name from box score game notes}

GAME SHAPE: {Classify as one of: blowout, wire-to-wire lead, pitchers' duel, comeback, seesaw, walk-off, extra-innings}

GAME FLOW: {2-3 factual sentences describing how the game unfolded — who scored when, when the lead changed, how it ended. Reference specific innings.}

STARTING PITCHERS:
  San Diego: {name}
  Cleveland: {name}
WINNING PITCHER: {name} {decision, e.g. W (1-0)}
LOSING PITCHER: {name} {decision}
SAVE: {name and decision, or "none"}

KEY MOMENTS (3-4 plays ranked by impact on game outcome, using the WPA chart annotations as your primary guide, enriched with pitch-level detail from the play-by-play):

1. {INNING, HALF}: {Batter full name} — {what happened}
   Pitcher: {name}
   Game state before: {score}, {outs} out, runners on {bases or "none"}
   Game state after: {new score}
   Detail: {pitch count at result, hit type, exit velocity, distance if HR, runner movement}

2. {repeat}

3. {repeat}

4. {repeat if applicable}

DECISIVE MOMENT: {Which of the above was THE turning point, in one sentence, and why — e.g., "Moment #2 broke a tie in the 7th with no answer from San Diego."}

NOTABLE PERFORMANCES:
- {Player}: {batting line from box score — e.g., 3-for-4, 2B, HR, 3 RBI}
- {Player}: {batting line}
- {Pitcher}: {IP, H, R, ER, K, BB, PI pitches}

ATMOSPHERIC DATA:
  Weather: {from box score game notes}
  Attendance: {from box score game notes}
  Game duration: {from box score game notes}
  Start time: {from box score game notes}
  Ballpark: {from box score game notes}

WALK-OFF: {yes/no — if yes, describe the final at-bat sequence: batter, count, result, who scored, final score}
```

---

## Pass 1: Data Sources & Extraction Guide

For each of the 92 games, you need to assemble the following inputs for the Pass 1 prompt.

### 1. From the folder name
The folder name encodes the game number and final score:
```
infinite_cleveland_g{NN}_{winner_abbrev}{winner_runs}{loser_abbrev}{loser_runs}
```
Example: `infinite_cleveland_g01_cle6sdp4` → Timeline 1, Cleveland 6, San Diego 4

Team abbreviations: `cle` = Cleveland Indians, `sdp` = San Diego Padres.

### 2. From `box_scores/game_box_1.html`
- **Inning-by-inning line score**: Found in the `<table class="data" width="630px">` near the top. Each `<td class="dc">` contains one inning's runs. The final three columns are R, H, E totals.
- **Winning team headline**: The `<td class="boxtitle">` inside `<!--RECAP_START-->` (e.g., "Cleveland 1998 Takes Title").
- **Player of the Game**: In the game notes section near the bottom, look for `<b>Player of the Game: </b>` — the name appears on the next line as plain text.
- **Atmospheric data**: Also in the game notes: Ballpark, Weather, Start Time, Time (duration), Attendance.
- **WPA chart**: An `<img>` tag references `../images/wpa/wpa_1.png` — this is loaded separately as an image input.

### 3. From `images/wpa/wpa_1.png` (the WPA chart)
This is an image file that OOTP generates for each game. It shows:
- A win-probability line graph (y-axis: team win probability, x-axis: innings 1–9+)
- **4 numbered annotations** identifying the highest-leverage plays, formatted like:
  - "1. Top 3rd: T. Gwynn Sr hit a 2-run double vs B. Colon"
  - "2. Bot 5th: J. Thome hit a 2-run home run vs K. Brown"

Feed this image directly to the model in Pass 1. These annotations are the primary guide for identifying the game's key moments — they replace the per-at-bat WPA column that was available in the original Infinite Cleveland data.

### 4. From `game_logs/log_1.html` (the play-by-play)
This is the richest source. Key sections to extract:

**Structure**: The HTML is organized by half-inning. Each half-inning starts with:
```html
<th class="boxtitle" colspan="2">
  BOTTOM OF THE 9TH
</th>
```

The batting team and opposing pitcher are noted in a header row:
```html
<th align="left" colspan="2">
  Cleveland 1998 Indians batting - Pitching for San Diego 1998 Padres : RHP Kevin Brown
</th>
```

Each half-inning ends with a summary line:
```html
<td class="datathbg" colspan="2">
  Top of the 7th over - 2 runs, 3 hits, 1 error, 2 left on base; San Diego 1998 4 - Cleveland 1998 3
</td>
```

**What to extract**:
- The **last 2-3 innings** (or more if the game was wild throughout). Focus on where the runs scored.
- **Scoring plays** are marked in bold: `<b>SINGLE</b>`, `<b>3-RUN HOME RUN</b>`, `<b>Steve Finley scores</b>`
- **Key details per at-bat**:
  - Batter name and handedness: `Batting: LHB Jim Thome`
  - Pitch count progression: `0-0: Ball`, `1-0: Called Strike`, etc.
  - Result: `2-2: <b>SINGLE</b>  (Line Drive, 6D, EV 106.2 MPH)`
  - Runner advancement: `Einar Diaz to second`, `Steve Finley scores`
- **Home runs** include distance: `<b>3-RUN HOME RUN</b>  (Flyball, 9D, EV 91.2 MPH), Distance : 376 ft`
- **Pitcher changes** appear inline: `Pitching: LHP Randy Myers`
- **Walk-off indicator**: If the game ends in the bottom of the 9th (or later) with Cleveland winning, the final at-bat with a scoring bold line is the walk-off.

**Tip**: Search for `<b>` tags within the last 2–3 innings to quickly find all the dramatic moments — hits, home runs, scoring plays.

### 5. From CSV data (optional enrichment)
Located in `/Users/charles/golly/infinite/sportsball/data/98/csv/`:

- **`games.csv`**: Columns include `winning_pitcher`, `losing_pitcher`, `save_pitcher` (as player IDs), `starter0`, `starter1` — useful for resolving pitcher names.
- **`players.csv`**: Maps player IDs to names (`first_name`, `last_name`) and positions.
- **`players_at_bat_batting_stats.csv`**: Detailed at-bat records with `inning`, `outs`, `base1/base2/base3`, `run_diff`, `rbi`, `result`, `exit_velo`, `launch_angle`, `hit_loc`. Note: this CSV does **not** contain a WPA column.
- **`games_score.csv`**: Inning-by-inning runs scored by each team.

---

## Pass 2: Narrative Prompt

```
You are writing a 3-4 paragraph game recap for Timeline #{game_number} of "Infinite Cleveland 2" — a project that simulates 1998 World Series Game 7 between the Cleveland Indians and San Diego Padres at Jacobs Field, October 27, 1998, ninety-two times over.

THE CONCEIT: These players are trapped in an endless loop. The same game, the same October Tuesday night, replayed with different outcomes each time. The players don't know. They experience each game as singular. But you, the writer, know — and that knowledge should haunt the prose at its edges. A flicker of déjà vu. The eerie sense that Thome has stood in this box before, that Gwynn has lined one through the left side in some other version of tonight. Don't belabor it. One or two glancing references per piece. The uncanny feeling, not the explanation.

VOICE: Write in the style of Roger Angell — the New Yorker's baseball essayist for six decades. His hallmarks:
- Long, musical sentences that unspool with the patience of a 3-2 count
- Precise physical and spatial detail: the geometry of a relay throw, the specific arc of a fly ball against October sky, the sound of 45,000 people inhaling at once
- The sense of *being there* — the particular cold of a Cleveland October, the light towers making everything both vivid and slightly unreal, the quality of noise in a ballpark that hasn't won a championship since 1948
- Emotional calibration: if Cleveland wins, this is the end of a fifty-year drought. The crowd isn't politely applauding — they're losing their minds. The ending must match the stakes. Conversely, a Padres win means 45,000 people going silent at once. Get the emotional physics right.
- Wry warmth without sentimentality; humor that respects its subject
- Baseball understood as a meditation on time and repetition (which maps perfectly here)
- Trust the reader — no explaining rules, no cheap drama, no exclamation points

WHAT TO INCLUDE:
- The final score and which team won
- The decisive moment(s): the walk-off hit, the late rally, the key strikeout — whatever turned this particular version of the night. Be specific: name the pitch count, the fielder, the distance.
- At least 2-3 specific player names tied to what they actually did in THIS game
- When first mentioning a player in the recap — especially in the opening sentence — establish which team they play for. The reader hasn't memorized the lineup card. "Kevin Brown had spent the evening..." means nothing until you say "the Padres starter." This applies to every first mention throughout the piece, not just the opener. Never assume the reader is already inside the game.
- The shape of the game: a blowout that was over by the 4th? A pitchers' duel cracked open in the 8th? A seesaw with lead changes every other inning?
- Something about the starting pitchers' day — how many innings Kevin Brown or Bartolo Colon lasted, how hard they were hit, whether things unraveled early or late
- One vivid sensory detail grounded in the physical world of Jacobs Field
- A light reference to this being one iteration among many — "the ninety-second telling," "in this particular shuffling of the deck," "once more the lineup cards were exchanged" — but never more than a line or two

WHAT TO AVOID:
- Opening with a bare statistical declaration, a decontextualized game-state summary, or a player's name without identifying context. This includes "X hit Y home runs," "X hit a ball Y feet," "X went Y-for-Z," "The game was tied at two through six innings," "The hit cleared the fence," and critically: any sentence that opens with just a name. A name alone tells the reader nothing — who is this person, what team are they on? Give them their role: "Cleveland starter Bartolo Colon," "the Padres' left fielder Greg Vaughn," etc. The opening sentence must orient the reader — give them a team, a place, a feeling, a human being doing something specific. Stats and game states belong in the body of the prose where they illuminate what happened; they are not leads. Vary the entry point for every recap: a scene, a player in a moment, the quality of the night, a narrative observation. Never open two recaps the same way.
- Short dramatic reversal sentences: "They had not." "It was not." "He did not." "It did not last." Any three-to-five word sentence that exists solely as a theatrical pivot or dramatic beat. Angell would never write a sentence like that — he would fold the reversal into the texture of a longer, more considered sentence. These clipped pivots are an AI writing tic, not literary prose.
- Sports clichés ("gave 110%", "clutch performance", "wanted it more")
- The word "destiny"
- Direct player quotes (no one actually said anything — this is a simulation)
- Any mention of regular season records, franchise history beyond what's in the conceit, or "Simyou Lator Engine"
- Being heavy-handed about the simulation concept
- Concluding with a grand run-on sentence about timelines, exchanging lineup cards, anthems being sung, or patterns reasserting themselves. This is filler — a ham-handed attempt to tie a bow on the piece by restating the simulation conceit in flowery language. But don't overcorrect into an abrupt cutoff either — the piece still needs a proper landing. End on a concrete image or observation from the game itself: the sound of the crowd, a final pitching line, the stadium emptying. Something grounded and short, not a rhetorical flourish about repetition and fate.
- Endings that leave the outcome emotionally ambiguous — if Cleveland wins the World Series, the reader must feel that. Don't end on quiet contemplation when the moment calls for eruption. A crowd "standing in the chill" after a championship win reads like a loss.
- Exclamation points in the prose
- Headlines or titles — just the body text
- Game Score (the pitching metric) — it's an internal sabermetric stat that general readers won't know how to interpret. Use IP, hits, runs, strikeouts, and walks to convey a pitcher's dominance instead.

FORMAT:
- 3-4 paragraphs of flowing prose
- Use <br/><br/> between paragraphs (no <p> tags — this lives inside an existing HTML table cell)
- Approximately 250-400 words total
- Do not include any HTML tags other than <br/> for line breaks

GAME DIGEST FOR THIS TIMELINE:
[Paste the Pass 1 output here]
```

---

## Worked Example (Timeline 1)

### Pass 1 Output

```
TIMELINE: 1
GAME: 1998 World Series Game 7
DATE: October 27, 1998
VENUE: Jacobs Field

FINAL SCORE: Cleveland 6, San Diego 4
INNINGS: 9

LINE SCORE:
  San Diego:   0 0 2 0 0 0 2 0 0 — 4 H:6 E:1
  Cleveland:   0 0 0 1 2 0 2 1 X — 6 H:9 E:1

PLAYER OF THE GAME: Omar Vizquel

GAME SHAPE: Comeback

GAME FLOW: San Diego struck first with a 2-run double by Tony Gwynn in the 3rd off Bartolo Colon. Cleveland scratched one back in the 4th on a sac fly by Enrique Wilson (after Ramirez was hit by a pitch and Justice reached on an error), then Jim Thome's 2-run homer in the 5th gave Cleveland a 3-2 lead. The Padres retook the lead 4-3 in the top of the 7th on back-to-back RBI singles by Gwynn and Vaughn off Paul Shuey, but Cleveland responded immediately in the bottom of the 7th with run-scoring singles by Manny Ramirez and David Justice off Randy Myers to go ahead 5-4. Omar Vizquel's insurance RBI single in the 8th made it 6-4, and the Padres went quietly in the 9th.

STARTING PITCHERS:
  San Diego: Kevin Brown
  Cleveland: Bartolo Colon
WINNING PITCHER: Paul Shuey W (1-0)
LOSING PITCHER: Randy Myers L (0-1)
SAVE: Paul Assenmacher

KEY MOMENTS:

1. TOP 3RD: Tony Gwynn Sr — 2-run double
   Pitcher: Bartolo Colon
   Game state before: 0-0, 1 out, runners on 1st and 2nd
   Game state after: San Diego 2, Cleveland 0
   Detail: 1-0 count, double (Groundball, 5L, EV 95.6 MPH), scored Carlos Hernandez; Chris Gomez to 3rd then scored on throw by LF

2. BOTTOM 5TH: Jim Thome — 2-run home run
   Pitcher: Kevin Brown
   Game state before: San Diego 2, Cleveland 1, 2 out, Omar Vizquel on 1st (singled)
   Game state after: Cleveland 3, San Diego 2
   Detail: 0-0 count (first pitch), home run (Flyball, 9D, EV 102.5 MPH), Distance: 364 ft

3. BOTTOM 7TH: Manny Ramirez — run-scoring single (tying run)
   Pitcher: Randy Myers
   Game state before: San Diego 4, Cleveland 3, 2 out, runners on 1st (Vizquel) and 2nd (Diaz)
   Game state after: Tied 4-4
   Detail: 3-2 count after 6-pitch at-bat, single (Line Drive, 89S, EV 105.6 MPH), Diaz scores from 2nd, Vizquel to 3rd

4. BOTTOM 7TH: David Justice — go-ahead RBI single
   Pitcher: Randy Myers
   Game state before: Tied 4-4, 2 out, runners on 2nd (Ramirez) and 3rd (Vizquel)
   Game state after: Cleveland 5, San Diego 4
   Detail: 1-2 count, single (Groundball, 4MD, EV 103.1 MPH), Vizquel scores from 3rd, Ramirez to 2nd

DECISIVE MOMENT: Moments #3 and #4 together — Ramirez's tying single and Justice's go-ahead single, both with 2 outs in the bottom 7th off Randy Myers, erased a 4-3 deficit and gave Cleveland a lead they would not relinquish.

NOTABLE PERFORMANCES:
- Omar Vizquel: 3-for-4, 2B, BB, 2 R, 1 RBI (Player of the Game)
- Jim Thome: 1-for-5, HR (2-run), 2 RBI, 4 K
- Manny Ramirez: 2-for-3, HBP, 1 R, 1 RBI
- Tony Gwynn Sr: 2-for-5, 2B, 3 RBI
- Kevin Brown: 6.0 IP, 4 H, 4 R, 3 ER, 9 K, 1 BB, 107 pitches
- Bartolo Colon: 6.1 IP, 3 H, 4 R, 4 ER, 8 K, 6 BB, 103 pitches
- Paul Shuey: 1.0 IP, 3 H, 0 R, 1 K, W (1-0), BS (1)

ATMOSPHERIC DATA:
  Weather: Clear skies (45 degrees), no wind
  Attendance: 45,225
  Game duration: 3:35
  Start time: 8:05 PM EST

WALK-OFF: No (Cleveland led after the 8th; game ended on a routine top-of-9th)
```

---

## Human Review Step (MANDATORY)

**Never write the narrative directly into the HTML file.** Always present the proposed recap to the user first for approval.

After generating the Pass 2 narrative:

1. **Display the proposed recap in the Claude Code window as plain readable text.** Use actual paragraph breaks (blank lines between paragraphs) so the prose is easy to read — not run together, not wrapped in HTML tags. The user needs to be able to read it as prose, not as markup.

2. **Wait for explicit user approval.** The user may:
   - Approve the recap as-is (then proceed to insert it into the HTML)
   - Request specific edits (revise and re-present)
   - Reject it entirely and ask for a fresh attempt

3. **Only after approval**, insert the recap into the box score HTML between the `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers, converting paragraph breaks to `<br/><br/>` and stripping any other formatting.

This step is non-negotiable. The Roger Angell voice is too difficult to nail without a human ear in the loop. An AI cannot reliably judge whether its own prose sounds right.

---

## Verification Checklist

After generating each recap (during the review step, before insertion):
- Confirm it's 3-4 paragraphs, 250-400 words
- Check that specific game details (score, player names, key plays) match the actual game data
- Ensure the HTML will render properly (only `<br/>` tags, no unclosed elements)
- Read it aloud — does it sound like Angell? Long sentences, precise imagery, no clichés?
- Is the simulation conceit present but restrained (1-2 references max)?
- Cross-check Pass 2 output against Pass 1 digest — are all cited facts traceable to the digest?
- Does the recap mention the starting pitchers' performance in some way? (Their success or unraveling is central to the game's story)
