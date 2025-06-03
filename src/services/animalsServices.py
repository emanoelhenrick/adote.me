from src.repositories import animalsRepository

def requestAdoption(adopter_id, animal_id):
    animal = animalsRepository.readById(animal_id)
    animal['adoption_requests'].append(adopter_id)
    animalsRepository.update(animal)
    return True

def cancelAdoption(adopter_id, animal_id):
    animal = animalsRepository.readById(animal_id)
    if adopter_id in animal['adoption_requests']:
        animal['adoption_requests'].remove(adopter_id)
        animalsRepository.update(animal)
        return True
    return False

def fetchAllAvailableAnimals():
    animals = animalsRepository.readAll()
    available = []

    if animals is None:
        return []

    for animal in animals:
        if not animal['adopted']:
            available.append(animal)

    return available
