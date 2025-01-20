# Security Group для відкриття портів
resource "aws_security_group" "nginx_sg" {
  name        = "nginx-sg"
  description = "Allow specified ports"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  dynamic "ingress" {
    for_each = var.list_of_open_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Nginx-SG"
  }
}

resource "aws_instance" "nginx_instance" {
  ami           = "ami-034ca4376fad19554"  # Замініть на правильне ID AMI для Amazon Linux 2
  instance_type = "t2.micro"
  subnet_id     = var.subnet_id

  # Заміна groupName на vpc_security_group_ids
  vpc_security_group_ids = [aws_security_group.nginx_sg.id]

  tags = {
    Name = "nginx-instance"
  }

  # Скрипт user_data для встановлення та запуску nginx
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras enable nginx1
              yum install -y nginx
              systemctl start nginx
              systemctl enable nginx
              EOF
}
