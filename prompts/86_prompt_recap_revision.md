# Prompt for Revising OOTP Recap Text - Rocket vs Ryan (Universe 86)

## Context

The "Rocket vs Ryan" project simulates a hypothetical 1986 World Series Game 2 (Boston Red Sox at Houston Astros, Astrodome, October 19, 1986) eighty-six times. Each simulation produces an almanac with a box score HTML file containing a game recap between `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers. These recaps are boilerplate OOTP templates - nearly identical across all 86 games, differing only in the final score, Player of the Game name, and a manager quote from "Jim Smith" (a template placeholder OOTP never fills in). The goal is to replace them with distinctive prose that captures the project's Groundhog Day conceit in a **Ron Shelton (Bull Durham) narrator voice**, with **heavy Jon Bois-style statistical setpieces** built into the narrative - reveling in the specific absurdities that emerge across the 86-game corpus.

This is deliberately a different voice from the other four universes (56, 72, 97, 98), which all use Roger Angell. Angell's cathedral tone and long musical sentences are the exact wrong register for the Astrodome. This universe is a circus - a plastic-domed circus with pistol-firing bulls, rainbow-gut uniforms, and a 24-year-old MVP pitching against a 39-year-old power arm in front of a Texas judge's ghost. It needs a narrator who's comfortable with the ridiculousness AND the beauty.

This prompt uses the same **two-pass approach** established for Universe 98 (`infcle2_prompt_recap_revision.md`): a data-digestion pass that extracts and structures the game's key moments, followed by a narrative-generation pass that writes the prose from that digest. This separation keeps the analytical and literary tasks from competing for the model's attention.

### The Alternate History

In reality, the 1986 World Series was Boston vs. the New York Mets. Houston lost the NLCS to the Mets 4-2, in a series that included Nolan Ryan's 9-inning, 2-hit, 12-K performance in Game 5. If Houston had won that NLCS, the World Series would have been Roger Clemens vs. Nolan Ryan - two of the greatest pitchers of their generation. That's the universe this simulation runs.

Game 6 of the real 1986 WS is what Boston fans remember: Buckner's ball-through-the-legs, blowing a 5-3 lead in the 10th, Mets winning 6-5. Two nights later, Boston blew a 3-0 lead in Game 7 and lost 8-5. Bill Buckner became a noun. The Curse of the Bambino - Boston's inability to win a World Series since Harry Frazee sold Babe Ruth to the Yankees on December 26, 1919 - had been sixty-eight years running by October 1986. It would run another eighteen. In this simulation, that curse is the freight every Boston at-bat carries, and Buckner is on the field, playing first base, one bad hop away from becoming the man he became in some other version of this same October. In this universe, his bat keeps finding Nolan Ryan for home runs instead.

### The Fixed Matchup

Every game features the same starting pitchers:

- **Roger Clemens (Boston)** - 24 years old, fourteen months out of shoulder surgery (Dr. James Andrews, torn labrum, 1985). 1986 was his first fully healthy season: 24-4, 2.48 ERA, 238 K, 254 IP. AL Cy Young. AL MVP - the first starting pitcher to win MVP since Vida Blue in 1971, next after him would be Verlander in 2011. Threw the first 20-strikeout game in MLB history on April 29, 1986 vs. Seattle. In real-life Game 2 of the '86 WS, he was pulled with a 6-2 lead in the 5th on three days' rest and got a no-decision. In this simulation, he takes the mound 86 nights in a row.
- **Nolan Ryan (Houston)** - 39 years old, in his seventh season as an Astro. 1986 season: 12-8, 3.34 ERA, 194 K in 178 IP. Would go on to pitch until age 46, throw his 7th no-hitter at 44, and record his 5,000th career strikeout in 1989. In real-life NLCS Game 5, he threw 9 innings, 2 hits, 12 K, and Houston lost 2-1 in 12 innings.

Both pitchers throw the entire 86-game series. The results across those 86 games:

- Ryan: 34-24 with 28 no-decisions, 2.52 ERA, 717 K in 663⅓ IP (8.34 K per start, 9.73 per nine - almost exactly his real 1986 rate of 9.8), 10 complete games, 6 shutouts, 46 Player of the Game awards
- Clemens: 29-39 with 18 no-decisions, 3.07 ERA, 541 K in 675⅓ IP, 60 HR allowed, 66 starts of 8+ IP, 28 Player of the Game awards. 33 official complete games, but 26 of those are eight-inning road losses (Houston led, so the bottom of the 9th was never played); in his seven complete games of nine innings or more he went 7-0
- Clemens at the plate (NL rules, no DH): 9-for-225, .040, 156 K, 1 HR - hit off Nolan Ryan leading off the fifth inning of Game 2. Ryan at the plate: 13-for-182, .071
- Houston walked off Boston 11 times. Bob Stanley took the loss in eight of them
- Bill Buckner hit 8 HR, seven of them off Ryan (the eighth was a two-out 9th-inning grand slam off Kerfeld in Game 47)
- Glenn Davis hit 14 HR, thirteen of them off Clemens. Denny Walling hit 15, all fifteen off Clemens. Kevin Bass hit 10, all ten off Clemens
- Two Madduxes (complete game in under 100 pitches): Ryan in Game 79 (94 pitches, 9-inning shutout) and Clemens in Game 57 (96 pitches, 8-inning complete-game loss)

`prompts/PlanUniverse86Themes.md` catalogs the deep patterns across the corpus (Seven Lists format). Use them as *textures* that occasionally surface in a recap when the specific game triggers them - never as the recap's subject. The per-game recap tells the story of ONE game. The seven-lists themes belong at the top-level almanac index page.

### The Rosters (fixed, actual 1986 Game 2 lineups)

**Boston Red Sox (away, bat first):**
- Wade Boggs (3B) - Hall of Famer, .357 BA in real 1986
- Marty Barrett (2B) - had 13 hits in real '86 WS (WS record for a 7-game series)
- Bill Buckner (1B) - 34 years old, ankle wraps, one week from the noun
- Jim Rice (LF) - cleanup, real '86: .324, 20 HR, 110 RBI
- Dwight Evans (RF) - Gold Glove arm in RF
- Rich Gedman (C)
- Dave Henderson (CF) - the ALCS Game 5 hero, home run off Donnie Moore
- Spike Owen (SS) - trade-deadline pickup from Seattle
- Roger Clemens (P)

**Houston Astros (home, bat last):**
- Bill Doran (2B)
- Billy Hatcher (CF)
- Denny Walling (3B) - hit .307 in the series; every one of his 15 home runs came off Clemens
- Glenn Davis (1B) - 31 HR in real '86, franchise cornerstone
- Kevin Bass (RF) - .311 in real '86
- Jose Cruz (LF) - "Cheo," the Astros' longtime face
- Alan Ashby (C)
- Craig Reynolds (SS)
- Nolan Ryan (P)

Houston bench regulars: Phil Garner (the go-to pinch hitter; also pitched the 13th inning of Game 4), Davey Lopes (pitched in the 13th inning of Game 10), Dickie Thon. Boston bench: Don Baylor (pinch hitter, 2 HR including the 10th-inning game-winner off Ryan in Game 56), Ed Romero, Mike Greenwell, Dave Stapleton.

Bullpens actually used in the corpus: Boston - Bob Stanley (closer, 39 appearances, 22 saves, 9 losses), Calvin Schiraldi, Steve Crawford. Houston - Charlie Kerfeld (73 appearances), Larry Andersen. Joe Sambito, Aurelio Lopez, and Dave Smith never pitched; do not put them on the mound.

### The Venue: The Eighth Wonder of the World, aging

**The Astrodome, Houston** - the freakiest ballpark ever built in the major leagues, and the single strongest vein of Jon Bois-flavor absurdity available to this project. The venue itself is a recurring character; you should be reaching for its specific weirdness at least once per recap.

**Origin story.** Opened April 9, 1965 as the world's first fully-enclosed, air-conditioned domed stadium. Judge Roy Hofheinz called it "The Eighth Wonder of the World" and by 1965 he was not entirely wrong. It was built because Houston in summer is uninhabitable and Hofheinz decided the future of baseball was going to happen indoors, in air conditioning, on a surface that could be vacuumed. Twenty-one years later, in 1986, the building is starting to show its age. But nothing else on earth looks like it.

**The roof and the grass problem.** The original roof had 4,796 semi-transparent plastic panels that let sunlight in so grass could grow. It didn't work. The glare made fly balls impossible to track - Mickey Mantle in a 1965 exhibition famously lost one, and outfielders started wearing batting helmets and sunglasses. So they painted the roof panels. Now the grass died. So in 1966 they invented AstroTurf, a nylon-fiber carpet named for the stadium, and rolled it over the dirt. **The Astrodome is the reason artificial turf exists.** In 1986 the field is AstroTurf-8, worn thin along the base paths, with seams the groundskeepers tape down between innings. A hard ground ball skips on it like a stone on a lake. An outfielder in Astrodome carpet chases a ball that never slows down.

**The scoreboard.** The largest in baseball - 474 feet across, three stories tall, occupying the entire outfield wall in center. When a HOME TEAM Astro hits a home run, the scoreboard's centerpiece animation plays: a giant electronic **bull** with steam coming out of its nostrils, flanked by cowboys, spaceships, and a full-color rainbow. The bull fires two pistols. Firecrackers go off. A sequence of American flags waves. Cattle brands scroll past. The whole thing takes forty seconds. When a road-team player homers, none of this happens - just the runs update on the line score. In this simulation you will have games with FIVE or SIX Astros home runs. The bull will fire pistols six times. In games where Boston homers three times off Ryan and Houston doesn't answer, the bull is silent all night, which is somehow worse.

**The uniforms.** In 1986, the Astros wear the **rainbow guts** - a horizontal navy-orange-red-orange-yellow gradient across the chest, on both home whites and road grays, unmatched in baseball history for pure visual chaos. Rice picked their colors to match Texas sunsets. Nobody outside Houston can talk about them without laughing. Nolan Ryan pitches in this uniform. Take a moment to sit with that. Boston wears their standard road grays, boring and Puritan, which is exactly what a curse-carrying team should wear inside a rainbow-gut stadium.

**The gimmicks Roy Hofheinz built in.** Cushioned "sky boxes" (a term he invented). His own personal apartment inside the stadium, complete with putting green and barber's chair. A fold-up seat design so that ushers could spot who was still sitting after the seventh-inning stretch and hustle them for a beer order. A bowling alley in the concourse. A private chapel for the Judge. A bank vault for the ticket receipts. The building is less a baseball park than a monument to one Texan's belief that everything in the world should be indoors and slightly on fire.

**No weather. Ever.** Roof always closed - it was built enclosed and does not open. No wind. No sun on the field. No rain. No cold. No stars. No moon. No October chill. The building's air is the same temperature every night of every season. There is no atmosphere to describe in the outdoor sense. Everything atmospheric in a Universe 86 recap must be about the ARCHITECTURE of the dome and the theatrical apparatus of the scoreboard and the crowd.

**Sound.** The dome traps noise. A cheer doesn't dissipate the way it does at Fenway - it hits the roof and rains back down. A hush inside a dome is different from a hush outdoors; it has a physical presence. When Houston walks off in the 9th, forty-six thousand people erupt inside a sealed container, and the noise has nowhere to go. When Houston loses, the silence is louder than any silence should be.

**Dimensions and how the park plays.** 340 (LF) - 375 (LF-CF power alley) - 400 (CF) - 375 (RF-CF power alley) - 340 (RF). The heavy, still, air-conditioned air of the dome kills fly balls - the ball doesn't carry. This is a pitcher's park. In 86 games there were 110 total home runs in this simulation - a rate of 1.28 per game, well below the '86 major-league average of ~1.85. Both Ryan and Clemens benefit from pitching here. Home runs earned inside the dome are earned.

**Attendance.** Use 46,101 every game - the figure in each box score's page header. The OOTP game notes at the bottom of the box score show a different, varying number (about 32,500-32,800); ignore it. The Astrodome held roughly 45,000 for baseball in 1986; the 54,816 figure often quoted is from after the 1989-90 expansion. Note that the real 1986 Astros didn't sell out most games - the Astrodome was chronically half-empty in the '80s. In our universe, this is the World Series; the place is full every night.

**A note on tone.** The Astrodome is inherently absurd. Do not pretend otherwise. When a recap needs a Bois-flavor beat, the Astrodome is your first tool - a Houston home run triggers the bull, the pistols, the rainbow, and forty seconds of scoreboard theater between a home-run trot and the next batter. Boston fans, sixty-eight years into a drought and one week from a curse they don't know is coming, are watching this play out under the specific plastic acoustics of a dome named for a rocket program. The visual gap between what they are wearing (drab road grays, tight expressions) and what surrounds them (rainbow guts, animated bulls, spaceships) is inherently a story. Angell would notice it. Bois would name it. You should do both.

---

## Two-Pass Overview

**Pass 1 (Game Digest):** Analytical. Reads the raw HTML play-by-play, box score, and WPA chart image. Produces a structured text summary of the game.

**Pass 2 (Narrative):** Literary. Reads only the Pass 1 digest (no HTML, no images). Writes 3-4 paragraphs of Shelton-voice narration with embedded Bois statistical setpieces.

---

## Target Voice: A Calibration Example

Before the prompts themselves, here is a paragraph in the target voice. Use it as the tuning fork for what the recaps should sound like.

Timeline 11 (Houston 2, Boston 1 - Glenn Davis game-tying HR off Clemens leading off the bottom of the 9th; walk-off on a Dwight Evans throwing error off Bob Stanley):

> Glenn Davis had spent eight innings watching Roger Clemens get the Houston lineup out, himself included - a popup in the first, a strikeout in the fourth, a walk in the sixth - and had gone back to the dugout each time with the quiet of a man doing math in his head. Dwight Evans had put Nolan Ryan's first pitch of the second inning 369 feet into the right-field seats, and that was the whole scoreboard. Clemens, 24 years old with a shoulder he'd had cleaned out fourteen months ago and a Cy Young season in his back pocket, walked out for the bottom of the ninth at 100 pitches with a 1-0 lead and looked like he could go another three innings if you asked him to. So Boston did. Then Davis, leading off, took a 2-1 pitch and drove it 395 feet, and the big animated bull up on the scoreboard fired its pistols, and forty-six thousand people inside a sealed dome named after a rocket program made a noise that had nowhere to go but back down onto the field. Davis rounded the bases inside a stadium designed by a Texas judge who believed the future would be air-conditioned. That was the end of Clemens's night. Bob Stanley came in and gave up two singles, and when Evans's throw from right got away, Kevin Bass came around to score and it was over. It was the first time Glenn Davis had ever hit a home run off Roger Clemens. In this loop, over the course of a lot of Sunday nights that hadn't happened yet, it would not be the last. Every home run he hit in this series from then on would be off the same pitcher.

What that paragraph is doing, that the recaps should also do:

- **Narrator with a chair in the dugout.** He knows Davis's mental state, knows Clemens' shoulder history, knows Clemens walked out for the ninth at exactly 100 pitches. He's not omniscient in a literary way - he's just been around this game long enough to know these people.
- **Stats embedded in narrative, not tabled.** "100 pitches with a 1-0 lead," "24 years old with a shoulder he'd had cleaned out fourteen months ago," "395 feet" - facts that pull weight in the sentence, not decorations.
- **The corpus-aware pivot.** The fourth-wall break is real but earned: "It was the first time Glenn Davis had ever hit a home run off Roger Clemens. In this loop, over the course of a lot of Sunday nights that hadn't happened yet, it would not be the last." That's the Bois beat - one specific pattern named with dry precision.
- **The Astrodome as circus.** "Big animated bull," "sealed dome named after a rocket program," "stadium designed by a Texas judge who believed the future would be air-conditioned." The building is a character; the ridiculousness is part of the beauty.
- **Long sentences that DON'T sound like Angell.** They're loose, comma-strung, plainspoken. They pile up specifics. They're not musical; they're colloquial. That's the Shelton thing.
- **NOT idealizing the players.** Davis is doing math. Clemens looks like he could go three more innings. Nobody is a hero of destiny. They're grown men doing a strange job on a Sunday night.

The recaps should sound like *that*, adjusted for whatever the specific game demands.

---

## Pass 1: Game Digest Prompt

```
You are a baseball data analyst preparing a structured game summary. Your job is to extract facts from the provided game data - no literary embellishment, no opinions, no invented details. Include ONLY information that can be verified from the provided sources.

