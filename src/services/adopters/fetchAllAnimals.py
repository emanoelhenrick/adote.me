import src.data.animals as animalsRepository

def fetchAllAnimals():
  animals = animalsRepository.readAll()
  if animals is None:
    return []
  return animals