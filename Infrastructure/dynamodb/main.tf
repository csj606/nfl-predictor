resource "aws_dynamodb_table" "prev-year-stats" {
    name = "PrevYearStats"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
    hash_key = "ID"

    attribute {
        name = "ID"
        type = "S"
    }

    attribute {
        name = "WeekNum"
        type = "N"
    }

    attribute {
        name = "DayOfWeek"
        type = "S"
    }
}

resource "aws_dynamodb_table" "cur_year_ended_games" {
    name = "CurYearEndedGames"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}

resource "aws_dynamodb_table" "cur_year_upcoming_games"{
    name = "CurYearUpcomingGames"
    read_capacity = 5
    write_capacity = 5
    tags = {
        name = "nfl"
    }
}