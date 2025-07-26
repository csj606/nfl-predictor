resource "aws_vpc" "main" {
    cidr_block = "172.16.0.0/12"
    tags = {
        Name = "nfl"
    }
}

resource "aws_network_acl" "public"{
    vpc_id = aws_vpc.main.id
    tags = {
        Name = "nfl"
    }

    ingress = {
        from_port = 443
        to_port = 443
        rule_no = 1
        action = "allow"
    }

    subnet_ids = [aws_subnet.public_sub]
}

resource "aws_network_acl" "private"{
    vpc_id = aws_vpc.main.id
    tags = {
        Name = "nfl"
    }
    subnet_ids = [aws_subnet.private_sub]
}

resource "aws_subnet" "public_sub" {
    vpc_id = aws_vpc.main.id
    tags = {
        Name = "nfl"
    }
    cidr_block = "172.16.2.0/24"
}

resource "aws_subnet" "private_sub"{
    vpc_id = aws_vpc.main.id
    tags = {
        Name = "nfl"
    }
    cidr_block = "172.16.1.0/24"
}

resource "aws_internet_gateway" "gate"{
    vpc_id = aws_vpc.main.id
}