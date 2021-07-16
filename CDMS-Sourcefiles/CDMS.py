# CDMS: V2
# Bart Westhoff (0991807) 
# Niels Krommenhoek

import re
import sqlite3
import io
import databaseclass as sqlClass

Loginusername = ""
Loginpassword = ""
def stopApp():
    quit()

class userinterface:
    def __init__(self):
        pass

    def mainScreen(self):
            choice = self.choices(["Login", "Exit application"], "Which option do you want to choose?: ")
            if choice == 1:
                userinterface.loginScreen(self)
            if choice == 2:
                stopApp()
            else:
                print("Incorrect input, try again.")
                self.mainScreen()


    def loginScreen(self):
        
        global Loginpassword, Loginusername
        choice = self.choices(["Advisor", "System Administrators", "Super Administrator"], "What type of user is logging in?: " )
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
        while loop:
            Loginusername = input("What is your username?: ")
            Loginpassword = input("What is your password?: ")
            database = sqlClass.Database("analyse.db")
            try: data = database.get(columns='*', table=f'{_type}', where=f"`username`='{Loginusername}' AND `password`='{Loginpassword}'")
            except: print("Username or password not correct! try again")
            for row in data:
                if row[3] == Loginusername and row[4] == Loginpassword:
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
        index =0
        while index < len(choices):
            print(f"{index+1}. {choices[index]}")
            index+=1
        c = input(question)
        if c.isnumeric():
            return int(c)
        else:
            self.choices(choices, question)

    def superAdminMenu(self):
        choice = self.choices(["List of users | not ready","Check client", "Add client", "Modify client", "Delete client","Add a new advisor", "Modify advisor", "Delete advisor", "reset advisor password","change systemadmin password","make a backup | not ready","see log(s) | not ready","Press q to logout"], "Wich option do you want to choose?: ")
        kind = "SystemAdmins"
        kind2 = "client"
        kind3 = "Advisors"
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD.searchPerson(self,kind2)
            self.systemAdministatorMenu()
        elif choice == 3:
            PersonCRUD.addPerson(self,kind2)
            self.systemAdministatorMenu()
        elif choice == 4:
            PersonCRUD.modifyPerson(self,kind2)
            self.systemAdministatorMenu()
        elif choice == 5:
            PersonCRUD.deletePerson(self,kind2)
            self.systemAdministatorMenu()
        elif choice == 6:
            PersonCRUD.addPerson(self,kind3)
            self.systemAdministatorMenu()
        elif choice == 7:
            PersonCRUD.modifyPerson(self,kind3)
            self.systemAdministatorMenu()
        elif choice == 8:
            PersonCRUD.deletePerson(self,kind3)
            self.systemAdministatorMenu()
        elif choice == 9:
            clientUsername = input("What is the username of the client you want to reset the password for? ")
            Advisor.changePassword(self,clientUsername)
            self.systemAdministatorMenu()
        elif choice == 10:
            Advisor.changePassword(self,Loginusername)
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
        choice = self.choices(["List of users | not ready","Check client", "Add client", "Modify client", "Delete client","Add a new advisor", "Modify advisor", "Delete advisor", "reset advisor password","change systemadmin password","make a backup | not ready","see log(s) | not ready","Press q to logout"], "Wich option do you want to choose?: ")
        kind = "SystemAdmins"
        kind2 = "client"
        kind3 = "Advisors"
        if choice == 1:
            pass
        elif choice == 2:
            PersonCRUD.searchPerson(self,kind2)
        elif choice == 3:
            PersonCRUD.addPerson(self,kind)
        elif choice == 4:
            PersonCRUD.modifyPerson(self,kind2)
        elif choice == 5:
            PersonCRUD.deletePerson(self,kind2)
        elif choice == 6:
            PersonCRUD.addPerson(self,kind3)
        elif choice == 7:
            PersonCRUD.modifyPerson(self,kind3)
        elif choice == 8:
            PersonCRUD.deletePerson(self,kind3)
        elif choice == 9:
            clientUsername = input("What is the username of the client you want to reset the password for? ")
            Advisor.changePassword(self,clientUsername)
        elif choice == 10:
            Advisor.changePassword(self,Loginusername)
        elif choice == 11:
            makeBackup()
        elif choice == 12:
            pass
        elif choice == 13:
            userinterface().mainScreen()
        else:
            print("\nWrong input, try again.\n")
            self.systemAdministatorMenu()


    def advisorMenu(self):
        choice = self.choices(["Add new client", "Modify Client", "Search client", "Update advisor password"], "\nWhich option do you want to choose?: ")
        kind = "client"
        if choice == 1:
            PersonCRUD.addPerson(self,kind)
            self.advisorMenu()
        elif choice == 2:
            PersonCRUD.modifyPerson(self,kind)
            self.advisorMenu()
        elif choice == 3:
            PersonCRUD.searchPerson(self,kind)
            self.advisorMenu()
        elif choice == 4:
            Advisor.changePassword(self, Loginusername)
            self.advisorMenu()
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
    firstname = Encrypt(firstname)
    lastname = input("What is your Lastname?: ")
    lastname = Encrypt(lastname)
    mail = input("What is the email?: ")
    _validEmail = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail)
    if _validEmail:
        print("Pass")
        mail = Encrypt(mail)
    street = input("streetname?: ")
    if street.isalpha():
        print("pass")
        street = Encrypt(street)
    housenumber = input("house number?: ")
    if housenumber.isnumeric():
        print("pass")
        housenumber = Encrypt(housenumber)
    zipcode = input("zipcode?: ").upper()
    if zipcode[0:3].isnumeric() and zipcode[4:5].isalpha() and len(zipcode) ==6:
        print("pass")
        zipcode = Encrypt(zipcode)
    listOfCities = ["Rotterdam", "Amsterdam", "Alkmaar", "Maastricht", "Utrecht", "Almere", "Lelystad", "Maassluis", "Vlaardingen", "Schiedam"]
    index =1
    while index <= len(listOfCities):
        print(f"{index}. {listOfCities[index-1]}")
        index +=1
    city = listOfCities[(int(input("In wich city do you live (choose from 1-10)")))-1]
    print(city)
    city = Encrypt(city)
    mobile_number = input("What is your mobile number?:\n31-6-")
    if mobile_number.isnumeric() and len(mobile_number) == 8:
        print("pass")
    mobile_number = "31-6-" + mobile_number
    print(mobile_number)
    mobile_number = Encrypt(mobile_number)
    return Client(firstname, lastname,mail,street,housenumber,zipcode,city,mobile_number)


