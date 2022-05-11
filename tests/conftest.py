import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.cars import Car

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def six_cars(app):
    verstappen = Car(id=1, driver="Max Verstappen", team="Red Bull", mass_kg='711')
    ricciardo = Car(id=3, driver="Daniel Ricciardo", team="McLaren", mass_kg ='734')
    norris = Car(id=4, driver="Lando Norris", team="McLaren", mass_kg ='734')
    vettel = Car(id=5, driver="Sebastian Vettel", team="Aston Martin", mass_kg=700)
    latifi = Car(id=6, driver="Nicholas Latifi", team="Williams", mass_kg='762')
    leclerc = Car(id=16, driver="Sharles Leclerc", team="Ferrari", mass_kg='715')


    db.session.add(verstappen)
    db.session.add(ricciardo)
    db.session.add(norris)
    db.session.add(vettel)
    db.session.add(latifi)
    db.session.add(leclerc)
    db.session.commit()

# alfa_romeo1 = Car(id=24, driver="Zhou Guanyu", team="Alfa Romeo", mass_kg='727')
# alfa_romeo2 = Car(id=77, driver="Valtteri Bottas", team="Alfa Romeo", mass_kg='727')
# alphatauri1 = Car(id=10, driver="Pierre Gasly", team="AlphaTauri", mass_kg='712')
# alphatauri2 = Car(id=22, driver="Yuki Tsunoda", team="AlphaTauri", mass_kg='712')
# alpine1 = Car(id=14, driver="Fernando Alonso", team="Alpine", mass_kg='713')
# alpine2 = Car(id=31, driver="Esteban Ocon", team="Alpine", mass_kg='713')
# aston_martin1 = Car(id=5, driver="Sebastian Vettel", team="Aston Martin", mass_kg ='751')
# aston_martin2 = Car(id=18, driver="Lance Stroll", team="Aston Martin", mass_kg ='751')
# ferrari1 = Car(id=16, driver="Sharles Leclerc", team="Ferrari", mass_kg='715')
# ferrari2 = Car(id=55, driver="Carlos Sainz", team="Ferrari", mass_kg='715')
# haas1 = Car(id=20, driver="Kevin Magnussen", team="Haas", mass_kg='724')
# haas2 = Car(id=47, driver="Mick Schumacher", team="Haas", mass_kg='724')
# mclaren1 = Car(id=3, driver="Daniel Ricciardo", team="McLaren", mass_kg ='734')
# mclaren2 = Car(id=4, driver="Lando Norris", team="McLaren", mass_kg ='734')
# mercedes1 = Car(id=44, driver="Lewis Hamilton", team="Mercedes", mass_kg='746')
# mercedes2 = Car(id=63, driver="George Russell", team="Mercedes", mass_kg='746')
# redbull1 = Car(id=1, driver="Max Verstappen", team="Red Bull", mass_kg='711')
# redbull2 = Car(id=11, driver="Sergio Perez", team="Red Bull", mass_kg='711')
# williams1 = Car(id=23, driver="Alexander Albon", team="Williams", mass_kg='762')
# williams2 = Car(id=6, driver="Nicholas Latifi", team="Williams", mass_kg='762')
