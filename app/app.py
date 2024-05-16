"""app.py"""
from flask import Flask, render_template, url_for
# from flask_bootstrap import Bootstrap

# from routes.login import login_bp
# from routes.home import home_bp

app = Flask(__name__)
# bootstrap = Bootstrap(app)
# Registra el blueprint para las rutas de login
# app.register_blueprint(login_bp)
# app.register_blueprint(home_bp)


@app.route('/')
def index():
    """
        Pagina de inicio
    """
    return render_template('index.html')

@app.route('/login')
def login():
    """
    Página de listado de temas
    """
    return render_template('login.html')

@app.route('/main')
def main():
    """
    ------------------
    """
    return render_template('main.html')

@app.route('/chat')
def chat():
    """
    Página de listado de temas
    """
    return render_template('chat.html')


@app.route('/video')
def video():
    """
    Página de listado de temas
    """
    return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
