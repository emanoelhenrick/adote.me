from src.repositories import sheltersRepository
from src.repositories import volunteersRepository
from src.repositories import adoptersRepository

def isUserExists(email):
    user = None

    vonlunteer = volunteersRepository.readByEmail(email)
    if vonlunteer:
        user = vonlunteer

    adopter = adoptersRepository.readByEmail(email)
    if adopter:
        user = adopter

    shelter = sheltersRepository.readByEmail(email)
    if shelter:
        user = shelter
    
    if user:
        return user
    else:
        return None

def authenticateUser(email, password):
    if not email or not password:
        return None
    
    user = isUserExists(email)
    
    if user and user.get('password') == password:
        return {
            'id': user.get('id'),
            'role': user.get('role')
        }
    else:
        return None
    
def registerUser(user_data):
    if not user_data:
        return None
    
    user_exists = isUserExists(user_data.get('email'))

    if user_exists:
        return None
    
    user = None

    if user_data.get('role') == 'volunteer':
        user = volunteersRepository.create(user_data)
    elif user_data.get('role') == 'adopter':
        user = adoptersRepository.create(user_data)
    elif user_data.get('role') == 'shelter':
        user = sheltersRepository.create(user_data)
    
    if user:
        return {
          'id': user.get('id'),
          'role': user.get('role')
        }
    else:
        return None
