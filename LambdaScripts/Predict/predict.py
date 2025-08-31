import sys
import boto3


def predict(team_name):
    pred_score = -1
    annual_stats_table = boto3.resource("dynamodb").Table("annual_stats")
    weekly_stats_table = boto3.resource("dynamodb").Table("weekly_statistics")

    team_ann_stats = annual_stats_table.get_item(
        Key={}
    )

    return pred_score


if __name__ == '__main__':
    team_name = sys.argv[1]
    oppo_name = sys.argv[2]
    predict(team_name, oppo_name)