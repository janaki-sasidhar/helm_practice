from turtle import rt
from flask import Flask
import socket
import requests

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    return 'Hello World!\nI am running on: {}'.format(hostname)

@app.route('/connect')
def connect_to_app_two():
    url = 'http://app-two:5000/'
    response = requests.get(url)
    return response.text



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
