
from cdms.personCrudClass import PersonCRUD


class Advisor:

    def __init__(self):
        super().__init__()

    def addClient(self):
        from cdms.clientClass import Client
        Client().newClient()

    # To add a new client to the system

    def modifyClient(self):
        PersonCRUD().modifyPerson("Clients")

    # To modify or update the information of a client in the system

    def searchClient(self):
        PersonCRUD().searchPerson("Clients")
    # To search and retrieve the information of a client
