from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'BadWare API: Online'


@app.route('/discord', methods=['GET'])
def discord():
    return 'https://discord.gg/4jAczz5DEW'


@app.route('/api', methods=['GET'])
def api():
    response = requests.get('https://api.whatexploitsare.online/status')
    data = response.json()
    content = {'data': data}
    return jsonify(content)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
