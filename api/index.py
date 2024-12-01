from flask import Flask, render_template, request, jsonify
import os
from http.server import BaseHTTPRequestHandler

app = Flask(__name__)
app.template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/render', methods=['POST'])
def render_latex():
    text = request.json.get('text', '')
    text = text.replace('\n', '<br>')
    return jsonify({'text': text})

class handler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = app.handle_request()
        self.wfile.write(response.get_data())
    
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        response = app.handle_request()
        self.wfile.write(response.get_data())

if __name__ == '__main__':
    app.run(debug=True) 