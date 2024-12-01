from flask import Flask, render_template, request, jsonify
from flask.helpers import send_from_directory
import os

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/render', methods=['POST'])
def render_latex():
    text = request.json.get('text', '')
    text = text.replace('\n', '<br>')
    return jsonify({'text': text})

# Vercel requires this handler
def handler(environ, start_response):
    return app(environ, start_response) 