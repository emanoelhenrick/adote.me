from src.repositories import animalsRepository

def requestAdoption(request_data):
    animal = animalsRepository.readById(request_data.get('animal_id'))
    animal['adoption_requests'].append(request_data.get('adopter_id'))
    animalsRepository.update(animal)
    return True

def cancelAdoption(request_data):
    animal = animalsRepository.readById(request_data.get('animal_id'))
    if request_data.get('adopter_id') in animal['adoption_requests']:
        animal['adoption_requests'].remove(request_data.get('adopter_id'))
        animalsRepository.update(animal)
        return True
    return False

def fetchAllAvailableAnimals():
    # pega todos os animais e filtra os que estão disponíveis para adoção
    # deve retornar uma lista com os animais que estiverem com a propriedade 'adopted' = False
    pass

