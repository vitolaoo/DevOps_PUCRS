# tests/test_models.py
import pytest
from app import create_app, db
from app.models import Movie

@pytest.fixture
def app_context(tmp_path):
    # Configura um app de teste com um DB SQLite temporário
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{tmp_path}/test.db"
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app_context):
    return app_context.test_client()

def test_movie_model_create_and_query(app_context):
    # Cria um filme e verifica se ele aparece no banco
    m = Movie.create("Inception", "Excelente thriller psicológico.")
    assert isinstance(m.id, int)
    all_movies = Movie.get_all()
    assert len(all_movies) == 1
    assert all_movies[0].title == "Inception"
    assert "thriller psicológico" in all_movies[0].description
