from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/hello')
def hello():
    data = {"mensagem": "aquele que deixou a cesar school"}
    return jsonify(data)
