module "vpc" {
    source = "./modules/vpc"
}

module "annual_stat_caller" {
    source = "./modules/annual_stat_caller"
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
}

module "dynamodb" {
    source = "./modules/dynamodb"
}

module "predictor" {
    source = "./modules/predictor"
}

module "eventbridge"{
    source = "./modules/eventbridge"
}