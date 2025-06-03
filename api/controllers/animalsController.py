from flask import Blueprint, jsonify, request
from src.repositories import animalsRepository
from src.services import animalsServices
import os
import uuid

controller = Blueprint('animals', __name__, url_prefix='/animals')

@controller.post('/')
def createNewAnimal():
  if request.content_type.startswith('multipart/form-data'):
    new_animal_data = request.form.to_dict()
    image = request.files.get('image')
    if not new_animal_data or not image:
      return jsonify({ "message": "Dados ou imagem não enviados" }), 400

    ext = os.path.splitext(image.filename)[1]
    unique_filename = f"{uuid.uuid4()}{ext}"

    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    upload_folder = os.path.join(project_root, "dist", "images")
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, unique_filename)
    image.save(image_path)

    new_animal_data['image_filename'] = unique_filename
    animalsRepository.create(new_animal_data)
    return '', 201
  else:
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

@controller.post('/update')
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
