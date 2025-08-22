resource "aws_iam_role" "week_updator_role" {
  name = "week_updator_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid = "AssumeSchedulerRole"
        Principal = {
          Service = "lambdas.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "update_game_policy" {
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["dynamodb:PutItem"]
                Effect = "Allow"
                Resource = var.weekly_statistics_arn
            },
            {
              Action = ["dynamodb:PutItem"]
              Effect = "Allow"
              Resource = var.finished_games_arn
            },
            {
              Action = ["dynamodb:PutItem"]
              Effect = "Allow"
              Resource = var.upcoming_games_arn
            },
            {
              Action = ["dynamodb:GetItem"]
              Effect = "Allow"
              Resource = var.team_standings_arn
            },
            {
              Action = ["dynamodb:PutItem"]
              Effect = "Allow"
              Resource = var.team_standings_arn
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "predictor_attach" {
    role = aws_iam_role.week_updator_role
    policy_arn = aws_iam_policy.update_game_policy.arn
}

resource "aws_lambda_function" "weekly_update"{
    function_name = "weekly_update"
    role = aws_iam_role
    package_type = "Image"
    image_uri = ""

    image_config {
      command = ["python team_statistics.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}