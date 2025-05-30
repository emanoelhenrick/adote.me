from src.repositories import animalsRepository
from src.repositories import sheltersRepository
from src.repositories import volunteersRepository
from src.repositories import adoptersRepository

def acceptAdoptionRequest(animal_id, adopter_id):
    # altera a propriedade 'adopted' do animal para True
    # remove o id do adotante da lista de 'adoption_requests' do animal
    # adiciona o id do animal na lista de 'adopted_animals' do adotante
    # deve retornar True se a operação for bem-sucedida, False caso contrário
    pass

def cancelAdoptionRequest(animal_id, adopter_id):
    # remove o id do adotante da lista de 'adoption_requests' do animal
    # remove o id do animal da lista de 'adoption_requests' do adotante
    # deve retornar True se a operação for bem-sucedida, False caso contrário teste
    pass

def updateAcceptingVolunteers(shelter_id):
    # atualiza a propriedade 'accepting_volunteers' do abrigo
    # deve receber um id de abrigo e inverter o valor da propriedade
    # deve retornar True se a operação for bem-sucedida, False caso contrário
    pass

