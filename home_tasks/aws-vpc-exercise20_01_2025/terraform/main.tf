provider "aws" {
  region = "us-east-1"
}

# створення VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "main-vpc"
  }
}

# створення Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main-igw"
  }
}

# таблиця маршрутів
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-route-table"
  }
}

resource "aws_route_table_association" "public_route_association" {
  subnet_id      = aws_subnet.subnet_a.id
  route_table_id = aws_route_table.public_route_table.id
}

# створення підмережі
resource "aws_subnet" "subnet_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "subnet-a"
  }
}

# генерація EC2 інстансів
resource "aws_instance" "ec2_instances" {
  count         = 2
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.subnet_a.id

  tags = {
    Name = "Ansible-EC2-${count.index + 1}"
  }
}

# генерація Ansible inventory через null_resource
resource "null_resource" "generate_inventory" {
  provisioner "local-exec" {
    command = <<EOT
      echo "[ec2_instances]" > ${path.module}/inventory.ini
      %{ for ip in aws_instance.ec2_instances[*].public_ip ~}
      echo "${ip} ansible_ssh_user=ubuntu ansible_ssh_private_key_file=/home/admindl/.ssh/tempo-key.pem" >> ${path.module}/inventory.ini
      %{ endfor ~}
    EOT
  }

  depends_on = [aws_instance.ec2_instances]
}

# вивід IP-адрес EC2-інстансів
output "ec2_ips" {
  value = aws_instance.ec2_instances[*].public_ip
}
