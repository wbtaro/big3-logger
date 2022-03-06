import datetime

from app import db

class Genres(db.Model):
    id = db.Column(
        db.intger,
        primary_key=True
    )
    name = db.Column(db.String, nullabel=False)

class TrainingLogs(db.Model):
    id = db.Column(
        db.integer,
        primary_key=True
    )
    user = db.Column(db.String, nullable=False)
    training_date = db.Column(db.Datetime.date(), nullable=False)
    genre_id = db.Column(
        db.integer,
        db.ForeignKey('Genres.id'),
        nullable=False
    )
    weight = db.Column(db.Int, nullabler=False)
    reps = db.Column(db.Int, nullable=False)
    created_at = db.Column(
        db.Datetime,
        default=datetime.now(),
        nullable=False
        )
    updated_at = db.Column(
        db.Datetime,
        default=datetime.now(),
        nullable=False
        )
