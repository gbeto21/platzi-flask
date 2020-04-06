from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired 
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video al productor.']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(err):
    return render_template('404.html', error = err)

@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html', error = err)

@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip' : user_ip, 
        'todos' : todos,
        'username': username
    }
 
    return render_template('hello.html', **context )
