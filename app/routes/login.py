from flask import Flask, render_template
from login import login_bp

app = Flask(__name__)
# app.register_blueprint(login_bp, url_prefix='/auth')  # Prefijo para las rutas de autenticación
# Prefijo para las rutas de autenticación
app.register_blueprint(login_bp, url_prefix='/auth')

# Ruta para la página principal


@app.route('/')
def home():
    return render_template('home.html')

# Ruta para la página de registro


@app.route('/registro')
def register():
    return render_template('register.html')

# Ruta para la página de registro exitoso


@app.route('/registro_exitoso')
def registration_success():
    return render_template('registro_exitoso.html')


if __name__ == '__main__':
    app.run(debug=True)
