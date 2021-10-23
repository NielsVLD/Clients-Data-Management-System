from cdms.clientClass import Client
from cdms.databaseclass import Database
from cdms.helperClass import Helper



class PersonCRUD():

    def addPerson(self, kind):
        database = Database("analyse.db")
        if kind == "Advisors" or kind == "SystemAdmins":
            firstname = input("firstname?: ")
            firstname = Helper().Encrypt(firstname)
            lastname = input("lastname?: ")
            lastname = Helper().Encrypt(lastname)
            username = input("username?:")
            username = Helper().Encrypt(username)
            password = input("password?: ")
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
        while loop:
            database = Database("analyse.db")
            firstname = input("firstname?: ")
            firstname = Helper().Encrypt(firstname)

            lastname = input("lastname?: ")
            lastname = Helper().Encrypt(lastname)
            print(firstname)
            print(lastname)
            try:
                data = database.get(columns='*', table=f'${kind}',
                                    where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
                database.commit()
                for row in data:
                    if row[1] != firstname and row[2] != lastname:
                        print("Client not found, try again.")
                        print(row[1], row[2])
                        # self.searchPerson(self)

                # values = ["ID: ", "Firstname: ","Lastname: ","Streetname: ","Housenumber: ", "Zipcode: ","City: ","Email: ", "Mobilephone: " ]
                # i = 0
                # while i < 9:
                #     #print(values[i])
                #     print(data[0])
                #     i += 1
                #TODO: list data of user
                print("Client found!:\n")
                print(data)
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
            # database.query(f"DELETE FROM 'SystemAdmins' WHERE 'firstname'='{firstname}' AND 'lastname'='{lastname}'")
            database.query(f"DELETE FROM '{kind}' WHERE firstname='{firstname}' AND lastname='{lastname}'")
            database.commit()

            print("Deleted")

        except:
            print("not deleted")
        data = database.get(columns='*', table=f'{kind}',
                            where=f"`firstname`='{firstname}' AND `lastname`='{lastname}'")
        print(data)


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

        choices = ["Modify firstname", "Modify lastname", "Modify streetname", "Modify housenumber", "Next Page"]
        choice = userinterface().choices(choices, "Wich option do you want to choose?: ")

        if choice == 1:
            newfirstname = input("What will be the new firstname? ")
            if len(newfirstname) < 20:
            #if Helper().nameChecker(newfirstname) == True:
                newfirstname = Helper().Encrypt(newfirstname)

                database.query(
                    f"UPDATE Clients SET firstname = '{newfirstname}' WHERE firstname = '{_firstname}' AND lastname = '{_lastname}';")
                database.commit()
                database.close()
                # TODO: check wich type is logged

                #userinterface().superAdminMenu()
            else:
                print("Invalid name, try again.")
                PersonCRUD.modifyPerson(self, kind)
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

