[ec2_instances]
%{ for ip in ips ~}
${ip} ansible_ssh_user=ubuntu ansible_ssh_private_key_file=/mnt/c/Users/lapti/.ssh/tempo-key.pem
%{ endfor ~}
