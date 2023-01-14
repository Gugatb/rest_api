
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask import jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/hello')
def print_hello():
    return jsonify('Hello world!')

@app.route('/param')
def print_params():
    return jsonify({'key1': request.args.get('key1'), 'key2': request.args.get('key2')})

@app.route('/text/<text>')
def print_text(text):
    return jsonify({'text': text})

if __name__ == '__main__':
	app.run(debug=True, port='8080')
