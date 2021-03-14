from sqlalchemy import String

from domain.entities.planet import Planet
from domain.entities.user import User


def init(db):
    user_mapping = db.Table('users',
                            db.Column('id', db.Integer, primary_key=True),
                            db.Column('first_name', db.String(50)),
                            db.Column('last_name', db.String(50)),
                            db.Column('email', db.String(100)),
                            db.Column('password', db.String(100))
                            )
    planet_mapping = db.Table('planets',
                              db.Column('planet_id', db.Integer, primary_key=True),
                              db.Column('planet_name', db.String(50)),
                              db.Column('planet_type', db.String(50)),
                              db.Column('home_star', db.String(50)),
                              db.Column('mass', db.Float),
                              db.Column('radius', db.Float),
                              db.Column('distance', db.Float)
                              )
    db.mapper(User, user_mapping)
    db.mapper(Planet, planet_mapping)
