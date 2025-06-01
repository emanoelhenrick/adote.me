from src.repositories import volunteersRepository
from src.repositories import sheltersRepository
from src.repositories import animalsRepository
from src.repositories import adoptersRepository

def fetchAvailableShelters():
    # pega todos os abrigos e filtra os que estão disponíveis para voluntários
    # deve retornar uma lista com os abrigos que estiverem com a propriedade 'accepting_volunteers' = True
    pass


def fetchActiveShelters(volunteer_id):
    # retorna os abrigos que o voluntário está ativo
    # devolve os abrigos que estão na propriedade 'active_volunteering' do voluntario
    pass


def fetchPendingRequests(volunteer_id):
    # retorna os abrigos que o voluntário solicitou para ser voluntário
    # devolve os abrigos que estão na propriedade 'applied_shelters' do voluntário
    pass


def requestVolunteer(shelter_id, volunteer_id):
    # adiciona o id do voluntário na lista de 'volunteer_requests' do abrigo
    # adiciona o id do abrigo na lista de 'applied_shelters' do voluntário
    # deve retornar True se a operação for bem-sucedida, False caso contrário
    pass


def cancelVolunteerRequest(shelter_id, volunteer_id):
    # remove o id do voluntário na lista de 'volunteer_requests' do abrigo
    # remove o id do abrigo na lista de 'applied_shelters' do voluntário
    # deve retornar True se a operação for bem-sucedida, False caso contrário
    pass


def acceptVolunteerRequest(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)

    if volunteer_id in shelter['volunteer_requests']:
        shelter['active_volunteering'].append(volunteer_id)
        volunteer['applied_shelters'].remove(shelter_id)
        shelter['volunteer_requests'].remove(volunteer_id)

        sheltersRepository.update(shelter)
        volunteersRepository.update(volunteer)

        return True
    return False