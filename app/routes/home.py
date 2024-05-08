"""home.py"""
from flask import Blueprint, render_template, redirect, url_for

home_bp = Blueprint('home', __name__)


@home_bp.route('/home', methods=['GET', 'POST'])
def home():
    # Lógica de autenticación y redirección si es exitoso
    return redirect(url_for('login.error_page'))


@home_bp.route('/error.html')
def error_page():
    return render_template('error.html')
