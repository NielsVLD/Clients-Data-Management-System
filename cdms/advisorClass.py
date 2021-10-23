
from cdms.helperClass import Helper
from cdms.personCrudClass import PersonCRUD
from cdms.databaseclass import Database


class Advisor():

    def __init__(self):
        super().__init__()

    def addClient(self):
        from cdms.clientClass import Client
        Client.newClient(self)

    # To add a new client to the system

    def modifyClient(self):
        PersonCRUD.modifyPerson()

    # To modify or update the information of a client in the system

    def searchClient(self):
        pass
    # To search and retrieve the information of a client
