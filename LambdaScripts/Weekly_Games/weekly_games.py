import time
import boto3
import requests


def weekly_games():
    espn_games = requests.get("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard")
    if not espn_games.ok:
        print("Request failed, retrying in five minutes")
        time.sleep(300)
        weekly_games()
    data = espn_games.json()
    nfl_data = data["leagues"][0]
    games = nfl_data["events"]
    table = boto3.resource("dynamodb").Table('weekly_games')
    for game in games:
        home_team = game["competitions"][0]["competitors"][0]["abbreviation"]
        oppo_team = game["competitions"][0]["competitors"][1]["abbreviation"]
        table.put_item()