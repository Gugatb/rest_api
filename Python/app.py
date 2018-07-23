
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask import jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/hello')
def print_hello():
    '''
    Exibir o ola mundo.
    Author: Gugatb
    Date: 15/06/2018
    '''
    return jsonify('Ola mundo')

@app.route('/param')
def print_params():
    '''
    Exibir os parametros.
    Author: Gugatb
    Date: 15/06/2018
    '''
    return jsonify({'key1': request.args.get('key1'), 'key2': request.args.get('key2')})

@app.route('/text/<text>')
def print_text(text):
    '''
    Imprimir a informacao.
    Author: Gugatb
    Date: 23/07/2018
    Param: information a informacao
    '''
    return jsonify({'text': text})

if __name__ == '__main__':
	app.run(debug=True, port='8080')
