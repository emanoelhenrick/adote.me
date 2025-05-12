from uuid import uuid4
from src.data import utils

def create(new_shelter):
    new_uuid = uuid4().__str__()
    new_shelter['id'] = new_uuid
    return new_shelter

def update(updated_shelter):
    print("altera uma entidade")

def readById(shelter_id):
    print("lê uma entidade")

def readAll():
    print("lê uma entidade")

def delete(shelter_id):
    print("remove uma entidade")