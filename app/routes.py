# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Movie

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """Página inicial com formulário de cadastro de filme."""
    return render_template('index.html')

@main_bp.route('/add', methods=['POST'])
def add_movie():
    """Processa submissão do formulário e cria novo Movie."""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()

    if not title or not description:
        flash('Por favor, preencha Título e Descrição.', 'warning')
        return redirect(url_for('main.index'))

    Movie.create(title, description)
    flash(f'Filme "{title}" cadastrado com sucesso!', 'success')
    return redirect(url_for('main.list_movies'))

@main_bp.route('/movies', methods=['GET'])
def list_movies():
    """Lista todos os filmes cadastrados."""
    movies = Movie.get_all()
    return render_template('list_movies.html', movies=movies)
