from flask import Blueprint, jsonify, request
from src.data import adopters

controller = Blueprint('adopters', __name__, url_prefix='/adopters')

@controller.post('/')
def createNewAdopter():
  newAdopter = request.get_json()

  if not newAdopter:
    return { "error": "no adopter data provided" }, 400
  
  savedAdopter = adopters.create(newAdopter)
  return savedAdopter, 201

@controller.get('/')
def fetchAllAdopters():
  allAdopters = adopters.readAll()
  return jsonify(allAdopters), 200

@controller.get('/<id>')
def getAdopterById(id):
  adopter = adopters.readById(id)
  if not adopter:
    return { "error": "adopter not found" }, 404
  return adopter, 200

@controller.put('/')
def updateAdopter():
  updated_adopter = request.get_json()
  if not updated_adopter:
    return { "error": "no adopter data provided" }, 400
  savedAdopter = adopters.update(updated_adopter)
  return jsonify(savedAdopter), 200

@controller.delete('/<id>')
def deleteAdopter(id):
  adopters.delete(id)
  return '', 200