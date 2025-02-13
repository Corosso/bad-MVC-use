from models.database import db

class UserBad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    universidad = db.Column(db.String(100), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    facultad = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(20), nullable=False)

    def __init__(self, universidad, carrera, facultad, celular):
        self.universidad = universidad
        self.carrera = carrera
        self.facultad = facultad
        self.celular = celular
