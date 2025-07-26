# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd

team_names = ["buffalo", "49er", "eagles", "vikings", "bears", "jets", "giants", "dolphins", "patriots", "steeler",
              "browns", "bengals", "colts", "titans", "chargers", "broncos", "raiders", "commanders", "cowboys",
              "lions", "packers", "buccaneers", "falcons", "panthers", "saints", "rams", "seahawks", "cardinals",
              "jaguars", "texans", "chiefs", "ravens"]
logged_games = {}


def team_name_to_num(team_name) -> int:
    return team_names.index(team_name)


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
        file_name = f"data/{team}_{year}.csv"
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
        if pd.isna(records.at[1, stat]) or records.at[1, stat] == "Canceled":
            return 0
        return records.at[1, stat]
    elif index == 3:
        if pd.isna(records.at[1, stat]) or records.at[1, stat] == "Canceled":
            a = 0
        else:
            a = float(records.at[1, stat])
        if pd.isna(records.at[2, stat]) or records.at[2, stat] == "Canceled":
            b = 0
        else:
            b = float(records.at[2, stat])
        summation = a + b
        return summation / 2
    else:
        if index < len(records):
            a, b, c = index - 1, index - 2, index - 3
        else:
            a, b, c = index - 2, index - 3, index - 4
        if pd.isna(records.at[a, stat]) or records.at[a, stat] == "Canceled":
            d = 0
        else:
            d = float(records.at[a, stat])
        if pd.isna(records.at[b, stat]) or records.at[b, stat] == "Canceled":
            e = 0
        else:
            e = float(records.at[b, stat])
        if pd.isna(records.at[c, stat]) or records.at[c, stat] == "Canceled":
            f = 0
        else:
            f = float(records.at[c, stat])
        summation = d + e + f
        return summation / 3


