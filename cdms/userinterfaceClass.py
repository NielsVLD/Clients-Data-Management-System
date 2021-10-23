from CDMS.advisorClass import Advisor
from CDMS.helperClass import Helper
from CDMS.personCrudClass import PersonCRUD
from CDMS.databaseclass import Database


class userinterface:
    def __init__(self):
        pass

    def mainScreen(self):
        Database("analyse.db").checkMigrations()
        choice = self.choices(["Login", "Exit application"], "Which option do you want to choose?: ")
        if choice == 1:
            userinterface.loginScreen(self)
        elif choice == 2:
            Helper().stopApp()
        else:
            print("Incorrect input, try again.")
            self.mainScreen()

    def loginScreen(self):

        global loginusername, loginpassword
        choice = self.choices(["Advisor", "System Administrators", "Super Administrator"],
                              "What type of user is logging in?: ")
        _type = None
        if choice == 1:
            _type = 'Advisors'
        elif choice == 2:
            _type = 'SystemAdmins'
        elif choice == 3:
            _type = 'SuperAdmin'
        else:
            print("Incorrect input, try again.")
            self.loginScreen()
        loop = True
        count = 0
        loginusername = input("What is your username?: ")
        loginpassword = input("What is your password?: ")
        #TODO: change to superadmin and Admin!23
        while loop and loginusername != "super" and loginpassword != "123":
            loginusername = input("What is your username?: ")
            loginpassword = input("What is your password?: ")
            database = Database("analyse.db")
            try:
                data = database.get(columns='*', table=f'{_type}',
                                    where=f"`username`='{loginusername}' AND `password`='{loginpassword}'")
            except:
                print("Username or password not correct! try again")
            for row in data:
                if row[3] == loginusername and row[4] == loginpassword:
                    loop = False
                    count = 1
            if count == 0:
                print("Wrong username or password, try again.\n")
                loop = True

        if _type == "Advisors":
            self.advisorMenu()
        if _type == "SystemAdmins":
            self.systemAdministatorMenu()
        if _type == "SuperAdmin":
            self.superAdminMenu()

    def choices(self, choices, question):
        index = 0
        while index < len(choices):
            print(f"{index + 1}. {choices[index]}")
            index += 1
        c = input(question)
        if c.isnumeric():
            return int(c)
        else:
            self.choices(choices, question)

    def superAdminMenu(self):
        choice = self.choices(
            ["List of users | not ready", "Check client | partial ready", "Add client | works", "Modify client",
             "Delete client | works",
             "Add a new advisor", "Modify advisor", "Delete advisor", "reset advisor password",
             "change systemadmin password", "make a backup | not ready", "see log(s) | not ready", "Press q to logout"],
            "Wich option do you want to choose?: ")
        kind3 = "Advisors"
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD().searchPerson("Clients")
            self.systemAdministatorMenu()

        elif choice == 3:
            PersonCRUD().addPerson("Clients")
            self.systemAdministatorMenu()

        elif choice == 4:
            PersonCRUD().modifyPerson("Clients")
            self.systemAdministatorMenu()
        elif choice == 5:
            PersonCRUD().deletePerson("Clients")
            self.systemAdministatorMenu()
        elif choice == 6:
            PersonCRUD().addPerson(kind3)
            self.systemAdministatorMenu()
        elif choice == 7:
            PersonCRUD().modifyPerson(kind3)
            self.systemAdministatorMenu()
        elif choice == 8:
            PersonCRUD().deletePerson(kind3)
            self.systemAdministatorMenu()
        elif choice == 9:
            clientUsername = input("What is the username of the client you want to reset the password for? ")
            Advisor.changePassword(self, clientUsername)
            self.systemAdministatorMenu()
        elif choice == 10:
            Advisor.changePassword(self, loginusername)
            self.systemAdministatorMenu()
        elif choice == 11:
            pass
        elif choice == 12:
            pass
        elif choice == 13:
            userinterface().mainScreen()

        else:
            print("Wrong input, try again.")
            self.systemAdministatorMenu()

    def systemAdministatorMenu(self):
        choice = self.choices(
            ["List of users | not ready", "Check client", "Add client", "Modify client", "Delete client",
             "Add a new advisor", "Modify advisor", "Delete advisor", "reset advisor password",
             "change systemadmin password", "make a backup | not ready", "see log(s) | not ready", "Press q to logout"],
            "Wich option do you want to choose?: ")
        kind = "SystemAdmins"
        kind2 = "client"
        kind3 = "Advisors"
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD.searchPerson(self, kind2)
        elif choice == 3:
            PersonCRUD.addPerson(self, kind)
        elif choice == 4:
            PersonCRUD.modifyPerson(self, kind2)
        elif choice == 5:
            PersonCRUD.deletePerson(self, kind2)
        elif choice == 6:
            PersonCRUD.addPerson(self, kind3)
        elif choice == 7:
            PersonCRUD.modifyPerson(self, kind3)
        elif choice == 8:
            PersonCRUD.deletePerson(self, kind3)
        elif choice == 9:
            clientUsername = input("What is the username of the client you want to reset the password for? ")
            Advisor.changePassword(self, clientUsername)
        elif choice == 10:
            Advisor.changePassword(self, loginusername)
        elif choice == 11:
            Helper().makeBackup()
        elif choice == 12:
            pass
        elif choice == 13:
            userinterface().mainScreen()
        else:
            print("\nWrong input, try again.\n")
            self.systemAdministatorMenu()

    def advisorMenu(self):
        choice = self.choices(["Add new client", "Modify Client", "Search client", "Update advisor password"],
                              "\nWhich option do you want to choose?: ")
        kind = "client"
        if choice == 1:
            PersonCRUD.addPerson(self, kind)
            self.advisorMenu()
        elif choice == 2:
            PersonCRUD.modifyPerson(self, kind)
            self.advisorMenu()
        elif choice == 3:
            PersonCRUD.searchPerson(self, kind)
            self.advisorMenu()
        elif choice == 4:
            Advisor.changePassword(self, loginusername)
            self.advisorMenu()
        else:
            print("Incorrect input, try again.")
            self.clientMenu()
