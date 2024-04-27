#!/usr/bin/python3
"""
This module contains the endpoint definitions for the AirBnB clone API.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """
    Returns the status of the API as a JSON response.
    """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def api_stats():
    """
    Retrieves the number of each object type and returns as a JSON response.
    """
    classes = [Amenity, City, Place, Review, State, User]
    values = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[values[i]] = storage.count(classes[i])
    return jsonify(num_objs)
