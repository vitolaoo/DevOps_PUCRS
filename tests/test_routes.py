# tests/test_routes.py
import pytest
from app import create_app, db
from app.models import Movie

@pytest.fixture
def client(tmp_path):
    # Cria app de teste com DB em arquivo temporário
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{tmp_path}/test_routes.db"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_index_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Cadastrar Filme" in response.data

def test_add_movie_and_list(client):
    # Cadastrar um filme via POST
    response = client.post('/add', data={
        'title': 'Matrix',
        'description': 'Ótimo filme sci-fi'
    }, follow_redirects=True)
    assert response.status_code == 200
    # Deve ter redirecionado para /movies, então verifica se "Matrix" aparece
    assert b"Matrix" in response.data
    assert b"Otimo filme sci-fi" in response.data
