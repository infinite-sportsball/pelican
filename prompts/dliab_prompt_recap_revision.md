# Prompt for Revising OOTP Recap Text — Don Larsen is a Bum

## Context

The "Don Larsen is a Bum" project simulates 1956 World Series Game 5 (Brooklyn Dodgers at New York Yankees at Yankee Stadium) 51 times. Each simulation produces an almanac with a box score HTML file containing a game recap between `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers. These recaps are boilerplate OOTP templates — nearly identical across all 51 games, differing only in the final score and Player of the Game name. The goal is to replace them with distinctive prose that captures the project's Groundhog Day conceit in Roger Angell's voice.

This prompt uses a **two-pass approach**: a data-digestion pass that extracts and structures the game's key moments, followed by a narrative-generation pass that writes the Angell prose from that digest. This separation keeps the analytical and literary tasks from competing for the model's attention, and compensates for the loss of numerical WPA data in this OOTP version.

### Historical Background

On October 8, 1956, Don Larsen pitched the only perfect game in World Series history — 27 up, 27 down — to give the Yankees a 2-0 win and a 3-2 series lead. The Dodgers never got a baserunner. In this project, every simulation undoes that perfection: Brooklyn wins all 51 games. Larsen never comes close to a perfect game. The conceit is that he wakes up each morning doomed to fail again, though he doesn't know it.

**Larsen's Game 2 disaster (October 5, 1956):** Three days before his perfect game, Larsen started Game 2 of the same World Series and was handed a 6-0 lead after Yogi Berra's grand slam highlighted a five-run Yankee second inning. Larsen immediately blew it — he walked four batters in a six-run Dodger second inning and was pulled before recording the final out. The Dodgers won 13-8. This is rich material for the recaps: in reality, the Game 5 perfection was Larsen's redemption for Game 2. In our simulations, that redemption never comes — he keeps failing, and the Game 2 collapse becomes the pattern rather than the exception. Use this parallel when it fits naturally (especially when Larsen loses a lead or walks too many batters), but don't force it into every recap.

The rosters are small and fixed — 12 players per side, the actual Game 5 lineups:

**Brooklyn Dodgers (away, bat first):** Jim Gilliam (2B), Pee Wee Reese (SS), Duke Snider (CF), Jackie Robinson (3B), Gil Hodges (1B), Sandy Amoros (LF), Carl Furillo (RF), Roy Campanella (C), Sal Maglie (P), plus reserves Ransom Jackson (3B) and Rube Walker (P).

**New York Yankees (home, bat last):** Hank Bauer (RF), Joe Collins (1B), Mickey Mantle (CF), Yogi Berra (C), Enos Slaughter (LF), Billy Martin (2B), Gil McDougald (SS), Andy Carey (3B), Don Larsen (P), plus reserves Bob Cerv (P) and Elston Howard (P).

---

## Two-Pass Overview

**Why two passes?**

1. The play-by-play HTML for a single game runs 800–1,000+ lines. Parsing that while simultaneously crafting literary prose degrades both tasks.
2. This OOTP version does not export per-at-bat WPA data in CSV form. Identifying the game's pivotal moments requires analyzing game state from the play-by-play and the WPA chart image — an analytical task best done separately from prose generation.
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
GAME: 1956 World Series Game 5
DATE: October 8, 1956
VENUE: Yankee Stadium

FINAL SCORE: Brooklyn {runs}, New York {runs}
INNINGS: {number}

LINE SCORE:
  Brooklyn:    {inning scores separated by spaces} — {R} H:{H} E:{E}
  New York:    {inning scores separated by spaces} — {R} H:{H} E:{E}

PLAYER OF THE GAME: {name from box score game notes}

GAME SHAPE: {Classify as one of: blowout, wire-to-wire lead, pitchers' duel, comeback, seesaw, extra-innings}

GAME FLOW: {2-3 factual sentences describing how the game unfolded — who scored when, when the lead changed, how it ended. Reference specific innings.}

STARTING PITCHERS:
  Brooklyn: Sal Maglie
  New York: Don Larsen
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

DECISIVE MOMENT: {Which of the above was THE turning point, in one sentence, and why — e.g., "Moment #2 broke a tie in the 5th with no answer from New York."}

NOTABLE PERFORMANCES:
- {Player}: {batting line from box score — e.g., 3-for-4, 2B, HR, 3 RBI}
- {Player}: {batting line}
- {Pitcher}: {IP, H, R, ER, K, BB, PI pitches}

ATMOSPHERIC DATA:
  Weather: {from box score game notes}
  Attendance: 64,519 (IMPORTANT: Always use the historical attendance of 64,519 from the box score header, NOT the simulated ~43,000 figure from the game notes section. The real Game 5 drew 64,519 fans. When referencing the crowd in prose, use 64,519 or "sixty-four thousand" or similar.)
  Game duration: {from box score game notes}
  Start time: {from box score game notes}
  Ballpark: {from box score game notes — will be "Yankee Stadium I"}

WALK-OFF: No (Brooklyn bats first as the visiting team; the game cannot end on a walk-off)

LARSEN LINE: {Don Larsen's pitching line — IP, H, R, ER, K, BB, PI pitches, game score. Note whether he was pulled early or went the distance.}
```

