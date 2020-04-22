#!/usr/bin/python3
"""
flask init
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    hello_route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    c_route
    """
    return "C {}".format(text.replace("_",  " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """
    python_route
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """
    number route
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    number template
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
