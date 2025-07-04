# This is a file for the Python scripts I used to parse and create my training data.
import pandas as pd

team_names = ["buffalo", "49er", "eagles", "vikings", "bears", "jets", "giants", "dolphins", "patriots", "steeler",
              "browns", "bengals", "colts", "titans", "chargers", "broncos", "raiders", "commanders", "cowboys",
              "lions", "packers", "buccaneers", "falcons", "panthers", "saints", "rams", "seahawks", "cardinals",
              "jaguars", "texans", "chiefs", "ravens"]

print(len(team_names))


def load_datasheet(year: int, team: str, are_games):
    str_year = str(year)
    if are_games:
        file_name = f"{team}_{str_year}_games.csv"
    else:
        file_name = f"{team}_{str_year}.csv"
    return pd.read_csv(file_name)


def create_records(team: str, year: int):
    games = load_datasheet(year, team, True)
    team_stats = load_datasheet(year, team, False)

    records = pd.DataFrame()

    for game in games.iterrows():
        #TODO
        print(game)
        final = pd.DataFrame()
        final.loc["Week"] = game[0]
    return records

def create_training_data():
    data = pd.DataFrame()

    for year in [2024]:
        for team in team_names:
            records = create_records(team, year)
            if data.empty:
                data = records
            else:
                pd.concat([data, records])
    # data.to_csv("final_data")
    print("Done")


create_training_data()

