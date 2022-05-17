from cdms.clientClass import Client
from cdms.databaseclass import Database
from cdms.helperClass import Helper


# database.write(f"Logging", '`username`, `datetime`, `description`, `suspicious`', f"'{firstname}', '{lastname}', '{username}', '{password}'")

class PersonCRUD():

    def addPerson(self, kind):
        database = Database("analyse.db")
        if kind == "Advisors" or kind == "SystemAdmins":
            firstname = input("firstname?: ")
            firstname = Helper().Encrypt(firstname)
            lastname = input("lastname?: ")
            lastname = Helper().Encrypt(lastname)
            username = input("username?:")
            username = Helper().usernameChecker(username)
            username = Helper().Encrypt(username)
            password = input("password?: ")
            password = Helper().passwordChecker(password)
            password = Helper().Encrypt(password)
            database.write(f'{kind}', '`firstname`, `lastname`, `username`, `password`',
                           f"'{firstname}', '{lastname}', '{username}', '{password}'")

        elif kind == "Clients":
            client = Client().newClient()
            database.write(f'Clients',
                           '`firstname`, `lastname`, `streetname`, `housenumber`, `zipcode`, `city`, `emailaddress`, `mobilephone`',
                           f"'{client.firstname}', '{client.lastname}', '{client.street}', '{client.housenumber}', '{client.zipcode}', '{client.city}', '{client.mail}', '{client.mobile_number}'")

        database.commit()
        database.close()

    def searchPerson(self, kind):
        loop = True
        count = 0
        user = Helper().checkLoggedIn()
        print(user)
        database = Database("analyse.db")
        while loop:

            firstname = input("firstname?: ")
            firstname = Helper().Encrypt(firstname)

            lastname = input("lastname?: ")
            lastname = Helper().Encrypt(lastname)
            data = database.get(columns='*', table=f'{kind}',
                                where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
            database.commit()
            try:
                for row in data:
                    print("ID          |", row[0])
                    print("Firstname   |", Helper().Decrypt(row[1]))
                    print("Lastname    |", Helper().Decrypt(row[2]))
                    print("Streetname  |", Helper().Decrypt(row[3]))
                    print("Housenumber |", Helper().Decrypt(row[4]))
                    print("Zipcode     |", Helper().Decrypt(row[5]))
                    print("City        |", Helper().Decrypt(row[6]))
                    print("Email       |", Helper().Decrypt(row[7]))
                    print("Mobilephone |", Helper().Decrypt(row[8]), "\n")
                    loop = False

            except:
                print("Person not found, try again. excpet")

        database.close()

    def deletePerson(self, kind):
        database = Database("analyse.db")
        firstname = input("firstname?: ")

        lastname = input("lastname?: ")
        firstname = Helper().Encrypt(firstname)
        lastname = Helper().Encrypt(lastname)
        print(firstname)
        print(lastname)
        try:
            data = database.get(columns='*', table=f'{kind}',
                                where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
            print(data)
            # database.query(f"DELETE FROM 'SystemAdmins' WHERE 'firstname'='{firstname}' AND 'lastname'='{lastname}'")
            # database.query(f"DELETE FROM '{kind}' WHERE firstname='{firstname}' AND lastname='{lastname}'", )
            database.query(sql="DELETE FROM '?' WHERE firstname='?' AND lastname='?'",
                           values=(kind, firstname, lastname))
            database.commit()

            print("Deleted")

        except:
            print("not deleted")

    def modifyPerson(self, kind):

        from cdms.userinterfaceClass import userinterface
        database = Database("analyse.db")
        _firstname = input(f"What is the firstname of the {kind[:-1]}?: ")
        _lastname = input(f"What is the lastname of the {kind[:-1]}?: ")
        _firstname = Helper().Encrypt(_firstname)
        _lastname = Helper().Encrypt(_lastname)
        data = database.get(columns='*', table=f'{kind}',
                            where=f"`firstname`='{_firstname}' AND `lastname`='{_lastname}'")
        for row in data:
            if row[1] != _firstname and row[2] != _lastname:
                print("Client not found, try again.")
                PersonCRUD.modifyPerson(self, kind)
        attr = ["firstname", "lastname", "username", "password"]
        choices = []
        for att in attr:
            choices.append(f"Modify {att}")
        choice = userinterface().choices(choices, "Wich option do you want to choose?: ")

        new_data = input(f"What will be the new {attr[choice - 1]}")
        new_data = Helper().Encrypt(new_data)
        database.query(
            sql="UPDATE ? SET ? = '?' WHERE firstname = '?' AND lastname = '?';", values=(kind, attr[choice - 1], new_data, _firstname, _lastname))
        database.commit()
        database.close()

    def changePassword(self, kind):
        while True:
            database = Database("analyse.db")

            # _checkPW = Helper().usernameChecker(_password)
            # TODO: niels even kijken
            #    if _checkPW == 0:
            username = input("For extra security please fill in your username:\n")
            username = Helper().Encrypt(username)
            _password = input("For extra security please fill in your password:\n")

            # TODO Niels check if match
            _password = input("What will be ur password? Min length of 5, max length of 20, MUST start with a letter: ")
            _password = Helper().Encrypt(_password)
            database.query(f"UPDATE ? SET password = '?' WHERE username = '?';", values=(kind, _password, username))
            database.commit()
            database.close()
            break
            #     break
            # else:
            #     print("Password not in the required criteria, try again.")

    # To update  password

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

    def checkUsers(self, kind):
        loop = True
        database = Database("analyse.db")
        while loop:
            choice = self.choices(["Check Advisors", "Check System Administrators", "Check Super Administrator"],
                                  "Who do you want to view?: ")
            _type = None
            if choice == 1:
                loop = False
                print("Hello")
                _type = 'Advisors'
                # Display data
                print('\nAdvisors: \n')
                data = database.get(columns='*', table=f'{_type}')
                for row in data:
                    print("ID          |", row[0])
                    print("Firstname   |", Helper().Decrypt(row[1]))
                    print("Lastname    |", Helper().Decrypt(row[2]))
                    print("Username    |", Helper().Decrypt(row[3]))
                    print("Role        | Advisor\n")


            elif choice == 2:
                _type = 'SystemAdmins'
                print('\SystemAdmins: \n')
                data = database.get(columns='*', table=f'{_type}')
                for row in data:
                    print(row)
                    print("ID          |", row[0])
                    print("Firstname   |", Helper().Decrypt(row[1]))
                    print("Lastname    |", Helper().Decrypt(row[2]))
                    print("Username    |", Helper().Decrypt(row[3]))
                    print("Role        | SystemAdmin\n")
                loop = False
            elif choice == 3:
                _type = 'SuperAdmin'
                print('SuperAdmin: \n')
                data = database.get(columns='*', table=f'{_type}')
                for row in data:
                    print("ID          |", row[0])
                    print("Firstname   |", Helper().Decrypt(row[1]))
                    print("Lastname    |", Helper().Decrypt(row[2]))
                    print("Username    |", Helper().Decrypt(row[3]))
                    print("Role        | SuperAdmin\n")
                loop = False
            else:
                print("Incorrect input, try again.")

        database.close()
