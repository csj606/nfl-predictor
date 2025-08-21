resource "aws_iam_role" "ec2_role" {
    name = "cluster"
    assume_role_policy = jsonencode({
        Version = "2025-08-20"
        Effect = "Allow"
        Sid = ""
        Principal = {
            Service = "ecs-tasks.amazonaws.com"
        }
    })
}

resource "aws_ecs_cluster" "nfl_cluster"{
    name = "blue_red"
}