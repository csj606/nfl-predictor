from datetime import datetime, timedelta

import boto3
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
        return datetime.date.today() - timedelta(days=6)
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

def get_games(event, context):
    table = boto3.resource("dynamodb").Table('upcoming_games')
    week_num = get_week_num()
    if week_num == -1:
        print("week_num unavailable, failed")
        return {
            "statusCode": 501,
            "body": "Error - week number unavailable"
        }

    games = table.get_item(
        Key={
            "week_num": week_num
        }
    )

    return {
        "statusCode": 200,
        "body": games
    }
    