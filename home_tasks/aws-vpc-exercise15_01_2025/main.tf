provider "aws" {
  region = "eu-central-1"
}

# Створення VPC
resource "aws_vpc" "main_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "My-VPC"
  }
}

# Створення публічної Subnet
resource "aws_subnet" "main_subnet" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "eu-central-1a"
  tags = {
    Name = "My-Public-Subnet"
  }
}

# Створення Internet Gateway
resource "aws_internet_gateway" "main_igw" {
  vpc_id = aws_vpc.main_vpc.id
  tags = {
    Name = "My-Internet-Gateway"
  }
}

# Маршрутна таблиця для публічного доступу
resource "aws_route_table" "main_route_table" {
  vpc_id = aws_vpc.main_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main_igw.id
  }

  tags = {
    Name = "My-Route-Table"
  }
}

# Прив'язка маршрутної таблиці до Subnet
resource "aws_route_table_association" "main_route_table_association" {
  subnet_id      = aws_subnet.main_subnet.id
  route_table_id = aws_route_table.main_route_table.id
}

# Виклик модуля для створення EC2 та Security Group
module "ec2_nginx" {
  source             = "./modules/ec2-nginx"
  vpc_id             = aws_vpc.main_vpc.id
  subnet_id          = aws_subnet.main_subnet.id
  list_of_open_ports = var.list_of_open_ports
}



