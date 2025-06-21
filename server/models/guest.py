from sqlalchemy_serializer import SerializerMixin
from . import db

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")

