
from classes import databaseclass as sqlClass

class userinterface:
    def __init__(self):
        pass

    def mainScreen(self):

        choice = self.choices(["Login", "Exit application"], "Wich option do you want to choose?: ")
        if choice == 1:
            userinterface.loginScreen(self)
        if choice == 2:
            return

    def loginScreen(self):
        choice = self.choices(["Advisor", "System Administrators", "Super Administrator"], "What type of user is logging in?: " )
        _type = None
        if choice == 1:
            _type = "Advisors"
        elif choice == 2:
            _type = "SystemAdmins"
        elif choice == 3:
            _type = "SuperAdmins"
        else:
            self.loginScreen()

        _username = input("What is your username?: ")
        _password = input("What is your password?: ")
        database = sqlClass.Database("analyse.db")
        data = database.get(columns='*', table=f'{_type}', where=f"`username`='{_username}' AND `password`='{_password}'")
        print(data)
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
        choice = self.choices(["Check advisor", "Add advisor", "Modify advisor", "Delete advisor"], "Wich option do you want to choose?: ")
        kind = "Advisors"
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

    def addPerson(self, kind):
        if kind == "advisor" or kind == "System administrator" :

            database = sqlClass.Database("analyse.db")
            firstname = input("firstname?: ")
            lastname = input("lastname?: ")
            password = input("password?: ")
            database.write(f'{kind}', '`firstname`, `lastname`, `username`, `password`', f"'{firstname}', '{lastname}', '{firstname + lastname}', '{password}'")
            database.commit()
            database.close()

        elif kind == "client":
            pass
            # 'firstname'  'lastname'  'streetname' 'housenumber' 'zipcode', 'city'  'emailaddress' 'mobilephone'

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
        pass
