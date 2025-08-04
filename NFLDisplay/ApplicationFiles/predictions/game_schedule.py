import time

import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


class UpcomingGames:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def exists(self):
        try:
            table = self.dynamodb.Table('upcoming_games')
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                return False

    def get_upcoming_weekly_games(self, week_num):
        if self.exists():
            table = self.dynamodb.Table("upcoming_games")
            cur_time = time.localtime().__str__()
            results = table.query(
                KeyConditionExpression=Key('week_num').eq(week_num) & Key("game_time").gte(cur_time)
            )
            items = results["Items"]
            return items
        else:
            return "Table doesn't exist"

    def get_games_for_team(self, week_num, team_name):
        if self.exists():
            table = self.dynamodb.Table("upcoming_games")
            cur_time = time.localtime().__str__()
            results = table.query(
                KeyConditionExpression=Key('week_num').eq(week_num) & Key("game_time").gte(cur_time),
                FilterExpression=Attr('team_name').eq(team_name)
            )
        else:
            return "Table doesn't exist"

