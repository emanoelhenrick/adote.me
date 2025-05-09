from flask import Blueprint, jsonify
from src.data import volunteers

controller = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@controller.post('/')
def createNewVolunteer():
  volunteers.create({ "name": "manel" })
  return jsonify({ "message": "cria uma catraia"})

@controller.get('/')
def fetchAllVolunteers():
  volunteers.readAll()
  return jsonify({ "message": "cuida catraias"})

@controller.get('/<id>')
def getVolunteerById(id):
  volunteers.readById(id)
  return jsonify({ 
    "message": "cuida catraia no singular",
    "id": id
  })

@controller.put('/')
def updateVolunteer():
  volunteers.update({ "name": "manel" })
  return jsonify({ "message": "catraia agr é malabares"})

@controller.delete('/<id>')
def deleteVolunteer(id):
  volunteers.delete(id)
  return jsonify({ "message": "catraia agr é malabares"})

