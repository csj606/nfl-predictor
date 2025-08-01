# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd

team_names = ["buffalo", "49er", "eagles", "vikings", "bears", "jets", "giants", "dolphins", "patriots", "steeler",
              "browns", "bengals", "colts", "titans", "chargers", "broncos", "raiders", "commanders", "cowboys",
              "lions", "packers", "buccaneers", "falcons", "panthers", "saints", "rams", "seahawks", "cardinals",
              "jaguars", "texans", "chiefs", "ravens"]
logged_games = {}


def team_name_to_num(team_name: str) -> int:
    """
    Returns the team name as an integer - used for specific features in the model
    :param team_name: The name of the team, as listed in team_names
    :return: The index of the team name in the team_name list
    """
    return team_names.index(team_name)


def create_files():
    """
    Creates the CSV file stubs for the data we are cleaning
    :return: None
    """
    for team in team_names:
        for year in [2019, 2018, 2017]:
            with open(f"data/{team}_{year}_games.csv", 'w') as f:
                f.write("Stub")
        for year in [2018, 2017, 2016]:
            with open(f"data/{team}_{year}.csv", 'w') as f:
                f.write("Stub")


def convert_full_name_to_acronym(full_name: str):
    """
    Takes the team name as listed in the data and converts it to a name as listed in team_names
    :param full_name: Team name listed in the data as a string
    :return: The team name as listed in team_names returned as a string
    """
    if "Redskins" in full_name:
        return "commanders"
    check = full_name.lower()
    for name in team_names:
        if name in check:
            return name


def load_datasheet(year: int, team: str, are_games):
    """

    :param year: The year I want data from
    :param team: The team I want data about. Note - the team name must be contained within team_names list
    :param are_games: Boolean to indicate whether I want to retrieve game statistics or annual statistics
    :return: Formatted dataframe, either containing game statistics or annual statistics
    """
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
    """
    Provides a number corresponding to what week in the season it is
    :param game: A key-value list of values corresponding to a game record
    :return: The numeric representation of what week the season is in
    """
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


def log_game_record(opp: str, team: str, week_num: int, year: int):
    """
    Adds a key value pair to logged_games to keep track of what games we've seen
    :param opp: The name of the opponent
    :param team: The name of the team we are recording results of
    :param week_num: The week in the NFL season
    :param year: The year of the record
    :return: None
    """
    concat_str = opp + team + str(week_num) + str(year)
    logged_games[concat_str] = 1


def check_game_records(opp: str, team: str, week_num: int, year: int) -> bool:
    """
    Checks to see if we've recorded this game before
    :param year: The year of the record
    :param opp: The name of the opponenet
    :param team: The name of the team we are currently recording data for
    :param week_num: The current week in the season
    :return: Returns true if we've seen this game, false otherwise
    """
    concat_str = team + opp + str(week_num) + str(year)
    if logged_games.get(concat_str) is not None:
        return True
    else:
        return False


def clean_cell(stat:str, index, records) -> float:
    """
    Hands some data formatting issue - canceled weeks, missing values, etc. by returning 0. Otherwise returns the value
    :param stat: Statistic we are trying to retrieve
    :param index: The
    :param records:
    :return:
    """
    if pd.isna(records.at[index, stat]) or records.at[1, stat] == "Canceled":
        return 0
    else:
        return float(records.at[index, stat])


def get_rolling_five_week_avg(stat: str, index, records) -> float:
    """
    Calculates the five-week rolling average for a statistic from a specific week
    :param stat: The statistic we are calculating the rolling average for
    :param index: The week we are currently looking at
    :param records: The game statistics for a year
    :return: The average for that statistic as a float
    """
    a, b, c, d, e = 0, 0, 0, 0, 0  # These are the indexes of the records we are going to iterate through
    summation = 0

    if index < len(records):
        a, b, c, d, e = index - 1, index - 2, index - 3, index - 4, index - 5 # Index is a hashable, so this is the easiest way to do this, albeit difficult to understand
    else:
        a, b, c, d, e = index - 2, index - 3, index - 4, index - 5, index - 6

    if a > 0:
        summation += clean_cell(stat, a, records)
    if b > 0:
        summation += clean_cell(stat, b, records)
    if c > 0:
        summation += clean_cell(stat, c, records)
    if d > 0:
        summation += clean_cell(stat, d, records)
    if e > 0:
        summation += clean_cell(stat, e, records)
    return summation / 5


def get_rolling_three_week_avg(stat: str, index, records) -> float:
    """
    Calculates the three-week rolling average for a statistic from a specific week
    :param stat: The statistic we are calculating the rolling average for
    :param index: The week we are currently looking at
    :param records: The game statistics for a year
    :return: The average for that statistic as a float
    """
    if index == 1:
        return 0
    elif index == 2:
        return clean_cell(stat, index - 1, records)
    elif index == 3:
        first_result = clean_cell(stat, 1, records)
        second_result = clean_cell(stat, 2, records)
        summation = first_result + second_result
        return summation / 2
    else:
        if index < len(records):
            first_index, second_index, third_index = index - 1, index - 2, index - 3
        else:
            first_index, second_index, third_index = index - 2, index - 3, index - 4
        first_stat = clean_cell(stat, first_index, records)
        second_stat = clean_cell(stat, second_index, records)
        third_stat = clean_cell(stat, third_index, records)
        summation = first_stat + second_stat + third_stat
        return summation / 3


def create_records(team: str, year: int):
    """
    Creates training records for a specific team in a specific year
    :param team: The team we are creating records for
    :param year: The year we are creating records for
    :return: A dataframe containing the formatted training data
    """
    games = load_datasheet(year, team, True)
    team_stats = load_datasheet(year - 1, team, False)  # Want to load the last year for team stats

    records = pd.DataFrame()

    for index, game in games.iterrows():
        print(game)
        if game["week_num"] != "Week" and game['week_num'] is not None and game["opp_team"] != "Bye Week" and game["date_str"] != "Playoffs" and game["team_pt"] != "Canceled":
            opp_name = convert_full_name_to_acronym(game["opp_team"])
            week_num = get_week_num(game)
            # Check if game already recorded
            if not check_game_records(opp_name, team, week_num, year):
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

                # Create three week rolling average differences for teams
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

                # Create five week rolling average differences for teams
                final["MA5Off1stDDiff"] = [float(get_rolling_five_week_avg('num_fd', index, games)) - float(get_rolling_five_week_avg('num_fd', index, opp_games))]

                # Create "spread" for prediction
                final["score_diff"] = [int(game["team_pt"]) - int(game["opp_pt"])]

                # Log game to prevent duplicates
                log_game_record(opp_name, team, week_num, year)

                # Combine new record with records table
                records = pd.concat([records, final])
    return records


def create_training_data(year: int):
    """
    Creates a CSV containing training data for a specific year
    :param year: the year we are creating data for
    :return: None
    """
    data = pd.DataFrame()
    for team in team_names:
        records = create_records(team, year)
        data = pd.concat([data, records])
    file_name = f"formatted_data_{year}.csv"
    data.to_csv(file_name)
    print(f"Done - created records for {year}")


if __name__ == "__main__":
    create_training_data(2017)
    create_training_data(2018)
    create_training_data(2019)
