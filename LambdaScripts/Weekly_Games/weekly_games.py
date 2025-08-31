import datetime
import json
from datetime import timedelta
import time
import boto3
import requests
from botocore.exceptions import ClientError
import pandas as pd

team_acronyms = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET", "GB", "HOU", "IND", "JAX",
                 "KC", "LA", "LAC", "LV", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "PHI", "PIT", "SEA", "SF", "TB",
                 "TEN", "WAS"]


def get_end_of_week(day_of_week):
    mon, tue, wed, thu, fri, sat, sun = range(1, 8)
    # End of the week == Monday
    if day_of_week == mon:
        return datetime.date.today()
    elif day_of_week == tue:
        return datetime.date.today() + timedelta(days=6)
    elif day_of_week == wed:
        return datetime.date.today() + timedelta(days=5)
    elif day_of_week == thu:
        return datetime.date.today() + timedelta(days=4)
    elif day_of_week == fri:
        return datetime.date.today() + timedelta(days=3)
    elif day_of_week == sat:
        return datetime.date.today() + timedelta(days=2)
    else:
        return datetime.date.today() + timedelta(days=1)


def get_start_of_week(day_of_week):
    mon, tue, wed, thu, fri, sat, sun = range(1, 8)
    if day_of_week == mon:
        return datetime.date.today() - datetime.timedelta(days=6)
    elif day_of_week == tue:
        return datetime.date.today()
    elif day_of_week == wed:
        return datetime.date.today() - timedelta(days=1)
    elif day_of_week == thu:
        return datetime.date.today() - timedelta(days=2)
    elif day_of_week == fri:
        return datetime.date.today() - timedelta(days=3)
    elif day_of_week == sat:
        return datetime.date.today() - timedelta(days=4)
    else:
        return datetime.date.today() - timedelta(days=5)


def get_week_num():
    try:
        table = boto3.resource("dynamodb").Table("season_weeks")
        cur_time = datetime.date.today()
        day_of_week = cur_time.isoweekday()

        start_of_week = get_start_of_week(day_of_week)
        end_of_week = get_end_of_week(day_of_week)

        range_str = start_of_week.__str__() + end_of_week.__str__()

        results = table.get_item(
            Key={"date_range": range_str}
        )
        week_num = results["Item"]["week_num"]
        return week_num
    except ClientError as err:
        if err.response["Error"]["Code"] == "ResourceNotFoundException":
            return -1


def weekly_games():
    espn_games = requests.get("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard")
    if not espn_games.ok:
        print("Request failed, retrying in fifteen minutes")
        time.sleep(900)
        weekly_games()
    data = espn_games.json()
    nfl_data = data["leagues"][0]
    games = nfl_data["events"]
    table = boto3.resource("dynamodb").Table('upcoming_games')
    week_num = get_week_num()
    if week_num == -1:
        print("Week number unavailable, retrying in fifteen minutes")
        time.sleep(900)
        weekly_games()

    info = []
    for game in games:
        home_team = game["competitions"][0]["competitors"][0]["abbreviation"]
        oppo_team = game["competitions"][0]["competitors"][1]["abbreviation"]
        info.append({
            "home_team": home_team,
            "oppo_team": oppo_team
        })

    table.put_item(
        Item={
            'week_num': week_num,
            'games': json.dumps(info)
        }
    )

def update_weekly_stats():
    year = time.localtime().tm_year
    week_num = get_week_num()
    weekly_stat_table = boto3.resource("dynamodb").Table("weekly_statistics")
    check = requests.request("head", f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_week_{year}.csv")
    if check.status_code != 200:
        zero = {"invalid": 0}
        z = json.dumps(zero)
        for team in team_acronyms:
            weekly_stat_table.put_item(
                Item={
                    "team": team,
                    "stats": z
                }
            )
    else:
        weekly_data = pd.read_csv(f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_week_{year}.csv")
        weekly_data = weekly_data.fillna(0)
        for team in team_acronyms:
            team_avgs = weekly_data.query("(team == @team) and ((week < @week_num) and (week > (@week_num - 3)))").reset_index(drop=True)
            team_avgs = team_avgs.mean(numeric_only=True).to_frame().T
            weekly_stat_table.put_item(
                Item={
                    "team": team,
                    "stats": team_avgs
                }
            )


if __name__ == '__main__':
    weekly_games()
    update_weekly_stats()
