from src.repositories import adoptersRepository
from src.repositories import animalsRepository


def getPendingAdoptionRequests(adopter_id):
    adopter = adoptersRepository.readById(adopter_id)
    if not adopter:
        return None
    
    adoption_requests = adopter.get('adoption_requests')
    if not adoption_requests:
        return []

    requested_animals = []
    for animal_id in adoption_requests:
        animal = animalsRepository.readById(animal_id)
        if animal:  
            requested_animals.append(animal)

    return requested_animals


def fetchAdoptedAnimals(adopter_id):

    adopter = adoptersRepository.readById(adopter_id)
    if not adopter:
        return None
    
    adopted_animals_id = adopter.get('adopted_animals')
    if not adopted_animals_id:
        return []
    
    adopted_animals = []
    for animal_id in adopted_animals_id:
        animal = animalsRepository.readById(animal_id)
        if animal:
            adopted_animals.apend(animal)
    return adopted_animals
    

   

