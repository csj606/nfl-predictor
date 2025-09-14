resource "aws_iam_role" "games_role" {
  name = "games_role"
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

resource "aws_iam_policy" "games_query_policy" {
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["dynamodb:Query"]
                Effect = "Allow"
                Resource = var.games_table
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "games_attach" {
    role = aws_iam_role.games_role.name
    policy_arn = aws_iam_policy.games_query_policy.arn
}

resource "aws_lambda_function" "games" {
    function_name = "games"
    role = aws_iam_role.games_role
    package_type = "Image"
    image_uri = "" 

    image_config {
      command = ["python predict.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}