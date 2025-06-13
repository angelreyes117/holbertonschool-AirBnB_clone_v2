#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
import models

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(content):
    """ removes current SQLAlchemy sesh """
    models.storage.close()


@app.route('/states_list')
def states_list():
    """ prints list of states """
    states = models.storage.all(models.state.State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
