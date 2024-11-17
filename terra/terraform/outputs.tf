
output "redis_primary_instance_public_ip" {
  description = "redis primary public IP"
  value       = aws_instance.redis_primary.public_ip
}

output "redis_secondary_instance_public_ip" {
  description = "redis secondary public IP"
  value       = aws_instance.redis_secondary.public_ip
}


output "redis_primary_instance_private_ip" {
  description = "redis primary private IP"
  value       = aws_instance.redis_primary.private_ip
}

output "redis_secondary_instance_private_ip" {
  description = "redis secondary private IP"
  value       = aws_instance.redis_secondary.private_ip
}

