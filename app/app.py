"""Archivo principal de ejecución"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
        Pagibna de inicio
    """
    data = {
        'titulo': 'Index',
        'bienvenida': '!Saludos, Cracks¡'
    }

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
