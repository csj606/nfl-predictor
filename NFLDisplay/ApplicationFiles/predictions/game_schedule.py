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
            results = table.get_item(
                Key={"week_num": week_num}
            )
            items = results["Item"]["games"]
            return items
        else:
            return "Table doesn't exist"

