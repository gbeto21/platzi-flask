from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video al productor.']

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
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : todos,
    }
    return render_template('hello.html', **context )
