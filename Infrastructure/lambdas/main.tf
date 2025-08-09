resource "aws_lambda_function" "prediction" {
    function_name = "prediction"
    role = aws_iam_role # TODO - Define IAM roles
    package_type = "Image"
    image_uri = "" #TODO - Define URL

    image_config {
      command = ["python predict.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}

resource "aws_lambda_function" "annual_stats"{
    function_name = "annual_stats"
    role = aws_iam_role # TODO, see above
    package_type = "Image"
    image_uri = "" # TODO, see above

    image_config {
      command = ["python annual_statistics.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}

resource "aws_lambda_function" "schedule"{
    function_name = "get_schedule"
    role = aws_iam_role
    package_type = "Image"
    image_uri = ""

    image_config {
        command = ["python schedule.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
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