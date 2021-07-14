# CDMS: V2
# Bart Westhoff (0991807) 
# Niels Krommenhoek

import re
import sqlite3
from classes import databaseclass as sqlClass

Loginusername = ""
Loginpassword = ""
def stopApp():
    quit()

class userinterface:
    def __init__(self):
        pass

    def mainScreen(self):
        while True:
            choice = self.choices(["Login", "Exit application"], "Which option do you want to choose?: ")
            if choice == 1:
                userinterface.loginScreen(self)
            if choice == 2:
                stopApp()
            else:
                print("Incorrect input, try again.")
                continue


    def loginScreen(self):
        
        global Loginpassword, Loginusername
        choice = self.choices(["Advisor", "System Administrators", "Super Administrator"], "What type of user is logging in?: " )
        _type = None
        if choice == 1:
            _type = "Advisors"
        elif choice == 2:
            _type = "SystemAdmins"
        elif choice == 3:
            _type = "SuperAdmin"
        else:
            print("Incorrect input, try again.")
            self.loginScreen()

        Loginusername = input("What is your username?: ")
        Loginpassword = input("What is your password?: ")
        database = sqlClass.Database("analyse.db")
        try: data = database.get(columns='*', table=f'{_type}', where=f"`username`='{Loginusername}' AND `password`='{Loginpassword}'")
        except: print("Username or password not correct! try again")
        #print(data)
        if _type == "Advisors":
            self.advisorMenu()
        if _type == "SystemAdmins":
            self.systemAdministatorMenu()
        else:
            print("Not yet SuperAdmin screen implemented")
            self.systemAdministatorMenu()

    def choices(self, choices, question):
        index =0
        while index < len(choices):
            print(f"{index+1}. {choices[index]}")
            index+=1
        c = input(question)
        if c.isnumeric():
            return int(c)
        else:
            self.choices(choices, question)

    def clientMenu(self):
        choice = self.choices(["Check client", "Add client", "Modify client", "Delete client"], "Wich option do you want to choose?: ")
        kind = "Clients"
        if choice == 1:
            self.searchPerson(kind)
        elif choice == 2:
            self.addPerson(kind)
        elif choice == 3:
            self.modifyPerson(kind)
        elif choice == 4:
            self.deletePerson(kind)
        else:
            self.clientMenu()

    def systemAdministatorMenu(self):
        choice = self.choices(["Check System administrator", "Add System administrator", "Modify System administrator", "Delete System administrator"], "Wich option do you want to choose?: ")
        kind = "SystemAdmins"
        if choice == 1:
            self.searchPerson(kind)
        elif choice == 2:
            self.addPerson(kind)
        elif choice == 3:
            self.modifyPerson(kind)
        elif choice == 4:
            self.deletePerson(kind)
        else:
            self.systemAdministatorMenu()

    def advisorMenu(self):
        choice = self.choices(["Add new client", "Modify Client", "Search client", "Update advisor password"], "Wich option do you want to choose?: ")
        kind = "client"
        if choice == 1:
            PersonCRUD.addPerson(self,kind)
        elif choice == 2:
            PersonCRUD.modifyPerson(self,kind)
        elif choice == 3:
            PersonCRUD.searchPerson(self,kind)
        elif choice == 4:
            Advisor.changePassword(self, Loginusername)
        else:
            print("Incorrect input, try again.")
            self.clientMenu()


class Client():
    def __init__(self, firstname, lastname, mail, street,housenumber,zipcode,city,mobile_number):
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.street = street
        self.housenumber = housenumber
        self.zipcode = zipcode
        self.city = city
        self.mobile_number = mobile_number

def newClient():
    firstname = input("What is your Firstname?: ")
    lastname = input("What is your Lastname?: ")
    print(lastname)
    mail = input("What is the email?: ")
    _validEmail = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail)
    if _validEmail:
        print("Pass")
    street = input("streetname?: ")
    if street.isalpha():
        print("pass")
    housenumber = input("house number?: ")
    if housenumber.isnumeric():
        print("pass")
    zipcode = input("zipcode?: ").upper()
    if zipcode[0:3].isnumeric() and zipcode[4:5].isalpha() and len(zipcode) ==6:
        print("pass")
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
    return Client(firstname, lastname,mail,street,housenumber,zipcode,city,mobile_number)


