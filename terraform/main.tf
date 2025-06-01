################################################################################
# 1) Recurso para baixar (pull) a imagem Python do Docker Hub
################################################################################
resource "docker_image" "flask_image" {
  # Nome da imagem que o Terraform deve puxar
  name         = var.image         # normalmente "python:3.11-slim"
  keep_locally = false             # não manter cache após criação
}

################################################################################
# 2) Recurso para criar uma rede Docker isolada (opcional, mas recomendável)
################################################################################
resource "docker_network" "flask_network" {
  name = "devops_flask_network"
}

################################################################################
# 3) Recurso para criar e executar o container Flask
################################################################################
resource "docker_container" "flask_container" {
  name  = var.app_name
  image = docker_image.flask_image.name

  networks_advanced {
    name = docker_network.flask_network.name
  }

  ports {
    internal = var.app_port
    external = var.host_port
  }

  mounts {
    type   = "bind"
    source = abspath("${path.module}/../app")
    target = "/app"
  }

  env = [
    "FLASK_ENV=development",
    "FLASK_APP=/app/run.py"
  ]

  command = [
    "sh",
    "-c",
    "pip install --no-cache-dir -r /app/../requirements.txt && python /app/run.py"
  ]

  restart = "on-failure"
}
