import os
import json
from uuid import uuid4
from src.data.utils import getJsonPath

ADOPTERS_PATH = getJsonPath('adopters')

def create(new_adopter):
    new_uuid = uuid4().__str__()
    new_adopter['id'] = new_uuid

    if not os.path.exists(ADOPTERS_PATH):
        with open(ADOPTERS_PATH, 'w') as file:
            json.dump([new_adopter], file, indent=4)
        return new_adopter

    with open(ADOPTERS_PATH, 'r') as file:
        adopter_json = json.load(file)
        adopter_json.append(new_adopter)

    with open(ADOPTERS_PATH, 'w') as file:
        json.dump(adopter_json, file, indent=4)

    return new_adopter



def update(updated_adopter):
    if not os.path.exists(ADOPTERS_PATH):
        return None

    with open(ADOPTERS_PATH, 'r') as file:
        adopter_json = json.load(file)

        for adopter in adopter_json:
            if adopter['id'] == updated_adopter['id']:
                adopter.update(updated_adopter)
                break

        with open(ADOPTERS_PATH, 'w') as file:
          json.dump(adopter_json, file, indent=4)

    return updated_adopter



def readAll():
    if not os.path.exists(ADOPTERS_PATH):
        return None

    with open(ADOPTERS_PATH, 'r') as file:
        adopter_json = json.load(file)
        return adopter_json



def readById(adopter_id):
    if not os.path.exists(ADOPTERS_PATH):
        return None

    with open(ADOPTERS_PATH, 'r') as file:
        adopter_json = json.load(file)
        for adopter in adopter_json:
            if adopter['id'] == adopter_id:
                return adopter
    return None



def delete(adopter_id):
    if not os.path.exists(ADOPTERS_PATH):
        return None

    with open(ADOPTERS_PATH, 'r') as file:
        adopter_json = json.load(file)

        for adopter in adopter_json:
            if adopter['id'] == adopter_id:
                adopter_json.remove(adopter)
                break

        with open(ADOPTERS_PATH, 'w') as file:
          json.dump(adopter_json, file, indent=4)

    return None