from uuid import uuid4

def create(new_adopter):
    new_uuid = uuid4().__str__()
    new_adopter['id'] = new_uuid
    return new_adopter

def update(updated_adopter):
    print("altera uma entidade")

def readAll():
    print("lê todas as entidade")

def readById(adopter_id):
    print("lê uma entidade")

def delete(adopter_id):
    print("remove uma entidade")