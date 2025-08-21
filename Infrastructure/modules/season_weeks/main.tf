resource "aws_iam_policy" "schedule_write_policy" {
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["dynamodb:PutItem"]
                Effect = "Allow"
                Resource = var.season_weeks_arn
            }
        ]
    })
}

resource "aws_iam_role" "scheduler_role"{
    name = "scheduler_role"
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

resource "aws_iam_role_policy_attachment" "schedule_attach" {
    role = aws_iam_role.scheduler_role
    policy_arn = aws_iam_policy.schedule_write_policy.arn
}

resource "aws_lambda_function" "season_weeks"{
    function_name = "get_schedule"
    role = aws_iam_role.scheduler_role
    package_type = "Image"
    image_uri = ""

    image_config {
        command = ["python schedule.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}