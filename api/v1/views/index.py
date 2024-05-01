#!/usr/bin/python3
"""module for the api"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns a json response"""
    return jsonify({"status": "OK"})
