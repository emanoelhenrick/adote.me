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
            json.dump([ANIMAL_PATH], file, indent=4)
    return animal


def update(updated_animal):
    print("altera uma entidade")

def readById(animal_id):
    print("lê uma entidade")

def readAll():
    print("lê todas as entidades")

def readAllByShelterId(shelter_id):
    print("lê todas as entidades relacionadas a um abrigo")

def delete(animal_id):
    print("remove uma entidade")