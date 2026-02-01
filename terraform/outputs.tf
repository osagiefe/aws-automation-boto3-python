output "ec2_public_ip" {
  value = aws_instance.automation-server.public_ip
}