class Advisor():
    
    def __init__(self):
        super().__init__()

    def changePassword(self, username):
        database = sqlClass.Database("analyse.db")
        _password = input("What will be ur password?: ")
        _checkPW = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", _password)
        if _checkPW:
            print("good")
        else:
            print("bad")
        print(Loginpassword)
        print(Loginusername)
        print(username)
        database.query(f"UPDATE Advisors SET password = '{_password}' WHERE username = '{Loginusername}';")
        database.commit()
        database.close()

    #To update their own password


    def addClient(self):
        Client.newClient(self)
    # To add a new client to the system

    def modifyClient(self):
        PersonCRUD.modifyPerson()
    # To modify or update the information of a client in the system

    def searchClient(self):
        pass
    # To search and retrieve the information of a client

class PersonCRUD():

    def addPerson(self, kind):
        database = sqlClass.Database("analyse.db")
        if kind == "advisor" or kind == "System administrator" :
            firstname = input("firstname?: ")
            lastname = input("lastname?: ")
            username = input("username?:")
            password = input("password?: ")
            database.write(f'{kind}', '`firstname`, `lastname`, `username`, `password`', f"'{firstname}', '{lastname}', '{username}', '{password}'")

        elif kind == "client":
            client = newClient()
            database.write(f'Clients', '`firstname`, `lastname`, `streetname`, `housenumber`, `zipcode`, `city`, `emailaddress`, `mobilephone`', f"'{client.firstname}', '{client.lastname}', '{client.street}', '{client.housenumber}', '{client.zipcode}', '{client.city}', '{client.mail}', '{client.mobile_number}'")
            # 'firstname'   'lastname'  'streetname' 'housenumber' 'zipcode', 'city'  'emailaddress' 'mobilephone'
        database.commit()
        database.close()

    def searchPerson(self, kind):
        database = sqlClass.Database("analyse.db")
        firstname = input("firstname?: ")
        lastname = input("lastname?: ")
        try:
            data= database.get(columns='*', table=f'{kind}', where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
            print(data)
        except: print("Error getting person")

        database.commit()
        database.close()

    def deletePerson(self, kind):
        database = sqlClass.Database("analyse.db")
        firstname = input("firstname?: ")
        lastname = input("lastname?: ")
        try:
           # database.query(f"DELETE FROM 'SystemAdmins' WHERE 'firstname'='{firstname}' AND 'lastname'='{lastname}'")
            database.query(f"DELETE FROM '{kind}' WHERE firstname='{firstname}' AND lastname='{lastname}'")
            database.commit()
            print("Deleted")

        except: print("not deleted")
        data= database.get(columns='*', table=f'{kind}', where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
        print(data)
        database.close()

    def modifyPerson(self, kind):
        if kind == "Client":
            _firstname= input("What is the firstname of the Client?: ")
            _lastname = input("What is the lastname of the Client?: ")

            choices = ["Modify firstname", "Modify lastname", "Modify streetname", "Modify housenumber", "Next Page"]
            choice = self.choices(choices, "Wich option do you want to choose?: ")
            to_change = input(f"What will be the new {choices[choice].split(' ')[1]}")
            if choice == 1:
               pass
            if choice == 2:
                pass
            if choice == 3:
                pass
            if choice == 4:
                pass
            if choice == 5:
                # 'firstname'  'lastname'  'streetname' 'housenumber' 'zipcode', 'city'  'emailaddress' 'mobilephone'
                choices_p2 = ["Modify zipcode", "Modify city", "Modify emailaddress", "Modify phone_number", "Previous Page"]
                choice = self.choices(choices_p2, "Wich option do you want to choose?: ")

                to_change = input(f"What will be the new {choices[choice].split(' ')[1]}")
                if choice == 1:
                   pass
                if choice == 2:
                    pass
                if choice == 3:
                    pass
                if choice == 4:
                    pass
                if choice == 5:
                    self.modifyPerson(kind)




















userinterface().mainScreen()