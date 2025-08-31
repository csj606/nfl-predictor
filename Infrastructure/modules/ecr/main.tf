resource "aws_ecr_repository" "web_server_repo"{
    name = "web_server_repo"
    image_tag_mutability = "IMMUTABLE"
    image_scanning_configuration {
      scan_on_push = true
    }
}

resource "aws_ecr_repository" "season_weeks_repo"{
    name = "season_weeks_repo"
    image_tag_mutability = "IMMUTABLE"
    image_scanning_configuration {
      scan_on_push = true
    }
}

resource "aws_ecr_repository" "predictor_repo"{
    name = "predictor_repo"
    image_tag_mutability = "IMMUTABLE"
    image_scanning_configuration {
      scan_on_push = true
    }
}

resource "aws_ecr_repository" "week_updates_repo"{
    name = "week_updates_repo"
    image_tag_mutability = "IMMUTABLE"
    image_scanning_configuration {
      scan_on_push = true
    }
}

resource "aws_ecr_repository" "annual_stats_repo"{
    name = "annual_stats_repo"
    image_tag_mutability = "IMMUTABLE"
    image_scanning_configuration {
      scan_on_push = true
    }
}