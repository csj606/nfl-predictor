# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd
from pandas import DataFrame, Series

team_acronyms = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET", "GB", "HOU", "IND", "JAX",
                 "KC", "LA", "LAC", "LV", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "PHI", "PIT", "SEA", "SF", "TB",
                 "TEN", "WAS"]
logged_games = {}


def get_records():
    """
    Gets NFL-Verse data and stores it as a CSV for later use
    :return:
    """
    years = [2018, 2019]
    for year in years:
        regular_season = pd.read_csv(
            f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_reg_{year - 1}.csv")
        weekly_season = pd.read_csv(
            f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_week_{year}.csv")
        regular_season.to_csv(f"annual_{year - 1}.csv")
        weekly_season.to_csv(f"weekly_{year}.csv")


def create_training_data():
    years = [2018, 2019]
    for year in years:
        annual_record = pd.read_csv(f"annual_{year - 1}.csv")
        weekly_records = pd.read_csv(f"weekly_{year}.csv")
        # Modify and clean data
        weekly_records.drop(
            columns=["fg_missed_list", "fg_made_list", "fg_blocked_list", "fg_made_0_19", "fg_made_20_29",
                     "fg_missed_30_39", "fg_missed_40_49", "fg_missed_50_59", "fg_missed_60_", "fg_made_30_39",
                     "fg_made_40_49", "fg_made_50_59", "fg_made_60_", "fg_missed_0_19", "fg_missed_20_29",
                     "season",
                     "season_type", "gwfg_made", "gwfg_att", "gwfg_missed", "gwfg_blocked", "gwfg_distance",
                     "Unnamed: 0"])
        annual_record.drop(
            columns=["gwfg_blocked", "gwfg_distance_list", "fg_missed_list", "fg_made_list", "fg_blocked_list",
                     "fg_missed_60_", "fg_made_60_", "games", "season", "Unnamed: 0"])
        weekly_records.fillna(0)
        annual_record.fillna(0)
        # Create training data
        columns = ["week", "team", "opponent_team", "avg_completions", "avg_attempts",
                   "avg_passing_yards",
                   "avg_passing_tds", "avg_passing_interceptions", "avg_sacks_suffered",
                   "avg_sack_yards_lost", "avg_sack_fumbles", "avg_sack_fumbles_lost",
                   "avg_passing_air_yards", "avg_passing_yards_after_catch", "avg_passing_first_downs",
                   "avg_passing_epa", "avg_passing_cpoe", "avg_passing_2pt_conversions", "avg_carries",
                   "avg_rushing_yards", "avg_rushing_tds", "avg_rushing_fumbles",
                   "avg_rushing_fumbles_lost",
                   "avg_rushing_first_downs", "avg_rushing_epa", "avg_rushing_2pt_conversions",
                   "avg_receptions", "avg_targets", "avg_receiving_yards", "avg_receiving_tds",
                   "avg_receiving_fumbles", "avg_receiving_fumbles_lost", "avg_receiving_air_yards",
                   "avg_receiving_yards_after_catch", "avg_receiving_first_downs", "avg_receiving_epa",
                   "avg_receiving_2pt_conversions", "avg_special_teams_tds", "avg_def_tackles_solo",
                   "avg_def_tackles_with_assist",
                   "avg_def_tackle_assists", "avg_def_tackles_for_loss", "avg_def_tackles_for_loss_yards",
                   "avg_def_fumbles_forced",
                   "avg_def_sacks", "avg_def_sack_yards", "avg_def_qb_hits", "avg_def_interceptions",
                   "avg_def_interception_yards",
                   "avg_def_pass_defended", "avg_def_tds", "avg_def_fumbles", "avg_def_safeties",
                   "avg_misc_yards", "avg_fumble_recovery_own",
                   "avg_fumble_recovery_yards_own", "avg_fumble_recovery_opp",
                   "avg_fumble_recovery_yards_opp",
                   "avg_fumble_recovery_tds", "avg_penalties", "avg_penalty_yards", "avg_timeouts",
                   "avg_punt_returns", "avg_punt_return_yards",
                   "avg_kickoff_returns", "avg_kickoff_return_yards", "avg_fg_made", "avg_fg_att",
                   "avg_fg_missed", "avg_fg_blocked",
                   "avg_fg_long", "avg_fg_pct", "avg_fg_made_distance", "avg_fg_missed_distance",
                   "avg_fg_blocked_distance",
                   "avg_pat_made", "avg_pat_att", "avg_pat_missed", "avg_pat_blocked", "avg_pat_pct",
                   "pst_completions", "pst_attempts", "pst_passing_yards", "pst_passing_tds",
                   "pst_passing_interceptions",
                   "pst_sacks_suffered", "pst_sack_yards_lost", "pst_sack_fumbles",
                   "pst_sack_fumbles_lost", "pst_passing_air_yards",
                   "pst_passing_yards_after_catch", "pst_passing_first_downs", "pst_passing_epa",
                   "pst_passing_cpoe",
                   "pst_passing_2pt_conversions", "pst_carries", "pst_rushing_yards", "pst_rushing_tds",
                   "pst_rushing_fumbles", "pst_rushing_fumbles_lost", "pst_rushing_first_downs",
                   "pst_rushing_epa",
                   "pst_rushing_2pt_conversions", "pst_receptions", "pst_targets", "pst_receiving_yards",
                   "pst_receiving_tds",
                   "pst_receiving_fumbles", "pst_receiving_fumbles_lost", "pst_receiving_air_yards",
                   "pst_receiving_yards_after_catch", "pst_receiving_first_downs", "pst_receiving_epa",
                   "pst_receiving_2pt_conversions", "pst_special_teams_tds", "pst_def_tackles_solo",
                   "pst_def_tackles_with_assist", "pst_def_tackle_assists", "pst_def_tackles_for_loss",
                   "pst_def_tackles_for_loss_yards", "pst_def_fumbles_forced", "pst_def_sacks",
                   "pst_def_sack_yards",
                   "pst_def_qb_hits", "pst_def_interceptions", "pst_def_interception_yards",
                   "pst_def_pass_defended",
                   "pst_def_tds", "pst_def_fumbles", "pst_def_safeties", "pst_misc_yards",
                   "pst_fumble_recovery_own",
                   "pst_fumble_recovery_yards_own", "pst_fumble_recovery_opp",
                   "pst_fumble_recovery_yards_opp",
                   "pst_fumble_recovery_tds", "pst_penalties", "pst_penalty_yards", "pst_timeouts",
                   "pst_punt_returns",
                   "pst_punt_return_yards", "pst_kickoff_returns", "pst_kickoff_return_yards",
                   "pst_fg_made", "pst_fg_att",
                   "pst_fg_missed", "pst_fg_blocked", "pst_fg_long", "pst_fg_pct", "pst_fg_made_0_19",
                   "pst_fg_made_20_29",
                   "pst_fg_made_30_39", "pst_fg_made_40_49", "pst_fg_made_50_59", "pst_fg_missed_0_19",
                   "pst_fg_missed_20_29",
                   "pst_fg_missed_30_39", "pst_fg_missed_40_49", "pst_fg_missed_50_59",
                   "pst_fg_made_distance",
                   "pst_fg_missed_distance", "pst_fg_blocked_distance",
                   "pst_pat_made", "pst_pat_att", "pst_pat_missed", "pst_pat_blocked", "pst_pat_pct",
                   "pst_gwfg_made", "pst_gwfg_att"]
        training_data: DataFrame = pd.DataFrame(columns=columns)

        for index, row in weekly_records.iterrows():
            week = int(row["week"])
            team = row["team"]
            opponent_team = row["opponent_team"]
            avg_completions = get_rolling_avg(statistic="completions", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_attempts = get_rolling_avg(statistic="attempts", dataframe=weekly_records, end_week=week,
                                           select_team=team)
            avg_passing_yards = get_rolling_avg(statistic="passing_yards", dataframe=weekly_records, end_week=week,
                                                select_team=team)
            avg_passing_tds = get_rolling_avg(statistic="passing_tds", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_passing_interceptions = get_rolling_avg(statistic="passing_interceptions", dataframe=weekly_records,
                                                        end_week=week, select_team=team)
            avg_sacks_suffered = get_rolling_avg(statistic="sacks_suffered", dataframe=weekly_records, end_week=week,
                                                 select_team=team)
            avg_sack_yards_lost = get_rolling_avg(statistic="sack_yards_lost", dataframe=weekly_records, end_week=week,
                                                  select_team=team)
            avg_sack_fumbles = get_rolling_avg(statistic="sack_fumbles", dataframe=weekly_records, end_week=week,
                                               select_team=team)
            avg_sack_fumbles_lost = get_rolling_avg(statistic="sack_fumbles_lost", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_passing_air_yards = get_rolling_avg(statistic="passing_air_yards", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_passing_yards_after_catch = get_rolling_avg(statistic="passing_yards_after_catch",
                                                            dataframe=weekly_records, end_week=week, select_team=team)
            avg_passing_first_downs = get_rolling_avg(statistic="passing_first_downs", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_passing_epa = get_rolling_avg(statistic="passing_epa", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_passing_cpoe = get_rolling_avg(statistic="passing_cpoe", dataframe=weekly_records, end_week=week,
                                               select_team=team)
            avg_passing_2pt_conversions = get_rolling_avg(statistic="passing_2pt_conversions", dataframe=weekly_records,
                                                          end_week=week, select_team=team)
            avg_carries = get_rolling_avg(statistic="carries", dataframe=weekly_records, end_week=week,
                                          select_team=team)
            avg_rushing_yards = get_rolling_avg(statistic="rushing_yards", dataframe=weekly_records, end_week=week,
                                                select_team=team)
            avg_rushing_tds = get_rolling_avg(statistic="rushing_tds", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_rushing_fumbles = get_rolling_avg(statistic="rushing_fumbles", dataframe=weekly_records, end_week=week,
                                                  select_team=team)
            avg_rushing_fumbles_lost = get_rolling_avg(statistic="rushing_fumbles_lost", dataframe=weekly_records,
                                                       end_week=week, select_team=team)
            avg_rushing_first_downs = get_rolling_avg(statistic="rushing_first_downs", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_rushing_epa = get_rolling_avg(statistic="rushing_epa", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_rushing_2pt_conversions = get_rolling_avg(statistic="rushing_2pt_conversions", dataframe=weekly_records,
                                                          end_week=week, select_team=team)
            avg_receptions = get_rolling_avg(statistic="receptions", dataframe=weekly_records, end_week=week,
                                             select_team=team)
            avg_targets = get_rolling_avg(statistic="targets", dataframe=weekly_records, end_week=week,
                                          select_team=team)
            avg_receiving_yards = get_rolling_avg(statistic="receiving_yards", dataframe=weekly_records, end_week=week,
                                                  select_team=team)
            avg_receiving_tds = get_rolling_avg(statistic="receiving_tds", dataframe=weekly_records, end_week=week,
                                                select_team=team)
            avg_receiving_fumbles = get_rolling_avg(statistic="receiving_fumbles", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_receiving_fumbles_lost = get_rolling_avg(statistic="receiving_fumbles_lost", dataframe=weekly_records,
                                                         end_week=week, select_team=team)
            avg_receiving_air_yards = get_rolling_avg(statistic="receiving_air_yards", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_receiving_yards_after_catch = get_rolling_avg(statistic="receiving_yards_after_catch",
                                                              dataframe=weekly_records, end_week=week, select_team=team)
            avg_receiving_first_downs = get_rolling_avg(statistic="receiving_first_downs", dataframe=weekly_records,
                                                        end_week=week, select_team=team)
            avg_receiving_epa = get_rolling_avg(statistic="receiving_epa", dataframe=weekly_records, end_week=week,
                                                select_team=team)
            avg_receiving_2pt_conversions = get_rolling_avg(statistic="receiving_2pt_conversions",
                                                            dataframe=weekly_records, end_week=week, select_team=team)
            avg_special_teams_tds = get_rolling_avg(statistic="special_teams_tds", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_def_tackles_solo = get_rolling_avg(statistic="def_tackles_solo", dataframe=weekly_records,
                                                   end_week=week, select_team=team)
            avg_def_tackles_with_assist = get_rolling_avg(statistic="def_tackles_with_assist", dataframe=weekly_records,
                                                          end_week=week, select_team=team)
            avg_def_tackle_assists = get_rolling_avg(statistic="def_tackle_assists", dataframe=weekly_records,
                                                     end_week=week, select_team=team)
            avg_def_tackles_for_loss = get_rolling_avg(statistic="def_tackles_for_loss", dataframe=weekly_records,
                                                       end_week=week, select_team=team)
            avg_def_tackles_for_loss_yards = get_rolling_avg(statistic="def_tackles_for_loss_yards",
                                                             dataframe=weekly_records, end_week=week, select_team=team)
            avg_def_fumbles_forced = get_rolling_avg(statistic="def_fumbles_forced", dataframe=weekly_records,
                                                     end_week=week, select_team=team)
            avg_def_sacks = get_rolling_avg(statistic="def_sacks", dataframe=weekly_records, end_week=week,
                                            select_team=team)
            avg_def_sack_yards = get_rolling_avg(statistic="def_sack_yards", dataframe=weekly_records, end_week=week,
                                                 select_team=team)
            avg_def_qb_hits = get_rolling_avg(statistic="def_qb_hits", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_def_interceptions = get_rolling_avg(statistic="def_interceptions", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_def_interception_yards = get_rolling_avg(statistic="def_interception_yards", dataframe=weekly_records,
                                                         end_week=week, select_team=team)
            avg_def_pass_defended = get_rolling_avg(statistic="def_pass_defended", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_def_tds = get_rolling_avg(statistic="def_tds", dataframe=weekly_records, end_week=week,
                                          select_team=team)
            avg_def_fumbles = get_rolling_avg(statistic="def_fumbles", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_def_safeties = get_rolling_avg(statistic="def_safeties", dataframe=weekly_records, end_week=week,
                                               select_team=team)
            avg_misc_yards = get_rolling_avg(statistic="misc_yards", dataframe=weekly_records, end_week=week,
                                             select_team=team)
            avg_fumble_recovery_own = get_rolling_avg(statistic="fumble_recovery_own", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_fumble_recovery_yards_own = get_rolling_avg(statistic="fumble_recovery_yards_own",
                                                            dataframe=weekly_records, end_week=week, select_team=team)
            avg_fumble_recovery_opp = get_rolling_avg(statistic="fumble_recovery_opp", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_fumble_recovery_yards_opp = get_rolling_avg(statistic="fumble_recovery_yards_opp",
                                                            dataframe=weekly_records, end_week=week, select_team=team)
            avg_fumble_recovery_tds = get_rolling_avg(statistic="fumble_recovery_tds", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_penalties = get_rolling_avg(statistic="penalties", dataframe=weekly_records, end_week=week,
                                            select_team=team)
            avg_penalty_yards = get_rolling_avg(statistic="penalty_yards", dataframe=weekly_records, end_week=week,
                                                select_team=team)
            avg_timeouts = get_rolling_avg(statistic="timeouts", dataframe=weekly_records, end_week=week,
                                           select_team=team)
            avg_punt_returns = get_rolling_avg(statistic="punt_returns", dataframe=weekly_records, end_week=week,
                                               select_team=team)
            avg_punt_return_yards = get_rolling_avg(statistic="punt_return_yards", dataframe=weekly_records,
                                                    end_week=week, select_team=team)
            avg_kickoff_returns = get_rolling_avg(statistic="kickoff_returns", dataframe=weekly_records, end_week=week,
                                                  select_team=team)
            avg_kickoff_return_yards = get_rolling_avg(statistic="kickoff_return_yards", dataframe=weekly_records,
                                                       end_week=week, select_team=team)
            avg_fg_made = get_rolling_avg(statistic="fg_made", dataframe=weekly_records, end_week=week,
                                          select_team=team)
            avg_fg_att = get_rolling_avg(statistic="fg_att", dataframe=weekly_records, end_week=week, select_team=team)
            avg_fg_missed = get_rolling_avg(statistic="fg_missed", dataframe=weekly_records, end_week=week,
                                            select_team=team)
            avg_fg_blocked = get_rolling_avg(statistic="fg_blocked", dataframe=weekly_records, end_week=week,
                                             select_team=team)
            avg_fg_long = get_rolling_avg(statistic="fg_long", dataframe=weekly_records, end_week=week,
                                          select_team=team)
            avg_fg_pct = get_rolling_avg(statistic="fg_pct", dataframe=weekly_records, end_week=week, select_team=team)
            avg_fg_made_distance = get_rolling_avg(statistic="fg_made_distance", dataframe=weekly_records,
                                                   end_week=week, select_team=team)
            avg_fg_missed_distance = get_rolling_avg(statistic="fg_missed_distance", dataframe=weekly_records,
                                                     end_week=week, select_team=team)
            avg_fg_blocked_distance = get_rolling_avg(statistic="fg_blocked_distance", dataframe=weekly_records,
                                                      end_week=week, select_team=team)
            avg_pat_made = get_rolling_avg(statistic="pat_made", dataframe=weekly_records, end_week=week,
                                           select_team=team)
            avg_pat_att = get_rolling_avg(statistic="pat_att", dataframe=weekly_records, end_week=week,
                                          select_team=team)
            avg_pat_missed = get_rolling_avg(statistic="pat_missed", dataframe=weekly_records, end_week=week,
                                             select_team=team)
            avg_pat_blocked = get_rolling_avg(statistic="pat_blocked", dataframe=weekly_records, end_week=week,
                                              select_team=team)
            avg_pat_pct = get_rolling_avg(statistic="pat_pct", dataframe=weekly_records, end_week=week,
                                          select_team=team)

            # Get past statistics
            pst_completions = get_last_years_stat(statistic="completions", dataframe=annual_record, select_team=team)
            pst_attempts = get_last_years_stat(statistic="attempts", dataframe=annual_record, select_team=team)
            pst_passing_yards = get_last_years_stat(statistic="passing_yards", dataframe=annual_record,
                                                    select_team=team)
            pst_passing_tds = get_last_years_stat(statistic="passing_tds", dataframe=annual_record, select_team=team)
            pst_passing_interceptions = get_last_years_stat(statistic="passing_interceptions", dataframe=annual_record,
                                                            select_team=team)
            pst_sacks_suffered = get_last_years_stat(statistic="sacks_suffered", dataframe=annual_record,
                                                     select_team=team)
            pst_sack_yards_lost = get_last_years_stat(statistic="sack_yards_lost", dataframe=annual_record,
                                                      select_team=team)
            pst_sack_fumbles = get_last_years_stat(statistic="sack_fumbles", dataframe=annual_record, select_team=team)
            pst_sack_fumbles_lost = get_last_years_stat(statistic="sack_fumbles_lost", dataframe=annual_record,
                                                        select_team=team)
            pst_passing_air_yards = get_last_years_stat(statistic="passing_air_yards", dataframe=annual_record,
                                                        select_team=team)
            pst_passing_yards_after_catch = get_last_years_stat(statistic="passing_yards_after_catch",
                                                                dataframe=annual_record, select_team=team)
            pst_passing_first_downs = get_last_years_stat(statistic="passing_first_downs", dataframe=annual_record,
                                                          select_team=team)
            pst_passing_epa = get_last_years_stat(statistic="passing_epa", dataframe=annual_record, select_team=team)
            pst_passing_cpoe = get_last_years_stat(statistic="passing_cpoe", dataframe=annual_record, select_team=team)
            pst_passing_2pt_conversions = get_last_years_stat(statistic="passing_2pt_conversions",
                                                              dataframe=annual_record, select_team=team)
            pst_carries = get_last_years_stat(statistic="carries", dataframe=annual_record, select_team=team)
            pst_rushing_yards = get_last_years_stat(statistic="rushing_yards", dataframe=annual_record,
                                                    select_team=team)
            pst_rushing_tds = get_last_years_stat(statistic="rushing_tds", dataframe=annual_record, select_team=team)
            pst_rushing_fumbles = get_last_years_stat(statistic="rushing_fumbles", dataframe=annual_record,
                                                      select_team=team)
            pst_rushing_fumbles_lost = get_last_years_stat(statistic="rushing_fumbles_lost", dataframe=annual_record,
                                                           select_team=team)
            pst_rushing_first_downs = get_last_years_stat(statistic="rushing_first_downs", dataframe=annual_record,
                                                          select_team=team)
            pst_rushing_epa = get_last_years_stat(statistic="rushing_epa", dataframe=annual_record, select_team=team)
            pst_rushing_2pt_conversions = get_last_years_stat(statistic="rushing_2pt_conversions",
                                                              dataframe=annual_record, select_team=team)
            pst_receptions = get_last_years_stat(statistic="receptions", dataframe=annual_record, select_team=team)
            pst_targets = get_last_years_stat(statistic="targets", dataframe=annual_record, select_team=team)
            pst_receiving_yards = get_last_years_stat(statistic="receiving_yards", dataframe=annual_record,
                                                      select_team=team)
            pst_receiving_tds = get_last_years_stat(statistic="receiving_tds", dataframe=annual_record,
                                                    select_team=team)
            pst_receiving_fumbles = get_last_years_stat(statistic="receiving_fumbles", dataframe=annual_record,
                                                        select_team=team)
            pst_receiving_fumbles_lost = get_last_years_stat(statistic="receiving_fumbles_lost",
                                                             dataframe=annual_record, select_team=team)
            pst_receiving_air_yards = get_last_years_stat(statistic="receiving_air_yards", dataframe=annual_record,
                                                          select_team=team)
            pst_receiving_yards_after_catch = get_last_years_stat(statistic="receiving_yards_after_catch",
                                                                  dataframe=annual_record, select_team=team)
            pst_receiving_first_downs = get_last_years_stat(statistic="receiving_first_downs", dataframe=annual_record,
                                                            select_team=team)
            pst_receiving_epa = get_last_years_stat(statistic="receiving_epa", dataframe=annual_record,
                                                    select_team=team)
            pst_receiving_2pt_conversions = get_last_years_stat(statistic="receiving_2pt_conversions",
                                                                dataframe=annual_record, select_team=team)
            pst_special_teams_tds = get_last_years_stat(statistic="special_teams_tds", dataframe=annual_record,
                                                        select_team=team)
            pst_def_tackles_solo = get_last_years_stat(statistic="def_tackles_solo", dataframe=annual_record,
                                                       select_team=team)
            pst_def_tackles_with_assist = get_last_years_stat(statistic="def_tackles_with_assist",
                                                              dataframe=annual_record, select_team=team)
            pst_def_tackle_assists = get_last_years_stat(statistic="def_tackle_assists", dataframe=annual_record,
                                                         select_team=team)
            pst_def_tackles_for_loss = get_last_years_stat(statistic="def_tackles_for_loss", dataframe=annual_record,
                                                           select_team=team)
            pst_def_tackles_for_loss_yards = get_last_years_stat(statistic="def_tackles_for_loss_yards",
                                                                 dataframe=annual_record, select_team=team)
            pst_def_fumbles_forced = get_last_years_stat(statistic="def_fumbles_forced", dataframe=annual_record,
                                                         select_team=team)
            pst_def_sacks = get_last_years_stat(statistic="def_sacks", dataframe=annual_record, select_team=team)
            pst_def_sack_yards = get_last_years_stat(statistic="def_sack_yards", dataframe=annual_record,
                                                     select_team=team)
            pst_def_qb_hits = get_last_years_stat(statistic="def_qb_hits", dataframe=annual_record, select_team=team)
            pst_def_interceptions = get_last_years_stat(statistic="def_interceptions", dataframe=annual_record,
                                                        select_team=team)
            pst_def_interception_yards = get_last_years_stat(statistic="def_interception_yards",
                                                             dataframe=annual_record, select_team=team)
            pst_def_pass_defended = get_last_years_stat(statistic="def_pass_defended", dataframe=annual_record,
                                                        select_team=team)
            pst_def_tds = get_last_years_stat(statistic="def_tds", dataframe=annual_record, select_team=team)
            pst_def_fumbles = get_last_years_stat(statistic="def_fumbles", dataframe=annual_record, select_team=team)
            pst_def_safeties = get_last_years_stat(statistic="def_safeties", dataframe=annual_record, select_team=team)
            pst_misc_yards = get_last_years_stat(statistic="misc_yards", dataframe=annual_record, select_team=team)
            pst_fumble_recovery_own = get_last_years_stat(statistic="fumble_recovery_own", dataframe=annual_record,
                                                          select_team=team)
            pst_fumble_recovery_yards_own = get_last_years_stat(statistic="fumble_recovery_yards_own",
                                                                dataframe=annual_record, select_team=team)
            pst_fumble_recovery_opp = get_last_years_stat(statistic="fumble_recovery_opp", dataframe=annual_record,
                                                          select_team=team)
            pst_fumble_recovery_yards_opp = get_last_years_stat(statistic="fumble_recovery_yards_opp",
                                                                dataframe=annual_record, select_team=team)
            pst_fumble_recovery_tds = get_last_years_stat(statistic="fumble_recovery_tds", dataframe=annual_record,
                                                          select_team=team)
            pst_penalties = get_last_years_stat(statistic="penalties", dataframe=annual_record, select_team=team)
            pst_penalty_yards = get_last_years_stat(statistic="penalty_yards", dataframe=annual_record,
                                                    select_team=team)
            pst_timeouts = get_last_years_stat(statistic="timeouts", dataframe=annual_record, select_team=team)
            pst_punt_returns = get_last_years_stat(statistic="punt_returns", dataframe=annual_record, select_team=team)
            pst_punt_return_yards = get_last_years_stat(statistic="punt_return_yards", dataframe=annual_record,
                                                        select_team=team)
            pst_kickoff_returns = get_last_years_stat(statistic="kickoff_returns", dataframe=annual_record,
                                                      select_team=team)
            pst_kickoff_return_yards = get_last_years_stat(statistic="kickoff_return_yards", dataframe=annual_record,
                                                           select_team=team)
            pst_fg_made = get_last_years_stat(statistic="fg_made", dataframe=annual_record, select_team=team)
            pst_fg_att = get_last_years_stat(statistic="fg_att", dataframe=annual_record, select_team=team)
            pst_fg_missed = get_last_years_stat(statistic="fg_missed", dataframe=annual_record, select_team=team)
            pst_fg_blocked = get_last_years_stat(statistic="fg_blocked", dataframe=annual_record, select_team=team)
            pst_fg_long = get_last_years_stat(statistic="fg_long", dataframe=annual_record, select_team=team)
            pst_fg_pct = get_last_years_stat(statistic="fg_pct", dataframe=annual_record, select_team=team)
            pst_fg_made_0_19 = get_last_years_stat(statistic="fg_made_0_19", dataframe=annual_record, select_team=team)
            pst_fg_made_20_29 = get_last_years_stat(statistic="fg_made_20_29", dataframe=annual_record,
                                                    select_team=team)
            pst_fg_made_30_39 = get_last_years_stat(statistic="fg_made_30_39", dataframe=annual_record,
                                                    select_team=team)
            pst_fg_made_40_49 = get_last_years_stat(statistic="fg_made_40_49", dataframe=annual_record,
                                                    select_team=team)
            pst_fg_made_50_59 = get_last_years_stat(statistic="fg_made_50_59", dataframe=annual_record,
                                                    select_team=team)
            pst_fg_missed_0_19 = get_last_years_stat(statistic="fg_missed_0_19", dataframe=annual_record,
                                                     select_team=team)
            pst_fg_missed_20_29 = get_last_years_stat(statistic="fg_missed_20_29", dataframe=annual_record,
                                                      select_team=team)
            pst_fg_missed_30_39 = get_last_years_stat(statistic="fg_missed_30_39", dataframe=annual_record,
                                                      select_team=team)
            pst_fg_missed_40_49 = get_last_years_stat(statistic="fg_missed_40_49", dataframe=annual_record,
                                                      select_team=team)
            pst_fg_missed_50_59 = get_last_years_stat(statistic="fg_missed_50_59", dataframe=annual_record,
                                                      select_team=team)
            pst_fg_made_distance = get_last_years_stat(statistic="fg_made_distance", dataframe=annual_record,
                                                       select_team=team)
            pst_fg_missed_distance = get_last_years_stat(statistic="fg_missed_distance", dataframe=annual_record,
                                                         select_team=team)
            pst_fg_blocked_distance = get_last_years_stat(statistic="fg_blocked_distance", dataframe=annual_record,
                                                          select_team=team)
            pst_pat_made = get_last_years_stat(statistic="pat_made", dataframe=annual_record, select_team=team)
            pst_pat_att = get_last_years_stat(statistic="pat_att", dataframe=annual_record, select_team=team)
            pst_pat_missed = get_last_years_stat(statistic="pat_missed", dataframe=annual_record, select_team=team)
            pst_pat_blocked = get_last_years_stat(statistic="pat_blocked", dataframe=annual_record, select_team=team)
            pst_pat_pct = get_last_years_stat(statistic="pat_pct", dataframe=annual_record, select_team=team)
            pst_gwfg_made = get_last_years_stat(statistic="gwfg_made", dataframe=annual_record, select_team=team)
            pst_gwfg_att = get_last_years_stat(statistic="gwfg_att", dataframe=annual_record, select_team=team)
            training_data.loc[len(training_data)] = [
                week,
                team_name_to_num(team),
                team_name_to_num(opponent_team),
                avg_completions, avg_attempts, avg_passing_yards, avg_passing_tds, avg_passing_interceptions,
                avg_sacks_suffered, avg_sack_yards_lost, avg_sack_fumbles, avg_sack_fumbles_lost, avg_passing_air_yards,
                avg_passing_yards_after_catch, avg_passing_first_downs, avg_passing_epa, avg_passing_cpoe,
                avg_passing_2pt_conversions,
                avg_carries, avg_rushing_yards, avg_rushing_tds, avg_rushing_fumbles, avg_rushing_fumbles_lost,
                avg_rushing_first_downs, avg_rushing_epa, avg_rushing_2pt_conversions, avg_receptions, avg_targets,
                avg_receiving_yards, avg_receiving_tds, avg_receiving_fumbles, avg_receiving_fumbles_lost,
                avg_receiving_air_yards,
                avg_receiving_yards_after_catch, avg_receiving_first_downs, avg_receiving_epa,
                avg_receiving_2pt_conversions,
                avg_special_teams_tds, avg_def_tackles_solo, avg_def_tackles_with_assist, avg_def_tackle_assists,
                avg_def_tackles_for_loss, avg_def_tackles_for_loss_yards, avg_def_fumbles_forced, avg_def_sacks,
                avg_def_sack_yards, avg_def_qb_hits, avg_def_interceptions, avg_def_interception_yards,
                avg_def_pass_defended,
                avg_def_tds, avg_def_fumbles, avg_def_safeties, avg_misc_yards, avg_fumble_recovery_own,
                avg_fumble_recovery_yards_own, avg_fumble_recovery_opp, avg_fumble_recovery_yards_opp,
                avg_fumble_recovery_tds,
                avg_penalties, avg_penalty_yards, avg_timeouts, avg_punt_returns, avg_punt_return_yards,
                avg_kickoff_returns, avg_kickoff_return_yards, avg_fg_made, avg_fg_att, avg_fg_missed, avg_fg_blocked,
                avg_fg_long, avg_fg_pct, avg_fg_made_distance, avg_fg_missed_distance, avg_fg_blocked_distance,
                avg_pat_made, avg_pat_att, avg_pat_missed, avg_pat_blocked, avg_pat_pct,
                pst_completions, pst_attempts, pst_passing_yards, pst_passing_tds, pst_passing_interceptions,
                pst_sacks_suffered, pst_sack_yards_lost, pst_sack_fumbles, pst_sack_fumbles_lost, pst_passing_air_yards,
                pst_passing_yards_after_catch, pst_passing_first_downs, pst_passing_epa, pst_passing_cpoe,
                pst_passing_2pt_conversions, pst_carries, pst_rushing_yards, pst_rushing_tds,
                pst_rushing_fumbles, pst_rushing_fumbles_lost, pst_rushing_first_downs, pst_rushing_epa,
                pst_rushing_2pt_conversions, pst_receptions, pst_targets, pst_receiving_yards, pst_receiving_tds,
                pst_receiving_fumbles, pst_receiving_fumbles_lost, pst_receiving_air_yards,
                pst_receiving_yards_after_catch, pst_receiving_first_downs, pst_receiving_epa,
                pst_receiving_2pt_conversions, pst_special_teams_tds, pst_def_tackles_solo,
                pst_def_tackles_with_assist, pst_def_tackle_assists, pst_def_tackles_for_loss,
                pst_def_tackles_for_loss_yards, pst_def_fumbles_forced, pst_def_sacks, pst_def_sack_yards,
                pst_def_qb_hits, pst_def_interceptions, pst_def_interception_yards, pst_def_pass_defended,
                pst_def_tds, pst_def_fumbles, pst_def_safeties, pst_misc_yards, pst_fumble_recovery_own,
                pst_fumble_recovery_yards_own, pst_fumble_recovery_opp, pst_fumble_recovery_yards_opp,
                pst_fumble_recovery_tds, pst_penalties, pst_penalty_yards, pst_timeouts, pst_punt_returns,
                pst_punt_return_yards, pst_kickoff_returns, pst_kickoff_return_yards, pst_fg_made, pst_fg_att,
                pst_fg_missed, pst_fg_blocked, pst_fg_long, pst_fg_pct, pst_fg_made_0_19, pst_fg_made_20_29,
                pst_fg_made_30_39, pst_fg_made_40_49, pst_fg_made_50_59, pst_fg_missed_0_19, pst_fg_missed_20_29,
                pst_fg_missed_30_39, pst_fg_missed_40_49, pst_fg_missed_50_59,
                pst_fg_made_distance, pst_fg_missed_distance,
                pst_fg_blocked_distance,
                pst_pat_made, pst_pat_att, pst_pat_missed, pst_pat_blocked, pst_pat_pct, pst_gwfg_made, pst_gwfg_att
            ]
        training_data.to_csv(f"training_data_{year}.csv", index=False)


def get_rolling_avg(statistic: str, dataframe: DataFrame, end_week, select_team):
    begin_week = end_week - 3
    selected_games = dataframe.query("@begin_week <= week < @end_week and team == @select_team")
    summation = 0
    items = 0
    for index, row in selected_games.iterrows():
        summation += row[statistic]
        items += 1
    if items == 0:
        return 0
    return summation / items


def get_last_years_stat(statistic: str, dataframe: DataFrame, select_team):
    selected_stat_block = dataframe.query("team == @select_team")
    selected_stat_block = selected_stat_block.reset_index(drop=True)
    result = selected_stat_block.loc[0, statistic]
    return result


def team_name_to_num(team_name: str) -> int:
    """
    Returns the team name as an integer - used for specific features in the model
    :param team_name: The name of the team, as listed in team_acronyms
    :return: The index of the team name in the team_name list
    """
    return team_acronyms.index(team_name)


def num_to_team_name(team_name: int) -> str:
    return team_acronyms[team_name]


def add_dependent_variable():
    years = [2018, 2019]
    for year in years:
        training_data = pd.read_csv(f"training_data_{year}.csv")
        scores = pd.read_csv("nfl_scores.csv")
        training_data["score_diff"] = 0
        for index, row in training_data.iterrows():
            team = num_to_team_name(int(row["team"]))
            week = int(row["week"])
            query_results = scores.query("(season==@year) and (week_num==@week) and ((Home==@team) or (Away==@team))")
            query_results = query_results.reset_index(drop=True)
            if query_results.loc[0, "Home"] == team:
                training_data.loc[index, "score_diff"] = query_results.loc[0, "score_diff"]
            else:
                training_data.loc[index, "score_diff"] = query_results.loc[0, "score_diff"] * -1
        training_data.to_csv(f"training_data_{year}.csv", index=False)


def difference_records():
    years = [2018, 2019]
    for year in years:
        training_data = pd.read_csv(f"training_data_{year}.csv")
        for index, row in training_data.iterrows():
            team = row["team"]
            week = int(row["week"])
            exclude = ["team", "week", "opponent_team", "score_diff"]
            query_results = training_data.query("(opponent_team==@team) and (week==@week)").reset_index(drop=True)
            second_row: Series = query_results.iloc[0]
            for col in training_data.columns:
                if col not in exclude:
                    row[col] -= second_row[col]
            training_data.iloc[index] = row
        training_data.to_csv(f"training_data_{year}.csv",index=False)


if __name__ == "__main__":
    get_records()
    print("Created records")
    create_training_data()
    print("Made training data")
    add_dependent_variable()
    print("Added scores to new training data")
    difference_records()
    print("Subtracted records")