---

## Pass 1: Data Sources & Extraction Guide

For each of the 51 games, you need to assemble the following inputs for the Pass 1 prompt.

### 1. From the folder name
The folder name encodes the game number and final score:
```
dliab_g{NN}_{winner_abbrev}{winner_runs}{loser_abbrev}{loser_runs}
```
Example: `dliab_g49_dod4nyy2` → Timeline 49, Brooklyn (Dodgers) 4, New York (Yankees) 2

Team abbreviations: `dod` = Brooklyn Dodgers, `nyy` = New York Yankees.

Note: Brooklyn wins all 51 games. The folder name will always show `dod` before `nyy`.

### 2. From `box_scores/game_box_1.html`
- **Inning-by-inning line score**: Found in the `<table class="data" width="630px">` near the top. Each `<td class="dc">` contains one inning's runs. The final three columns are R, H, E totals.
- **Winning team headline**: The `<td class="boxtitle">` inside `<!--RECAP_START-->` (e.g., "Dodgers Top Yankees").
- **Player of the Game**: In the game notes section near the bottom, look for `<b>Player of the Game: </b>` — the name appears on the next line as plain text.
- **Atmospheric data**: Also in the game notes: Ballpark (Yankee Stadium I), Weather, Start Time, Time (duration), Attendance.
- **WPA chart**: An `<img>` tag references `../images/wpa/wpa_1.png` — this is loaded separately as an image input.
- **Batting tables**: Both teams' batting linescores with AB, R, H, RBI, BB, K, LOB, AVG, HR columns. Below each table are batting notes (home runs with inning/pitcher detail, doubles, triples, sac flies, etc.).
- **Pitching tables**: Both teams' pitching linescores with IP, H, R, ER, BB, K, HR, PI (pitches), PS (strikes), ERA columns.

### 3. From `images/wpa/wpa_1.png` (the WPA chart)
This is an image file that OOTP generates for each game. It shows:
- A win-probability line graph (y-axis: team win probability, x-axis: innings 1–9+)
- The y-axis labels use team abbreviations: `BRO1956` (Brooklyn) at top, `NYA1956` (New York) at bottom
- **4 numbered annotations** identifying the highest-leverage plays, formatted like:
  - "1. Top 4th: J. Robinson hit a solo home run vs D. Larsen"
  - "2. Top 5th: J. Robinson drew a walk, driving in 1 run vs D. Larsen"

Feed this image directly to the model in Pass 1. These annotations are the primary guide for identifying the game's key moments — they replace the per-at-bat WPA column that was available in older data formats.

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
  Brooklyn 1956 Dodgers batting - Pitching for New York 1956 Yankees : RHP Don Larsen
