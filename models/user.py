# Modelo de usuario
from models.database import db
#Clase usuario con nuevos campos, pero usando mal el principio
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    
    def __init__(self, nombre, cedula, fecha_nacimiento, sexo):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo

