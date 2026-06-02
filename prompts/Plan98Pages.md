# Universe 98: Infinite Cleveland II — Page Ideas

Six deep-dive page ideas for the Universe 98 dataset (92 simulations of a hypothetical Game 7, 1998 World Series: San Diego Padres @ Cleveland Indians).

Data sources:
- Game logs and box scores: `pelican/98/content/almanacs/`
- CSV stats: `sportsball/data/98/csv/`
- Team 0 / away = San Diego Padres, Team 1 / home = Cleveland Indians

Overall series result: **San Diego 51 wins, Cleveland 41 wins** out of 92 games.

---

## Idea 1: "The Nine Lives of 5-6"

### Concept

Out of 92 games, **nine ended with a final score of 5-6 or 6-5**. Nearly 10% of all timelines converge on this exact scoreline. No other final score appears more than 6 times. The universe keeps returning to this margin like a groove in a record.

Cleveland won 5 of these 9 games. San Diego won 4. Even in the multiverse's most stubborn pattern, there is no consensus on who deserves to win.

### The Nine Games (inning-by-inning scores)

| Timeline | SDP line | CLE line | Final | Winner |
|----------|----------|----------|-------|--------|
| T5  | 2-0-3-0-0-0-0-0-0 = 5 | 0-0-2-1-1-0-0-0-2 = 6 | 5-6 | CLE (walk-off, scored 2 in bottom 9) |
| T15 | 0-1-0-4-0-0-0-0-0 = 5 | 0-1-0-0-1-2-2-0-0 = 6 | 5-6 | CLE |
| T59 | 0-0-0-1-0-0-4-0-1 = 6 | 1-1-1-0-0-2-0-0-0 = 5 | 6-5 | SDP |
| T62 | 0-2-1-0-1-0-1-0-0 = 5 | 1-0-0-1-1-1-0-2-0 = 6 | 5-6 | CLE |
| T72 | 0-0-0-0-1-2-0-3-0 = 6 | 1-2-0-0-1-0-1-0-0 = 5 | 6-5 | SDP (SDP committed 4 errors and still won) |
| T79 | 0-0-0-0-1-2-1-0-1 = 5 | 2-0-2-1-0-0-0-1-0 = 6 | 5-6 | CLE |
| T82 | 0-0-3-0-0-0-1-0-2 = 6 | 0-0-4-0-0-0-0-0-1 = 5 | 6-5 | SDP |
| T87 | 2-1-1-0-1-0-0-0-1 = 6 | 2-1-0-0-0-0-1-0-1 = 5 | 6-5 | SDP |
| T90 | 0-4-0-0-0-0-1-0-0 = 5 | 0-0-0-0-0-0-6-0-0 = 6 | 5-6 | CLE (scored 0 through 6 inn, then 6 in the 7th) |

### Key details

- **T5 walk-off**: Cleveland trailed 5-4 entering the bottom of the 9th. They'd been chipping away all game from down 5-0 after three innings: 0-0-2-1-1-0-0-0... then 2 in the 9th.
- **T90 explosion**: Cleveland had zero runs through six full innings. San Diego led 5-0. Then Cleveland scored 6 runs in the bottom of the 7th — all their runs in one inning — and held on.
- **T72 the sloppy win**: San Diego committed 4 errors (the most by any team in any game in the entire dataset) and still won 6-5.
- **T82**: Both teams scored big in the 3rd (SDP 3, CLE 4), then near-silence for four innings. SDP snuck out 1 in the 7th and 2 in the 9th.

### Supplementary stats

- For comparison, the next most common scorelines: 4-6 appeared 6 times, 2-4 appeared 6 times, 1-2 appeared 6 times.
- 32 of 92 games (35%) were decided by one run.
- The 5-6/6-5 games account for 28% of all one-run games.

---

## Idea 2: "Timeline 13"

### Concept

A deep dive into the single most lopsided game in the entire dataset. San Diego 25, Cleveland 0. What happened, inning by inning, pitch by pitch. The facts laid out with the detachment of a crime scene report.

### The Line Score

```
         1  2  3  4  5  6  7  8  9    R   H   E
SDP      4  7  4  2  1  2  0  5  0   25  28   0
CLE      0  0  0  0  0  0  0  0  0    0   3   1
```

### Padres Batting (the carnage)

