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
            results = table.get_item(
                Key={"team_name": team}
            )
            return f"{results['Item']['wins']} - {results['Item']['defeats']}"
        else:
            return "Table doesn't exist"
