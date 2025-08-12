# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd

team_acronyms = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", ""]
logged_games = {}


def get_records():
    """
    Gets NFL-Verse data and stores it as a CSV for later use
    :return:
    """
    years = [2021, 2022, 2023, 2024]
    for year in years:
        regular_season = pd.read_csv(
            f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_reg_{year}.csv")
        weekly_season = pd.read_csv(
            f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_week_{year}.csv")
        regular_season.to_csv(f"annual_{year}")
        weekly_season.to_csv(f"weekly_{year}")


def create_training_data():
    years = [2022, 2023, 2024]
    for year in years:
        annual_record = pd.read_csv(f"annual_{year - 1}.csv")
        weekly_records = pd.read_csv(f"weekly_{year}.csv")
        # Modify and clean data
        weekly_records.drop(["fg_missed_list", "fg_made_list", "fg_blocked_list", "fg_made_0_19", "fg_made_20_29",
                             "fg_missed_30_39", "fg_missed_40_49", "fg_missed_50_59", "fg_missed_60_", "fg_made_30_39",
                             "fg_made_40_49", "fg_made_50_59", "fg_made_60_", "fg_missed_0_19", "fg_missed_20_29", "season",
                             "season_type", "gwfg_made", "gwfg_att", "gwfg_missed", "gwfg_blocked", "gwfg_distance"])
        annual_record.drop(["gwfg_blocked", "gwfg_distance_list", "fg_missed_list", "fg_made_list", "fg_blocked_list",
                            "fg_missed_60_", "fg_made_60_", "games", "season"])
        weekly_records.fillna(0)
        annual_record.fillna(0)
        # Create training data
        training_data = pd.DataFrame
        training_data.columns = ["week" ,"team","opponent_team","avg_completions","avg_attempts","avg_passing_yards",
                                 "avg_passing_tds","avg_passing_interceptions","avg_sacks_suffered",
                                 "avg_sack_yards_lost","avg_sack_fumbles","avg_sack_fumbles_lost",
                                 "avg_passing_air_yards","avg_passing_yards_after_catch","avg_passing_first_downs",
                                 "avg_passing_epa","avg_passing_cpoe","avg_passing_2pt_conversions","avg_carries",
                                 "avg_rushing_yards","avg_rushing_tds","avg_rushing_fumbles","avg_rushing_fumbles_lost",
                                 "avg_rushing_first_downs","avg_rushing_epa","avg_rushing_2pt_conversions",
                                 "avg_receptions","avg_targets","avg_receiving_yards","avg_receiving_tds",
                                 "avg_receiving_fumbles","avg_receiving_fumbles_lost","avg_receiving_air_yards",
                                 "avg_receiving_yards_after_catch","avg_receiving_first_downs","avg_receiving_epa",
                                 "avg_receiving_2pt_conversions","avg_special_teams_tds","avg_def_tackles_solo","avg_def_tackles_with_assist",
                                 "avg_def_tackle_assists","avg_def_tackles_for_loss","avg_def_tackles_for_loss_yards","avg_def_fumbles_forced",
                                 "avg_def_sacks","avg_def_sack_yards","avg_def_qb_hits","avg_def_interceptions","avg_def_interception_yards",
                                 "avg_def_pass_defended","avg_def_tds","avg_def_fumbles","avg_def_safeties","avg_misc_yards","avg_fumble_recovery_own",
                                 "avg_fumble_recovery_yards_own","avg_fumble_recovery_opp","avg_fumble_recovery_yards_opp",
                                 "avg_fumble_recovery_tds","avg_penalties","avg_penalty_yards","avg_timeouts","avg_punt_returns","avg_punt_return_yards",
                                 "avg_kickoff_returns","avg_kickoff_return_yards","avg_fg_made","avg_fg_att","avg_fg_missed","avg_fg_blocked",
                                 "avg_fg_long","avg_fg_pct","avg_fg_made_distance","avg_fg_missed_distance","avg_fg_blocked_distance",
                                 "avg_pat_made","avg_pat_att","avg_pat_missed","avg_pat_blocked","avg_pat_pct",
                                 "pst_completions","pst_attempts","pst_passing_yards","pst_passing_tds","pst_passing_interceptions",
                                 "pst_sacks_suffered","pst_sack_yards_lost","pst_sack_fumbles","pst_sack_fumbles_lost","pst_passing_air_yards",
                                 "pst_passing_yards_after_catch","pst_passing_first_downs","pst_passing_epa","pst_passing_cpoe",
                                 "pst_passing_2pt_conversions","pst_carries","pst_rushing_yards","pst_rushing_tds",
                                 "pst_rushing_fumbles","pst_rushing_fumbles_lost","pst_rushing_first_downs","pst_rushing_epa",
                                 "pst_rushing_2pt_conversions","pst_receptions","pst_targets","pst_receiving_yards","pst_receiving_tds",
                                 "pst_receiving_fumbles","pst_receiving_fumbles_lost","pst_receiving_air_yards",
                                 "pst_receiving_yards_after_catch","pst_receiving_first_downs","pst_receiving_epa",
                                 "pst_receiving_2pt_conversions","pst_special_teams_tds","pst_def_tackles_solo",
                                 "pst_def_tackles_with_assist","pst_def_tackle_assists","pst_def_tackles_for_loss",
                                 "pst_def_tackles_for_loss_yards","pst_def_fumbles_forced","pst_def_sacks","pst_def_sack_yards",
                                 "pst_def_qb_hits","pst_def_interceptions","pst_def_interception_yards","pst_def_pass_defended",
                                 "pst_def_tds","pst_def_fumbles","pst_def_safeties","pst_misc_yards","pst_fumble_recovery_own",
                                 "pst_fumble_recovery_yards_own","pst_fumble_recovery_opp","pst_fumble_recovery_yards_opp",
                                 "pst_fumble_recovery_tds","pst_penalties","pst_penalty_yards","pst_timeouts","pst_punt_returns",
                                 "pst_punt_return_yards","pst_kickoff_returns","pst_kickoff_return_yards","pst_fg_made","pst_fg_att",
                                 "pst_fg_missed","pst_fg_blocked","pst_fg_long","pst_fg_pct","pst_fg_made_0_19","pst_fg_made_20_29",
                                 "pst_fg_made_30_39","pst_fg_made_40_49","pst_fg_made_50_59","pst_fg_missed_0_19","pst_fg_missed_20_29",
                                 "pst_fg_missed_30_39","pst_fg_missed_40_49","pst_fg_missed_50_59","pst_fg_made_list",
                                 "pst_fg_missed_list","pst_fg_blocked_list","pst_fg_made_distance","pst_fg_missed_distance","pst_fg_blocked_distance",
                                 "pst_pat_made","pst_pat_att","pst_pat_missed","pst_pat_blocked","pst_pat_pct","pst_gwfg_made","pst_gwfg_att"]

        for index, row in weekly_records.iterrows():
            








def team_name_to_num(team_name: str) -> int:
    """
    Returns the team name as an integer - used for specific features in the model
    :param team_name: The name of the team, as listed in team_names
    :return: The index of the team name in the team_name list
    """
    return team_acronyms.index(team_name)


if __name__ == "__main__":
    get_records()
