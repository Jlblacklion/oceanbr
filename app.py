from flask import Flask

app = Flask(__name__)

@app.route('/')
def menssagem():
    nome = "Joel"
    return nome



@app.route('/contato')
def contato():
    return "<p>Hello, World!</p>"