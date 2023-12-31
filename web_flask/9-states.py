#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id=None):
    """Displayng the states with their id(s)"""
    status_not_found = False
    if id is not None:
        states = storage.all(State, id)
        status = True
        if len(states) == 0:
            status_not_found = True
    else:
        states = storage.all(State)
        status = False
    return render_template('9-states.html', states=states,
                           status=status, status_not_found=status_not_found)


@app.teardown_appcontext
def close(arg=None):
    """Close session when app content torn down."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
