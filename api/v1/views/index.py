#!/usr/bin/python3
"""
Index views for the API.

This module contains the basic routes for the API,
including status and other general information endpoints.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route("/status", strict_slashes=False)
def status():
    """
    Return the API status.

    Returns:
        dict: JSON response containing API status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    return_dict = {}
    for key, value in hbnbText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)

if __name__ == "__main__":
    pass
