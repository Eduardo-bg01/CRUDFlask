from app.models import *
<<<<<<< HEAD
def create_db():
    db.drop_all()
    db.create_al()

def init_db():
    create_db()
    admin = Users(mail="Eduardo")
=======


def create_db():
    db.drop_all()
    db.create_all()


def init_db():
    create_db()
    admin = Users(
        name="Pedro"

    )
>>>>>>> af86ed3e86aa2656c59a8860b29965c80fc59832

    db.session.add(admin)
    db.session.commit()