#!/usr/bin/python3
"""module for the api"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns a json response"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Return a JSON stats response """
    classes = {"Amenity": "amenities", "City": "cities",
               "Place": "places", "Review": "reviews",
               "State": "states", "User": "users"}
    stats = {}
    for key, value in classes.items():
        stats[value] = storage.count(key)
    return jsonify(stats)