</th>
```

Each half-inning ends with a summary line:
```html
<td class="datathbg" colspan="2">
  Top of the 1st over -  1 run, 1 hit, 1 error, 1 left on base; Brooklyn 1956 1 - New York 1956 0
</td>
```

**What to extract**:
- The **last 2-3 innings** (or more if the game was wild throughout). Focus on where the runs scored.
- **Scoring plays** are marked in bold: `<b>SINGLE</b>`, `<b>3-RUN HOME RUN</b>`, `<b>Runner from 3rd tags up, SCORES</b>`
- **Key details per at-bat**:
  - Batter name and handedness: `Batting: RHB Jackie Robinson`
  - Pitch count progression: `0-0: Ball`, `1-0: Called Strike`, etc.
  - Result: `2-2: <b>SINGLE</b>  (Line Drive, 6D, EV 106.2 MPH)`
  - Runner advancement: `Jim Gilliam to third`, `Pee Wee Reese scores`
- **Home runs** include distance: `<b>SOLO HOME RUN</b>  (Flyball, 9D, EV 91.2 MPH), Distance : 376 ft`
- **Pitcher changes** appear inline: `Pitching: RHP Elston Howard` or `Pitching: RHP Bob Cerv` (the Yankees' only relief options)
- **Errors**: Noted inline: `Reached on error, E2 (Groundball, 2L, EV 71.2 MPH)` — errors can be pivotal in these games

**Tip**: Search for `<b>` tags within each inning to quickly find all the dramatic moments — hits, home runs, scoring plays.

**Note on team names**: The HTML uses "Brooklyn 1956" and "New York 1956" throughout. In the digest, use "Brooklyn" and "New York" without the year suffix.

### 5. From CSV data (optional enrichment)
Located in `/Users/charles/golly/infinite/sportsball/data/56/csv/`:

- **`games.csv`**: Columns include `winning_pitcher`, `losing_pitcher`, `save_pitcher` (as player IDs), `starter0`, `starter1`, `runs0`/`runs1`, `hits0`/`hits1`, `errors0`/`errors1`, `innings`, `attendance`. Team 1 = Brooklyn (away, `runs0`), Team 2 = New York (home, `runs1`).
- **`players.csv`**: Maps player IDs to names (`first_name`, `last_name`) and positions. Only 22 players total (12 Brooklyn, 10 New York, plus 2 reserves on each side).
- **`players_at_bat_batting_stats.csv`**: Detailed at-bat records with `inning`, `outs`, `base1/base2/base3`, `run_diff`, `rbi`, `result`, `exit_velo`, `launch_angle`, `hit_loc`. Note: this CSV does **not** contain a WPA column.
- **`games_score.csv`**: Inning-by-inning runs scored by each team. Team `0` = Brooklyn (away), Team `1` = New York (home).
- **`players_game_batting.csv`**: Per-game batting stats with AB, H, K, PA, HR, R, RBI, BB, etc.
- **`players_game_pitching_stats.csv`**: Per-game pitching stats with IP (as outs), H, K, BB, R, ER, PI (pitches), HR allowed, etc.

---

## Pass 2: Narrative Prompt

```
You are writing a 3-4 paragraph game recap for Timeline #{game_number} of "Don Larsen is a Bum" — a project that simulates 1956 World Series Game 5 between the Brooklyn Dodgers and New York Yankees at Yankee Stadium, October 8, 1956, fifty-one times over.

THE CONCEIT: On this date in real history, Don Larsen pitched a perfect game — the only one in World Series history. Twenty-seven Dodgers came to the plate, and twenty-seven sat back down. In this project, that never happens. Each simulation begins with Larsen on the mound and Maglie on the mound, same lineups, same October Monday afternoon — and each time, Brooklyn wins. Larsen gets hit, gets rattled, gets pulled. The perfection never materializes. The players don't know they're trapped in a loop. They experience each game as singular. But you, the writer, know — and that knowledge should haunt the prose at its edges. The ghost of the perfect game that was supposed to happen. The sense that Larsen keeps winding up and the ball keeps finding Brooklyn bats. Don't belabor it. One or two glancing references per piece. The uncanny feeling, not the explanation.

