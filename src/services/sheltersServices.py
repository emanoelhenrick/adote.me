from src.repositories import animalsRepository
from src.repositories import sheltersRepository
from src.repositories import volunteersRepository
from src.repositories import adoptersRepository

def acceptAdoptionRequest(animal_id, adopter_id):
    animal= animalsRepository.readById(animal_id)
    adopter= adoptersRepository.readById(adopter_id)
    if animal is None or adopter is None:
        return False
    
    animal['adopted']= True

    if adopter_id in animal['adoption_requests']:
        animal['adoption_requests'].remove(adopter_id)
    
    if'adopted_animals' not in adopter:
        adopter['adopted_animals']=[]

        adopter['adopted_animals'].append(animal_id)

        animalsRepository.update(animal)
        adoptersRepository.update(adopter)

        return True

def cancelAdoptionRequest(animal_id, adopter_id):
    animal = animalsRepository.readById(animal_id)
    newRequestsList = []
    for requestAdopterId in animal['adoption_requests']:
        if requestAdopterId != adopter_id:
            newRequestsList.append(requestAdopterId)
    animal['adoption_requests'] = newRequestsList
    animalsRepository.update(animal)
    return True
           

def updateAcceptingVolunteers(shelter_id):
    shelter = sheltersRepository.readById(shelter_id)
    if shelter is None:
        return False
    
    if 'accepting_volunteers' in shelter:
        if shelter['accepting_volunteers']:
            shelter['accepting_volunteers'] = False
        else:
            shelter['accepting_volunteers'] = True
    sheltersRepository.update(shelter)
    return shelter['accepting_volunteers']


def acceptingVolunteers(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)
    if volunteer_id in shelter['volunteer_requests']:
        volunteer['accepting_volunteers'] = True
        shelter['volunteers'].append(volunteer_id)
        shelter['volunteer_requests'].remove(volunteer_id)
        sheltersRepository.update(shelter)
        volunteersRepository.update(volunteer)
        return True
    return False

def refusingVolunteers(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)
    if volunteer_id in shelter['volunteer_requests']:
        volunteer['accepting_volunteers'] = False
        shelter['volunteer_requests'].remove(volunteer_id)
        sheltersRepository.update(shelter)
        volunteersRepository.update(volunteer)
        return True
    return False 


def fetchAllVolunteers():
    volunteers = volunteersRepository.readAll()
    accepted_volunteers = []

    if volunteers is None:
        return []
    
    for volunteer in volunteers:
        if volunteer.get('accepting_volunteers'):
            accepted_volunteers.append(volunteer)

    return accepted_volunteers

def fetchAllAdoptionRequests(shelter_id):
    animals = animalsRepository.readAllByShelterId(shelter_id)
    adoption_requests = []

    if animals is None:
        return []
    
    for animal in animals:
        if animal.get('adoption_requests'):
            for adopter_id in animal['adoption_requests']:
                adoption_requests.append({
                    'animal_id': animal['id'],
                    'adopter_id': adopter_id
                })

    return adoption_requests