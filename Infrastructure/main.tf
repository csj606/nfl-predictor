module "vpc" {
    source = "./modules/vpc"
}

module "annual_stat_caller" {
    source = "./modules/annual_stat_caller"
    annual_stats_arn = module.dynamodb.annual_stats_table_arn
}

module "ecs" {
    source = "./module/ecs"
}

module "season_weeks" {
    source = "./modules/season_weeks"
    season_weeks_arn = module.dynamodb.season_weeks_table_arn
}

module "week_updates" {
    source = "./modules/week_updates"
    weekly_statistics_arn = module.dynamodb.weekly_statistics_table_arn
    finished_games_arn = module.dynamodb.finished_games_table_arn
    upcoming_games_arn = module.dynamodb.upcoming_games_table_arn
    team_standings_arn = module.dynamodb.upcoming_games_table_arn
}

module "dynamodb" {
    source = "./modules/dynamodb"
}

module "predictor" {
    source = "./modules/predictor"
    weekly_statistics_arn = module.dynamodb.weekly_statistics_table_arn
    annual_stats_arn = module.dynamodb.annual_stats_table_arn
}

module "eventbridge"{
    source = "./modules/eventbridge"
}