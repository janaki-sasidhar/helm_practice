from turtle import rt
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    return 'Hello World!\nI am running on: {}'.format(hostname)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
