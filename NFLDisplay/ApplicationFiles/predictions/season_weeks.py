import boto3
import time

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


class SeasonWeeks:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def exists(self):
        try:
            table = self.dynamodb.Table('upcoming_games')
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                return False

    def get_week_num(self):
        if self.exists():
            table = self.dynamodb.Table("season_weeks")
            cur_time = time.localtime().__str__()
            results = table.query(
                KeyConditionExpression=Key('start_time').lte(cur_time) & Key("end_time").gte(cur_time)
            )
            items = results["Items"]
            return items
        else:
            return "Table doesn't exist"
