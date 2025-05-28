import os
import json
from uuid import uuid4
from src.data.utils import getJsonPath 

ANIMAL_PATH = getJsonPath('animal')

def create(animal):
    new_uuid = uuid4().__str__()
    animal['id'] = new_uuid

    if not os.path.exists(ANIMAL_PATH):
        with open(ANIMAL_PATH, 'w') as file:
            json.dump([animal], file, indent=4)
        return animal

    with open(ANIMAL_PATH, 'r') as file:
        animal_json = json.load(file)
        animal_json.append(animal)

    with open(ANIMAL_PATH, 'w') as file:
        json.dump(animal_json, file, indent=4)

    return animal 


def update(updated_animal):
    if not os.path.exists(ANIMAL_PATH):
        return None
    
    with open(ANIMAL_PATH, 'r') as file:
        animal_json = json.load(file)

        for animal in animal_json:
             if animal['id'] == updated_animal['id']:
                animal.update(updated_animal)
                break
        with open(ANIMAL_PATH, 'w') as file:
          json.dump(animal_json, file, indent=4)

    return updated_animal

def readById(animal_id):
     if not os.path.exists(ANIMAL_PATH):
        return None

     with open(ANIMAL_PATH, 'r') as file:
        animal_json = json.load(file)
        for animal in animal_json:
            if animal['id'] == animal_id:
                return animal
     return None

def readAll():
    if not os.path.exists(ANIMAL_PATH):
        return None

    with open(ANIMAL_PATH, 'r') as file:
        animal_json = json.load(file)
        return animal_json
    
def readAllByShelterId(shelter_id):
    if not os.path.exists(ANIMAL_PATH):
        return None

    with open(ANIMAL_PATH, 'r') as file:
        animals = []
        animal_json = json.load(file)
        for animal in animal_json:
            if animal['shelter_id'] == shelter_id:
                animals.append(animal)
        if len(animals) > 0:
            return animals
    return None

def delete(animal_id):
    if not os.path.exists(ANIMAL_PATH):
        return None
    
    with open(ANIMAL_PATH, 'r') as file:
        animal_json = json.load(file)
    
        for animal in animal_json:
            if animal["id"] == animal_id:
                animal_json.remove(animal)
                break
            
        with open(ANIMAL_PATH, 'w') as file:
          json.dump(animal_json, file, indent=4)

    return None