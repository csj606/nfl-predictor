resource "aws_dynamodb_table" "annual_stats" {
    name = "annual_stats"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}

resource "aws_dynamodb_table" "ended_games" {
    name = "ended_games"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}

resource "aws_dynamodb_table" "upcoming_games"{
    name = "upcoming_games'"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}

resource "aws_dynamodb_table" "predictions"{
    name = "predictions"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}

resource "aws_dynamodb_table" "team_standings"{
    name = "standings"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}

resource "aws_dynamodb_table" "season_weeks"{
    name = "season_weeks"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}