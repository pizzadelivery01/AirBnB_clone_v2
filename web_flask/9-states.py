#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_city(id=None):
    """
    states_city
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)

@app.teardown_appcontext
def teardown_db(exception):
    """
    teardown
    """
    storage.close()

if __name__ == '__main__':
    app.run()
