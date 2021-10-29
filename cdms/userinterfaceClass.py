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
        while loop and loginusername != "super" and loginpassword != "123":
 
            loginusername = input("What is your username?: ")
            loginpassword = input("What is your password?: ")
            loginusername = Helper().Encrypt(loginusername)
            loginpassword = Helper().Encrypt(loginpassword)
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
            ["List of users", "Check client", "Add client", "Modify client",
             "Delete client",
             "Add a new advisor", "Modify advisor", "Delete advisor", "Add new systemadmin",
             "change passwords", "make a backup", "see log(s)", "Logout"],
            "Wich option do you want to choose?: ")
        if choice == 1:
            PersonCRUD().checkUsers("Clients")
            self.superAdminMenu()
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
            PersonCRUD().addPerson("SystemAdmins")
            self.superAdminMenu()
        elif choice == 10:
            PersonCRUD().changePassword("SuperAdmin")
            self.superAdminMenu()
        elif choice == 11:
            Helper().makeBackup()
        elif choice == 12:
            print("see logs init")
            Helper().seelogs()
            self.superAdminMenu()
        elif choice == 13:
            userinterface().mainScreen()
        else:
            print("Wrong input, try again.")
            self.superAdminMenu()
 
    def systemAdministatorMenu(self):
        choice = self.choices(
            ["List of users", "Check client", "Add client", "Modify client",
             "Delete client",
             "Add a new advisor", "Modify advisor", "Delete advisor",
             "Change passwords", "make a backup", "see log(s)", "Logout"],
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
            PersonCRUD().changePassword("SystemAdmins")
            self.superAdminMenu()
        elif choice == 10:
            Helper().makeBackup()
        elif choice == 11:
            Helper().seelogs()
            self.superAdminMenu()
        elif choice == 12:
            userinterface().mainScreen()
        else:
            print("Wrong input, try again.")
            self.systemAdministatorMenu()
 
    def advisorMenu(self):
        choice = self.choices(
            ["Add client | works", "Modify client", "Search client",
             "Reset your password",
            "Logout"],
            "Wich option do you want to choose?: ")
        if choice == 1:
            PersonCRUD().addPerson("Clients")
            self.advisorMenu()
        elif choice == 2:
            PersonCRUD.modifyPerson("Clients")
            self.advisorMenu()
        elif choice == 3:
            PersonCRUD().searchPerson("Clients")
            self.advisorMenu()
        elif choice == 4:
            PersonCRUD().changePassword("Advisors")
            self.advisorMenu()
        elif choice == 5:
            self.loginScreen()
        else:
            print("Wrong input, try again.")
            self.advisorMenu()