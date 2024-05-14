from flask import Blueprint, render_template, redirect, url_for

# app = Flask(__name__)
# app.register_blueprint(login_bp, url_prefix='/auth')  # Prefijo para las rutas de autenticación
# Prefijo para las rutas de autenticación
login_bp = Blueprint('login', __name__)

# Ruta para la página principal


@login_bp.route('/')
def home():
    return render_template('home.html')

# Ruta para la página de registro


@login_bp.route('/registro')
def register():
    return render_template('register.html')

# Ruta para la página de registro exitoso


@login_bp.route('/registro_exitoso')
def registration_success():
    return render_template('registro_exitoso.html')
