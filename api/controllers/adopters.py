from flask import Blueprint, jsonify, request
from repositories import adoptersRepository
import src.services.adoptersServices as adoptersServices

controller = Blueprint('adopters', __name__, url_prefix='/adopters')

@controller.post('/')
def createNewAdopter():
  newAdopter = request.get_json()
  if not newAdopter:
    return { "error": "no adopter data provided" }, 400
  savedAdopter = adoptersRepository.create(newAdopter)
  if not savedAdopter:
    return { "error": "adopter already exists" }, 400
  return '', 201

@controller.get('/')
def fetchAllAdopters():
  allAdopters = adoptersRepository.readAll()
  return jsonify(allAdopters), 200

@controller.get('/<id>')
def getAdopterById(id):
  adopter = adoptersRepository.readById(id)
  if not adopter:
    return { "error": "adopter not found" }, 404
  return adopter, 200

@controller.put('/')
def updateAdopter():
  updated_adopter = request.get_json()
  if not updated_adopter:
    return { "error": "no adopter data provided" }, 400
  savedAdopter = adoptersRepository.update(updated_adopter)
  return jsonify(savedAdopter), 200

@controller.delete('/<id>')
def deleteAdopter(id):
  adoptersRepository.delete(id)
  return '', 200

@controller.get('/pending-requests/<adopter_id>')
def getPendingAdoptionRequests(adopter_id):
  pending_requests = adoptersServices.getPendingAdoptionRequests(adopter_id)
  return jsonify(pending_requests), 200

@controller.get('/adopted-animals/<adopter_id>')
def fetchAdoptedAnimals(adopter_id):
  adopted_animals = adoptersServices.fetchAdoptedAnimals(adopter_id)
  return jsonify(adopted_animals), 200