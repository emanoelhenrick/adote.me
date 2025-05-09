from uuid import uuid4

def create(volunteer):
    new_uuid = uuid4().__str__()
    volunteer['id'] = new_uuid
    return volunteer

def update(updated_volunteer):
    print("altera uma entidade")

def readById(volunteer_id):
    print("lê uma entidade")

def readAll():
    print("lê todas as entidades")

def readByShelterId(shelter_id):
    print("lê todas as entidades relacionadas a um abrigo")

def delete(volunteer_id):
    print("remove uma entidade")