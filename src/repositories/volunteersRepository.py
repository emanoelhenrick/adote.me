import os
import json
from uuid import uuid4
from src.repositories.utils import getJsonPath

VOLUNTEER_PATH = getJsonPath('volunteers')

def create(volunteer):
    new_uuid = uuid4().__str__()
    volunteer['id'] = new_uuid

    if not os.path.exists(VOLUNTEER_PATH):
        with open(VOLUNTEER_PATH, 'w') as file:
            json.dump([volunteer], file, indent=4)
        return volunteer
    
    with open(VOLUNTEER_PATH, 'r') as file:
        volunteer_json = json.load(file)
        volunteer_json.append(volunteer)

    with open(VOLUNTEER_PATH, 'w') as file:
        json.dump(volunteer_json, file, indent=4)

    return volunteer



def update(updated_volunteer):
    if not os.path.exists(VOLUNTEER_PATH):
        return None
    
    with open(VOLUNTEER_PATH, 'r') as file:
        volunteer_json = json.load(file)

        for volunteer in volunteer_json:
            if volunteer['id'] == updated_volunteer['id']:
                volunteer.update(updated_volunteer)
                break
        
        with open(VOLUNTEER_PATH, 'w') as file:
            json.dump(volunteer_json, file, indent=4)

    return updated_volunteer



def readById(volunteer_id):
    if not os.path.exists(VOLUNTEER_PATH):
        return None
    
    with open(VOLUNTEER_PATH, 'r') as file:
        volunteer_json = json.load(file)

        for volunteer in volunteer_json:
            if volunteer["id"] == volunteer_id:
                return volunteer
    
    return None

def readByEmail(email):
    if not os.path.exists(VOLUNTEER_PATH):
        return None
    
    with open(VOLUNTEER_PATH, 'r') as file:
        volunteer_json = json.load(file)

        for volunteer in volunteer_json:
            if volunteer["email"] == email:
                return volunteer
    
    return None

def readAll():
   if not os.path.exists(VOLUNTEER_PATH):
       return None
   
   with open(VOLUNTEER_PATH, 'r') as file:
       volunteer_json = json.load(file)
       return volunteer_json



def delete(volunteer_id):
    if not os.path.exists(VOLUNTEER_PATH):
        return None
    
    with open(VOLUNTEER_PATH, 'r') as file:
        volunteer_json = json.load(file)

        for volunteer in volunteer_json:
            if volunteer["id"] == volunteer_id:
                volunteer_json.remove(volunteer)
                break
        
        with open(VOLUNTEER_PATH, 'w') as file:
            json.dump(volunteer_json, file, indent=4)
    
    return None