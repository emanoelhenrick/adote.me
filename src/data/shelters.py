from uuid import uuid4
from src.data.utils import getJsonPath
import os
import json


SHELTER_PATH = getJsonPath('shelter')


def create(new_shelter):
    new_uuid = uuid4().__str__()
    new_shelter['id'] = new_uuid

    if not os.path.exists(SHELTER_PATH):
        with open(SHELTER_PATH, 'w') as file:
            json.dump([new_shelter], file, indent=4)
        return new_shelter

    with open(SHELTER_PATH, 'r') as file:
        shelter_json = json.load(file)
        shelter_json.append(new_shelter)

    with open(SHELTER_PATH, 'w') as file:
        json.dump(shelter_json, file, indent=4)

    return new_shelter


def update(updated_shelter):
    if not os.path.exists(SHELTER_PATH):
        return None

    with open(SHELTER_PATH, 'r') as file:
        shelter_json = json.load(file)

        for shelter in shelter_json:
            if shelter['id'] == updated_shelter['id']:
                shelter.update(updated_shelter)
                break

        with open(SHELTER_PATH, 'w') as file:
            json.dump(shelter_json, file, indent=4)

    return updated_shelter


def readById(shelter_id):
    if not os.path.exists(SHELTER_PATH):
        return None
    
    with open(SHELTER_PATH, 'r') as file:
        shelter_json = json.load(file)

        for shelter in shelter_json:
            if shelter["id"] == shelter_id:
                return shelter
            
    return None


def readAll():
    if not os.path.exists(SHELTER_PATH):
        return None
    
    with open(SHELTER_PATH, 'r') as file:
        shelter_json = json.load(file)
        return shelter_json


def delete(shelter_id):
    if not os.path.exists(SHELTER_PATH):
        return None
    
    with open(SHELTER_PATH, 'r') as file:
        shelter_json = json.load(file)

        for shelter in shelter_json:
            if shelter["id"] == shelter_id:
                shelter_json.remove(shelter)
                break
            
        with open(SHELTER_PATH, 'w') as file:
          json.dump(shelter_json, file, indent=4)

    return None