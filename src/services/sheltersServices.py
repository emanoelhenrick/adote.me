from src.repositories import animalsRepository
from src.repositories import sheltersRepository
from src.repositories import volunteersRepository
from src.repositories import adoptersRepository

def acceptAdoptionRequest(animal_id, adopter_id):
    animal = animalsRepository.readById(animal_id)
    adopter = adoptersRepository.readById(adopter_id)

    if adopter_id in animal['adoption_requests']:
        animal['adopted'] = True
        animal['adoption_requests'].remove(adopter_id)
        adopter['adopted_animals'].append(animal_id)
        animalsRepository.update(animal)
        adoptersRepository.update(adopter)
        return True
    return False

    # altera a propriedade 'adopted' do animal para True
    # remove o id do adotante da lista de 'adoption_requests' do animal
    # adiciona o id do animal na lista de 'adopted_animals' do adotante
    # deve retornar True se a operação for bem-sucedida, False caso contrário

def cancelAdoptionRequest(animal_id, adopter_id):
    animal = animalsRepository.readById(animal_id)
    newRequestsList = []
    for requestAdopterId in animal['adoption_requests']:
        if requestAdopterId != adopter_id:
            newRequestsList.append(requestAdopterId)
    animal['adoption_requests'] = newRequestsList

    adopter= adoptersRepository.readById(adopter_id)
    newRequestList2= []
    for requestAnimalId in adopter['adoption_requests']:
        if requestAnimalId !=animal_id:
            newRequestList2.append(requestAnimalId)
    adopter['adoption_requests']
   
def updateAcceptingVolunteers(shelter_id):
    # atualiza a propriedade 'accepting_volunteers' do abrigo
    # deve receber um id de abrigo e inverter o valor da propriedade
    # deve retornar True se a operação for bem-sucedida, False caso contrário
    pass

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