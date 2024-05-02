#!/usr/bin/python3
"""module for the api"""
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

# add cors support
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def eliminate_db(exception):
    """teardown the database"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """a handler for 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', default='5000'))
    app.run(host=host, port=port, threaded=True, debug=True)
