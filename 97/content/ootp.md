Title: ootp
Date: 2000-01-01 00:00

# Out of the Park Baseball Simulator

[Out of the Park Baseball Simulator homepage (link)](https://www.ootpdevelopments.com/out-of-the-park-baseball-home/)

## Overview


[Out of the Park Baseball (OOTP)](https://www.ootpdevelopments.com/out-of-the-park-baseball-home/)
is a computer game that lets you simulate baseball leagues and teams.
The game can simulate everything from multiple seasons of hundreds
of games between dozens of teams, all the way down to interactively
simulating games and making managerial decisions like which pitches
should be thrown or when batters should swing.

The game is extremely flexible, with an array of adjustable
parameters, and the ability to either micromanage, or to allow the
computer to run simulations using its best judgement. The simulator 
is also programmed
with a wide variety of managerial strategies from different baseball
eras, and even the automatic decision-making is easily customized.

The program also offers a suite of tools for importing and exporting
data from a variety of formats and for a variety of uses, ranging from
raw data in CSV format, to pre-formatted HTML pages and stylesheets.
This proved invaluable for assembling Infinite Cleveland timelines.

## Infinite Cleveland Exhibition Games

OOTP has several simulation modes.
To generate alternate timelines for the Infinite Cleveland project, we used 
OOTP in Exhibition Mode, which is a way of simulating a single playoffs game, 
series, or bracket.  (Infinite Cleveland is just scratching the surface of
the different ways of dipping into the pool of infinite timelines.)

We set the roster to 17 players, to match the number of
players that were on the field during the real Game 3.
The remaining players are benched, to ensure realistic
rotations during the games (for example, not having the
Game 4 starters come into the game to pitch in relief).

![Screenshot of OOTP setup for exhibition match between 1997 World Series teams.](/img/ootp1.png)

![Screenshot of OOTP setup for Infinite Cleveland exhibition matches.](/img/ootp2.png)

## Infinite Cleveland Roster Setup

The rosters were set up so that only players appearing in Game 3 were on the
active roster, and the lineups were rearranged so that each player was batting
in the same lineup spot as Game 3, and playing in the correct position for Game 3.

Once the roster is set up, the game state can be frozen, and copies can be made
of the frozen game state whenever we want to generate a new simulation/timeline.

We obtained the roster of players used in Game 3 of the 1997 World Series
from [baseball-reference.com (link)](https://www.baseball-reference.com/boxes/CLE/CLE199710210.shtml).

**Rosters Tab:**

Players that were in Game 3 were moved to the left side (active roster),
while players that were not in Game 3 were moved to the right side
(reserve roster).

Here is the roster from baseball-reference.com:

![Screenshot of baseball-reference.com Florida Marlins lineup for 1997 World Series Game 3.](/img/baseballreference1.png)

Here is a screenshot of the Florida Marlins roster with Game 3 players active:

![Screenshot of OOTP roster for 1997 Florida Marlins in World Series Game 3.](/img/ootp3.png)

**Lineups Tab:**

The Lineups tab is where players are arranged in the correct batting order
and set up to start at the correct position.

The starting pitchers are set (Al Leiter for the Marlins, Charles Nagy for the Indians),
and each team has a 1-man pitching rotation so all other pitchers are in the bullpen.

Next, the batting lineup is set up in the correct order by dragging and dropping players.
Here is a screenshot of the completed batting lineup for the Florida Marlins:

![Screenshot of OOTP lineup for 1997 Florida Marlins in World Series Game 3.](/img/ootp4.png)

**Play Ball! Tab:**

Once the lineups are set, the Play Ball! tab shows two green buttons:
"Play" (watch the game as it is simulated) or "Simulate" (get an instantaneous
simulation).

Clicking "Return to OOTP Main Screen" without cliking either "Play" or "Simulate" will
automatically save the game state; no lineups or rosters are lost. Confirm that's the case
by loading a saved game on the OOTP Main Screen. The exhibition match just set up should be
called "HistoricalExhibition".

## Copying a Saved Game

Once the clean, unsimulated version of the Game 3 matchup has been saved, locate
and stash a copy of the clean, unsimulated version. Then make copies of it to create
new simulations/timelines.

Start by locating the directory where OOTP stores application data; it should be listed
somewhere in the game's Settings panel. On Mac, the application data directory is here:

```
$ open "/Users/<username>/Library/Application Support/Out of the Park Developments/OOTP Baseball 20"
```

The directory `saved_games` contains the saved games, which are contained in folders with an
`.lg` extension. The game created above should be called `HistoricalExhibition.lg`.

There is also a `saved_games.dat` file, which contains references to all saved games.


The `saved_games.dat` file must be consistent with the saved games that are present, and will complain
if a saved game has been removed. However, if the file is deleted, OOTP will automatically detect that,
find saved games, and regenerate a `saved_games.dat` file using the games it finds.

## Procedure to Create New Game from Saved Game

* Remove or rename `saved_games` directory, if it exists
* Create a new, empty directory named `saved_games` in the OOTP data directory
* Copy `HistoricalExhibition.lg` (the clean, unsimulated game) into the new, empty `saved_games` directory
* Start up OOTP Baseball Simulator; this will automatically create a `saved_games.dat` file
* Click "Load Game" and load up your clean, unsimulated exhibition game with correct rosters and lineups.
* Click "Play" or "Simulate" to create a new simulation/timeline
* Save the game and exit OOTP
* Move the game `HistoricalExhibition.lg` to a directory of simulated games, for further processing

With some practice, it only takes a minute or two to run the above steps
and generate a new Infinite Cleveland timeline.
