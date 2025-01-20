variable "list_of_open_ports" {
  type        = list(number)
  description = "List of ports to open in the security group"
  default     = [80, 443]
}


