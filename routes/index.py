from flask import jsonify
from . import routes

# Index
@routes.route("/")
def index():
    return jsonify({
        'msg': 'Success', 
        'info': 'View readme for info on this API', 
        'status': 200
        })