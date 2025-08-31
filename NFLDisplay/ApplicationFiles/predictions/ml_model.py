import json
import boto3


class PredictionModel:
    def __init__(self):
        self.client = boto3.client('lambda')

    def model_call(self, team_name, opp_name):
        function_name = 'prediction'
        payload = {'team_name': team_name, 'opp_name': opp_name}

        response = self.client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )

        if response["StatusCode"] == 200:
            response_data = json.loads(response['Payload'].read())
            return response_data
        else:
            return f"Error: {response['StatusCode']}"
