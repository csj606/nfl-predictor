import boto3
from boto3 import dynamodb
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


class SeasonStanding:

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def exists(self):
        try:
            table = self.dynamodb.Table('standings')
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                return False

    def get_team_standing(self, team):
        if self.exists():
            table = self.dynamodb.Table('standings')
            results = table.query(
                KeyConditionExpression= Key('team_name').eq(team)
            )
            return results
        else:
            return "Table doesn't exist"
