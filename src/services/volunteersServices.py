from src.repositories import volunteersRepository
from src.repositories import sheltersRepository
from src.repositories import animalsRepository
from src.repositories import adoptersRepository

def fetchAvailableShelters():
    all_shelters = sheltersRepository.readAll()
    available_shelters = []

    if all_shelters:
        for shelter in all_shelters:
            if shelter['accepting_volunteers'] is True:
                available_shelters.append(shelter)
    
    return available_shelters


def fetchActiveShelters(volunteer_id):
    volunteer = volunteersRepository.readById(volunteer_id)
    active_shelters_list = []

    if volunteer:
        for shelter_id_active in volunteer['active_volunteering']:
            shelter = sheltersRepository.readById(shelter_id_active)
            if shelter:
                active_shelters_list.append(shelter)
        
        return active_shelters_list


def fetchPendingRequests(volunteer_id):
    volunteer = volunteersRepository.readById(volunteer_id)
    pending_shelters_list = []

    if volunteer:
        for shelter_id_pending in volunteer['applied_shelters']:
            shelter = sheltersRepository.readById(shelter_id_pending)
            if shelter:
                pending_shelters_list.append(shelter)
    
    return pending_shelters_list


def requestVolunteer(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)

    if shelter and volunteer:
        shelter['volunteer_requests'].append(volunteer_id)
        volunteer['applied_shelters'].append(shelter_id)

        sheltersRepository.update(shelter)
        volunteersRepository.update(volunteer)

        return True
    return False


def cancelVolunteerRequest(shelter_id, volunteer_id):
    shelter = sheltersRepository.readById(shelter_id)
    volunteer = volunteersRepository.readById(volunteer_id)
    if not shelter or not volunteer:
        return False

    new_requests_list = []
    for requests_volunteer_id in shelter['volunteer_requests']:
        if requests_volunteer_id != volunteer_id:
            new_requests_list.append(requests_volunteer_id)
    shelter['volunteer_requests'] = new_requests_list

    new_requests_list2 = []
    for requests_shelter_id in volunteer['applied_shelters']:
        if requests_shelter_id != shelter_id:
            new_requests_list2.append(requests_shelter_id)
    volunteer['applied_shelters'] = new_requests_list2

    sheltersRepository.update(shelter)
    volunteersRepository.update(volunteer)

    return True


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