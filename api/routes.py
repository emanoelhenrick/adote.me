from flask import Blueprint
from api.controllers import adoptersController, animalsController, sheltersController, volunteersController, authController

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(authController.controller)
api.register_blueprint(adoptersController.controller)
api.register_blueprint(animalsController.controller)
api.register_blueprint(sheltersController.controller)
api.register_blueprint(volunteersController.controller)
