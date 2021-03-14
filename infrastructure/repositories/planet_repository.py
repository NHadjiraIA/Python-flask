import sys

from domain.entities.planet import Planet
from infrastructure.repositories import repository_base

class PlanetRepository(repository_base.RepositoryBase):
    def __init__(self, app, db):
        super(PlanetRepository, self).__init__(db)

    def get_all(self):
        try:
            return self.session().query(Planet).all()
        except:
            return None

    def get_by_id(self, id):
        try:
            return self.session().query(Planet).filter_by(planet_id=id).one()
        except:
            return None

    def get_by_name(self, name):
        try:
            return self.session().query(Planet).filter_by(planet_name=name).one()
        except:
            return None

    def Update(self, item):
        try:
            existing = self.session().query(Planet).filter_by(planet_id=item.planet_id).one()
            if existing:
                existing.planet_name = item.planet_name
                existing.planet_type = item.planet_type
                existing.home_star = item.home_star
                existing.mass = item.mass
                existing.radius = item.radius
                existing.distance = item.distance
                self.session().commit()
                return existing
            return None
        except:
            return None

    def delete(self, planet_id):
        try:
            existing = self.session().query(Planet).filter_by(planet_id=planet_id).one()
            print('this is the existing planet', existing)
            if existing:
                self.session().delete(existing)
                self.session().commit()
                return True
            return False
        except:
            return False


