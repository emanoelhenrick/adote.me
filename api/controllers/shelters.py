from flask import Blueprint, jsonify
from src.data import shelters

controller = Blueprint('shelters', __name__, url_prefix='/shelters')

@controller.post('/')
def createNewShelter():
  shelters.create({ "name": "casa de mae joana" })
  return jsonify({ "message": "cria uma catraia"})

@controller.get('/')
def fetchAllShelters():
  shelters.readAll()
  return jsonify({ "message": "cuida catraias"})

@controller.get('/<id>')
def getShelterById(id):
  shelters.readById(id)
  return jsonify({ 
    "message": "cuida catraia no singular",
    "id": id
  })

@controller.put('/')
def updateShelter():
  shelters.update({ "name": "casa nao mais de mae joana" })
  return jsonify({ "message": "catraia agr é malabares"})

@controller.delete('/<id>')
def deleteShelter(id):
  shelters.delete(id)
  return jsonify({ "message": "catraia agr é malabares"})

