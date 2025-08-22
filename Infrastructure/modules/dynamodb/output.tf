output "season_weeks_table_arn" {
    value = aws_dynamodb_table.season_weeks.arn
}

output "annual_stats_table_arn" {
    value = aws_dynamodb_table.annual_stats.arn
}

output "finished_games_table_arn" {
    value = aws_dynamodb_table.finished_games.arn
}

output "upcoming_games_table_arn" {
    value = aws_dynamodb_table.upcoming_games.arn
}

output "team_standings_table_arn" {
    value = aws_dynamodb_table.team_standings.arn
}

output "weekly_statistics_table_arn" {
    value = aws_dynamodb_table.weekly_statistics
}