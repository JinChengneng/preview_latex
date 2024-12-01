from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/render', methods=['POST'])
def render_latex():
    text = request.json.get('text', '')
    text = text.replace('\n', '<br>')
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True) 