from datetime import datetime

from . import db

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(db.String, nullable=False)

class TrainingLog(db.Model):
    __tablename__ = 'training_logs'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user = db.Column(db.String, nullable=False)
    training_date = db.Column(db.DateTime, nullable=False)
    genre_id = db.Column(
        db.Integer,
        db.ForeignKey('genres.id'),
        nullable=False
    )
    weight = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.now(),
        nullable=False
        )
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(),
        nullable=False
        )