class Advisor():
    
    def __init__(self):
        super().__init__()

    def changePassword(self, username):
        while True:
            database = sqlClass.Database("analyse.db")
            _password = input("What will be ur password? Min length of 5, max length of 20, MUST start with a letter: ")
            _checkPW = usernameChecker(_password)
            if _checkPW == 0:
                database.query(f"UPDATE Advisors SET password = '{_password}' WHERE username = '{username}';")
                database.commit()
                database.close()
                break
            else:
                print("Password not in the required criteria, try again.")
                

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
        if kind == "Advisors" or kind == "SystemAdmins" :
            firstname = input("firstname?: ")
            firstname = Encrypt(firstname)
            lastname = input("lastname?: ")
            lastname = Encrypt(lastname)
            username = input("username?:")
            username = Encrypt(username)
            password = input("password?: ")
            password = Encrypt(password)
            database.write(f'{kind}', '`firstname`, `lastname`, `username`, `password`', f"'{firstname}', '{lastname}', '{username}', '{password}'")

        elif kind == "client":
            client = newClient()
            database.write(f'Clients', '`firstname`, `lastname`, `streetname`, `housenumber`, `zipcode`, `city`, `emailaddress`, `mobilephone`', f"'{client.firstname}', '{client.lastname}', '{client.street}', '{client.housenumber}', '{client.zipcode}', '{client.city}', '{client.mail}', '{client.mobile_number}'")
            # 'firstname'   'lastname'  'streetname' 'housenumber' 'zipcode', 'city'  'emailaddress' 'mobilephone'
        database.commit()
        database.close()

    def searchPerson(self, kind):
        loop = True
        count = 0
        while loop:
            database = sqlClass.Database("analyse.db")
            firstname = input("firstname?: ")
            firstname = Encrypt(firstname)
            
            lastname = input("lastname?: ")
            lastname = Encrypt(lastname)
            try:
                data = database.get(columns='*', table=f'Clients', where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
                database.commit()
                for row in data:
                    if row[1] != firstname and row[2] != lastname:
                        print("Client not found, try again.")
                        print(row[1],row[2])
                        #self.searchPerson(self)

                # values = ["ID: ", "Firstname: ","Lastname: ","Streetname: ","Housenumber: ", "Zipcode: ","City: ","Email: ", "Mobilephone: " ]
                # i = 0
                # while i < 9:
                #     #print(values[i])
                #     print(data[0])
                #     i += 1
                print("Client found!:\n")
                for row in data:
                    print("ID          |",row[0])
                    print("Firstname   |",Decrypt(row[1]))
                    print("Lastname    |",Decrypt(row[2]))
                    print("Streetname  |",Decrypt(row[3]))
                    print("Housenumber |",Decrypt(row[4]))
                    print("Zipcode     |",Decrypt(row[5]))
                    print("City        |",Decrypt(row[6]))
                    print("Email       |",Decrypt(row[7]))
                    print("Mobilephone |",Decrypt(row[8]),"\n")
                    loop = False

            except: print("Person not found, try again. excpet")

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
        database = sqlClass.Database("analyse.db")
        if kind == "client":
            _firstname= input("What is the firstname of the Client?: ")
            _lastname = input("What is the lastname of the Client?: ")
            data = database.get(columns='*', table=f'Clients', where=f"`firstname`='{_firstname}' AND `lastname`='{_lastname}'")
            for row in data:
                if row[1] != _firstname and row[2] != _lastname:
                    print("Client not found, try again.")
                    PersonCRUD.modifyPerson(self,kind)

            choices = ["Modify firstname", "Modify lastname", "Modify streetname", "Modify housenumber", "Next Page"]
            #choice = self.choices(["List of users | not ready","Check client", "Add client", "Modify client", "Delete client","Add a new advisor", "Modify advisor", "Delete advisor", "reset advisor password","change systemadmin password","make a backup | not ready","see log(s) | not ready","Press q to logout"], "Wich option do you want to choose?: ")
            choice = self.choices(choices, "Wich option do you want to choose?: ")

            if choice == 1:
                newfirstname = input("What will be the new firstname? ")
                if nameChecker(newfirstname) == True:
                    newfirstname = Encrypt(newfirstname)
                    database.query(f"UPDATE Clients SET firstname = '{newfirstname}' WHERE firstname = '{_firstname}' AND lastname = '{_lastname}';")
                    database.commit()
                    database.close()
                else:
                    print("Invalid name, try again.")
                    PersonCRUD.modifyPerson(self,kind)
            if choice == 2:
                pass
            if choice == 3:
                pass
            if choice == 4:
                pass
            if choice == 5:
                pass
                # 'firstname'  'lastname'  'streetname' 'housenumber' 'zipcode', 'city'  'emailaddress' 'mobilephone'
                # choices_p2 = ["Modify zipcode", "Modify city", "Modify emailaddress", "Modify phone_number", "Previous Page"]
                # choice = self.choices(choices_p2, "Wich option do you want to choose?: ")

                # to_change = input(f"What will be the new {choices[choice].split(' ')[choices_p2]}")
                # if choices_p2 == 1:
                #    pass
                # if choices_p2 == 2:
                #     pass
                # if choices_p2 == 3:
                #     pass
                # if choices_p2 == 4:
                #     pass
                # if choices_p2 == 5:
                #     self.modifyPerson(kind)
            



def Encrypt(input):
    
    text = input
    encryption =  ""
    for char in text:
        if char == " ":
            encryption = encryption+char
        elif char.isupper():
            encryption += chr((ord(char) + 22 - 65) % 26 + 65)
        else:
            encryption += chr((ord(char) + 22 - 97) % 26 + 97)
    return  encryption


def Decrypt(output):

    text = output

    encryption =  ""
    for char in text:
        if char == " ":
            encryption = encryption+char
        elif char.isupper():
            encryption += chr((ord(char) - 22 - 65) % 26 + 65)
        else:
            encryption += chr((ord(char) - 22 - 97) % 26 + 97)
    return  encryption


def nameChecker(input):
    name = input
    flag = 0
    while True:  
        if (len(name)<20):
            flag = -1
            break
        else:
            flag = 0
            break
        
        if flag == 0:
            return True
        if flag ==-1:
            print("Not a Valid Password")
            return False


def usernameChecker(input):

    username = input

    flag = 0
    while True:  
        if (len(username)>20):
            flag = -1
            break
        elif (len(username)< 5):
            flag -= 1
            break
        else:
            flag = 0
            break
        for word in username.split():
            if word[0].isdigit():
                flag -= 1
                break
  
        if flag ==-1:
            print("Username is not valid!")

def makeBackup():
    conn = sqlClass.Database("analyse.db") 
    
    # Open() function 
    with io.open('backupdatabase_dump.sql', 'w') as p: 
            
        # iterdump() function
        for line in conn.iterdump(): 
            
            p.write('%s\n' % line)
        
    print(' Backup performed successfully!')
    print(' Data Saved as backupdatabase_dump.sql')
    
    conn.close()










data = sqlClass.Database("analyse.db")
data.checkMigrations()
data.close()

userinterface().mainScreen()