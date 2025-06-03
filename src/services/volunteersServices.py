from src.repositories import volunteersRepository
from src.repositories import sheltersRepository

def fetchAvailableShelters():
    all_shelters = sheltersRepository.readAll()
    return [
        shelter for shelter in all_shelters
        if shelter.get('accepting_volunteers') is True
    ]


def fetchActiveShelters(volunteer_id):
    volunteer = volunteersRepository.readById(volunteer_id)
    if not volunteer:
        return []
    
    shelters = sheltersRepository.readAll()
    lista = []

    for shelter in shelters:
        if volunteer_id in shelter.get('active_volunteers'):
            lista.append(shelter)
    return lista


def fetchPendingRequests(volunteer_id):
    volunteer = volunteersRepository.readById(volunteer_id)
    if not volunteer:
        return []

    return [
        shelter for shelter_id in volunteer.get('applied_shelters')
        if (shelter := sheltersRepository.readById(shelter_id))
    ]


def requestVolunteer(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)

    if not shelter or not volunteer:
        return False
    
    if volunteer_id in shelter.get('active_volunteers'):
        return False

    if volunteer_id not in shelter.get('volunteer_requests'):
        shelter['volunteer_requests'].append(volunteer_id)

    if shelter_id not in volunteer.get('applied_shelters'):
        volunteer['applied_shelters'].append(shelter_id)

    sheltersRepository.update(shelter)
    volunteersRepository.update(volunteer)

    return True


def cancelVolunteerRequest(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)

    if not shelter or not volunteer:
        return False

    shelter['volunteer_requests'] = [
        v_id for v_id in shelter.get('volunteer_requests')
        if v_id != volunteer_id
    ]

    volunteer['applied_shelters'] = [
        s_id for s_id in volunteer.get('applied_shelters')
        if s_id != shelter_id
    ]

    sheltersRepository.update(shelter)
    volunteersRepository.update(volunteer)

    return True


def acceptVolunteerRequest(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)

    if not shelter or not volunteer:
        return False

    if (
        volunteer_id in shelter.get('volunteer_requests') and
        shelter_id in volunteer.get('applied_shelters')
    ):
        shelter['volunteer_requests'].remove(volunteer_id)
        volunteer['applied_shelters'].remove(shelter_id)

        if volunteer_id not in shelter.get('active_volunteers'):
            shelter['active_volunteers'].append(volunteer_id)

        sheltersRepository.update(shelter)
        volunteersRepository.update(volunteer)

        return True

    return False
