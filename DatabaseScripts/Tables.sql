CREATE DATABASE nfl_app;
USE nfl_app;

CREATE TYPE team_acr AS ENUM (
    "ARI", "ATL", "BLT", "BUF", "CAR", "CHI", "CIN", "CLV", "DAL",
    "DEN", "DET", "GB", "HST", "IND", "JAX", "KC", "LV", "LA", "LAC", "MIA",
    "MIN", "NE", "NO", "NYG", "NYJ", "PHI", "PIT", "SF", "SEA", "TB", 
    "TEN", "WAS"
)

CREATE TABLE IF NOT EXISTS gen_team (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    team_name VARCHAR(255),
    acr team_acr
);

CREATE TABLE IF NOT EXISTS team_stat_block (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    gen_id REFERENCES gen_team(id),
    stat_year YEAR,
    total_points INTEGER,
    total_yards INTEGER,
    num_of_off_plays INTEGER,
    yards_per_off_play DECIMAL,
    team_turnovers_lost INTEGER,
    fumbles_lost INTEGER,
    first_downs INTEGER,
    passes_completed INTEGER,
    passes_attempted INTEGER,
    total_yards_passed INTEGER,
    passing_touchdowns INTEGER,
    interceptions_thrown INTEGER,
    net_yards_gained_per_pass_attempt DECIMAL,
    first_downs_by_passing INTEGER,
    rushing_attempts INTEGER,
    rushing_yards INTEGER,
    rushing_touchdowns INTEGER,
    rushing_yards_per_attempt DECIMAL,
    first_downs_by_rushing INTEGER,
    penalties INTEGER,
    penalty_yards INTEGER,
    first_yards_by_penalty INTEGER,
    num_of_drives INTEGER,
    per_of_drives_with_score DECIMAL,
    turnover_percentage DECIMAL,
    avg_num_plays_per_drive DECIMAL,
    net_yards_per_drive DECIMAL,
    net_points_per_drive DECIMAL,
    opp_total_points INTEGER,
    opp_total_yards INTEGER,
    opp_num_of_off_plays INTEGER,
    opp_yards_per_off_play DECIMAL,
    opp_team_turnovers_lost INTEGER,
    opp_fumbles_lost INTEGER,
    opp_first_downs INTEGER,
    opp_passes_completed INTEGER,
    opp_passes_attempted INTEGER,
    opp_total_yards_passed INTEGER,
    opp_passing_touchdowns INTEGER,
    opp_interceptions_thrown INTEGER,
    opp_net_yards_gained_per_pass_attempt DECIMAL,
    opp_first_downs_by_passing INTEGER,
    opp_rushing_attempts INTEGER,
    opp_rushing_yards INTEGER,
    opp_rushing_touchdowns INTEGER,
    opp_rushing_yards_per_attempt DECIMAL,
    opp_first_downs_by_rushing INTEGER,
    opp_penalties INTEGER,
    opp_penalty_yards INTEGER,
    opp_first_yards_by_penalty INTEGER,
    opp_num_of_drives INTEGER,
    opp_per_of_drives_with_score DECIMAL,
    opp_turnover_percentage DECIMAL,
    opp_avg_num_plays_per_drive DECIMAL,
    opp_net_yards_per_drive DECIMAL,
    opp_net_points_per_drive DECIMAL
);

CREATE TABLE IF NOT EXISTS past_games (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    home_team REFERENCES gen_team(id)
    away_team REFERENCES gen_team(id)
    game_year YEAR,
    game_month MONTH,
    game_day DAY,
    winner REFERENCES gen_team(id),
    home_score INTEGER,
    away_score INTEGER,
    home_first_down INTEGER,
    home_total_yards INTEGER,
    home_pass_yards INTEGER,
    home_rush_yards INTEGER,
    home_turnovers INTEGER,
    away_first_down INTEGER,
    away_total_yards INTEGER,
    away_pass_yards INTEGER,
    away_rush_yards INTEGER,
    away_turnovers INTEGER
);

CREATE TABLE IF NOT EXISTS upcoming_games(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    home_team REFERENCES gen_team(id),
    away_team REFERENCES gen_team(id),
    game_year YEAR,
    game_month MONTH,
    game_day DAY
);