import time
import pandas as pd
import boto3
import json


def annual_stats():
    cur_year = time.localtime().tm_year
    annual_statistics = pd.read_csv(
        f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_reg_{cur_year - 1}.csv")
    annual_statistics = annual_statistics.fillna(0)
    objects = []
    team_index = {}
    for index, row in annual_statistics.iterrows():
        j = row.to_json()
        objects.append(j)
        team_index[index] = row["team"]
    annual_stat_table = boto3.resource("dynamodb").Table("annual_stats")
    for i in range(len(objects)):
        team = team_index[i]
        j = json.dumps(objects[i])
        annual_stat_table.put_item(
            Item={
                "team": team,
                "stats": j
            }
        )


if __name__ == '__main__':
    annual_stats()
