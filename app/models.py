# app/models.py
from app import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    @classmethod
    def create(cls, title, description):
        movie = cls(title=title, description=description)
        db.session.add(movie)
        db.session.commit()
        return movie

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.id.desc()).all()