VOICE: Write in the style of Roger Angell — the New Yorker's baseball essayist for six decades. His hallmarks:
- Long, musical sentences that unspool with the patience of a 3-2 count
- Precise physical and spatial detail: the geometry of a relay throw, the specific arc of a fly ball against October sky, the sound of 64,000 people inhaling at once
- The sense of *being there* — the particular cool of an early-October afternoon in the Bronx, the light falling across the Yankee Stadium grandstand, the quality of noise in a ballpark that has seen so many Octobers it takes them for granted
- Wry warmth without sentimentality; humor that respects its subject
- Baseball understood as a meditation on time and repetition (which maps perfectly here)
- Trust the reader — no explaining rules, no cheap drama, no exclamation points
- These are the '56 Dodgers — Robinson, Campanella, Reese, Snider, Hodges. Future Hall of Famers in their twilight. Write with awareness that this is the last great Brooklyn team, one year from the move to Los Angeles, though the characters don't know that either.

WHAT TO INCLUDE:
- The final score and which team won
- The decisive moment(s): the big home run, the late rally, the key strikeout — whatever turned this particular version of the afternoon. Be specific: name the pitch count, the fielder, the distance.
- At least 2-3 specific player names tied to what they actually did in THIS game
- When first mentioning a player in the recap — especially in the opening sentence — establish which team they play for. The reader hasn't memorized the lineup card. "Carl Furillo's home run" means nothing until you say "for Brooklyn." This is especially important for less famous names (Amoros, Furillo, Carey, Collins) but applies to anyone introduced without prior context.
- The shape of the game: a blowout that was over by the 3rd? A pitchers' duel cracked open in the 6th? A seesaw with lead changes every other inning?
- Something about Larsen's day — how many innings he lasted, how hard he was hit, whether the wheels came off early or late
- One vivid sensory detail grounded in the physical world of Yankee Stadium
- A light reference to this being one iteration among many — "the fifty-first telling," "in this particular reshuffling of the afternoon," "once more the lineup cards were exchanged at home plate" — but never more than a line or two

