provider "aws" {
  region = "us-east-1"
}

# VPC
resource "aws_vpc" "my_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "my-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "my-internet-gateway"
  }
}

# Subnets
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
  tags = {
    Name = "public-subnet"
  }
}

resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "private-subnet"
  }
}

# Public Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "public-route-table"
  }
}

resource "aws_route" "public_route" {
  route_table_id         = aws_route_table.public_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.my_igw.id
}

resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# Security Groups
resource "aws_security_group" "public_sg" {
  name        = "public-sg"
  vpc_id      = aws_vpc.my_vpc.id
  description = "Allow public access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "private_sg" {
  name        = "private-sg"
  vpc_id      = aws_vpc.my_vpc.id
  description = "Allow SSH from public instance"

  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.public_sg.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# SSH Key Pair
resource "tls_private_key" "private_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "aws_key_pair" "my_key" {
  key_name   = "my-key-name"
  public_key = tls_private_key.private_key.public_key_openssh
}

# Public Instance
resource "aws_instance" "public_instance" {
  ami                         = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public_subnet.id
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.public_sg.id]
  key_name                    = aws_key_pair.my_key.key_name

  user_data = <<-EOF
              #!/bin/bash
              mkdir -p /home/ec2-user/.ssh
              echo '${tls_private_key.private_key.private_key_pem}' > /home/ec2-user/.ssh/id_rsa
              chmod 600 /home/ec2-user/.ssh/id_rsa
              chown ec2-user:ec2-user /home/ec2-user/.ssh/id_rsa
              EOF

  tags = {
    Name = "public-instance"
  }
}

# Private Instance
resource "aws_instance" "private_instance" {
  ami                    = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private_subnet.id
  vpc_security_group_ids = [aws_security_group.private_sg.id]
  key_name               = aws_key_pair.my_key.key_name

  user_data = <<-EOF
              #!/bin/bash
              mkdir -p /home/ec2-user/.ssh
              echo '${tls_private_key.private_key.public_key_openssh}' > /home/ec2-user/.ssh/authorized_keys
              chmod 600 /home/ec2-user/.ssh/authorized_keys
              chown ec2-user:ec2-user /home/ec2-user/.ssh/authorized_keys
              EOF

  tags = {
    Name = "private-instance"
  }
}



output "private_instance_ip" {
  value = aws_instance.private_instance.private_ip
}
