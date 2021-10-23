
from CDMS.helperClass import Helper
from CDMS.personCrudClass import PersonCRUD
from CDMS.databaseclass import Database


class Advisor():

    def __init__(self):
        super().__init__()

    def changePassword(self, username):
        while True:
            database = Database("analyse.db")
            _password = input("What will be ur password? Min length of 5, max length of 20, MUST start with a letter: ")
            _checkPW = Helper().usernameChecker(_password)
            if _checkPW == 0:
                database.query(f"UPDATE Advisors SET password = '{_password}' WHERE username = '{username}';")
                database.commit()
                database.close()
                break
            else:
                print("Password not in the required criteria, try again.")

    # To update their own password

    def addClient(self):
        from CDMS.clientClass import Client
        Client.newClient(self)

    # To add a new client to the system

    def modifyClient(self):
        PersonCRUD.modifyPerson()

    # To modify or update the information of a client in the system

    def searchClient(self):
        pass
    # To search and retrieve the information of a client
