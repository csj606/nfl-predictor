import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


class TeamStatistics:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def exists(self):
        try:
            table = self.dynamodb.Table('team_statistics')
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                return False

    def get_team_stats(self, name):
        if self.exists():
            table = self.dynamodb.Table('team_statistics')
            result = table.get_item(
                Key={"team": name}
            )
            return result["Item"]["stats"]
        else:
            return "Table doesn't exist"
