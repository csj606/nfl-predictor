USE nfl_app

INSERT INTO gen_team (team_name, acr) VALUES ("Cleveland Browns", "CLV");
INSERT INTO gen_team (team_name, acr) VALUES ("Philadephia Eagles", "PHI");
INSERT INTO gen_team (team_name, acr) VALUES ("Dallas Cowboys", "DAL");
INSERT INTO gen_team (team_name, acr) VALUES ("Washington Commanders", "WAS");
INSERT INTO gen_team (team_name, acr) VALUES ("Miami Dolphins", "MIA");
INSERT INTO gen_team (team_name, acr) VALUES ("Cincinnati Bengals", "CIN");
INSERT INTO gen_team (team_name, acr) VALUES ("New York Jets", "NYJ");
INSERT INTO gen_team (team_name, acr) VALUES ("New England Patriots", "NE");
INSERT INTO gen_team (team_name, acr) VALUES ("Baltimore Ravens", "BLT");
INSERT INTO gen_team (team_name, acr) VALUES ("Pittsburgh Steelers", "PIT");
INSERT INTO gen_team (team_name, acr) VALUES ("Houston Texans", "HST");
INSERT INTO gen_team (team_name, acr) VALUES ("Indianapolis Colts", "IND");
INSERT INTO gen_team (team_name, acr) VALUES ("Jacksonville Jaguars", "JAX");
INSERT INTO gen_team (team_name, acr) VALUES ("Tennessee Titans", "TEN");
INSERT INTO gen_team (team_name, acr) VALUES ("Buffalo Bills", "BUF");
INSERT INTO gen_team (team_name, acr) VALUES ("Denver Broncos", "DEN");
INSERT INTO gen_team (team_name, acr) VALUES ("Kansas City Chiefs", "KC");
INSERT INTO gen_team (team_name, acr) VALUES ("Las Vegas Raiders", "LV");
INSERT INTO gen_team (team_name, acr) VALUES ("Los Angeles Chargers", "LAC");
INSERT INTO gen_team (team_name, acr) VALUES ("New York Giants", "NYG");
INSERT INTO gen_team (team_name, acr) VALUES ("Chicago Bears", "CHI");
INSERT INTO gen_team (team_name, acr) VALUES ("Detroit Lions", "DET");
INSERT INTO gen_team (team_name, acr) VALUES ("Minnesota Vikings", "MIN");
INSERT INTO gen_team (team_name, acr) VALUES ("Green Bay Packers", "GB");
INSERT INTO gen_team (team_name, acr) VALUES ("Atlanta Falcons", "ATL");
INSERT INTO gen_team (team_name, acr) VALUES ("Carolina Panthers", "CAR");
INSERT INTO gen_team (team_name, acr) VALUES ("New Orleans Saints", "NO");
INSERT INTO gen_team (team_name, acr) VALUES ("Tampa Bay Buccanneers", "TB");
INSERT INTO gen_team (team_name, acr) VALUES ("Arizona Cardinals", "ARI");
INSERT INTO gen_team (team_name, acr) VALUES ("Los Angeles Rams", "LA");
INSERT INTO gen_team (team_name, acr) VALUES ("San Francisco 49ers", "SF");
INSERT INTO gen_team (team_name, acr) VALUES ("Seattle Seahawks", "SEA");

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 04;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "KC"), (SELECT id FROM gen_team WHERE acr = "LAC"), 2025, 09, 05;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;

INSERT INTO upcoming_games (home_team, away_team, game_year, game_month, game_day)
SELECT (SELECT id FROM gen_team WHERE acr = "PHI"), (SELECT id FROM gen_team WHERE acr = "DAL"), 2025, 09, 07;