| Player | AB | R | H | RBI | BB | K | AVG | HR |
|--------|---:|--:|--:|----:|---:|--:|----:|---:|
| Q. Veras 2B | 8 | 1 | 2 | 0 | 0 | 2 | .250 | 0 |
| T. Gwynn Sr RF | 3 | 3 | 2 | 1 | 2 | 0 | .667 | 0 |
| G. Vaughn LF | 5 | 4 | 2 | 4 | 0 | 1 | .400 | 1 |
| K. Caminiti 3B | 5 | 2 | 2 | 4 | 2 | 1 | .400 | 1 |
| J. Leyritz DH | 5 | 3 | 3 | 3 | 2 | 2 | .600 | 1 |
| W. Joyner 1B | 7 | 4 | 5 | 1 | 0 | 0 | .714 | 0 |
| S. Finley CF | 6 | 3 | 5 | 4 | 1 | 1 | .833 | 0 |
| C. Hernandez C | 5 | 3 | 2 | 4 | 0 | 1 | .400 | 0 |
| C. Gomez SS | 6 | 2 | 5 | 4 | 1 | 1 | .833 | 0 |
| **Totals** | **51** | **25** | **28** | **25** | **8** | **10** | | |

Notable: Chris Gomez hit 4 doubles (the only player in any timeline to hit 4 doubles in a game). Steve Finley was named Player of the Game. Quilvio Veras batted 8 times — the most plate appearances of anyone in the entire 92-game dataset — and went 2-for-8.

### Indians Batting (the silence)

| Player | AB | R | H | RBI | BB | K |
|--------|---:|--:|--:|----:|---:|--:|
| K. Lofton CF | 4 | 0 | 0 | 0 | 0 | 3 |
| O. Vizquel SS | 4 | 0 | 2 | 0 | 0 | 0 |
| J. Thome 1B | 2 | 0 | 0 | 0 | 1 | 2 |
| M. Ramirez RF | 4 | 0 | 0 | 0 | 0 | 1 |
| D. Justice LF | 3 | 0 | 0 | 0 | 1 | 0 |
| B. Giles DH | 3 | 0 | 1 | 0 | 1 | 1 |
| E. Wilson 3B | 3 | 0 | 0 | 0 | 0 | 2 |
| J. Branson 2B | 3 | 0 | 0 | 0 | 0 | 1 |
| E. Diaz C | 3 | 0 | 0 | 0 | 0 | 1 |
| **Totals** | **29** | **0** | **3** | **0** | **3** | **11** |

All three Cleveland hits were doubles (Vizquel x2, Giles x1). All stranded.

### Pitching

**Kevin Brown (SDP)**: 9.0 IP, 3 H, 0 R, 0 ER, 3 BB, 11 K, 118 pitches (76 strikes). Game score: **89**. Complete game shutout. Faced 33 batters. This is one of four complete game shutouts Brown threw across the 92 timelines (also T21, T27, T70). In T70 he held Cleveland to 1 hit.

**Cleveland pitching (7 pitchers used)**:

| Pitcher | IP | H | R | ER | BB | K | Notes |
|---------|---:|--:|--:|---:|---:|--:|-------|
| B. Colon (L) | 1.2 | 6 | 7 | 7 | 2 | 0 | Game score: **7**. ERA: 37.80 |
| D. Burba | 0.0 | 4 | 4 | 4 | 1 | 0 | Faced 5 batters, recorded 0 outs. 19 pitches, 7 strikes. |
| J. Poole | 1.0 | 5 | 4 | 0 | 0 | 1 | |
| P. Shuey | 2.1 | 6 | 3 | 3 | 0 | 4 | Longest outing by any Cleveland pitcher this game |
| **T. Fryman** | 2.0 | 3 | 2 | 2 | 2 | 1 | **Position player (3B)**. Threw 44 pitches. |
| **S. Alomar Jr** | 0.2 | 3 | 5 | 5 | 3 | 0 | **Position player (C)**. ERA: 67.50. Walked in runs. |
| P. Assenmacher | 1.1 | 1 | 0 | 0 | 0 | 4 | The only Cleveland pitcher who didn't give up a run. |

This is the only game in 92 timelines where a position player pitched. It is the only game where two position players pitched. It is the only game where any starter lasted fewer than 2 innings.

### Context within the dataset

- **25 runs**: the next highest single-team score is 21 (CLE in T34). The next SDP high is 16 (T36).
- **28 hits**: the next highest is 24 (CLE in T34).
- **3 hits for Cleveland**: the fewest hits in any timeline (tied with T70, also a Kevin Brown shutout).
- **Game score of 7 vs 89**: the widest gap between opposing starters in any timeline.
- **Shutout asymmetry**: Cleveland was shut out 9 times across 92 games. San Diego was shut out 3 times.
- Timeline 13 is the most lopsided result in the dataset. The next largest margin of victory is 13 runs (T70: SDP 13, CLE 0; T34: CLE 21, SDP 8).

### Game conditions

- Ballpark: Jacobs Field
- Weather: Partly Cloudy, 43 degrees, no wind
- Start time: 8:05 PM EST
- Game duration: 4 hours, 8 minutes
- Attendance: 45,225

---

## Idea 3: "Greg Vaughn Was Here (0-for-4)"

### Concept

