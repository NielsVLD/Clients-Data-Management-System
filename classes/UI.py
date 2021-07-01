
from classes import databaseclass as sqlClass

class userinterface:
    def __init__(self):
        pass

    def mainScreen(self):

        print("1. Login")
        print("2. Exit application")
        choice =  input("Wich option do you want to choose?: ")
        if choice == "1":
            userinterface.loginScreen(self)
        if choice == "2":
            return
    def loginScreen(self):
        print("1. Advisor\n2. System Administrators\n3. Super Administrator")
        self.choices(["Advisor", "System Administrators", "Super Administrator"])
        _type = input("What type of user is logging in?: ")
        if _type == "1":
            _type = "Advisors"
        elif _type == "2":
            _type = "SystemAdmins"
        elif _type == "3":
            _type = "SuperAdmins"
        else:
            ## again
            pass
        _username = input("What is your username?: ")
        _password = input("What is your password?: ")
        database = sqlClass.Database("analyse.db")
        data = database.get(columns='*', table=f'{_type}', where=f"`username`='{_username}' AND `password`='{_password}'")
        print(data)


    def choices(self, choices):
        index =0
        while index < len(choices):
            print(f"{index+1}. {choices[index]}")
            index+=1
        c = input("What is your choice?: ")
        if c.isnumeric():
            return choices[int(c)-1]
        else:
            self.choices(choices)
