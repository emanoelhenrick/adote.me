from flask import Blueprint, jsonify
from src.data import adopters

controller = Blueprint('adopters', __name__, url_prefix='/adopters')

@controller.post('/')
def createNewAdopter():
  adopters.create({ "name": "manel" })
  return jsonify({ "message": "cria uma catraia"})

@controller.get('/')
def fetchAllAdopters():
  adopters.readAll()
  return jsonify({ "message": "cuida catraias"})

@controller.get('/<id>')
def getAdopterById(id):
  adopters.readById(id)
  return jsonify({ 
    "message": "cuida catraia no singular",
    "id": id
  })

@controller.put('/')
def updateAdopter():
  adopters.update({ "name": "manel" })
  return jsonify({ "message": "catraia agr é malabares"})

@controller.delete('/<id>')
def deleteAdopter(id):
  adopters.delete(id)
  return jsonify({ "message": "catraia agr é malabares"})