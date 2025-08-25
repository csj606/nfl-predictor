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
      subnets = [  ]
      security_groups = [  ]
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
      subnets = [  ]
      security_groups = [  ]
      assign_public_ip = true
    }
}

resource "aws_ecs_task_definition" "web_server_definition" {
    family = "service"
    requires_compatibilities = [ "FARGATE" ]
    container_definitions = jsonencode({

    })
}

resource "aws_ecs_task_definition" "redis_definition" {
    family = "service"
    requires_compatibilities = ["FARGATE"]
    container_definitions = jsonencode({

    })
}