A portrait of the most unreliable important hitter in the multiverse. Greg Vaughn batted third for the San Diego Padres in 92 consecutive Game 7s. He batted .237 — the worst average of any starting position player in either lineup. He went hitless in 29 of 92 games. He struck out 112 times. And he hit 18 home runs.

There is no arc. There is no redemption. There is no lesson. He was 0-for-4 and then he hit a three-run homer and then he was 0-for-5 again.

### Vaughn's Aggregate Line

| G | AB | H | AVG | HR | RBI | K | BB | R |
|--:|---:|--:|----:|---:|----:|--:|---:|--:|
| 92 | 397 | 94 | .237 | 18 | 65 | 112 | 33 | 64 |

### Complete Timeline-by-Timeline Performance

```
T01: 1-4          T24: 1-5  HR  3RBI   T47: 1-4          T70: 2-5   1RBI
T02: 0-for-5      T25: 1-4             T48: 1-4          T71: 2-3  HR  1RBI
T03: 2-4  HR 2RBI T26: 0-for-4         T49: 2-4  HR 2RBI T72: 1-5
T04: 1-5          T27: 3-5             T50: 1-4   1RBI   T73: 0-for-4
T05: 2-4          T28: 0-for-5         T51: 0-for-4      T74: 2-5  HR  2RBI
T06: 1-4          T29: 3-6  HR 2RBI    T52: 2-4          T75: 1-5
T07: 1-6   1RBI   T30: 1-5             T53: 2-5  HR 3RBI T76: 2-4   1RBI
T08: 1-4   1RBI   T31: 1-4             T54: 1-5          T77: 1-5
T09: 0-for-3 1RBI T32: 2-4  HR 2RBI    T55: 1-4          T78: 2-4   1RBI
T10: 1-4          T33: 1-3   1RBI      T56: 0-for-4 1RBI T79: 0-for-4  3K
T11: 0-for-4      T34: 2-6   1RBI      T57: 2-5  HR 3RBI T80: 0-for-4  2K
T12: 1-4   1RBI   T35: 1-4             T58: 2-5   2RBI   T81: 0-for-4  1RBI
T13: 2-5  HR 4RBI T36: 0-for-5 1RBI    T59: 2-4  HR 2RBI T82: 0-for-5  3K
T14: 1-5  HR 1RBI T37: 1-4  HR 1RBI    T60: 1-4          T83: 0-for-5
T15: 1-5          T38: 3-5   1RBI      T61: 0-for-4      T84: 2-3
T16: 0-for-4      T39: 2-5  HR 2RBI    T62: 2-4  HR 1RBI T85: 2-5   2RBI
T17: 2-4          T40: 0-for-4         T63: 0-for-5      T86: 0-for-4
T18: 1-4          T41: 0-for-4         T64: 0-for-4      T87: 0-for-5
T19: 2-3   2RBI   T42: 1-5   1RBI      T65: 1-5          T88: 1-4   1RBI
T20: 0-for-4      T43: 0-for-3         T66: 2-5          T89: 1-4
T21: 1-3  HR 3RBI T44: 0-for-3 1RBI    T67: 0-for-3      T90: 0-for-5
T22: 1-5          T45: 1-5   1RBI      T68: 0-for-3      T91: 2-5  HR  4RBI
T23: 0-for-5 3K   T46: 2-4  HR 2RBI    T69: 2-4          T92: 0-for-3  1K
```

### The 29 Hitless Games

T2, T9, T11, T16, T20, T23, T26, T28, T36, T40, T41, T43, T44, T51, T56, T61, T63, T64, T67, T68, T73, T79, T80, T81, T82, T83, T86, T87, T90, T92.

Of these, 24 had 4 or more at-bats (the "golden sombrero" threshold).

**Longest consecutive hitless streak**: 5 timelines (T79 through T83).
- T79: 0-for-4, 3 strikeouts
- T80: 0-for-4, 2 strikeouts
- T81: 0-for-4, 1 strikeout, 1 RBI (sac fly/walk — drove in a run without a hit)
- T82: 0-for-5, 3 strikeouts
- T83: 0-for-5, 1 strikeout

Twenty-two at-bats across five consecutive timelines. Zero hits.

### The 18 Home Runs

