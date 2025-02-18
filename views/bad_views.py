from flask import Blueprint, render_template, request, redirect
from models.database import db
from models.user_bad import UserBad  # Ahora usamos UserBad

bad_bp = Blueprint('bad_bp', __name__)

@bad_bp.route('/bad_form')
def bad_form():
    return render_template('bad_form.html')

@bad_bp.route('/bad_register', methods=['POST'])
def bad_register():
    universidad = request.form['universidad']
    carrera = request.form['carrera']
    facultad = request.form['facultad']
    celular = request.form['celular']

    # ❌ Mal diseño: Lógica de base de datos en la vista
    nuevo_usuario = UserBad(universidad, carrera, facultad, celular)
    db.session.add(nuevo_usuario)
    db.session.commit()