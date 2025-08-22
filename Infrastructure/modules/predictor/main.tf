resource "aws_iam_role" "predictor_role" {
  name = "predictor_role"
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

resource "aws_iam_policy" "predictor_query_policy" {
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["dynamodb:Query"]
                Effect = "Allow"
                Resource = var.weekly_statistics_arn
            },
            {
              Action = ["dynamodb:Query"]
              Effect = "Allow"
              Resource = var.annual_stats_arn
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "predictor_attach" {
    role = aws_iam_role.predictor_role
    policy_arn = aws_iam_policy.predictor_query_policy.arn
}

resource "aws_lambda_function" "predictor" {
    function_name = "predictor"
    role = aws_iam_role.predictor_role
    package_type = "Image"
    image_uri = "" #TODO - Define URL

    image_config {
      command = ["python predict.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}