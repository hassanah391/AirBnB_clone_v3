#!/usr/bin/python3
"""cities.py"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City
from models.state import State


@app_views.route("/states/<state_id>/cities", methods=['GET'],
                 strict_slashes=False)
def get_cities_of_state(state_id):
    """return cities of a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = state.cities
    return make_response(jsonify([city.to_dict() for city in cities]))


@app_views.route("/cities/<city_id>", methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrives a city by its id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route("cities/<city_id>", methods=['DELETE'])
def delete_city(city_id):
    """Deletes a city obj if exist"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """Creates new city"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)  
    if request.content_type != 'application/json':
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    try:
        r = request.get_json()
        if r is None:
            raise ValueError
    except ValueError:
        return make_response(jsonify({'error': 'Invalid JSON'}), 400)

    if 'name' not in r:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    r['state_id'] = state_id
    city = City(**r)
    city.save()

    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Updates an exist city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.is_json:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(city, attr, val)
    city.save()
    return jsonify(city.to_dict())
