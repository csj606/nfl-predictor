# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd

team_names = ["buffalo", "49er", "eagles", "vikings", "bears", "jets", "giants", "dolphins", "patriots", "steeler",
              "browns", "bengals", "colts", "titans", "chargers", "broncos", "raiders", "commanders", "cowboys",
              "lions", "packers", "buccaneers", "falcons", "panthers", "saints", "rams", "seahawks", "cardinals",
              "jaguars", "texans", "chiefs", "ravens"]


def create_files():
    for team in team_names:
        if team != "buffalo" and team != "dolphins" and team != "colts" and team != "jets" and team != "patriots" and team != "texans":
            for year in [2022, 2023, 2024]:
                with open(f"data/{team}_{year}_games.csv", 'w') as f:
                    f.write("Stub")
            for year in [2021, 2022, 2023]:
                with open(f"data/{team}_{year}.csv", 'w') as f:
                    f.write("Stub")

logged_games = {}

def convert_full_name_to_acronym(full_name: str):
    check = full_name.lower()
    for name in team_names:
        if name in check:
            return name


def load_datasheet(year: int, team: str, are_games):
    str_year = str(year)
    if are_games:
        file_name = f"/data/{team}_{str_year}_games.csv"
        game_record = pd.read_csv(file_name)
        game_record.columns = ["week_num", 'day_of_week', 'date_str', 'time', 'missing_hyperlink', 'win/lose', 'went_ot', 'team_rec',
                               'away_stat', 'opp_team', 'team_pt', 'opp_pt', 'num_fd', 'total_yards', 'pass_yards',
                               'rush_yards', 'turnovers', 'def_fd', 'def_tot_yds', 'def_pass_yds', 'def_rush_yds',
                               'def_to', 'exp_points', 'def_exp_points', 'spec_exp_points']
        return game_record
    else:
        file_name = f"/data/{team}_{str_year}.csv"
        team_record = pd.read_csv(file_name)
        team_record.columns = ["row_names", "PF", "Yds", "ply", "y/p", "to", "fl", "fst_down", "pcmp", "patt", "pyds",
                               "ptd", "pint", 'pny/a', 'pfd', 'ratt', 'ryds', 'rtd', 'ry/a', 'rfstd', 'pen', 'penyds', 'pen_fst_down',
                               '#dr', 'sc%', 'TO%', 'avg_start_pos', 'avg_time_dr', 'avg_num_plys', 'avg_dr_yds',
                               'avg_dr_pts']
        return team_record


def get_week_num(game) -> int:

    return 0


def create_records(team: str, year: int):
    games = load_datasheet(year, team, True)
    team_stats = load_datasheet(year - 1, team, False)  # Want to load the last year for team stats

    records = pd.DataFrame()

    for index, game in games.iterrows():
        if game["week_num"] != "Week" or game['week_num'] is not None:
            #TODO
            opp_name = convert_full_name_to_acronym(game["opp_team"])
            opp_stats = load_datasheet(year, opp_name, False)
            opp_games = load_datasheet(year, opp_name, True)
            final = pd.DataFrame()
            final["Week"] = game["week_num"]

    return records


def create_training_data(year: int):
    data = pd.DataFrame()
    for team in team_names:
        records = create_records(team, year)
        if data.empty:
            data = records
        else:
            pd.concat([data, records])
    file_name = f"formatted_data_{year}"
    #data.to_csv(file_name)
    print("Done")


if __name__ == "__main__":
    create_files()