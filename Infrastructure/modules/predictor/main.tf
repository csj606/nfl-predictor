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