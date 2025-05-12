from flask import Blueprint, request
from src.data import shelters

controller = Blueprint('shelters', __name__, url_prefix='/shelters')

@controller.post('/')
def createNewShelter():
  newShelter = request.get_json()
  if not newShelter:
    return { "error": "no shelter data provided" }, 400
  savedShelter = shelters.create(newShelter)
  return savedShelter, 201

@controller.get('/')
def fetchAllShelters():
  all_shelters = shelters.readAll()
  return all_shelters, 200

@controller.get('/<id>')
def getShelterById(id):
  shelter = shelters.readById(id)
  return shelter, 200

@controller.put('/')
def updateShelter():
  updated_shelter = shelters.update({ "name": "casa nao mais de mae joana" })
  return updated_shelter, 200

@controller.delete('/<id>')
def deleteShelter(id):
  shelters.delete(id)
  return 'shelter deleted', 200

