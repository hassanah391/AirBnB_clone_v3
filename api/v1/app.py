#!/usr/bin/python3
"""
Flask application entry point.

This module initializes the Flask application, registers blueprints,
and sets up the basic configuration for the RESTful API.
"""
from flask import Flask,  make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    """
    Clean up function that closes the storage connection
    when the app context tears down.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """return JSON formatted 404 status code response"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True, debug=True)