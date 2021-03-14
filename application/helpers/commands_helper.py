from flask import Flask

from domain.entities.planet import Planet
from domain.entities.user import User

app = Flask(__name__)

class db_commands:
    def __init__(self, db):
        self.db = db

    @app.cli.command('db_create')
    def db_create(self):
        self.db.create_all()
        print('Database created !')


    @app.cli.command('db_drop')
    def db_drop(self):
        self.db.drop_all()
        print('Database dropped !')


    @app.cli.command('db_seed')
    def db_seed(self):
        mercury = Planet(planet_name='Mercury',
                         planet_type='Class D',
                         home_star='sol',
                         mass=3.258e23,
                         radius=1516,
                         distance=35.98e6)
        venus = Planet(planet_name='venus',
                       planet_type='Class K',
                       home_star='sol',
                       mass=34.867e24,
                       radius=3760,
                       distance=67.24e6)
        earth = Planet(planet_name='Earth',
                       planet_type='Class M',
                       home_star='sol',
                       mass=5.972e24,
                       radius=3959,
                       distance=92.96e6)
        self.db.session.add(mercury)
        self.db.session.add(venus)
        self.db.session.add(earth)

        test_user = User(first_name='William',
                         last_name='Herschel',
                         email='test@test.com',
                         password='P@ssw0rd')
        self.db.session.add(test_user)
        self.db.session.commit()
        print('Database seeded')