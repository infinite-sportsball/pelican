# Prompt for Revising OOTP Recap Text — Infinite Cleveland

## Context

The "Infinite Cleveland" project simulates 1997 World Series Game 3 (Cleveland Indians vs Florida Marlins at Jacobs
Field) 69 times. Each simulation produces an almanac with a box score HTML file containing a game recap between
`<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers. These recaps are boilerplate OOTP templates — nearly
identical across all 69 games, differing only in the final score and MVP name. The goal is to replace them with
distinctive prose that captures the project's Groundhog Day conceit in Roger Angell's voice.

This prompt uses a **two-pass approach**: a data-digestion pass that extracts and structures the game's key
moments, followed by a narrative-generation pass that writes the Angell prose from that digest. This separation
keeps the analytical and literary tasks from competing for the model's attention.

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
GAME: 1997 World Series Game 3
DATE: October 26, 1997
VENUE: Jacobs Field

FINAL SCORE: {Winner} {runs}, {Loser} {runs}
INNINGS: {number}

LINE SCORE:
  Florida:     {inning scores separated by spaces} — {R} H:{H} E:{E}
  Cleveland:   {inning scores separated by spaces} — {R} H:{H} E:{E}

PLAYER OF THE GAME: {name from box score game notes}

GAME SHAPE: {Classify as one of: blowout, wire-to-wire lead, pitchers' duel, comeback, seesaw, walk-off, extra-innings}

GAME FLOW: {2-3 factual sentences describing how the game unfolded — who scored when, when the lead changed, how it ended. Reference specific innings.}

STARTING PITCHERS:
  Florida:   {name}
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

For each of the 69 games, you need to assemble the following inputs for the Pass 1 prompt.

### 1. From the folder name
The folder name encodes the game number and final score:
```
infinite_cleveland_g{NN}_{winner_abbrev}{winner_runs}{loser_abbrev}{loser_runs}
```
Example: `infinite_cleveland_g01_cle15fla14` → Timeline 1, Cleveland 15, San Diego 14

Team abbreviations: `cle` = Cleveland Indians, `fla` = Florida Marlins.

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
  - "1. Top 3rd: E. Renteria hit a 2-run double vs C. Nagy"
  - "2. Bot 5th: J. Thome hit a 2-run home run vs A. Leiter"

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
  Cleveland 1997 Indians batting - Pitching for Florida 1997 Marlins : RHP Kevin Brown
</th>
```

