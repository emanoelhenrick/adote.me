from flask import Blueprint, jsonify, request
from src.services import authServices

controller = Blueprint('auth', __name__, url_prefix='/auth')

@controller.post('/register')
def registerAccount():
  user = request.get_json()
  if not user:
    return { "error": "no data provided" }, 400
  
  userRegistred = authServices.registerUser(user)
  if not userRegistred:
    return { "error": "user already exists" }, 400
  return jsonify(userRegistred), 201

@controller.post('/login')
def loginAccount():
  user = request.get_json()
  if not user:
    return { "error": "no data provided" }, 400
  
  authenticatedUser = authServices.authenticateUser(user.get('email'), user.get('password'))
  if not authenticatedUser:
    return { "error": "invalid credentials" }, 401
  
  return jsonify(authenticatedUser), 200