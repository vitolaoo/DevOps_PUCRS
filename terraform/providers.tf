# terrafrom/providers.tf
# Define que usaremos o provider Docker
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
  required_version = ">= 1.5.0"
}

provider "docker" {
  # O provider vai se conectar ao Docker Desktop local automaticamente
}
