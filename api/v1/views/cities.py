#!/usr/bin/python3
"""cities.py"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City
from models.state import State


@app_views.route("/states/<state_id>/cities", methods=['GET'], strict_slashes=False)
def get_cities_of_state(state_id):
    """return cities of a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = state.cities
    return make_response(jsonify([city.to_dict() for city in cities]))


