#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_by_template(n):
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_if_isodd_oreven(n):
    """Return if the n is even or odd."""
    if n % 2 == 0:
        temp = "even"
    else:
        temp = 'odd'

    return render_template('6-number_odd_or_even.html', value=n, text=temp)


@app.route('/states_list', strict_slashes=False)
def dsiplay_states_list():
    """Displaying state id and name"""
    states_cls = storage.all('State').values()
    return render_template('7-states_list.html', states=states_cls)


@app.teardown_appcontext
def teardown():
    """Close session when app content torn down."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
