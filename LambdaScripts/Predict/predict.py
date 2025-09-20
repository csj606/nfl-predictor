import sys
import boto3
import pandas as pd
import pickle


def prediction(event, context):
    parameters = event["queryStringParameters"]
    team_name = parameters["teamName"]
    oppo_name = parameters["oppoName"]

    annual_stats_table = boto3.resource("dynamodb").Table("annual_stats")
    weekly_stats_table = boto3.resource("dynamodb").Table("weekly_statistics")

    team_ann_stats = annual_stats_table.get_item(
        Key={"name": team_name}
    )
    oppo_ann_stats = annual_stats_table.get_item(
        Key={"name": oppo_name}
    )

    team_week_stats = weekly_stats_table.get_item(
        Key={
            "name": team_name
        }
    )

    oppo_week_stats = weekly_stats_table.get_item(
        Key={
            "name": oppo_name
        }
    )

    team_ann_stat_frame = pd.read_json(team_ann_stats["stats"])
    oppo_ann_stat_frame = pd.read_json(oppo_ann_stats["stats"])

    drop_columns_for_an = ["season", "team", "season_type", "games"]

    team_ann_stat_frame = team_ann_stat_frame.drop(drop_columns_for_an)
    oppo_ann_stat_frame = oppo_ann_stat_frame.drop(drop_columns_for_an)

    team_ann_stat_frame.columns = ["pst_" + col for col in team_ann_stat_frame.columns]
    oppo_ann_stat_frame.columns = ["pst_" + col for col in oppo_ann_stat_frame.columns]

    team_week_stat_frame = pd.read_json(team_week_stats["stats"])
    oppo_week_stat_frame = pd.read_json(oppo_week_stats["stats"])

    drop_columns_for_week = ["season", "week", "team", "season_type", "opponent_team"]

    team_week_stat_frame = team_week_stat_frame.drop(drop_columns_for_week)
    oppo_week_stat_frame = oppo_week_stat_frame.drop(drop_columns_for_week)

    team_week_stat_frame.columns = ["avg_" + col for col in team_week_stat_frame.columns]
    oppo_week_stat_frame.columns = ["avg_" + col for col in oppo_week_stat_frame.columns]

    diff_week_frame = team_week_stat_frame - oppo_week_stat_frame
    diff_ann_frame = team_ann_stat_frame - oppo_ann_stat_frame

    combo_frame = pd.concat([diff_week_frame, diff_ann_frame], axis=1)
    dropped_columns = ["avg_passing_tds", "avg_passing_interceptions", "avg_sack_fumbles",
                       "avg_sack_fumbles_lost", "avg_passing_2pt_conversions", "avg_rushing_tds", "avg_rushing_fumbles",
                       "avg_rushing_fumbles_lost", "avg_rushing_2pt_conversions", "avg_special_teams_tds",
                       "avg_def_sacks",
                       "avg_def_pass_defended", "avg_def_tds", "avg_def_safeties", "avg_fumble_recovery_own",
                       "avg_fumble_recovery_tds",
                       "avg_timeouts", "avg_fg_missed", "avg_pat_made", "avg_pat_missed", "avg_pat_blocked",
                       "pst_sack_fumbles_lost", "pst_receiving_fumbles_lost", "pst_fg_pct", "pst_fg_made_50_59",
                       "pst_fg_missed_20_29", "pst_fg_missed_40_49", "pst_fg_missed_50_59", "pst_pat_pct",
                       "avg_receptions", "avg_targets", "avg_receiving_yards", "avg_receiving_tds",
                       "avg_receiving_first_downs", "pst_fg_missed_0_19", "avg_completions", "avg_attempts",
                       "avg_passing_first_downs", "avg_sack_yards_lost", "avg_rushing_first_downs", "avg_carries",
                       "pst_receptions", "pst_targets", "pst_receiving_yards", "pst_receiving_tds",
                       "pst_receiving_first_downs", "pst_fg_missed_0_19", "pst_completions", "pst_attempts",
                       "pst_passing_first_downs", "pst_sack_yards_lost", "pst_rushing_first_downs",
                       "pst_carries", "avg_fumble_recovery_yards_opp", "pst_fumble_recovery_yards_opp",
                       "avg_fumble_recovery_yards_own", "pst_fumble_recovery_yards_own", "avg_penalty_yards",
                       "pst_penalty_yards", "avg_def_sack_yards", "pst_def_sack_yards",
                       "avg_def_tackles_for_loss_yards", "pst_def_tackles_for_loss_yards", "avg_receiving_epa",
                       "pst_receiving_epa", "avg_receiving_2pt_conversions", "pst_receiving_2pt_conversions",
                       "avg_passing_yards_after_catch", "pst_passing_yards_after_catch",
                       "avg_receiving_yards_after_catch",
                       "pst_receiving_yards_after_catch", "avg_receiving_air_yards", "pst_receiving_air_yards",
                       "avg_kickoff_return_yards", "pst_kickoff_return_yards", "pst_fg_made_distance",
                       "avg_fg_made_distance",
                       "avg_fg_att", "pst_fg_att", "avg_fg_missed_distance", "pst_fg_missed_distance",
                       "avg_fg_blocked_distance",
                       "pst_fg_blocked_distance", "pst_pat_att", "avg_pat_att", "pst_gwfg_att", "avg_fg_long",
                       "avg_fg_pct",
                       "avg_pat_pct", "avg_def_fumbles", "pst_def_fumbles"]
    combo_frame = combo_frame.drop(dropped_columns)
    with (open("model.pkl", "rb") as modelfile):
        model = pickle.load(modelfile)
        result = model.predict(combo_frame.iloc[0])
        return {
            "statusCode": 200,
            "body": result
        }


