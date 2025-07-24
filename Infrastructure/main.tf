provider "aws" {
    region = "us-east-1"
}

module "vpc" {
    source = "./vpc"
}

module "ec2" {
    source = "./ec2"
}

module "dynamodb" {
    source = "./dynamodb"
}

module "s3" {
    source = "./s3"
}