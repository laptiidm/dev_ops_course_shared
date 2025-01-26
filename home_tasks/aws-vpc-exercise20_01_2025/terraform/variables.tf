variable "aws_region" {
  default = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID для створення EC2 інстансів"
  default     = "ami-043a5a82b6cf98947" # Замість цього вкажіть актуальний AMI ID для вашого регіону
}

variable "instance_type" {
  description = "Тип EC2 інстансів"
  default     = "t2.micro" # Ви можете змінити тип інстансу за потреби
}

variable "key_name" {
  description = "Ім'я ключової пари для доступу до інстансів"
  default     = "tempo-key" # Змініть на актуальне ім'я вашого ключа
}
