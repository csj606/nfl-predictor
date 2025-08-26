resource "aws_iam_role" "annual_stat_caller" {
  name = "annual_stat_caller"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid = "AssumeAnnualStatCallerRole"
        Principal = {
          Service = "lambdas.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "annual_stat_write_policy" {
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["dynamodb:PutItem"]
                Effect = "Allow"
                Resource = var.annual_stats_arn
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "annual_stat_attach"{
  policy_arn = aws_iam_policy.annual_stat_write_policy.arn
  role = aws_iam_role.annual_stat_caller.name
}

resource "aws_lambda_function" "annual_stats"{
    function_name = "annual_stats"
    role = aws_iam_role.annual_stat_caller.name
    package_type = "Image"
    image_uri = ""

    image_config {
      command = ["python annual_statistics.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}