You will be given:
1. A WPA (Win Probability Added) chart image showing the game flow and 4 annotated key moments
2. The full play-by-play HTML game log
3. The box score HTML with line score, batting/pitching tables, and game notes
4. The game folder name (encoding timeline number and final score)

From these sources, produce the following structured output:

TIMELINE: {number}
GAME: 1986 World Series Game 2 (alternate history: BOS vs HOU)
DATE: October 19, 1986
VENUE: Astrodome

FINAL SCORE: {Winner} {runs}, {Loser} {runs}
INNINGS: {number}

LINE SCORE:
  Boston:      {inning scores separated by spaces} - {R} H:{H} E:{E}
  Houston:     {inning scores separated by spaces} - {R} H:{H} E:{E}

PLAYER OF THE GAME: {name from box score game notes}

GAME SHAPE: {Classify as one of: blowout, wire-to-wire lead, pitchers' duel, comeback, seesaw, walk-off, extra-innings}

GAME FLOW: {2-3 factual sentences describing how the game unfolded - who scored when, when the lead changed, how it ended. Reference specific innings.}

STARTING PITCHERS:
  Boston:  Roger Clemens
  Houston: Nolan Ryan
WINNING PITCHER: {name} {decision, e.g. W (1-0)}
LOSING PITCHER: {name} {decision}
SAVE: {name and decision, or "none"}

STARTER LINES (both, always):
  Clemens: {IP, H, R, ER, K, BB, PI pitches, HR allowed}
  Ryan:    {IP, H, R, ER, K, BB, PI pitches, HR allowed}

KEY MOMENTS (3-4 plays ranked by impact on game outcome, using the WPA chart annotations as your primary guide, enriched with pitch-level detail from the play-by-play):

1. {INNING, HALF}: {Batter full name} - {what happened}
   Pitcher: {name}
   Game state before: {score}, {outs} out, runners on {bases or "none"}
   Game state after: {new score}
   Detail: {pitch count at result, hit type, exit velocity, distance if HR, runner movement}

2. {repeat}

3. {repeat}

4. {repeat if applicable}

DECISIVE MOMENT: {Which of the above was THE turning point, in one sentence, and why.}

NOTABLE PERFORMANCES:
- {Player}: {batting line from box score}
- {Player}: {batting line}
- {Pitcher}: {IP, H, R, ER, K, BB, PI pitches}

CLEMENS AT THE PLATE: {his line, always - even if 0-for-3 with 3 K. This is a running thread across the corpus.}

RYAN K COUNT: {integer, always - it's the corpus's most-tracked stat}

WALK-OFF: {yes/no - if yes, describe the final at-bat sequence: batter, count, result, who scored, final score. Note if Houston came from behind in the 9th.}

BULLPEN NOTES:
  Boston: {who came in, when, what happened - Bob Stanley appearances matter - he took the loss in 8 of the 11 walk-offs}
  Houston: {who came in, when, what happened - Kerfeld and Andersen are the only relievers Houston uses}

CORPUS-LEVEL FLAGS (check each; mark yes/no/na):
- Ryan struck out 12+? {yes/no}
- Ryan complete game? {yes/no}
- Clemens complete game? {yes/no}
- Boston shut out? {yes/no}
- Houston shut out? {yes/no}
- Buckner HR off Ryan? {yes/no}
- Glenn Davis HR off Clemens? {yes/no}
- Denny Walling HR off Clemens? {yes/no - all 15 of his series HRs are off Clemens}
- Kevin Bass HR off Clemens? {yes/no}
- Boggs/Rice/Barrett/Evans/Henderson HR off Ryan? {list which, if any}
- Boston LOB >= 15? {yes/no, actual number}
- Houston 8th-inning rally (2+ runs)? {yes/no}
- Extra innings? {yes/no}
- Dave Henderson 0-fer with multi-K? {yes/no}
- Clemens at the plate: got a hit? {yes/no}
- Bob Stanley took the loss on a walk-off? {yes/no}
- Ryan no-hit bid through 6+ innings? {yes/no - if yes, inning and batter of the first hit}
- Maddux (complete game in under 100 pitches) by either starter? {yes/no, pitch count}. Note: a Clemens eight-inning complete-game loss counts; only two exist in the corpus (Ryan g79, Clemens g57)
- Position player pitching? {yes/no - Garner g4, Lopes g10}

ATMOSPHERIC DATA:
  Attendance: 46,101 (fixed across corpus; from the page header, not the OOTP game notes)
  Game duration: {from box score game notes}
  Start time: 8:05 PM EST (fixed)
  Ballpark: Astrodome (dome closed, no weather)
```

---

## Pass 1: Data Sources & Extraction Guide

### 1. From the folder name

The folder name encodes the game number and final score:
```
rocket_vs_ryan_g{NN}_{winner_abbrev}{winner_runs}{loser_abbrev}{loser_runs}
```
Example: `rocket_vs_ryan_g01_bos6hou5` -> Timeline 1, Boston 6, Houston 5.

Team abbreviations: `bos` = Boston Red Sox, `hou` = Houston Astros.

Some folder names have suffixes like `_10inn`, `_12inn`, `_15inn` for extra-inning games, or descriptive tags like `_brawl` or `_nightmare2` if the human has annotated them. Preserve the timeline number; ignore the tags for Pass 1.

### 2. From `box_scores/game_box_1.html`

- **Inning-by-inning line score**: Found in the top data table. Each `<td class="dc">` contains one inning's runs. Final three columns are R/H/E.
- **Winning team headline**: The `<td class="boxtitle">` inside `<!--RECAP_START-->`.
- **Player of the Game**: In the game notes near the bottom, `<b>Player of the Game: </b>` then a name.
- **Atmospheric data**: Ballpark (always Astrodome), Start Time (always 8:05 PM EST), Time (game duration - varies), Attendance (use 46,101 from the page header; the OOTP game-notes figure of ~32,600 is wrong and varies). **No Weather field for indoor games** - this is a dome.
- **WPA chart**: An `<img>` reference to `../images/wpa/wpa_1.png` - loaded separately as an image input.

### 3. From `images/wpa/wpa_1.png`

Same format as other universes. Four numbered annotations identifying the highest-leverage plays. Use them as the primary guide for KEY MOMENTS.

### 4. From `game_logs/log_1.html`

Same structure as other universes. Search for `<b>` tags within the innings where the WPA annotations happened. Note:
- Ryan's pitch-type isn't in the PBP - the sim doesn't export it - so don't attribute pitches by type. "Fastball" is broadly safe for Ryan given his real-life reputation, but only if the K is clearly a swinging strike; better to say "pitch" and let the count carry the drama.
- Clemens' at-bats matter for the corpus - always record whether he made contact, got a hit, or struck out. He goes 0-for-3 or 0-for-4 with multiple Ks in the vast majority of these games; the rare hit is a small event worth flagging.

---

## Pass 2: Narrative Prompt

```
You are writing a 3-4 paragraph game recap for Timeline #{game_number} of "Rocket vs Ryan" - a project that simulates a hypothetical 1986 World Series Game 2 between the Boston Red Sox and the Houston Astros at the Astrodome, October 19, 1986, eighty-six times over. In the real 1986 World Series, Boston played the Mets; this universe replaces the Mets with the Astros, giving us Roger Clemens vs Nolan Ryan for the entire series. Every game is Clemens vs Ryan.

THE CONCEIT: These players are trapped in an endless loop. The same game, the same October Sunday night at the Astrodome, replayed with different outcomes each time. The players don't know. They experience each game as singular. You, the writer, know - and you can name it when the numbers demand it. The Bois-style fourth-wall break is legal and encouraged, but only when a specific pattern in THIS game connects to something the corpus has already been building: Buckner homering off Ryan for the sixth time, Henderson striking out four times in a game for the fourth time, Kevin Bass going deep off Clemens for the seventh time. If the specific game doesn't hit one of those veins, don't force it - just tell the game.

THE FREIGHT BOSTON CARRIES: Sixty-eight years. Boston hasn't won a World Series since 1918. Harry Frazee sold Babe Ruth to the Yankees on December 26, 1919, and Boston has been looking at the trophy through glass ever since. This is 1986 - eighteen more years to go before the drought breaks - and every Boston at-bat has the weight of the Curse of the Bambino behind it. Bill Buckner is on the field, one week from becoming Bill Buckner-the-noun in some other universe. In THIS universe, his bat keeps finding Nolan Ryan for home runs, but he doesn't know that either. Do not name the curse. It should be a texture you feel behind the prose, not a mascot you wave around. Reference the real Game 6 or the real Game 7 or "the ball through the legs" once per recap at most, and only if the specific game genuinely gives you the hook. The reader knows. Trust them.

WHAT HOUSTON DOES NOT CARRY: The Astros are a 24-year-old expansion team in 1986. They've never been to a World Series. There is no curse; there is only inexperience and the pressure of a first-time chance. Their weight is "we've never done this," not "we can't do this."

THE STARTERS ARE THE GAME: Every recap features Clemens vs Ryan. This is the entire premise. The recap must engage with what both starters did - how deep they went, whether they had their stuff, when things unraveled if they did. Note the specific edge each pitcher has: Ryan the 39-year-old power arm still throwing 96 fifteen years past his prime, Clemens the 24-year-old MVP-year phenom fourteen months out of shoulder surgery. Their careers cross here for one night. This universe makes them cross eighty-six times.

VOICE: The narrator is a Ron Shelton-style baseball voice. Think Crash Davis narration in Bull Durham. Grown-up. Road-worn. Comfortable with the ridiculousness of a game that middle-aged men have decided is important, and comfortable with the beauty of it too. He's sat in dugouts. He knows who's warming up in the pen without having to be told. He can describe a pitcher's shoulder history in the same sentence as the current pitch count. He is not detached and he is not reverent. He knows baseball is largely about grown men doing a strange job on a Sunday night, and he loves it anyway, and part of loving it is being willing to say when it is stupid.

Voice hallmarks:
- Colloquial long sentences: comma-strung, plainspoken, piling up specifics without becoming musical. NOT Angell's cathedral prose. Think of the narrator as a slightly-cracked older ballplayer who's seen it all and can now describe it.
- Baseball as a discipline men have decided matters, which is inherently a little ridiculous and inherently beautiful because of that
- Specific over general: "100 pitches and a 1-0 lead" beats "a well-pitched close game." "24 years old with a shoulder cleaned out fourteen months ago" beats "the young phenom."
- Wisdom about small moments; unpretentiousness about big ones. A walk-off is a walk-off, but the narrator also sees the man circling the bases and knows what he's thinking.
- Willing to be philosophical about a bunt, unpretentious about a home run
- Willing to name what things are: "Bill Buckner homered off Nolan Ryan for the sixth time. There are six of them. Six discrete Sunday nights."
- Southern-adjacent cadence when it fits (this is Texas; use it lightly)
- Does not idealize the players. They are men doing this for a living.

BOIS-STYLE STATISTICAL SETPIECES: Heavy. Numbers ARE the drama. When the specific game triggers a corpus pattern, PAUSE mid-narrative and inventory it with dry astonishment.

Example beats:
- "Bill Buckner homered off Nolan Ryan for the sixth time. There are six of them. Six discrete Sunday nights when a 34-year-old first baseman with wrapped ankles turned on a 96 mph fastball from a 39-year-old who never gave up walk-off homers. The bull fired its pistols. The sixth time."
- "This was the fourth time Ryan had struck Dave Henderson out four times in the same game. The fourth. Twenty pitches, twenty different attempts, and Henderson had, over the course of the season, taken every one of them."
- "Glenn Davis has fourteen home runs in this series. Thirteen have been off Roger Clemens. There is no explanation for this. There is no explanation from Davis, who is presumably not aware. There is only the fact of it, adding up one at-bat at a time."

Each recap should contain AT MOST one such setpiece - the game has to actually trigger it, not the narrator forcing a pattern in. If nothing triggers, don't invent one. If two things trigger, pick the more surprising one.

THE ASTRODOME IS A CHARACTER, AND THE ASTRODOME IS FUNNY. Every recap must engage with the building. This is not optional. The Astrodome is the freakiest ballpark ever put up in the major leagues - a sealed plastic-roofed circus with rainbow-gut uniforms, an animated pistol-firing bull scoreboard, AstroTurf that skips ground balls like stones on a lake, and Judge Roy Hofheinz's private putting-green apartment tucked into the mezzanine. Boston plays this loop in a stadium where the ceiling is closer than the outfield fence in a psychological sense, where the noise has nowhere to escape to, where the color palette on the field belongs to a beer commercial from Mars.

Reach for one specific dome detail per recap. Vary across the batch:
- Bull scoreboard firing pistols after an Astros HR (~40-second animated sequence: bull, cowboys, spaceships, rainbow, flags, cattle brands)
- Bull scoreboard sitting inert while Boston homers off Ryan - just the line score updates
- AstroTurf seams that groundskeepers have taped down between innings
- Rainbow-gut Astros uniforms against Boston's Puritan road grays
- Roy Hofheinz's ghost apartment somewhere in the mezzanine, chandelier still lit, empty since November 1982
- The dome's specific acoustic: noise hits the roof and rains back down; a hush inside a dome is a physical presence
- Fold-up spring-loaded seats designed so ushers could spot empty spots and hustle beer sales
- The heavy still air that kills fly-ball carry - HRs are earned, not gifted
- The lighting - fluorescent-adjacent, flat, no shadows, no October darkness
- The fact that the Astrodome is why artificial turf exists (they painted the roof panels opaque, the grass died, they invented AstroTurf)

Do not lecture the reader on the building's history. Deploy one specific detail as a phrase inside a sentence, not as a paragraph of exposition. Trust the ridiculousness.

WHAT TO INCLUDE:
- The final score and which team won
- The decisive moment(s): the walk-off hit, the late rally, the key strikeout. Be specific: pitch count, direction, distance.
- BOTH starting pitchers' evenings. Every recap. How deep, how hard, how it ended.
- At least 2-3 specific player names tied to what they actually did in THIS game
- When first mentioning a player, establish which team they play for. Never assume the reader is inside the game.
- The shape of the game: pitchers' duel, walk-off, blowout, seesaw. A sentence answering "what was this?" belongs early.
- Clemens at the plate - if he did something notable (a hit, a struck-out to end a rally, a bunt), it goes in. If 0-for-3 with 3 K, one wry phrase suffices.
- One specific Astrodome detail
- A light corpus-loop reference OR a Bois setpiece, if the game triggers one. Not both. Not neither if the game genuinely gives you a hook.

WHAT TO AVOID:
- Opening with a bare statistical declaration or a name without team context. The opening sentence must orient the reader: a scene, a player in a moment, the atmosphere of the dome, a narrative observation. Never open with "X hit Y home runs." Vary the entry point for every recap.
- Angell-isms. Long musical sentences about "the geometry of a relay throw" or "the particular October light." This is not Angell. If a sentence sounds like it belongs at a Fenway pastoral, cut it.
- Short dramatic reversal sentences: "They had not." "It was not." "He did not." AI tic; not this voice.
- Sports cliches ("gave 110%", "clutch performance", "wanted it more")
- The word "destiny"
- Direct player quotes (no one actually said anything - this is a simulation)
- Explicit references to "Simyou Lator Engine" or OOTP
- Naming the Curse of the Bambino as a phrase
- Weather references. Dome. No October chill, no starlit sky, no cold wind, no rain, no moon. The only sky is a roof.
- Anthropomorphizing the building past what's earned. The dome does not "swallow" a fly ball; the dead air kills its carry. The scoreboard does not "watch"; it plays an animation when triggered. Be concrete.
- Endings that fail to deliver the emotional verdict. The final sentence must make the reader feel who won and what it meant.
  - **If Boston wins**: Sixty-eight years of drought have not ended (this is Game 2, not Game 7) but the possibility moved one game closer. Name the moment concretely. Name the noise from the Boston bench and the small pocket of Boston fans in the visitor sections.
  - **If Houston wins**: A young franchise has won a World Series game. Forty-six thousand people trapped under a roof erupt into a sound that has nowhere to go. Bill Buckner walks back to the visitors' clubhouse. Name a specific texture.
  - **In both cases**: Concrete. Particular to THIS game. Name a player, name what they did, name what the crowd felt. Never end on an abstraction or a metaphor about baseball. Never end on people leaving.
  - **A direction worth considering - the closing snapshot of a single player.** The pitcher who threw the last pitch. The batter who took the walk-off cut. Ryan on the mound absorbing what just happened. When you can identify the player whose story most contains the verdict, closing on a still image of THAT person at THAT moment lands.
  - **CRITICAL - get the post-game body language right.** Game 2 winners are not champions. Celebration is proportional. A walk-off winner mobs the plate, the bench is on its feet - but nobody's on a police horse, nobody's spraying champagne. Game 2 losers gather gloves and walk off. Neither team is done with the series.
- Dumping stats in the closing paragraph. Statistics belong in the body doing narrative work. The closing paragraph is emotional.
- Exclamation points
- Headlines or titles - just the body text
- Game Score (the pitching metric)

FORMAT:
- 3-4 paragraphs of flowing prose
- Use <br/><br/> between paragraphs (no <p> tags - this lives inside an existing HTML table cell)
- Approximately 250-400 words total
- Do not include any HTML tags other than <br/> for line breaks

GAME DIGEST FOR THIS TIMELINE:
[Paste the Pass 1 output here]
```

---

## Human Review Step (MANDATORY)

**Never write the narrative directly into the HTML file.** Always present the proposed recap to the user first for approval.

After generating the Pass 2 narrative:

1. **Display the proposed recap in the Claude Code window as plain readable text.** Use actual paragraph breaks (blank lines between paragraphs) so the prose is easy to read - not run together, not wrapped in HTML tags.

2. **Wait for explicit user approval.** The user may:
   - Approve the recap as-is (then proceed to insert it into the HTML)
   - Request specific edits (revise and re-present)
   - Reject it entirely and ask for a fresh attempt

3. **Only after approval**, insert the recap into the box score HTML between the `<!--RECAP_TEXT_START-->` and `<!--RECAP_TEXT_END-->` markers, converting paragraph breaks to `<br/><br/>` and stripping any other formatting.

This step is non-negotiable. The Shelton voice with heavy Bois-style setpieces is a specific register - warm and colloquial without becoming folksy, statistical without becoming a spreadsheet, aware of the loop without lecturing about it. An AI cannot reliably judge whether its own prose lands in the right place on that axis. The human ear stays in the loop.

---

## AI Failure Modes - Pre-Flight Checklist

These are recurring errors observed across many subagent-generated Pass 2 narratives, adapted for Universe 86.

1. **Final-out / catcher confusion.** When the final out is a strikeout, the ball is in the **catcher's** mitt, NOT the pitcher's glove. "The ball was still in [Pitcher]'s glove" on a strikeout ending is an automatic error.

2. **Fielder-team errors.** Cross-check: who plays that position for the FIELDING team in THIS game? Kevin Bass (RF, Houston) never catches a ball hit by a Houston batter. Wade Boggs is Boston's 3B - never put a Houston out in his glove. Bill Buckner is Boston's 1B (do NOT let a ball roll through his legs unless the PBP explicitly records an E3 - and even then, be careful: the *real* Buckner error is famous enough that inventing one in this simulation would be a serious factual violation).

3. **OOTP hit-location geometry.** Numeric prefixes: **7 = left, 8 = center, 9 = right.** "9LD" = right field deep. "7D" = left field deep. Never trust directional prose without checking the prefix.

4. **Pitch-type fabrication.** The PBP gives count and result, not pitch type. Ryan is famous for his fastball but the sim doesn't record it as such. Say "pitch" or "fastball" only when the PBP or WPA chart explicitly says so.

5. **Score / inning-state errors.** Cross-check line-score totals against the digest's KEY MOMENTS. Innings-ago and runners-on math are frequently wrong in first drafts.

6. **RBI-accounting overcount.** Don't claim a play scored more runs than crossed the plate.

7. **Final-out geometry.** "6-4-3" is short-second-first (double play). "4-6-3" is second-short-first. A "6-4 fielder's choice" retires the runner from first at second; the BATTER reaches first safely.

8. **Position-of-fielder fabrication.** Don't name fielders the PBP doesn't name.

9. **Banned phrasings.**
   - "Destined to" / "destiny" - banned.
   - "Curse of the Bambino" the phrase - banned. The freight is real, the phrase is a mascot.
   - "Ball through the legs" / "Bill Buckner error" - never invent in Universe 86; reference the real thing only obliquely, once per recap, if at all.
   - Clipped dramatic-reversal sentences ("It did not last." "They had not." "He did not.") - banned.
   - "Less a baseball game than a [X]" / "like two men passing [Y] back and forth" - recurring AI tropes; vary the analogy.
   - "Coming apart at the seams" - banned.
   - "Halfway out the door" - players don't leave through doors.
   - "Waved over a pitch" - not a phrase. Use "swung through," "waved at," "took a cut at."
   - Weather words: "October chill," "cold wind," "starlit sky," "the moon over" - all banned. Dome.
   - "Suffocating" applied to the crowd noise inside the dome - AI tic. Be more specific.
   - Angell-adjacent register: "the particular X of Y" ("the particular quiet of the seventh inning") is Angell's fingerprint. This voice doesn't do that construction. Say what it IS, don't hedge with "particular."
   - "The geometry of" - banned.
   - "Autumnal" / "October light" - both dome-inappropriate and Angell-adjacent. Banned.
   - "The eighty-sixth telling" / "one more shuffling of the deck" - too literary for this voice. The corpus-loop reference should be more matter-of-fact ("in this loop," "over eighty-six nights," "in some other Sunday").

10. **Body-language inversion.** Game 2 winners celebrate proportionally - a walk-off is a walk-off - but nobody is winning a series here. Game 2 losers are irritated, not devastated; they still play tomorrow.

11. **Crowd composition errors.** Attendance is 46,101, majority Astros fans (Houston has never seen a World Series game before). A significant traveling Boston contingent - hotel-package fans, Boston media - is present. Use "the Astrodome crowd," "the Houston faithful," "forty-six thousand" - not "46,101 Houstonians" as if every seat held a hometown fan.

12. **Conceit overreach.** "Had stood in this same box in some other version of this same night" - too on-the-nose. The prompt allows 1-2 glancing references; keep them light.

13. **The curse overreach.** Same problem as the conceit. Sixty-eight years is real, the freight is real, but the phrase and the naming of it are heavy tools. Use once, sparingly, and only if the specific game triggers it.

14. **Date math against real 1986.** Real 1986 WS Game 6 was October 25 at Shea (Buckner). Real Game 7 was October 27 (Boston blew 3-0). Real Game 2 was October 19 at Shea, Boston won 9-3 (they'd win Game 1 too, and lead the series 2-0 before losing four of the last five). This simulation's Game 2 is at the Astrodome instead of Shea because the alternate NLCS gave Houston the pennant. Any reference to the real WS dates or scores must be accurate.

15. **Nolan Ryan biographical facts.**
    - 39 years old in October 1986
    - Seventh season as an Astro (arrived 1980)
    - Real 1986 season: 12-8, 3.34 ERA, 194 K in 178 IP
    - Would record his 5,000th career K in 1989 and throw his 6th and 7th no-hitters as a Ranger in 1990 and 1991
    - Real 1986 NLCS Game 5: 9 IP, 2 H, 12 K, no decision (HOU lost 2-1 in 12)
    - Do NOT reference no-hitters that hadn't happened yet as if they were behind him (his first four were 1973, 1973, 1974, 1975 - safe. Five, six, seven were 1981, 1990, 1991 - two of those were still in the future in October 1986).

16. **Roger Clemens biographical facts.**
    - 24 years old in October 1986
    - Fifteen months out of shoulder surgery (Dr. James Andrews, torn labrum, cleaned arthroscopically, August 1985)
    - Real 1986: 24-4, 2.48 ERA, 238 K, 254 IP - AL Cy Young, AL MVP
    - Threw 20-strikeout game on April 29, 1986 vs Seattle (first pitcher ever)
    - Real 1986 WS Game 2 at Shea: pulled with a 6-2 lead in the bottom of the 5th on three days' rest, no decision, Steve Crawford got the W. The blister-and-argument-with-McNamara game was Game 6, not Game 2.
    - Do NOT reference Clemens' later career (five more Cy Youngs, the Blue Jays years, the Yankees, the trial, etc.) - it hadn't happened.

17. **Bill Buckner biographical facts.**
    - 34 years old, longtime Cubs first baseman before Boston
    - Chronic ankle injuries requiring high wraps and low socks in 1986
    - Was pinch-run for late in real 1986 games because of his mobility issues
    - The real Game 6 error happens on October 25, 1986 - SIX DAYS AFTER this simulated Game 2. In our universe, that hasn't happened yet either.
    - Buckner homering off Ryan in this simulation is a plausible power moment; he had 18 HR in real 1986.

18. **No-hitter watch.** If a starting pitcher's line shows 1 hit, locate which inning the hit came in. A late-broken no-hit bid is a meaningful narrative beat. Ryan had 5 no-hitters by October 1986 (7 total lifetime). Clemens never threw one in his career - a Clemens no-hit bid in this simulation would be a genuine "in this universe he came close" moment.

19. **Senseless metaphors.** Read every metaphor literally. "Yellow tangle of arms" - Astros wore orange rainbow uniforms in '86, not yellow. Boston wore road grays at the Astrodome. "The stadium held its breath" - okay, but note the dome makes noise trap, so a hush is different than an outdoor hush. Be specific.

20. **The Astrodome specifics.**
    - Roof always closed (built enclosed, does not open)
    - AstroTurf-8 in 1986, seamed, worn thin along infield base paths
    - Dimensions: 340 - 375 - 400 - 375 - 340
    - Home-run scoreboard: 474-foot-wide, three-story animated display; the "home-run spectacular" plays only for Astros home runs - bull with two pistols, cowboys, spaceships, rainbow, waving flags, ~40-second sequence
    - Bull is inert when a visitor homers - just the line-score updates
    - Astros uniforms: rainbow guts (navy/orange/red/orange/yellow horizontal gradient across the chest) - inherent visual chaos, unmatched in MLB history
    - Boston uniform at Astrodome: road grays, no color, small Puritan contrast to the rainbow theatrics
    - No wind, no sun, no rain, no snow, no clouds, no stars, no moon, no October chill
    - Roof panels were originally translucent; painted opaque in 1965 because fielders lost balls in the glare; grass died; AstroTurf invented as a result. The Astrodome is why artificial turf exists.
    - Roy Hofheinz's private stadium apartment: real. Hofheinz died November 21, 1982. In October 1986 it's been empty about four years. Chandelier still hangs, putting green still there.
    - Fold-up "spring-loaded" seats: real. When a fan stands up, the seat clicks back so ushers can spot open seats and hustle beer sales.
    - The dome dampens fly-ball carry - HRs are earned, not gifted. Series HR rate is 1.28/gm (110 in 86 games), below MLB '86 average of 1.85.
    - Sound: noise doesn't dissipate. It hits the roof and comes back down. A hush inside a dome is different from an outdoor hush.
    - "The roof came off" is fine as a figure of speech but is factually impossible - the roof does not open.
    - Attendance in this simulation: 46,101 every game, from the box score page header (the Astrodome held roughly 45,000 for baseball in 1986; 54,816 is the post-1990 figure)

21. **Rainbow guts specifically.** The 1986 Astros uniform is not a subtle thing. Do not describe it as "orange and yellow" - it is a full horizontal gradient: navy at the shoulders, then orange, then red, then orange, then yellow across the belly. It looks like a Texas sunset drawn by a child. Nolan Ryan wears it while pitching. Glenn Davis wears it while hitting his thirteenth home run off Roger Clemens. This detail can and should appear in recaps when useful. It is inherently funny; do not oversell it.

22. **No pitch-by-pitch narration.** Never walk through an at-bat pitch by pitch ("took ball one, fouled one off, swung through the next..."). Summarize: "struck out Gedman on four pitches," "fouled off four pitches and struck out on a full count." Keep it snappy and get to the point. Pitch-level detail belongs in the digest, not the prose, except for the one pitch that decides the at-bat. The 250-400 word target can be exceeded when a game's ending genuinely earns it (e.g., g63's bases-loaded, nobody-out 9th that stranded all three), but the extra length goes to the story, never to pitch sequences.

23. **Recycled closing images.** "First man out of the dugout to meet X" (and close variants: "met him halfway," "first to the top step") showed up in too many recaps; do not use it. Vary the closing snapshot. Also avoid pronoun-subject openings like "It won because..." that refer back to the team awkwardly; name the actor.

24. **Loop metaphors that are too on the nose.** "As if somebody had rewound the tape," "same week," or any calendar framing across timelines. Each game is the same Sunday; there is no calendar between them. Counting in nights is fine ("in eighty-six nights of this," "four nights ago"); calendar units (week, days, months) are not.

25. **Bull scoreboard etiquette.** The bull fires when an ASTRO hits a home run. When a Red Sox player homers - Buckner off Ryan, Boggs off Ryan, whoever - the scoreboard does not react. Just the line score updates. This silence is a specific narrative beat and worth using once or twice across the corpus.

---

## Verification Checklist

After generating each recap (during the review step, before insertion):
- Confirm it's 3-4 paragraphs, 250-400 words
- Read it aloud. Does it sound like the calibration paragraph above? Colloquial, comma-strung, unpretentious, specific? OR does it sound like Angell (long musical cathedral sentences)? If Angell, rewrite.
- Check specific game details (score, player names, key plays) against the actual game data
- Ensure HTML will render properly (only `<br/>` tags, no unclosed elements)
- Is the loop conceit present but restrained (1-2 references max, and only if the game triggers them)?
- Is the Boston-drought texture felt without being named as "the curse"?
- **Is there at least one specific Astrodome detail?** (Bull scoreboard, rainbow guts, turf seams, roof, dome acoustics, plastic light, still air, Hofheinz's ghost apartment, spring-loaded seats, etc.)
- Does the recap engage BOTH starters' evenings?
- Does Clemens' at-bat status appear if he did something notable?
- No weather references?
- Cross-check Pass 2 output against Pass 1 digest - are all cited facts traceable to the digest?
- Run through the AI Failure Modes Pre-Flight Checklist above.
- If a Bois setpiece is invoked (Henderson 4K number four, Buckner HR off Ryan number six, etc.), is it a specific pattern the corpus supports? Is it stated with dry precision, not lectured?
- **Are the dome details varied across the batch?** If every recap in a set of five leads with the bull scoreboard, that's slop. Rotate.
- **Voice check**: does the narrator sound like a road-worn baseball guy who's been in dugouts, or does he sound like a New Yorker essayist? If the latter, the voice is wrong.