Each half-inning ends with a summary line:
```html
<td class="datathbg" colspan="2">
  Top of the 7th over - 2 runs, 3 hits, 1 error, 2 left on base; Florida 1997 4 - Cleveland 1997 3
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
- **Pitcher changes** appear inline: `Pitching: LHP Jim Smith`
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
You are writing a 3-4 paragraph game recap for Timeline #{game_number} of "Infinite Cleveland" — a project that simulates 1997 World Series Game 3 between the Cleveland Indians and Florida Marlins at Jacobs Field, October 21, 1997, ninety-two times over.

THE CONCEIT: These players are trapped in an endless loop. The same game, the same October Tuesday night, replayed with different outcomes each time. The players don't know. They experience each game as singular. But you, the writer, know — and that knowledge should haunt the prose at its edges. A flicker of déjà vu. The eerie sense that Thome has stood in this box before, that Gwynn has lined one through the left side in some other version of tonight. Don't belabor it. One or two glancing references per piece. The uncanny feeling, not the explanation.

VOICE: Write in the style of Roger Angell — the New Yorker's baseball essayist for six decades. His hallmarks:
- Long, musical sentences that unspool with the patience of a 3-2 count
- Precise physical and spatial detail: the geometry of a relay throw, the specific arc of a fly ball against October sky, the sound of forty-four thousand people inhaling at once
- The sense of *being there* — the particular cold of a Cleveland October, the light towers making everything both vivid and slightly unreal, the quality of noise in a ballpark that hasn't won a championship since 1948
- Emotional calibration: Cleveland is fighting to end a fifty-year drought, and every win gets the team one step closer. The crowd isn't politely applauding — they're losing their minds. The ending must match the stakes. Conversely, a Marlins win means cold, miserable, silent Cleveland fans filing out of the building. Get the emotional physics right.
- Wry warmth without sentimentality; humor that respects its subject
- Baseball understood as a meditation on time and repetition (which maps perfectly here)
- Trust the reader — no explaining rules, no cheap drama, no exclamation points

WHAT TO INCLUDE:
- The final score and which team won
- The decisive moment(s): the walk-off hit, the late rally, the key strikeout — whatever turned this particular version of the night. Be specific: name the pitch count, the fielder, the distance.
- At least 2-3 specific player names tied to what they actually did in THIS game
- When first mentioning a player in the recap — especially in the opening sentence — establish which team they play for. The reader hasn't memorized the lineup card. "Al Leiter had spent the evening..." means nothing until you say "the Florida starter." This applies to every first mention throughout the piece, not just the opener. Never assume the reader is already inside the game or has team rosters memorized.
- The shape of the game: a blowout that was over by the 4th? A pitchers' duel cracked open in the 8th? A seesaw with lead changes every other inning?
- Something about the starting pitchers' day — how many innings Al Leiter or Charles Nagy lasted, how hard they were hit, whether things unraveled early or late
- One vivid sensory detail grounded in the physical world of Jacobs Field
- A light reference to this being one iteration among many — "the ninety-second telling," "in this particular shuffling of the deck," "once more the lineup cards were exchanged" — but never more than a line or two

WHAT TO AVOID:
- Opening with a bare statistical declaration, a decontextualized game-state summary, or a player's name without identifying context. This includes "X hit Y home runs," "X hit a ball Y feet," "X went Y-for-Z," "The game was tied at two through six innings," "The hit cleared the fence," and critically: any sentence that opens with just a name. A name alone tells the reader nothing — who is this person, what team are they on? Give them their role: "Cleveland starter Charles Nagy," "the Marlins' left fielder Cliff Floyd," etc. The opening sentence must orient the reader — give them a team, a place, a feeling, a human being doing something specific. Stats and game states belong in the body of the prose where they illuminate what happened; they are not leads. Vary the entry point for every recap: a scene, a player in a moment, the quality of the night, a narrative observation. Never open two recaps the same way.
- Short dramatic reversal sentences: "They had not." "It was not." "He did not." "It did not last." Any three-to-five word sentence that exists solely as a theatrical pivot or dramatic beat. Angell would never write a sentence like that — he would fold the reversal into the texture of a longer, more considered sentence. These clipped pivots are an AI writing tic, not literary prose.
- Sports clichés ("gave 110%", "clutch performance", "wanted it more")
- The word "destiny"
- Direct player or manager quotes (no one actually said anything — this is a simulation)
- Any mention of regular season records, franchise history beyond what's in the conceit, or "Simyou Lator Engine"
- Being heavy-handed about the simulation concept
- Concluding with a grand run-on sentence about timelines, exchanging lineup cards, anthems being sung, or patterns reasserting themselves. This is filler — a ham-handed attempt to tie a bow on the piece by restating the simulation conceit in flowery language. But don't overcorrect into an abrupt cutoff either — the piece still needs a proper landing.
- Endings that fail to deliver the emotional verdict. The final sentence must make the reader feel who won and what it meant. This is the single most important sentence in the piece — not a place for wry summations, combined stat lines, atmospheric scene-setting, or clever observations about the nature of the game. The last sentence is the emotional detonator, not a denouement.
  - **The final sentence**: should be concrete and particular to THIS game — name a player, name what they did, name what the crowd felt. Never end on an abstraction, a metaphor about baseball, a wry aside about the stat line, or a scene of people leaving. The reader's last impression must be the emotional truth of the outcome, not a writerly observation about it.
  - **A direction worth considering — the closing snapshot of a single player.** One of the most effective endings is not a panorama of the crowd or the city or the cold, but a tight close-up of a single human being at the moment the game ended — the player who quietly delivered the dagger standing at his position with a private, almost embarrassed half-smile; the Player of the Game catching the last out and not yet allowing himself to react; the one batter who both opened the scoring and made the final out walking back to the dugout with the particular weight of having bookended the night; the closer with the ball still in his glove. The image works because it lets the reader see the result in a body, not in a sentence about a result. When you can identify the player whose individual story most fully contains the game's verdict — the one who started AND finished the scoring, the one whose at-bat was the hinge, the one whose final pitch ended it — closing on a still image of THAT person at THAT moment can land harder than any rhetorical move. This is one option among several, not a formula; vary your endings so no two recaps close the same way.
  - **CRITICAL — get the post-game body language right for winners vs. losers.** Winning players do NOT sit in the dugout, jam their hands in their pockets, lean on the rail, or look contemplatively out at the field when their team wins the World Series. They sprint out of the dugout, they meet the winning run at the plate, they celebrate on the field. The cold doesn't exist anymore; the weather doesn't exist anymore; nothing exists except the win. LOSING players are the ones who sit in the dugout with their hands jammed in their pockets, feeling the cold, contemplating the long road ahead. Losing players go still. Losing players stare. Never assign losing-team body language to winning-team players, or vice versa.
- Dumping stats in the closing paragraph. The final paragraph is the emotional climax — it is not the place to recite combined hit totals, final scores with both teams' run counts, pitch counts, the number of runs scored by both teams combined, the temperature, or any other numerical inventory. Statistics belong in the body of the piece where they do narrative work — establishing a pitcher's collapse, showing how a rally built, conveying dominance. But the closing paragraph should be operating in a purely emotional register. If a number appears in your final paragraph, ask whether it serves the feeling or interrupts it. "Thirty-three hits" in a closing sentence is a sportswriter's tic, not a literary one — it converts the ending into a box-score summary right when the reader needs to feel something. One specific number tied to a specific human moment (a distance, a count) can work; a statistical roll call cannot.
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

## AI Failure Modes — Pre-Flight Checklist

These are recurring errors observed across many subagent-generated Pass 2 narratives. Check each one before accepting any recap.

1. **Final-out / catcher confusion.** When the final out is a strikeout, the ball is in the **catcher's** mitt, NOT the pitcher's glove. "The ball was still in [Pitcher]'s glove" on a strikeout ending is an automatic error.

2. **Fielder-team errors.** Subagents repeatedly assign outs to fielders on the wrong team. Cross-check: who plays that position for the FIELDING team in THIS game? Craig Counsell is a Marlin — never put a Cleveland out in his glove. Cliff Floyd is the Marlins LF; balls to right are caught by Gary Sheffield (RF). Etc.

3. **OOTP hit-location geometry.** Numeric prefixes follow the standard: **7 = left, 8 = center, 9 = right.** "9LD" = right field deep, NOT left-center. "7D" = left field deep. Never trust the subagent's directional prose on home runs and doubles — verify against the prefix in the PBP/digest.

4. **Pitch-type fabrication.** The PBP gives count and result, not pitch type. "Slider," "fastball," "changeup," "sinker" — if it isn't in the digest, don't assert it. Use "pitch" instead.

5. **Score / inning-state errors.** Subagents miscount innings ago ("four innings earlier" when it was two), misreport runners on base ("bases loaded" when only second and third were occupied), and invert who scored on a play. Cross-check line-score totals against the digest's KEY MOMENTS.

6. **RBI-accounting overcount.** Subagents sometimes claim a play scored more runs than actually crossed (e.g., "three runs scored, and a fourth on the throw home" when the actual total was three).

7. **Final-out geometry.** A "6-4 fielder's choice" means the shortstop fed the second baseman; the runner from first is forced at 2B; the BATTER reaches first safely. The batter is NOT "thrown out at second." A "4-3" grounder ends at first base — the throw arrives at first, not at second base.

8. **Position-of-fielder fabrication.** Don't name fielders the PBP doesn't name. "Through the second baseman's glove" is fine if the code is 4D; "off the third baseman's bag" requires evidence.

9. **Banned phrasings creeping back in.**
   - "Destined to" / "destiny" — banned.
   - Clipped dramatic-reversal sentences ("It did not last." "They had not." "He did not.") — banned; AI tics, not literary prose.
   - "Less a baseball game than a [X]" / "like two men passing [Y] back and forth" — recurring AI tropes; vary the analogy.
   - "Coming apart at the seams" — banned.
   - "Halfway out the door" used to mean "leaving the dugout" — players don't leave through doors when they go onto the field.
   - "Waved over a pitch" — not a phrase. Use "swung through," "waved at," "took a cut at."

10. **Body-language inversion.** WINNERS sprint, mob, pile on. LOSERS sit still, jam hands in pockets, stare. A celebrating Marlins outfielder does NOT "jog in with a small private smile." A losing Cleveland reliever does NOT charge the mound. The Player of the Game on the winning side does NOT "allow himself" anything — he is past control.

11. **Crowd composition errors.** Game 3 attendance is not 44,880 Clevelanders. There is a sizable Florida contingent and traveling media. Use "the Cleveland faithful," "forty-four thousand," "the home crowd" — not "44,880 Clevelanders" as if every seat held a hometown fan. Also: when Florida wins, the home crowd starts streaming for the exits — they do not sit and watch the visitors celebrate.

12. **Conceit overreach.** "Had stood in this same box in some other version of this same night" — too on-the-nose. The prompt allows 1–2 glancing references; subagents often hit 3–4 explicit ones. Cut all but the lightest.

13. **"Bookended" closing image.** When a player figures in both the opening and closing of the game, that's a high-leverage closing image — but verify which inning they actually batted in. Don't say "nine innings earlier" if it was actually the seventh.

14. **Pitcher-decision shorthand.** "Won" / "lost" should match the official decision. Be careful with "BS+W" combos (blown save AND win) — these are real but unusual.

15. **No-hitter watch.** If a starting pitcher's line shows 1 hit, locate which inning that hit came in. A late-broken no-hit bid is a meaningful narrative beat that should be acknowledged. A 1-hit complete game is a one-hitter, not just a shutout.

16. **Ramirez & defensive plays.** Manny was famously known for his bat, not his glove. A small Ramirez defensive lapse (stutter step on a throw, late jump) is in character. A boneheaded play (forgetting outs, dropping a routine fly) is overkill.

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
- Run through the AI Failure Modes Pre-Flight Checklist above.

