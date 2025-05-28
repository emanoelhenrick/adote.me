from flask import Blueprint, request
import src.repositories.sheltersRepository as sheltersRepository
import src.services.sheltersServices as sheltersServices

controller = Blueprint('shelters', __name__, url_prefix='/shelters')

@controller.post('/')
def createNewShelter():
  newShelter = request.get_json()
  if not newShelter:
    return { "error": "no shelter data provided" }, 400
  savedShelter = sheltersRepository.create(newShelter)
  return savedShelter, 201

@controller.get('/')
def fetchAllShelters():
  all_shelters = sheltersRepository.readAll()
  if not all_shelters:
    return { "message": "no shelters found" }, 404
  return all_shelters, 200

@controller.get('/<id>')
def getShelterById(id):
  shelter = sheltersRepository.readById(id)
  if not shelter:
    return { "message": "shelter not found" }, 404
  return shelter, 200

@controller.put('/')
def updateShelter():
  updated_shelter = request.get_json()
  if not updated_shelter:
    return { "error": "no shelter data provided" }, 400
  updated_shelter = sheltersRepository.update(updated_shelter)
  if not updated_shelter:
    return { "message": "shelter not found" }, 404
  return '', 200

@controller.delete('/<id>')
def deleteShelter(id):
  sheltersRepository.delete(id)
  return '', 200

@controller.post('/adoption')
def aceptAdoptionRequest():
  data = request.get_json()
  if not data or 'animal_id' not in data or 'adopter_id' not in data:
    return { "error": "animal_id and adopter_id are required" }, 400
  success = sheltersServices.aceptAdoptionRequest(data['animal_id'], data['adopter_id'])
  if not success:
    return { "message": "failed to accept adoption request" }, 500
  return '', 200

@controller.delete('/adoption')
def cancelAdoptionRequest():
  data = request.get_json()
  if not data or 'animal_id' not in data or 'adopter_id' not in data:
    return { "error": "animal_id and adopter_id are required" }, 400
  success = sheltersServices.cancelAdoptionRequest(data['animal_id'], data['adopter_id'])
  if not success:
    return { "message": "failed to cancel adoption request" }, 500
  return '', 200

@controller.put('/accepting-volunteers/<shelter_id>')
def updateAcceptingVolunteers(shelter_id):
  success = sheltersServices.updateAcceptingVolunteers(shelter_id)
  if not success:
    return { "message": "failed to update accepting volunteers status" }, 500
  return '', 200