from app.config import database
from .repository.repository import TopicsRepository


class Service:
    def __init__(self):
        self.repository = TopicsRepository(database)



def get_service():
    svc = Service()
    return svc