| Timeline | AB | H | HR | RBI | Game result |
|----------|---:|--:|---:|----:|-------------|
| T3 | 4 | 2 | 1 | 2 | SDP 11, CLE 5 (W) |
| T13 | 5 | 2 | 1 | 4 | SDP 25, CLE 0 (W) |
| T14 | 5 | 1 | 1 | 1 | SDP 4, CLE 3 (W, 12 inn) |
| T21 | 3 | 1 | 1 | 3 | SDP 7, CLE 0 (W) |
| T24 | 5 | 1 | 1 | 3 | SDP 5, CLE 7 (L) |
| T29 | 6 | 3 | 1 | 2 | SDP 12, CLE 10 (W) |
| T32 | 4 | 2 | 1 | 2 | SDP 5, CLE 9 (L) |
| T37 | 4 | 1 | 1 | 1 | SDP 11, CLE 15 (L) |
| T39 | 5 | 2 | 1 | 2 | SDP 5, CLE 0 (W) |
| T46 | 4 | 2 | 1 | 2 | SDP 6, CLE 3 (W) |
| T49 | 4 | 2 | 1 | 2 | SDP 5, CLE 4 (W) |
| T53 | 5 | 2 | 1 | 3 | SDP 12, CLE 8 (W) |
| T57 | 5 | 2 | 1 | 3 | SDP 6, CLE 7 (L) |
| T59 | 4 | 2 | 1 | 2 | SDP 6, CLE 5 (W) |
| T62 | 4 | 2 | 1 | 1 | SDP 5, CLE 6 (L) |
| T71 | 3 | 2 | 1 | 1 | SDP 5, CLE 4 (W) |
| T74 | 5 | 2 | 1 | 2 | SDP 12, CLE 4 (W) |
| T91 | 5 | 2 | 1 | 4 | SDP 9, CLE 5 (W) |

San Diego's record in Vaughn HR games: **13-5**. When he goes deep, the Padres almost always win.

### The Bookends

- **Timeline 91** (second-to-last game): 2-for-5, home run, 4 RBI. His best game in weeks.
- **Timeline 92** (final game): 0-for-3, 1 strikeout. The last thing Greg Vaughn did in Universe 98 was make an out.

### Supplementary: Starting Position Player Batting Averages (all 92 games)

For context on where Vaughn falls:

| Player | Team | G | AB | H | AVG | HR | RBI | K |
|--------|------|--:|---:|--:|----:|---:|----:|--:|
| T. Gwynn Sr | SDP | 92 | 415 | 142 | .342 | 12 | 69 | 37 |
| O. Vizquel | CLE | 92 | 381 | 123 | .323 | 0 | 28 | 49 |
| W. Joyner | SDP | 92 | 368 | 108 | .293 | 9 | 56 | 52 |
| K. Lofton | CLE | 92 | 384 | 111 | .289 | 2 | 32 | 55 |
| M. Ramirez | CLE | 92 | 367 | 106 | .289 | 11 | 66 | 108 |
| C. Hernandez | SDP | 92 | 369 | 105 | .285 | 10 | 43 | 64 |
| K. Caminiti | SDP | 92 | 368 | 104 | .283 | 21 | 75 | 105 |
| C. Gomez | SDP | 92 | 343 | 97 | .283 | 0 | 42 | 83 |
| Q. Veras | SDP | 92 | 393 | 108 | .275 | 7 | 34 | 72 |
| J. Thome | CLE | 92 | 360 | 99 | .275 | 13 | 83 | 139 |
| B. Giles | CLE | 92 | 325 | 89 | .274 | 10 | 40 | 83 |
| E. Wilson | CLE | 92 | 322 | 85 | .264 | 3 | 38 | 82 |
| D. Justice | CLE | 92 | 360 | 90 | .250 | 5 | 45 | 85 |
| S. Finley | SDP | 92 | 369 | 91 | .247 | 3 | 46 | 88 |
| J. Leyritz | SDP | 92 | 362 | 89 | .246 | 13 | 48 | 112 |
| **G. Vaughn** | **SDP** | **92** | **397** | **94** | **.237** | **18** | **65** | **112** |
| E. Diaz | CLE | 92 | 304 | 53 | .174 | 2 | 19 | 98 |
| J. Branson | CLE | 92 | 341 | 61 | .179 | 3 | 26 | 106 |

Vaughn is the worst-hitting starter in a lineup spot that matters. Diaz (.174) and Branson (.179) are worse, but they bat 8th and 9th. Vaughn bats 3rd.

### The Strikeout Leaders (all 92 games)

| Player | K | AB | K% |
|--------|--:|---:|---:|
| J. Thome | 139 | 360 | 38.6% |
| G. Vaughn | 112 | 397 | 28.2% |
| J. Leyritz | 112 | 362 | 30.9% |
| J. Branson | 106 | 341 | 31.1% |
| K. Caminiti | 105 | 368 | 28.5% |
| E. Diaz | 98 | 304 | 32.2% |

Vaughn is tied for 2nd in total strikeouts but had the most at-bats of anyone in the top 6. Thome struck out more, but Thome also hit .275 with 13 HR and 83 RBI. Vaughn's combination of volume, futility, and power is unique.

---

## Idea 4: "Hell's Bells at Jacobs Field"

### Concept

