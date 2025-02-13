from flask import Blueprint, render_template, request, redirect, url_for
from controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/register', methods=['POST'])
def register():
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    fecha_nacimiento = request.form['fecha_nacimiento']
    sexo = request.form['sexo']

    UserController.create_user(nombre, cedula, fecha_nacimiento, sexo)

    return redirect(url_for('user_bp.index'))
