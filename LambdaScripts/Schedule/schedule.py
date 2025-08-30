import requests
import time
import boto3


def schedule():
    espn_games = requests.get("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard")
    if not espn_games.ok:
        print("Request failed, retrying in fifteen minutes")
        time.sleep(900)
        schedule()
    data = espn_games.json()
    nfl_data = data["leagues"][0]
    regular_calendar = nfl_data["calendar"][1]
    table = boto3.resource("dynamodb").Table('season_week')
    for week in regular_calendar:
        table.put_item(
            Item={
                'date_range': f"{week['startDate'][0:10]}{week['endDate'][0:10]}",
                'week_num': int(week['value'])
            }
        )


if __name__ == "__main__":
    schedule()
