#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displaying "Hello HBNB!" on the webpage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "hbnb" on the webpage"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displaying c is fun"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displaying Python is coo"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def display_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_number_by_template(n):
    return render_template('5-number.html', value=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
