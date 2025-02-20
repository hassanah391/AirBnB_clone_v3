#!/usr/bin/python3
"""
Initialize Blueprint views for the API

This module creates a Blueprint instance for the API views
and imports all view modules that need to be registered.
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
