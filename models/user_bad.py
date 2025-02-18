#Modelo del usuario
from models.database import db
#Clase usuario con nuevos campos, pero usando mal el principio
class UserBad(db.Model):
    #Se crean los campos de la tabla de la BD
    id = db.Column(db.Integer, primary_key=True)
    universidad = db.Column(db.String(100), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    facultad = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    #Se inicializan los campos
    def __init__(self, universidad, carrera, facultad, celular):
        self.universidad = universidad
        self.carrera = carrera
        self.facultad = facultad
        self.celular = celular