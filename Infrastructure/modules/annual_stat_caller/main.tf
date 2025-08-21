resource "aws_lambda_function" "annual_stats"{
    function_name = "annual_stats"
    role = aws_iam_role
    package_type = "Image"
    image_uri = ""

    image_config {
      command = ["python annual_statistics.py"]
    }

    memory_size = 512
    timeout = 30

    architectures = ["arm64"]
}