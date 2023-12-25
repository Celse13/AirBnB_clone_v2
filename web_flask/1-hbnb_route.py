#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displaying "Hello HBNB!" on the webpage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "hbnb" on the webpage"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
