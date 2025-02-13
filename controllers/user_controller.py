from flask import redirect, url_for
from models.database import db
from models.user import User
from datetime import datetime

class UserController:
    @staticmethod
    def create_user(nombre, cedula, fecha_nacimiento, sexo):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()

        usuario_existente = User.query.filter_by(cedula=cedula).first()
        if usuario_existente:
            return "Error: La cédula ya está registrada"

        nuevo_usuario = User(nombre, cedula, fecha_nacimiento, sexo)
        db.session.add(nuevo_usuario)
        db.session.commit()

        # 🔄 Redirigir a la vista mala después de registrar
        return redirect(url_for('bad_bp.bad_form'))  # Redirige a la vista mala
