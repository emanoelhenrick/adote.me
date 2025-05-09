from uuid import uuid4

def create(animal):
    new_uuid = uuid4().__str__()
    animal['id'] = new_uuid
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