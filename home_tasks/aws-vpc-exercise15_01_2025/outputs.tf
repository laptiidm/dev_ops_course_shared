output "instance_ip" {
  description = "Public IP of the created EC2 instance"
  value       = module.ec2_nginx.instance_ip
}

