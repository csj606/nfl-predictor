# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd

team_names = ["buffalo", "49er", "eagles", "vikings", "bears", "jets", "giants", "dolphins", "patriots", "steeler",
              "browns", "bengals", "colts", "titans", "chargers", "broncos", "raiders", "commanders", "cowboys",
              "lions", "packers", "buccaneers", "falcons", "panthers", "saints", "rams", "seahawks", "cardinals",
              "jaguars", "texans", "chiefs", "ravens"]
logged_games = {}


def create_files():
    for team in team_names:
        if team != "buffalo" and team != "dolphins" and team != "colts" and team != "jets" and team != "patriots" and team != "texans":
            for year in [2022, 2023, 2024]:
                with open(f"data/{team}_{year}_games.csv", 'w') as f:
                    f.write("Stub")
            for year in [2021, 2022, 2023]:
                with open(f"data/{team}_{year}.csv", 'w') as f:
                    f.write("Stub")


def convert_full_name_to_acronym(full_name: str):
    check = full_name.lower()
    for name in team_names:
        if name in check:
            return name


def load_datasheet(year: int, team: str, are_games):
    if are_games:
        file_name = f"data/{team}_{year}_games.csv"
        game_record = pd.read_csv(file_name)
        game_record.columns = ["week_num", 'day_of_week', 'date_str', 'time', 'missing_hyperlink', 'win/lose', 'went_ot', 'team_rec',
                               'away_stat', 'opp_team', 'team_pt', 'opp_pt', 'num_fd', 'total_yards', 'pass_yards',
                               'rush_yards', 'turnovers', 'def_fd', 'def_tot_yds', 'def_pass_yds', 'def_rush_yds',
                               'def_to', 'exp_points', 'def_exp_points', 'spec_exp_points']
        return game_record
    else:
        file_name = f"data/{team}_{year - 1}.csv"
        team_record = pd.read_csv(file_name)
        team_record.columns = ["row_names", "PF", "Yds", "ply", "y/p", "to", "fl", "fst_down", "pcmp", "patt", "pyds",
                               "ptd", "pint", 'pny/a', 'pfd', 'ratt', 'ryds', 'rtd', 'ry/a', 'rfstd', 'pen', 'penyds', 'pen_fst_down',
                               '#dr', 'sc%', 'TO%', 'avg_start_pos', 'avg_time_dr', 'avg_num_plys', 'avg_dr_yds',
                               'avg_dr_pts']
        return team_record


def get_week_num(game) -> int:
    if game["week_num"] == "Wild Card":
        return 19
    elif game["week_num"] == "Division":
        return 20
    elif game["week_num"] == "Conf. Champ.":
        return 21
    elif game["week_num"] == "SuperBowl":
        return 22
    else:
        return game["week_num"]


def log_game_record(opp: str, team: str, week_num: int):
    concat_str = opp + team + str(week_num)
    logged_games[concat_str] = 1


def check_game_records(opp: str, team: str, week_num: int) -> bool:
    concat_str = team + opp + str(week_num)
    if logged_games.get(concat_str) is not None:
        return True
    else:
        return False


def get_rolling_three_week_avg(stat: str, index, records) -> float:
    if index == 1:
        return 0
    elif index == 2:
        if pd.isna(records.at[1, stat]):
            return 0
        return records.at[1, stat]
    elif index == 3:
        a, b = float(records.at[1, stat]), float(records.at[2, stat])
        if pd.isna(records.at[1, stat]):
            a = 0
        if pd.isna(records.at[2, stat]):
            b = 0
        summation = a + b
        return summation / 2
    else:
        if index < len(records):
            a, b, c = index, index - 1, index - 2
        else:
            a, b, c = index - 1, index - 2, index - 3
        d, e, f = float(records.at[a, stat]), float(records.at[b, stat]), float(records.at[c, stat])
        if pd.isna(records.at[a, stat]):
            d = 0
        if pd.isna(records.at[b, stat]):
            e = 0
        if pd.isna(records.at[c, stat]):
            f = 0
        summation = d + e + f
        return summation / 3


