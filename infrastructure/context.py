from flask_marshmallow import Marshmallow

from infrastructure import mappings
from infrastructure.repositories import planet_repository
from presentation import register_filters

class SQLContext(object):

    def __init__(self, app):
        from flask_sqlalchemy import SQLAlchemy
        from infrastructure.repositories import user_repository
        db = SQLAlchemy(app)
        mappings.init(db)
        self.db = db
        self.user_repository = user_repository.UserRepository(app, db)
        self.planet_repository = planet_repository.PlanetRepository(app, db)
        register_filters(app)

    def setup(self):
        self.db.create_all()

