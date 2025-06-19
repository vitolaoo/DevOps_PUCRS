# terraform/variables.tf
# Variáveis configuráveis para a montagem do container Docker

variable "app_name" {
  description = "Nome do container Docker"
  type        = string
  default     = "devops_flask_app"
}

variable "app_port" {
  description = "Porta interna onde o Flask roda (dentro do container)"
  type        = number
  default     = 5000
}

variable "host_port" {
  description = "Porta exposta no host (Windows) para acessar a aplicação"
  type        = number
  default     = 5000
}

variable "image" {
  description = "Imagem base de Python (para Flask)"
  type        = string
  default     = "python:3.11-slim"
}
