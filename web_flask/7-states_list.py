#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    states_list
    """
    s_list = storage.all("State").values()
    return render_template("7-states_list.html", s_list=s_list)


@app.teardown_appcontext
def teardown_db(exception):
    """
    teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run()