Trevor Hoffman's entrance music was AC/DC's "Hell's Bells." At Qualcomm Stadium in San Diego, it played over 60,000 sunburned fans and a sky the color of a screensaver. In Universe 98, it plays at Jacobs Field in 43-degree October darkness, and it means the same thing it always meant: this game is over.

Hoffman appeared in 46 of 92 timelines. He recorded 27 saves. He blew zero.

When Hoffman pitched, San Diego went **37-9**. When he didn't pitch, San Diego went **14-32**.

That is not a closer. That is a weather system. The palm tree came to the snowfield, and the snowfield lost.

### The Numbers

| Stat | Hoffman (SDP) | Assenmacher (CLE) |
|------|------:|------:|
| Games | 46 | 63 |
| IP | 53.2 | 72.2 |
| ERA | 3.02 | 5.20 |
| Saves | 27 | 27 |
| Blown Saves | 0 | 1 |
| K | 59 | 70 |
| Team record when he pitches | 37-9 | N/A |

They both finished with 27 saves. The same number. This is like saying two restaurants both served 27 meals — except one was a Michelin-starred omakase and the other was a gas station microwave.

### The 27 Saves (every one)

| Timeline | IP | H | R | K | Score |
|----------|---:|--:|--:|--:|-------|
| T4 | 1.1 | 0 | 0 | 2 | SDP 4, CLE 1 |
| T8 | 1.0 | 0 | 0 | 2 | SDP 6, CLE 4 |
| T12 | 1.0 | 1 | 0 | 0 | SDP 5, CLE 2 |
| T16 | 1.2 | 0 | 0 | 2 | SDP 2, CLE 1 |
| T17 | 2.0 | 0 | 0 | 4 | SDP 2, CLE 1 |
| T19 | 1.0 | 1 | 0 | 1 | SDP 5, CLE 4 |
| T35 | 1.0 | 0 | 0 | 1 | SDP 2, CLE 1 |
| T38 | 1.1 | 0 | 0 | 2 | SDP 6, CLE 4 |
| T39 | 0.1 | 0 | 0 | 0 | SDP 5, CLE 0 |
| T42 | 1.0 | 0 | 0 | 1 | SDP 6, CLE 4 |
| T43 | 1.1 | 1 | 0 | 3 | SDP 4, CLE 2 |
| T46 | 1.0 | 0 | 0 | 1 | SDP 6, CLE 3 |
| T47 | 1.0 | 2 | 0 | 1 | SDP 2, CLE 0 |
| T49 | 1.0 | 0 | 0 | 0 | SDP 5, CLE 4 |
| T56 | 1.0 | 1 | 0 | 0 | SDP 2, CLE 1 |
| T58 | 0.1 | 0 | 0 | 0 | SDP 5, CLE 1 |
| T59 | 1.0 | 0 | 0 | 2 | SDP 6, CLE 5 |
| T65 | 1.0 | 1 | 1 | 0 | SDP 5, CLE 4 |
| T68 | 1.0 | 0 | 0 | 2 | SDP 3, CLE 1 |
| T69 | 1.0 | 0 | 0 | 1 | SDP 8, CLE 6 |
| T71 | 1.0 | 2 | 0 | 2 | SDP 5, CLE 4 |
| T72 | 1.0 | 0 | 0 | 2 | SDP 6, CLE 5 |
| T73 | 1.2 | 2 | 0 | 2 | SDP 2, CLE 0 |
| T78 | 1.0 | 0 | 0 | 1 | SDP 4, CLE 2 |
| T82 | 1.0 | 3 | 1 | 1 | SDP 6, CLE 5 |
| T87 | 1.0 | 2 | 1 | 0 | SDP 6, CLE 5 |
| T92 | 1.1 | 1 | 0 | 1 | SDP 6, CLE 4 |

Twenty-seven doors slammed on Cleveland. Not one was pried back open. Nine of those saves were in one-run games.

### The Six Losses (the only cracks)

Hoffman didn't blow saves. He just occasionally lost. Every one of his 6 losses came when he entered tied or already behind — non-save situations where the bullpen asked him to perform miracles instead of protect leads.

- **T5**: 0.2 IP, 3 H, 2 R. SDP lost 5-6 (walk-off).
- **T44**: 0.2 IP, 2 H, 1 R. SDP lost 3-4.
- **T50**: 0.2 IP, 1 H, 1 R. SDP lost 6-7 (walk-off).
- **T51**: 0.0 IP, 1 H, 2 R. Recorded zero outs. SDP lost 1-2 (walk-off).
- **T61**: 0.0 IP, 5 H, 4 R. Recorded zero outs. SDP lost 4-6.
- **T80**: 0.0 IP, 1 H, 1 R. Recorded zero outs. SDP lost 3-4 (walk-off).

Three times he entered and didn't record a single out. But these weren't save situations. The distinction matters: when the Padres handed him a lead, he never gave it back. When they handed him a mess, sometimes the mess won.

