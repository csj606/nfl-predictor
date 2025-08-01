data "aws_ami" "ubuntu" {
    most_recent = true
    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"]
}

resource "aws_instance" "cluster" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t4g.large"
    tags = {
        Name = "nfl"
    }
}