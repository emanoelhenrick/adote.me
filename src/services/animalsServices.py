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
    animal = animalsRepository.readAll()
    available = []

    if animal is None:
        return []

    for animal in animalsRepository:
        if animal.get('adopted') == False:
            available.append(animal)

    return available