### The Real Contrast: Two Bullpens

Cleveland's "closer" situation was Assenmacher by volume, Shuey by committee. Here's what the Indians bullpen looked like across 92 timelines:

| Pitcher | G | IP | ERA | SV |
|---------|--:|---:|----:|---:|
| P. Assenmacher | 63 | 72.2 | 5.20 | 27 |
| J. Poole | 61 | 87.2 | 5.95 | 0 |
| P. Shuey | 59 | 65.1 | 6.89 | 2 |
| D. Burba | 31 | 52.2 | 5.98 | 1 |

Every single Cleveland reliever had an ERA above 5.00. The entire bullpen. Against Hoffman's 3.02. It's 43 degrees and the warm-weather reliever is the only one whose arm works.

### Trevor Hoffman Facts

A companion piece to the statistics: Chuck Norris-style "Trevor Hoffman Facts" that riff on his 0-blown-save, 27-for-27 dominance across Universe 98. Full list in `PlanTrevorHoffmanFacts.md` (22 facts and counting). Highlights include:

- Trevor Hoffman once threw a complete game in the ninth inning.
- Trevor Hoffman does not feel the 43 degrees and freezing cold rain of Jacobs Field. Jacobs Field feels the 43 degrees and freezing cold rain of Trevor Hoffman.
- Every time Trevor Hoffman blows a save in Universe 98, Cleveland wins a championship. Too bad Trevor Hoffman never blew a save.

### The Thesis

In the real 1998, San Diego's bullpen was its calling card. Hoffman saved 53 games that year, the most in the National League. In Universe 98, he does it again — 27 times out of 46 appearances, in a ballpark built for a different sport, in weather built for a different species. The Padres could afford to lose 32 games without him because the 37 wins with him were essentially guaranteed. No team in a 92-game hypothetical series should have a split that clean. But Hell's Bells doesn't care about the cold.

---

## Idea 5: "The Ace and the Boulder: Kevin Brown vs. Bartolo Colon"

### Concept

Kevin Brown and Bartolo Colon started every single one of the 92 games in Universe 98. Same matchup, 92 times. This is the story of two pitchers who walked to the same mound 92 times, and how one of them quietly won the multiverse.

But more than that, it's the story of how Bartolo Colon sometimes pitched brilliantly and it didn't matter. There are 25 timelines where Colon gave up 0 or 1 earned run in 6 or more innings — genuinely great starts. Cleveland went **12-13** in those games. He pitched the game of his life, and the coin still came up tails.

Bartolo Colon would go on to pitch in the major leagues until he was 47 years old. He would become a folk hero, a meme, a 285-pound man who hit a home run at age 42. None of that has happened yet. In Universe 98, he is just a 25-year-old standing on a mound in Cleveland, trying to beat Kevin Brown, and the universe has already decided he can't.

### The Aggregate Numbers

| | Kevin Brown (SDP) | Bartolo Colon (CLE) |
|-|------:|------:|
| W-L | 33-21 | 21-28 |
| IP | 617.0 | 566.0 |
| ERA | 3.41 | 4.17 |
| K | 647 | 476 |
| BB | 151 | 197 |
| CG Shutouts | 4 | 0 |
| Games with 0 R in 8+ IP | 7 | 3 |

Brown struck out more batters, walked fewer, pitched deeper, and won 12 more decisions. In 92 identical October nights, that gap never closed.

### Brown's Seven Zeros

Seven times, Kevin Brown pitched 8 or more innings and gave up zero runs:

| Timeline | IP | H | BB | K | SDP score |
|----------|---:|--:|---:|--:|----------|
| T13 | 9.0 | 3 | 3 | 11 | 25 |
| T21 | 9.0 | 2 | 1 | 10 | 7 |
| T27 | 9.0 | 2 | 0 | 6 | 5 |
| T39 | 8.0 | 3 | 1 | 7 | 5 |
| T51 | 8.0 | 4 | 2 | 9 | 1 (L) |
| T70 | 9.0 | **1** | 2 | 4 | 13 |
| T89 | 8.2 | 3 | 1 | 7 | 8 |

In T70, Brown held Cleveland to a single hit. One hit in a Game 7 of the World Series. He went 6-1 in these seven masterpieces. The one loss: T51, where he threw 8 shutout innings and San Diego gave him exactly 1 run of support. Brown's line was 8 IP, 4 H, 0 R, 9 K. He lost 1-2 because Cleveland scored twice in the bottom of the 9th off the bullpen.

That's the only time in 92 games that Brown pitched a shutout into the 9th and lost.

### Colon's Sisyphus Starts

Twenty-five times Colon gave up 0 or 1 earned run in 6 or more innings. Here are the losses:

