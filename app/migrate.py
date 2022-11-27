from app.models import *
def create_db():
    db.drop_all()
    db.create_al()

def init_db():
    create_db()
    admin = Users(mail="Eduardo")

    db.session.add(admin)
    db.session.commit()