def create_records(team: str, year: int):
    games = load_datasheet(year, team, True)
    team_stats = load_datasheet(year - 1, team, False)  # Want to load the last year for team stats

    records = pd.DataFrame()

    for index, game in games.iterrows():
        if game["week_num"] != "Week" and game['week_num'] is not None and game["opp_team"] != "Bye Week" and game["date_str"] != "Playoffs" and game["team_pt"] != "Canceled":
            opp_name = convert_full_name_to_acronym(game["opp_team"])
            week_num = get_week_num(game)
            # Check if game already recorded
            if not check_game_records(opp_name, team, week_num):
                opp_stats = load_datasheet(year - 1, opp_name, False)
                opp_games = load_datasheet(year, opp_name, True)
                final = pd.DataFrame()
                final["Week"] = [week_num]

                # Encode who is the "team" and who is the "opponent"
                final["Team"] = [team_names.index(team)]
                final["Opponent"] = [team_names.index(opp_name)]

                # Get Differences for Last Year Cumulative Stats
                final["LastYrTotalYdsDif"] = [int([team_stats.at[2, "Yds"]][0]) - int([opp_stats.at[2, "Yds"]][0])]
                final["LastYrTotalPlaysDif"] = [int([team_stats.at[2, "ply"]][0]) - int([opp_stats.at[2, "ply"]][0])]
                final["LastYrY/PDif"] = [float([team_stats.at[2, "y/p"]][0]) - float([opp_stats.at[2, "y/p"]][0])]
                final["LastYrTODif"] = [int([team_stats.at[2, "to"]][0]) - int([opp_stats.at[2, "to"]][0])]
                final["LastYr1stDsDif"] = [int([team_stats.at[2, "fst_down"]][0]) - int([opp_stats.at[2, "fst_down"]][0])]
                final["LastYrPCmpDif"] = [int([team_stats.at[2, "pcmp"]][0]) - int([opp_stats.at[2, "pcmp"]][0])]
                final["LastYrPAttDif"] = [int([team_stats.at[2, "patt"]][0]) - int([opp_stats.at[2, "patt"]][0])]
                final["LastYrPYDsDif"] = [int([team_stats.at[2, "pyds"]][0]) - int([opp_stats.at[2, "pyds"]][0])]
                final["LastYrPTDDif"] = [int([team_stats.at[2, "ptd"]][0]) - int([opp_stats.at[2, "ptd"]][0])]
                final["LastYrPIntDif"] = [int([team_stats.at[2, "pint"]][0]) - int([opp_stats.at[2, "pint"]][0])]
                final["LastYrPNY/ADif"] = [float([team_stats.at[2, "pny/a"]][0]) - float([opp_stats.at[2, "pny/a"]][0])]
                final["LastYrPFDDif"] = [int([team_stats.at[2, "pfd"]][0]) - int([opp_stats.at[2, "pfd"]][0])]
                final["LastYrRAttDif"] = [int([team_stats.at[2, "ratt"]][0]) - int([opp_stats.at[2, "ratt"]][0])]
                final["LastYrRYDsDif"] = [int([team_stats.at[2, "ryds"]][0]) - int([opp_stats.at[2, "ryds"]][0])]
                final["LastYrRTDsDif"] = [int([team_stats.at[2, "rtd"]][0]) - int([opp_stats.at[2, "rtd"]][0])]
                final["LastYrRY/ADif"] = [float([team_stats.at[2, "ry/a"]][0]) - float([opp_stats.at[2, "ry/a"]][0])]
                final["LastYrR1stDDif"] = [int([team_stats.at[2, "rfstd"]][0]) - int([opp_stats.at[2, "rfstd"]][0])]
                final["LastYrPenDif"] = [int([team_stats.at[2, "pen"]][0]) - int([opp_stats.at[2, "pen"]][0])]
                final["LastYrSc%Dif"] = [float([team_stats.at[2, "sc%"]][0]) - float([opp_stats.at[2, "sc%"]][0])]
                final["LastYrTO%Dif"] = [float([team_stats.at[2, "TO%"]][0]) - float([opp_stats.at[2, "TO%"]][0])]
                final["LastYrAvgPlyDif"] = [float([team_stats.at[2, "avg_num_plys"]][0]) - float([opp_stats.at[2, "avg_num_plys"]][0])]
                final["LastYrAvgDrYdsDif"] = [float([team_stats.at[2, "avg_dr_yds"]][0]) - float([opp_stats.at[2, "avg_dr_yds"]][0])]
                final["LastYrAvgDrPtsDif"] = [float([team_stats.at[2, "avg_dr_pts"]][0])- float([opp_stats.at[2, "avg_dr_pts"]][0])]

                # Create averages differences for teams
                final["MA3Off1stDDif"] = [float(get_rolling_three_week_avg('num_fd', index, games)) - float(get_rolling_three_week_avg('num_fd', index, opp_games))]
                final["MA3OffTotYdsDif"] = [float(get_rolling_three_week_avg('total_yards', index, games)) - float(get_rolling_three_week_avg('total_yards', index, opp_games))]
                final["MA3OffPYDSDif"] = [float(get_rolling_three_week_avg('pass_yards', index, games)) - float(get_rolling_three_week_avg('pass_yards', index, opp_games))]
                final["MA3OffRYDSDif"] = [float(get_rolling_three_week_avg('rush_yards', index, games)) - float(get_rolling_three_week_avg('rush_yards', index, opp_games))]
                final["MA3OffTOsDif"] = [float(get_rolling_three_week_avg('turnovers', index, games)) - float(get_rolling_three_week_avg('turnovers', index, opp_games))]
                final["MA3Def1stDDif"] = [float(get_rolling_three_week_avg('def_fd', index, games)) - float(get_rolling_three_week_avg('def_fd', index, opp_games))]
                final["MA3DefTotYdsDif"] = [float(get_rolling_three_week_avg('def_tot_yds', index, games)) - float(get_rolling_three_week_avg('def_tot_yds', index, opp_games))]
                final["MA3DefPYDSDif"] = [float(get_rolling_three_week_avg('def_pass_yds', index, games)) - float(get_rolling_three_week_avg('def_pass_yds', index, opp_games))]
                final["MA3DefRYDSDif"] = [float(get_rolling_three_week_avg('def_rush_yds', index, games)) - float(get_rolling_three_week_avg('def_rush_yds', index, opp_games))]
                final["MA3DefTOsDif"] = [float(get_rolling_three_week_avg('def_to', index, games)) - float(get_rolling_three_week_avg('def_to', index, opp_games))]

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
    print(f"Done - created records for {year}")


if __name__ == "__main__":
    create_training_data(2022)
    create_training_data(2023)
    create_training_data(2024)
