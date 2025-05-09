from flask import Blueprint, jsonify
from src.data import animals

controller = Blueprint('animals', __name__, url_prefix='/animals')

@controller.post('/')
def createNewAnimal():
  animals.create({ "name": "manel" })
  return jsonify({ "message": "cria uma catraia"})

@controller.get('/')
def fetchAllAnimals():
  animals.readAll()
  return jsonify({ "message": "cuida catraias"})

@controller.get('/<id>')
def getAnimalById(id):
  animals.readById(id)
  return jsonify({ 
    "message": "cuida catraia no singular",
    "id": id
  })

@controller.put('/')
def updateAnimal():
  animals.update({ "name": "click" })
  return jsonify({ "message": "catraia agr é malabares"})

@controller.delete('/<id>')
def deleteAnimal(id):
  animals.delete(id)
  return jsonify({ "message": "catraia agr é malabares"})

