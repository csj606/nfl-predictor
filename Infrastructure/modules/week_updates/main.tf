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