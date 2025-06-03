from flask import Blueprint, jsonify, request
from src.repositories import volunteersRepository
from src.services import volunteersServices

controller = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@controller.post('/')
def createNewVolunteer():
  new_volunteer = request.get_json()
  if not new_volunteer:
    return jsonify({ "message": "Novo voluntário não foi enviado" }), 400
  savedVolunteer = volunteersRepository.create(new_volunteer)
  return savedVolunteer, 201

@controller.get('/')
def fetchAllVolunteers():
  volunteers = volunteersRepository.readAll()
  return volunteers

@controller.get('/<id>')
def getVolunteerById(id):
  volunteer = volunteersRepository.readById(id)
  return jsonify(volunteer)

@controller.put('/')
def updateVolunteer():
  updated_volunteer = request.get_json()
  if not updated_volunteer:
    return jsonify({ "message": "Voluntário não foi enviado" }), 400
  updated_volunteer = volunteersRepository.update(updated_volunteer)
  if not updated_volunteer:
    return jsonify({ "message": "Voluntário não encontrado" }), 404
  return '', 200

@controller.delete('/<id>')
def deleteVolunteer(id):
  volunteersRepository.delete(id)
  return '', 200

@controller.get('/available-shelters')
def fetchAvailableShelters():
  shelters = volunteersServices.fetchAvailableShelters()
  return jsonify(shelters), 200

@controller.post('/request-volunteer')
def requestVolunteer():
  data = request.get_json()
  if not data or 'shelter_id' not in data or 'volunteer_id' not in data:
    return jsonify({ "message": "Dados inválidos" }), 400
  success = volunteersServices.requestVolunteer(data['shelter_id'], data['volunteer_id'])
  if not success:
    return jsonify({ "message": "Erro ao solicitar voluntariado" }), 500
  return jsonify({ "message": "Solicitação de voluntariado enviada com sucesso" }), 201

@controller.post('/accept-volunteer-request')
def acceptVolunteerRequest():
  data = request.get_json()
  if not data or 'shelter_id' not in data or 'volunteer_id' not in data:
    return jsonify({ "message": "Dados inválidos" }), 400
  success = volunteersServices.acceptVolunteerRequest(data['shelter_id'], data['volunteer_id'])
  if not success:
    return jsonify({ "message": "Erro ao aceitar solicitação de voluntariado" }), 500
  return jsonify({ "message": "Solicitação de voluntariado aceita com sucesso" }), 200

@controller.post('/cancel-volunteer-request')
def cancelVolunteerRequest():
  data = request.get_json()
  if not data or 'shelter_id' not in data or 'volunteer_id' not in data:
    return jsonify({ "message": "Dados inválidos" }), 400
  success = volunteersServices.cancelVolunteerRequest(data['shelter_id'], data['volunteer_id'])
  if not success:
    return jsonify({ "message": "Erro ao cancelar solicitação de voluntariado" }), 500
  return jsonify({ "message": "Solicitação de voluntariado cancelada com sucesso" }), 200

@controller.get('/active-shelters/<volunteer_id>')
def fetchActiveShelters(volunteer_id):
  shelters = volunteersServices.fetchActiveShelters(volunteer_id)
  return jsonify(shelters), 200

@controller.get('/pending-requests/<volunteer_id>')
def fetchPendingRequests(volunteer_id):
  shelters = volunteersServices.fetchPendingRequests(volunteer_id)
  return jsonify(shelters), 200


