from flask import Flask, render_template, request, jsonify
import os

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

# Vercel serverless handler
app.debug = True
handler = app.wsgi_app

if __name__ == '__main__':
    app.run(debug=True) 