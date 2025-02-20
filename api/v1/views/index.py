#!/usr/bin/python3
"""
Index views for the API.

This module contains the basic routes for the API,
including status and other general information endpoints.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """
    Return the API status.

    Returns:
        dict: JSON response containing API status
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'])
def number_of_objs():
    """retrieves the number of each objects by type"""
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    return jsonify(data)
