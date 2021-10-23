
from cdms.helperClass import Helper
from cdms.personCrudClass import PersonCRUD
from cdms.databaseclass import Database


class Advisor():

    def __init__(self):
        super().__init__()

    def changePassword(self):
        while True:
            database = Database("analyse.db")

            #_checkPW = Helper().usernameChecker(_password)
            # TODO: niels even kijken
        #    if _checkPW == 0:
            username = input("For extra security please fill in your username:\n")
            username = Helper().Encrypt(username)
            _password = input("For extra security please fill in your password:\n")

            #TODO Niels check if match
            _password = input("What will be ur password? Min length of 5, max length of 20, MUST start with a letter: ")
            _password = Helper().Encrypt(_password)
            database.query(f"UPDATE Advisors SET password = '{_password}' WHERE username = '{username}';")
            database.commit()
            database.close()
            break
            #     break
            # else:
            #     print("Password not in the required criteria, try again.")

    # To update their own password

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
