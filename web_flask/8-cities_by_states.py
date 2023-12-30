#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """Displaying cities id and name by their states"""
    states_cls = storage.all(State)
    return render_template('8-cities_by_states.html', states=states_cls)


@app.teardown_appcontext
def close(arg=None):
    """Close session when app conten torn down."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
