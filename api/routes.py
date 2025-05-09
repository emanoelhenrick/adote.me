from flask import Blueprint
from api.controllers import adopters, animals, shelters, volunteers

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(adopters.controller)
api.register_blueprint(animals.controller)
api.register_blueprint(shelters.controller)
api.register_blueprint(volunteers.controller)
