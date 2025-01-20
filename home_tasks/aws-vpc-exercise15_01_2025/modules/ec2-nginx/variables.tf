variable "vpc_id" {
  type        = string
  description = "The ID of the VPC"
}

variable "subnet_id" {
  type        = string
  description = "The ID of the Subnet"
}

variable "list_of_open_ports" {
  type        = list(number)
  description = "List of ports to open in the security group"
}
