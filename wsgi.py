from random import randint
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    x = [randint(0,9) for p in range(0,987)]
    return x

if __name__ == "__main__":
    application.run()
