# app/run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Rodar em debug=True para atualizar automaticamente ao salvar arquivos locais
    app.run(host='0.0.0.0', port=5000, debug=True)