| Timeline | IP | H | R | ER | K | CLE score | Result |
|----------|---:|--:|--:|---:|--:|----------|--------|
| T16 | 7.0 | 6 | 2 | 1 | 3 | 1 | L, 2-1 |
| T17 | 7.1 | 6 | 1 | 1 | 5 | 1 | L, 2-1 |
| T39 | 6.0 | 4 | 1 | 1 | 6 | 0 | L, 5-0 |
| T42 | 6.0 | 5 | 3 | 1 | 6 | 4 | L, 6-4 |
| T78 | 7.0 | 6 | 3 | 1 | 4 | 2 | L, 4-2 |

In T16 and T17 — back-to-back timelines — Colon gave up 1 earned run in 7+ innings, and his team scored exactly 1 run. Both times. In T39, he gave up 1 ER in 6 IP and Cleveland was shut out. His reward for brilliance was a 5-0 loss.

But the no-decisions are worse. In 14 of his 25 great starts, Colon didn't get a win OR a loss. He just... pitched. The bullpen came in. Things happened. He watched.

- **T47**: 8.0 IP, 5 H, 0 R, 0 ER, 7 K. Game score: elite. Cleveland scored 0 runs. SDP won 2-0. Colon: no decision.
- **T63**: 8.0 IP, 3 H, 0 R, 0 ER, 9 K. His best game by game score. Cleveland eventually lost 5-2 in 11 innings.
- **T86**: 8.2 IP, 3 H, 0 R, 0 ER, 4 K. Cleveland won 10-0. But by then it didn't matter — the offense did all the work and Colon still didn't get the decision.

When Colon was great, it was a coin flip. When Brown was great, it was a funeral.

### The Contrast in Real Life

In the real 1998, the Padres were swept by the Yankees in the World Series. Brown pitched Game 1 — 7 IP, 5 H, 2 R — and lost. The Padres scored 6 runs in the entire Series. Brown never got a chance to do what he does in Universe 98.

Colon, meanwhile, was just getting started. He would pitch for 8 more teams over 21 more years. He would throw 247 career wins. He would become a large adult son beloved by the entire internet.

In Universe 98, none of that exists. He is young and thin and good and it doesn't work. He rolls the boulder up 25 times and it rolls back 13 of them.

### Colon's Best Games That Cleveland Lost

| Timeline | Colon line | CLE scored | Final |
|----------|-----------|-----------|-------|
| T2 | 8.0 IP, 6 H, 1 R, 1 ER, 6 K | 2 | SDP 4, CLE 2 |
| T16 | 7.0 IP, 6 H, 2 R, 1 ER, 3 K | 1 | SDP 2, CLE 1 |
| T17 | 7.1 IP, 6 H, 1 R, 1 ER, 5 K | 1 | SDP 2, CLE 1 |
| T19 | 8.0 IP, 2 H, 1 R, 0 ER, 7 K | 4 | SDP 5, CLE 4 |
| T26 | 8.0 IP, 5 H, 1 R, 1 ER, 7 K | 1 | SDP 6, CLE 1 |
| T39 | 6.0 IP, 4 H, 1 R, 1 ER, 6 K | 0 | SDP 5, CLE 0 |
| T42 | 6.0 IP, 5 H, 3 R, 1 ER, 6 K | 4 | SDP 6, CLE 4 |
| T43 | 6.0 IP, 5 H, 2 R, 0 ER, 4 K | 2 | SDP 4, CLE 2 |
| T47 | 8.0 IP, 5 H, 0 R, 0 ER, 7 K | 0 | SDP 2, CLE 0 |
| T59 | 6.0 IP, 8 H, 1 R, 1 ER, 2 K | 5 | SDP 6, CLE 5 |
| T63 | 8.0 IP, 3 H, 0 R, 0 ER, 9 K | 2 | SDP 5, CLE 2 |
| T76 | 6.0 IP, 3 H, 4 R, 1 ER, 4 K | 4 | SDP 8, CLE 4 |
| T78 | 7.0 IP, 6 H, 3 R, 1 ER, 4 K | 2 | SDP 4, CLE 2 |

Thirteen times Colon gave up 0 or 1 earned run in 6+ innings and Cleveland still lost. That is the most Cleveland stat in the dataset.

---

## Idea 6: "Twelve Hits, Zero Runs: A Home Game"

### Concept

Every game in Universe 98 was played at Jacobs Field. Cleveland was the home team 92 times. The attendance was always 45,225. The weather was always partly cloudy, 43 degrees, no wind. The same fans, the same building, the same cold, 92 times.

Cleveland won 41 of those 92 home games. The home team winning percentage: **.446**.

This is a franchise that hasn't won a World Series since 1948. The Browns left for Baltimore in 1996. In 1997, Cleveland took the Marlins to Game 7 of the World Series and lost. Now, in Universe 98, they get 92 Game 7s at home — and they still lose 51 of them.

Some cities are cursed. Some cities make the curse look generous.

