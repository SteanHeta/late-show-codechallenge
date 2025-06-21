from models import db
from app import create_app
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="Zach Galifianakis", occupation="Comedian")
    guest2 = Guest(name="Natalie Portman", occupation="Actress")

    ep1 = Episode(date="2023-10-01", number=1)
    ep2 = Episode(date="2023-10-02", number=2)

    app1 = Appearance(rating=4, guest=guest1, episode=ep1)
    app2 = Appearance(rating=5, guest=guest2, episode=ep2)

    db.session.add_all([guest1, guest2, ep1, ep2, app1, app2])
    db.session.commit()
    print("Database seeded successfully!")
