from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def init():
    return {"data": "My first API Rest"}


if __name__ == '__main__':
    app.run(port=8000)
