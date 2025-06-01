## Infraestrutura Local (Terraform + Docker)

Este repositório utiliza Terraform para provisionar um container Docker que executa o app Flask localmente.

### Como usar:

1. Instalar e iniciar o **Docker Desktop** (verificar com `docker version`).
2. Verificar se o Terraform está instalado (rode `terraform version`).
3. No terminal, em `terraform/`:
   ```powershell
   terraform init
   terraform plan -out=tfplan
   terraform apply "tfplan"
