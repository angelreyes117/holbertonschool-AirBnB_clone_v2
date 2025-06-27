#!/usr/bin/python3
"""Starts a Flask web application for /states_list"""
from flask import Flask, render_template
from models import storage  # Importar storage correctamente
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Render HTML page with H1 tag 'States' and list of State objects sorted by name."""
    # Obtener todos los objetos State y ordenarlos por nombre
    states = sorted(storage.all("State").values(), key=lambda st: st.name)
    # Pasar la lista de estados a la plantilla
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Close storage session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
