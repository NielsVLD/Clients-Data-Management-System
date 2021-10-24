from cdms.advisorClass import Advisor
from cdms.helperClass import Helper
from cdms.personCrudClass import PersonCRUD
from cdms.databaseclass import Database


class userinterface:
    def __init__(self):
        pass

    def mainScreen(self):
        database = Database("analyse.db")
        database.checkMigrations()
        database.close()
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
        loginusername = ""
        loginpassword = ""
        #TODO: change to superadmin and Admin!23
        while loop and loginusername != "super" and loginpassword != "123":

            loginusername = input("What is your username?: ")
            loginpassword = input("What is your password?: ")
            loginusername = Helper().Encrypt(loginusername)
            loginpassword = Helper().Encrypt(loginpassword)
            database = Database("analyse.db")
            print(loginusername, loginpassword)
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
        Helper().logUsername(loginusername)
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
            ["List of users | not ready", "Check client | works", "Add client | works", "Modify client | works",
             "Delete client | works",
             "Add a new advisor | Works", "Modify advisor | Works", "Delete advisor | works", "reset advisor password",
             "change systemadmin password", "make a backup | works", "see log(s) | not ready", "Logout | works"],
            "Wich option do you want to choose?: ")
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD().searchPerson("Clients")
            self.superAdminMenu()

        elif choice == 3:
            PersonCRUD().addPerson("Clients")
            self.superAdminMenu()

        elif choice == 4:
            PersonCRUD().modifyPerson("Clients")
            self.superAdminMenu()
        elif choice == 5:
            PersonCRUD().deletePerson("Clients")
            self.superAdminMenu()
        elif choice == 6:
            PersonCRUD().addPerson("Advisors")
            self.superAdminMenu()
        elif choice == 7:
            PersonCRUD().modifyPerson("Advisors")
            self.superAdminMenu()
        elif choice == 8:
            PersonCRUD().deletePerson("Advisors")
            self.superAdminMenu()
        elif choice == 9:
            PersonCRUD().changePassword("Advisors")
            self.superAdminMenu()
        elif choice == 10:
            PersonCRUD().changePassword("SystemAdmins")
            self.superAdminMenu()
        elif choice == 11:
            Helper().makeBackup()
        elif choice == 12:
            pass
        elif choice == 13:
            userinterface().mainScreen()
        else:
            print("Wrong input, try again.")
            self.superAdminMenu()

    def systemAdministatorMenu(self):
        choice = self.choices(
            ["List of users | not ready", "Check client | works", "Add client | works", "Modify client | works",
             "Delete client | works",
             "Add a new advisor | Works", "Modify advisor | Works", "Delete advisor | works", "reset advisor password",
             "change systemadmin password", "make a backup | works", "see log(s) | not ready", "Logout | works"],
            "Wich option do you want to choose?: ")
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD().searchPerson("Clients")
            self.superAdminMenu()

        elif choice == 3:
            PersonCRUD().addPerson("Clients")
            self.superAdminMenu()

        elif choice == 4:
            PersonCRUD().modifyPerson("Clients")
            self.superAdminMenu()
        elif choice == 5:
            PersonCRUD().deletePerson("Clients")
            self.superAdminMenu()
        elif choice == 6:
            PersonCRUD().addPerson("Advisors")
            self.superAdminMenu()
        elif choice == 7:
            PersonCRUD().modifyPerson("Advisors")
            self.superAdminMenu()
        elif choice == 8:
            PersonCRUD().deletePerson("Advisors")
            self.superAdminMenu()
        elif choice == 9:
            PersonCRUD().changePassword("Advisors")
            self.superAdminMenu()
        elif choice == 10:
            PersonCRUD().changePassword("SystemAdmins")
            self.superAdminMenu()
        elif choice == 11:
            Helper().makeBackup()
        elif choice == 12:
            pass
        elif choice == 13:
            userinterface().mainScreen()
        else:
            print("Wrong input, try again.")
            self.systemAdministatorMenu()

    def advisorMenu(self):
        choice = self.choices(
            ["List of users | not ready", "Check client | works", "Add client | works", "Modify client | works",
             "Delete client | works",
             "Add a new advisor | Works", "Modify advisor | Works", "Delete advisor | works", "reset advisor password",
             "change systemadmin password", "make a backup | works", "see log(s) | not ready", "Logout | works"],
            "Wich option do you want to choose?: ")
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD().searchPerson("Clients")
            self.superAdminMenu()

        elif choice == 3:
            PersonCRUD().addPerson("Clients")
            self.superAdminMenu()

        elif choice == 4:
            PersonCRUD().modifyPerson("Clients")
            self.superAdminMenu()
        elif choice == 5:
            PersonCRUD().deletePerson("Clients")
            self.superAdminMenu()
        elif choice == 6:
            PersonCRUD().addPerson("Advisors")
            self.superAdminMenu()
        elif choice == 7:
            PersonCRUD().modifyPerson("Advisors")
            self.superAdminMenu()
        elif choice == 8:
            PersonCRUD().deletePerson("Advisors")
            self.superAdminMenu()
        elif choice == 9:
            PersonCRUD().changePassword("Advisors")
            self.superAdminMenu()
        elif choice == 10:
            PersonCRUD().changePassword("SystemAdmins")
            self.superAdminMenu()
        elif choice == 11:
            Helper().makeBackup()
        elif choice == 12:
            Helper().checkLogs()
        elif choice == 13:
            userinterface().mainScreen()
        else:
            print("Wrong input, try again.")
            self.advisorMenu()