def create_records(team: str, year: int):
    games = load_datasheet(year, team, True)
    team_stats = load_datasheet(year - 1, team, False)  # Want to load the last year for team stats

    records = pd.DataFrame()

    for index, game in games.iterrows():
        if game["week_num"] != "Week" and game['week_num'] is not None and game["opp_team"] != "Bye Week" and game["date_str"] != "Playoffs":
            opp_name = convert_full_name_to_acronym(game["opp_team"])
            week_num = get_week_num(game)
            # Check if game already recorded
            if not check_game_records(opp_name, team, week_num):
                opp_stats = load_datasheet(year, opp_name, False)
                opp_games = load_datasheet(year, opp_name, True)
                final = pd.DataFrame()
                final["Week"] = [week_num]

                # Get Last Year Stats for Team
                final["LastYrTotalYds"] = [team_stats.at[2, "Yds"]]
                final["LastYrTotalPlays"] = [team_stats.at[2, "ply"]]
                final["LastYrY/P"] = [team_stats.at[2, "y/p"]]
                final["LastYrTO"] = [team_stats.at[2, "to"]]
                final["LastYr1stDs"] = [team_stats.at[2, "fst_down"]]
                final["LastYrPCmp"] = [team_stats.at[2, "pcmp"]]
                final["LastYrPAtt"] = [team_stats.at[2, "patt"]]
                final["LastYrPYDs"] = [team_stats.at[2, "pyds"]]
                final["LastYrPTD"] = [team_stats.at[2, "ptd"]]
                final["LastYrPInt"] = [team_stats.at[2, "pint"]]
                final["LastYrPNY/A"] = [team_stats.at[2, "pny/a"]]
                final["LastYrPFD"] = [team_stats.at[2, "pfd"]]
                final["LastYrRAtt"] = [team_stats.at[2, "ratt"]]
                final["LastYrRYDs"] = [team_stats.at[2, "ryds"]]
                final["LastYrRTDs"] = [team_stats.at[2, "rtd"]]
                final["LastYrRY/A"] = [team_stats.at[2, "ry/a"]]
                final["LastYrR1stD"] = [team_stats.at[2, "rfstd"]]
                final["LastYrPen"] = [team_stats.at[2, "pen"]]
                final["LastYrSc%"] = [team_stats.at[2, "sc%"]]
                final["LastYrTO%"] = [team_stats.at[2, "TO%"]]
                final["LastYrAvgPly"] = [team_stats.at[2, "avg_num_plys"]]
                final["LastYrAvgDrYds"] = [team_stats.at[2, "avg_dr_yds"]]
                final["LastYrAvgDrPts"] = [team_stats.at[2, "avg_dr_pts"]]

                # Get Last Year Stats for Opponent
                final["LastYrOppTotalYds"] = [opp_stats.at[2, "Yds"]]
                final["LastYrOppTotalPlays"] = [opp_stats.at[2, "ply"]]
                final["LastYrOppY/P"] = [opp_stats.at[2, "y/p"]]
                final["LastYrOppTO"] = [opp_stats.at[2, "to"]]
                final["LastYrOpp1stDs"] = [opp_stats.at[2, "fst_down"]]
                final["LastYrOppPCmp"] = [opp_stats.at[2, "pcmp"]]
                final["LastYrOppPAtt"] = [opp_stats.at[2, "patt"]]
                final["LastYrOppPYDs"] = [opp_stats.at[2, "pyds"]]
                final["LastYrOppPTD"] = [opp_stats.at[2, "ptd"]]
                final["LastYrOppPInt"] = [opp_stats.at[2, "pint"]]
                final["LastYrOppPNY/A"] = [opp_stats.at[2, "pny/a"]]
                final["LastYrOppPFD"] = [opp_stats.at[2, "pfd"]]
                final["LastYrOppRAtt"] = [opp_stats.at[2, "ratt"]]
                final["LastYrOppRYDs"] = [opp_stats.at[2, "ryds"]]
                final["LastYrOppRTDs"] = [opp_stats.at[2, "rtd"]]
                final["LastYrOppRY/A"] = [opp_stats.at[2, "ry/a"]]
                final["LastYrOppR1stD"] = [opp_stats.at[2, "rfstd"]]
                final["LastYrOppPen"] = [opp_stats.at[2, "pen"]]
                final["LastYrOppSc%"] = [opp_stats.at[2, "sc%"]]
                final["LastYrOppTO%"] = [opp_stats.at[2, "TO%"]]
                final["LastYrOppAvgPly"] = [opp_stats.at[2, "avg_num_plys"]]
                final["LastYrOppAvgDrYds"] = [opp_stats.at[2, "avg_dr_yds"]]
                final["LastYrOppAvgDrPts"] = [opp_stats.at[2, "avg_dr_pts"]]

                # Create averages for team
                final["MA3Off1stD"] = [get_rolling_three_week_avg('num_fd', index, games)]
                final["MA3OffTotYds"] = [get_rolling_three_week_avg('total_yards', index, games)]
                final["MA3OffPYDS"] = [get_rolling_three_week_avg('pass_yards', index, games)]
                final["MA3OffRYDS"] = [get_rolling_three_week_avg('rush_yards', index, games)]
                final["MA3OffTOs"] = [get_rolling_three_week_avg('turnovers', index, games)]
                final["MA3Def1stD"] = [get_rolling_three_week_avg('def_fd', index, games)]
                final["MA3DefTotYds"] = [get_rolling_three_week_avg('def_tot_yds', index, games)]
                final["MA3DefPYDS"] = [get_rolling_three_week_avg('def_pass_yds', index, games)]
                final["MA3DefRYDS"] = [get_rolling_three_week_avg('def_rush_yds', index, games)]
                final["MA3DefTOs"] = [get_rolling_three_week_avg('def_to', index, games)]

                # Create averages for opponent
                final["OppMA3Off1stD"] = [get_rolling_three_week_avg('num_fd', index, opp_games)]
                final["OppMA3OffTotYds"] = [get_rolling_three_week_avg('total_yards', index, opp_games)]
                final["OppMA3OffPYDS"] = [get_rolling_three_week_avg('pass_yards', index, opp_games)]
                final["OppMA3OffRYDS"] = [get_rolling_three_week_avg('rush_yards', index, opp_games)]
                final["OppMA3OffTOs"] = [get_rolling_three_week_avg('turnovers', index, opp_games)]
                final["OppMA3Def1stD"] = [get_rolling_three_week_avg('def_fd', index, opp_games)]
                final["OppMA3DefTotYds"] = [get_rolling_three_week_avg('def_tot_yds', index, opp_games)]
                final["OppMA3DefPYDS"] = [get_rolling_three_week_avg('def_pass_yds', index, opp_games)]
                final["OppMA3DefRYDS"] = [get_rolling_three_week_avg('def_rush_yds', index, opp_games)]
                final["OppMA3DefTOs"] = [get_rolling_three_week_avg('def_to', index, opp_games)]

                # Create "spread" for prediction
                final["score_diff"] = [int(game["team_pt"]) - int(game["opp_pt"])]

                # Log game to prevent duplicates
                log_game_record(opp_name, team, week_num)

                # Combine new record with records table
                records = pd.concat([records, final])
    return records


def create_training_data(year: int):
    data = pd.DataFrame()
    for team in team_names:
        records = create_records(team, year)
        data = pd.concat([data, records])
    file_name = f"formatted_data_{year}.csv"
    data.to_csv(file_name)
    print("Done")


if __name__ == "__main__":
    create_training_data(2024)