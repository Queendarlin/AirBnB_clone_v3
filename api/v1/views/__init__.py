#!/usr/bin/python3
"""
This package contains the view endpoints for the AirBnB clone API.
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *