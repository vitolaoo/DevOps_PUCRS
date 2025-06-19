# terraform/outputs.tf
# Expor a porta do host e o ID do container

output "host_port" {
  description = "Porta no host (Windows) vinculada ao container"
  value       = var.host_port
}

output "container_id" {
  description = "ID do container Docker criado"
  value       = docker_container.flask_container.id
}
