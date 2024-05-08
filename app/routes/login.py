"""login.py"""
from flask import Blueprint, render_template, redirect, url_for

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica de autenticación y redirección si es exitoso
    return redirect(url_for('login.error_page'))


@login_bp.route('/error.html')
def error_page():
    return render_template('login.html')
