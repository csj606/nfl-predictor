resource "aws_dynamodb_table" "annual_stats" {
    name = "annual_stats"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
    hash_key = "team"

    attribute {
        name = "team"
        type = "S"
    }

    attribute {
        name = "stats"
        type = "S"
    }
}

resource "aws_dynamodb_table" "upcoming_games"{
    name = "upcoming_games'"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
    hash_key = "week_num"

    attribute {
        name = "week_num"
        type = "N"
    }

    attribute {
        name = "games"
        type = "S"
    }
}

resource "aws_dynamodb_table" "team_standings"{
    name = "standings"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
    hash_key = "team_name"

    attribute {
        name = "team_name"
        type = "S"
    }

    attribute {
        name = "wins"
        type = "N"
    }

    attribute {
        name = "defeats"
        type = "N"
    }
}

resource "aws_dynamodb_table" "season_weeks"{
    name = "season_weeks"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
    hash_key = "date_range"

    attribute {
        name = "date_range"
        type = "S"
    }

    attribute {
        name = "week_num"
        type = "N"
    }
}

resource "aws_dynamodb_table" "weekly_statistics"{
    name = "weekly_statistics"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
    hash_key = "team"

    attribute {
        name = "team"
        type = "S"
    }

    attribute {
        name = "stats"
        type = "S"
    }
}