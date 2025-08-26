resource "aws_ecs_cluster" "nfl_cluster"{
    name = "blue_red"
}

resource "aws_ecs_cluster_capacity_providers" "nfl_cluster_providers" {
    cluster_name = aws_ecs_cluster.nfl_cluster.name
    capacity_providers = ["FARGATE"]

    default_capacity_provider_strategy {
      capacity_provider = "FARGATE"
      base = 1
      weight = 100
    }
}

resource "aws_ecs_service" "web_server"{
    name = "web_server"
    cluster = aws_ecs_cluster.nfl_cluster.id
    task_definition = aws_ecs_task_definition.web_server_definition.arn
    desired_count = 1
    
    launch_type = "FARGATE"
    network_configuration {
      subnets = [ var.ecs_subnet.id ]
      security_groups = [ var_web_server_security_group.id ]
      assign_public_ip = true
    }
}

resource "aws_ecs_service" "redis" {
    name = "redis"
    cluster = aws_ecs_cluster.nfl_cluster.id
    task_definition = aws_ecs_task_definition.redis_definition.arn
    desired_count = 1

    launch_type = "FARGATE"
    network_configuration {
      subnets = [ var.ecs_subnet.id ]
      security_groups = [ var.redis_security_group.id ]
      assign_public_ip = true
    }
}

resource "aws_ecs_task_definition" "web_server_definition" {
    family = "service"
    requires_compatibilities = [ "FARGATE" ]
    cpu = "256"
    memory = "512"
    execution_role_arn = aws_iam_role.ecs_execution_role.arn
    
    container_definitions = jsonencode([{
        name = "web-server"
        image = ""
        essential = true
        portMappings = [
            {
                containerPort = 443
                hostPort = 443
                protocol = "tcp"
            }
        ]
        logConfiguration = {
            logDriver = "awslogs"
            options = {
                awslogs-group = "/ecs/web_server"
                awslogs-region = "us-east-1"
                awslogs-stream-prefix = "ecs"
            }
        }
    }])
}

resource "aws_ecs_task_definition" "redis_definition" {
    family = "service"
    requires_compatibilities = ["FARGATE"]
    cpu = "256"
    memory = "512"
    execution_role_arn = aws_iam_role.ecs_execution_role.arn

    container_definitions = jsonencode({
        name = "redis"
        image = ""
        essential = true
        portMappings = [
            {
                containerPort = 6379
                hostPort = 6379
                protocol = "tcp"
            }
        ]
        logConfiguration = {
            logDriver = "awslogs"
            options = {
                awslogs-group = "/ecs/redis"
                awslogs-region = "us-east-1"
                awslogs-stream-prefix = "ecs"
            }
        }
    })
}

resource "aws_iam_role" "ecs_execution_role"{
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Effect = "Allow"
                Principal = {
                    Service = "ecs-tasks.amazonaws.com"
                }
                Action = "sts:AssumeRole"
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "ecs_execution_attach" {
    role = aws_iam_role.ecs_execution_role.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}