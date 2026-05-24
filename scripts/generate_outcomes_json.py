import json
import os
import glob

"""
generate_outcomes_json.py

This script uses data in ../data/ic
to generate outcomes data in ../data/outcomes.json

outcomes.json data structure:
    [
        {
            "WName": "Cleveland",
            "WColor": "e1193a",
            "WRuns": 7,
            "LName": "Florida",
            "LColor": "18a0ad",
            "LRuns": 5,
            "Innings": 9,
            "AlmanacName": "infinite_cleveland_g01_XYZ"
        }
    ]
"""


#CLE_COLOR = "e1193a"
CLE_COLOR = "e31937"
#FLA_COLOR = "18a0ad"
FLA_COLOR = "009ca6"
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA = os.path.join(ROOT, 'data')
OOTP = os.path.join(DATA, 'ic')


outcomes_json = []
gamedirs = sorted(glob.glob(os.path.join(OOTP, '*')))
for k, gamedir in enumerate(gamedirs):
    gamefiles = glob.glob(os.path.join(gamedir, '*'))
    lgdir = None
    for gamefile in gamefiles:
        if gamefile[-3:] == '.lg':
            lgdir = gamefile
    if lgdir is None:
        raise Exception(f"Could not find .lg file for {gamedir}")

    # Now we can traverse the known directory structure
    # of a saved OOTP game.

    # We are only interested in games.csv
    csvdir = os.path.join(lgdir, 'import_export', 'csv')
    gamescsv = os.path.join(csvdir, 'games.csv')

    # Structure:
    # game_id,league_id,home_team,away_team,attendance,date,time,game_type,played,dh,innings,runs0,runs1,hits0,hits1,errors0,errors1,winning_pitcher,losing_pitcher,save_pitcher,starter0,starter1
    # 1,100,2,1,30878,"1997-10-1",2005,3,1,0,9,11,7,14,15,0,2,9,27,0,17,41
    with open(gamescsv, 'r') as f:
        gamescsvlines = f.readlines()
    data = gamescsvlines[1].split(",")
    innings = int(data[10])
    fla_runs = int(data[11])
    cle_runs = int(data[12])
    if fla_runs > cle_runs:
        wname = "Florida"
        wcolor = FLA_COLOR
        wruns = fla_runs
        lname = "Cleveland"
        lcolor = CLE_COLOR
        lruns = cle_runs
    else:
        wname = "Cleveland"
        wcolor = CLE_COLOR
        wruns = cle_runs
        lname = "Florida"
        lcolor = FLA_COLOR
        lruns = fla_runs

    almanac_name = gamedir.split("/")[-1]

    dat = {
        "Index": k+1,
        "WName": wname,
        "WColor": wcolor,
        "WRuns": wruns,
        "LName": lname,
        "LColor": lcolor,
        "LRuns": lruns,
        "Innings": innings,
        "AlmanacName": almanac_name
    }
    outcomes_json.append(dat)

outcomes_json_file = os.path.join(DATA, 'outcomes.json')
with open(outcomes_json_file, 'w') as f:
    json.dump(outcomes_json, f, indent=4)

print(f"Finished generating outcomes in {outcomes_json_file}")
