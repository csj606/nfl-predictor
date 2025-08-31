import datetime
import json
from datetime import timedelta
import time
import boto3
import requests
from botocore.exceptions import ClientError


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


if __name__ == '__main__':
    weekly_games()