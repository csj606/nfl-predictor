resource "aws_s3_bucket" "frontend" {
    bucket = "frontend"
    tags = {
        name = "nfl"
    }
}