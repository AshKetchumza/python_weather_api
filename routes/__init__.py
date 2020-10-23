from flask import Blueprint
routes = Blueprint('routes', __name__)

# Import routes AFTER blueprint definition
from .index import *