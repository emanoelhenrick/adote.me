from flask import Blueprint, jsonify, request
from src.repositories import animalsRepository
from src.services import animalsServices

controller = Blueprint('animals', __name__, url_prefix='/animals')

@controller.post('/')
def createNewAnimal():
  new_animal = request.get_json()
  if not new_animal:
    return jsonify({ "message": "Não foi possível adicionar um novo animal" }), 400
  animalsRepository.create(new_animal)
  return '', 201

@controller.get('/')
def fetchAllAnimals():
  animals = animalsRepository.readAll()
  return animals

@controller.get('/<id>')
def getAnimalById(id):
  animal = animalsRepository.readById(id)
  return animal

@controller.get('/shelter/<id>')
def getAnimalByShelter(id):
  animals = animalsRepository.readAllByShelterId(id)
  return animals

@controller.put('/')
def updateAnimal():
  updated_animal = request.get_json()
  if not updated_animal:
    return jsonify({ "message": "Animal não foi enviado" }), 400
  updatedAnimal = animalsRepository.update(updated_animal)
  if not updatedAnimal:
    return jsonify({ "message": "Animal não encontrado" }), 404
  return jsonify({ "message": "Animal atualizado com sucesso" }), 200

@controller.delete('/<id>')
def deleteAnimal(id):
  animalsRepository.delete(id)
  return '', 200

#------------------------------------------------#

# request_data example:
# {
#   'adopter_id': '12345',
#   'animal_id': '67890',
# }
@controller.post('/adoption')
def requestAdoption():
  request_data = request.get_json()
  if not request_data:
    return jsonify({ "error": "no request data provided" }), 400
  adopter_id = request_data.get('adopter_id')
  animal_id = request_data.get('animal_id')
  isSuccess = animalsServices.requestAdoption(adopter_id, animal_id)
  if not isSuccess:
    return jsonify({ "error": "adoption request failed" }), 500
  return jsonify({ "message": "adoption request successful" }), 200

@controller.post('/cancel-adoption')
def cancelAdoption():
  request_data = request.get_json()
  if not request_data:
    return jsonify({ "error": "no request data provided" }), 400
  adopter_id = request_data.get('adopter_id')
  animal_id = request_data.get('animal_id')
  isSuccess = animalsServices.cancelAdoption(adopter_id, animal_id)
  if not isSuccess:
    return jsonify({ "error": "cancellation of adoption request failed" }), 500
  return jsonify({ "message": "cancellation of adoption request successful" }), 200

@controller.get('/available')
def fetchAllAvailableAnimals():
  available_animals = animalsServices.fetchAllAvailableAnimals()
  if not available_animals:
    return jsonify({ "message": "no available animals found" }), 404
  return jsonify(available_animals), 200
