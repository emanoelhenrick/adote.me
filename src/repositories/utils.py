import os

DB_PATH = os.path.join(os.path.dirname(__file__), "json")

def getJsonPath(entity):
    return os.path.join(DB_PATH, f"{entity}.json")