WHAT TO AVOID:
- Sports clichés ("gave 110%", "clutch performance", "wanted it more")
- The word "destiny"
- The word "perfect" used earnestly about any aspect of this game (it's loaded — the real game was a perfect game, so the word carries ironic weight; use it only if you mean to invoke that irony)
- Direct player quotes (no one actually said anything — this is a simulation)
- Any mention of regular season records, franchise history beyond what's in the conceit, or "Simyou Lator Engine"
- Being heavy-handed about the simulation concept
- Concluding with a grand run-on sentence about timelines, exchanging lineup cards, anthems being sung, or patterns reasserting themselves. This is filler — a ham-handed attempt to tie a bow on the piece by restating the simulation conceit in flowery language. But don't overcorrect into an abrupt cutoff either — the piece still needs a proper landing. End on a concrete image or observation from the game itself: the sound of the crowd, a final pitching line, the stadium emptying. Something grounded and short, not a rhetorical flourish about repetition and fate.
- Exclamation points in the prose
- Headlines or titles — just the body text
- Game Score (the pitching metric) — it's an internal sabermetric stat that general readers won't know how to interpret. Use IP, hits, runs, strikeouts, and walks to convey a pitcher's dominance instead.

FORMAT:
- 3-4 paragraphs of flowing prose
- Use <br/><br/> between paragraphs (no <p> tags — this lives inside an existing HTML table cell)
- Approximately 250-400 words total
- Do not include any HTML tags other than <br/> for line breaks
```

---

## Worked Example (Timeline 49)

### Pass 1 Output

```
TIMELINE: 49
GAME: 1956 World Series Game 5
DATE: October 8, 1956
VENUE: Yankee Stadium

FINAL SCORE: Brooklyn 4, New York 2
INNINGS: 9

LINE SCORE:
  Brooklyn:    1 0 0 1 1 1 0 0 0 — 4 H:7 E:2
  New York:    0 1 1 0 0 0 0 0 0 — 2 H:5 E:1

PLAYER OF THE GAME: Sal Maglie

GAME SHAPE: Wire-to-wire lead

GAME FLOW: Brooklyn grabbed a 1-0 lead in the top of the 1st when Jim Gilliam singled and eventually scored on a Jackie Robinson sacrifice fly. New York answered with single runs in the 2nd (Billy Martin doubled, scored on an Andy Carey groundout) and 3rd (Hank Bauer doubled, scored on a Joe Collins single) to take a 2-1 lead. Robinson's solo home run in the 4th tied it 2-2, his bases-loaded walk in the 5th put Brooklyn ahead 3-2, and Sandy Amoros's solo homer in the 6th made it 4-2. Maglie shut out the Yankees over the final six innings.

STARTING PITCHERS:
  Brooklyn: Sal Maglie
  New York: Don Larsen
WINNING PITCHER: Sal Maglie W (1-0)
LOSING PITCHER: Don Larsen L (0-1)
SAVE: none

KEY MOMENTS:

1. TOP 4TH: Jackie Robinson — solo home run
   Pitcher: Don Larsen
   Game state before: New York 2, Brooklyn 1, 0 out, none on
   Game state after: Tied 2-2
   Detail: 1-2 count, home run (Flyball), tied the game after Brooklyn had trailed since the 2nd

2. TOP 5TH: Jackie Robinson — bases-loaded walk (RBI)
   Pitcher: Don Larsen
   Game state before: Tied 2-2, 1 out, bases loaded
   Game state after: Brooklyn 3, New York 2
   Detail: Full count walk, drove in Jim Gilliam from 3rd to give Brooklyn the lead for good

3. TOP 6TH: Sandy Amoros — solo home run
   Pitcher: Don Larsen
   Game state before: Brooklyn 3, New York 2, 0 out, none on
   Game state after: Brooklyn 4, New York 2
   Detail: Insurance run, solo homer to extend the lead to two

4. BOT 8TH: Enos Slaughter — grounded out
   Pitcher: Sal Maglie
   Game state before: Brooklyn 4, New York 2, 2 out, runners on 1st and 3rd
   Game state after: Brooklyn 4, New York 2 (inning over)
   Detail: Ended New York's best late threat; the WPA chart shows this as the point where Brooklyn's win probability surged back toward certainty

DECISIVE MOMENT: Moment #2 — Robinson's walk in the 5th gave Brooklyn the lead after having trailed since the 2nd inning, and the Yankees never tied it again.

NOTABLE PERFORMANCES:
- Jackie Robinson: 1-for-2, HR, 3 RBI, 1 BB (drove in 3 of Brooklyn's 4 runs)
- Jim Gilliam: 3-for-5, 2 R, 1 SB
- Sal Maglie: 9.0 IP, 5 H, 2 R, 2 ER, 0 K, 3 BB, 113 pitches (CG, W)
- Don Larsen: 9.0 IP, 7 H, 4 R, 3 ER, 10 K, 4 BB, 116 pitches (CG, L)

ATMOSPHERIC DATA:
  Weather: Rain (60 degrees), no wind
  Attendance: 43,472
  Game duration: 2:52
  Start time: 1:05 PM EST
  Ballpark: Yankee Stadium I

WALK-OFF: No (Brooklyn is the visiting team)

LARSEN LINE: Don Larsen — 9.0 IP, 7 H, 4 R, 3 ER, 10 K, 4 BB, 116 pitches, Game Score 65. Went the distance despite allowing 4 runs — no bullpen help. Struck out 10 Dodgers but walked 4, and Robinson got to him for a homer and a key walk.
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
- Does the recap mention Larsen's performance in some way? (His unraveling is central to the project's identity)