### The Series Arc

The multiverse didn't decide all at once. It took its time.

```
After T10:  SDP 5,  CLE 5    (tied)
After T20:  SDP 11, CLE 9    (close)
After T30:  SDP 18, CLE 12   (gap opening)
After T40:  SDP 22, CLE 18   (close again)
After T50:  SDP 27, CLE 23   (close again)
After T60:  SDP 31, CLE 29   (so close)
After T62:  SDP 31, CLE 31   (TIED. One last time.)
After T70:  SDP 37, CLE 33   (pulling away)
After T80:  SDP 44, CLE 36   (it's over)
After T92:  SDP 51, CLE 41   (final)
```

The series was tied 31-31 after Timeline 62. It was never tied again.

Cleveland's longest winning streak: **4 games** (T31-T34).
San Diego's longest winning streak: **9 games** (T68-T76).

CLE last held the lead in the overall series after Timeline 11. After that — for 81 straight timelines — they were never ahead again. Eighty-one consecutive Game 7s played from behind in the standings, in their own building, in front of their own fans.

### The Nine Shutouts

Cleveland was shut out 9 times at home. San Diego was shut out 3 times.

| Timeline | SDP score | CLE hits | Notes |
|----------|----------|---------|-------|
| T13 | 25-0 | 3 | (covered in Idea 2) |
| T21 | 7-0 | 2 | Kevin Brown CG, 10 K |
| T27 | 5-0 | 2 | Kevin Brown CG, 0 BB |
| T30 | 11-0 | 6 | |
| T39 | 5-0 | 4 | |
| T47 | 2-0 | 7 | CLE had 7 hits and scored nothing |
| T70 | 13-0 | **1** | One hit. In a Game 7. At home. |
| T73 | 2-0 | **12** | Twelve hits. Zero runs. |
| T89 | 8-0 | 3 | |

**Timeline 73 is the most Cleveland thing in the dataset.** Twelve hits. Zero runs. The Indians put twelve baserunners on via base hits and stranded every last one. They out-hit San Diego 12 to 8 and lost 2-0. It's like filling a bucket with a hole in the bottom. It's like pushing a revolving door. It's like being Cleveland.

For comparison, San Diego's 3 shutout losses:

| Timeline | CLE score | SDP hits |
|----------|----------|---------|
| T48 | 4-0 | 4 |
| T84 | 1-0 | 6 |
| T86 | 10-0 | 4 |

San Diego gets shut out and has the decency to not get many hits while doing it. Cleveland gets 12 hits and somehow builds nothing.

### The 9-Game Streak That Buried Them

From T68 through T76, San Diego won every game:

| Timeline | Score | Margin |
|----------|-------|--------|
| T68 | SDP 3, CLE 1 | 2 |
| T69 | SDP 8, CLE 6 | 2 |
| T70 | SDP 13, CLE 0 | 13 |
| T71 | SDP 5, CLE 4 | 1 |
| T72 | SDP 6, CLE 5 | 1 |
| T73 | SDP 2, CLE 0 | 2 |
| T74 | SDP 12, CLE 4 | 8 |
| T75 | SDP 7, CLE 3 | 4 |
| T76 | SDP 8, CLE 4 | 4 |

This stretch includes a 13-0 blowout, a one-hit shutout, the 12-hit/0-run shutout, two one-run squeakers, and an 8-run beatdown that went 12 innings. Every kind of loss. The whole vocabulary of failure, in nine consecutive games. The record went from SDP 37-33 (plausibly competitive) to SDP 44-36 (foregone conclusion).

### The Blowout Asymmetry

In games decided by 5 or more runs:
- **San Diego won 12 blowouts**
- **Cleveland won 5 blowouts**

When San Diego was good, it was devastating. When Cleveland was good, it was barely enough.

SDP blowout wins: 25-0, 13-0, 12-4, 12-4, 11-0, 11-5, 8-0, 8-0, 7-0, 6-1, 5-0, 5-0.

CLE blowout wins: 21-8, 10-4, 10-0, 9-4, 7-1.

Cleveland's biggest win was 21-8 in T34. San Diego's biggest win was 25-0 in T13. Even in victory, Cleveland couldn't quite match the scale of San Diego's dominance. The palm trees don't just win — they win in a way that makes you forget what snow looked like.

### 45,225

The attendance for every game in the dataset is 45,225. This is a stadium full of people watching Game 7 of the World Series. In the real 1998, Jacobs Field held 43,863 and was sold out for every postseason game. The simulation rounds it to 45,225.

Imagine being seat 45,225. You have watched your team play Game 7 ninety-two times. They have been shut out in front of you nine times. They have won 41 and lost 51. They have trailed in the series standings for 81 of 92 games. They have gotten 12 hits in a game and scored zero runs.

You keep coming back. That's what it means.
