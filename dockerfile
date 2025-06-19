# Dockerfile

FROM python:3.11-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia os arquivos da aplicação para dentro do container
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expondo a porta usada pelo Flask
EXPOSE 5000

# Rodando o app (usando variável de ambiente padrão do Flask)
CMD ["python", "run.py"]
