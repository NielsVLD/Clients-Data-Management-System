# hello everyone
# Bart Westhoff (0991807) 
# Niels Krommenhoek
import re

def newUsername():
    _username = input("What will be ur username?: ").lower()
    _firstLetter = _username[0].isalpha()
    _checkUser = re.search("[a-z0-9_'.]{5,20}", _username)
    if _username and _firstLetter:
        print("good")
    else:
        print("bad")
    return _username

def newPassword():

    _password = input("What will be ur password?: ")
    _checkPW = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", _password)
    if _checkPW:
        print("good")
    else:
        print("bad")
    return  _password

def register():
    username = newUsername()
    password = newPassword()


def newClient():
    # mail = input("What is the email?: ")
    # _validEmail = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail)
    # if _validEmail:
    #     print("Pass")
    # street = input("streetname?: ")
    # if street.isalpha():
    #     print("pass")
    # housenumber = input("house number?: ")
    # if housenumber.isnumeric():
    #     print("pass")
    # zipcode = input("zipcode?: ").upper()
    # if zipcode[0:3].isnumeric() and zipcode[4:5].isalpha() and len(zipcode) ==6:
    #     print("pass")
    listOfCities = ["Rotterdam", "Amsterdam", "Alkmaar", "Maastricht", "Utrecht", "Almere", "Lelystad", "Maassluis", "Vlaardingen", "Schiedam"]
    index =1
    while index <= len(listOfCities):
        print(f"{index}. {listOfCities[index-1]}")
        index +=1
    city = listOfCities[(int(input("In wich city do you live (choose from 1-10)")))-1]
    print(city)
    mobile_number = input("What is your mobile number?:\n31-6-")
    if mobile_number.isnumeric() and len(mobile_number) == 8:
        print("pass")
    mobile_number = "31-6-" + mobile_number
    print(mobile_number)
# newClient()

class User():

    def __init__(self):
        self.username = newUsername()
        self.pw = newPassword()

class Advisor(User):
    def __init__(self):
        super().__init__()

    def changePassword(self):
        pass
    #To update their own password

    def addClient(self):
        pass
    # To add a new client to the system

    def modifyClient(self):
        pass
    # To modify or update the information of a client in the system

    def searchClient(self):
        pass
    # To search and retrieve the information of a client

class SystemAdmin(Advisor):
    def __init__(self):
        super().__init__()

    def changePassword(self):
        pass
    #To update their own password

    def checkUsers(self):
        # To check the list of users and their roles
        pass

    def addAdvisor(self):
        pass
        # To define and add a new advisor to the system

    def modifyAdvisor(self):
        pass
    # To modify or update an existing advisor’s account and profile

    def deleteAdvisor(self):
        pass
    #To delete an existing advisor’s account

    def resetAdvisorPassword(self):
        pass
    #To reset an existing advisor’s password (a temporary password)

    def makeBackup(self):
        pass
    # To make a backup of the system (clients information and users’ data)
    def seeLogs(self):
        pass
    # To see the logs file of the system

    def deleteClient(self):
        pass
    # To delete a client's record from the database (note that an advisor can not delete a record, but can only modify or update a client’s information)

## Superadmin intherit allebei omdat systemadmin en adivsor verschillen in inheritance
class SuperAdmin(SystemAdmin, Advisor):
    ## Error overleggen/ laten staan
    def __init__(self):
        self.username = "superadmin"
        self.password = 'Admin!23'

    def AddAdmin(self):
        pass
        #To define and add a new admin to the system
    def modifyAdmin(self):
        pass
    # To modify or update an existing admin’s account and profile
    def deleteAdmin(self):
        pass
    # To delete an existing admin’s account
    def resetAdminPassword(self):
        pass
    # To reset an existing admin’s password (a temporary password)







p1 = SuperAdmin()
