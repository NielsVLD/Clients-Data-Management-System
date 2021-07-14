# Code dump


# class Client():
#     def __init__(self, firstname, lastname, mail, street,housenumber,zipcode,city,mobile_number):
#         self.firstname = firstname
#         self.lastname = lastname,
#         self.mail = mail
#         self.street = street
#         self.housenumber = housenumber
#         self.zipcode = zipcode
#         self.city = city
#         self.mobile_number = mobile_number

#     def newClient(self):

#         firstname = input("What is your Firstname?: ")
#         lastname = input("What is your Lastname?: ")
#         mail = input("What is the email?: ")
#         _validEmail = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail)
#         if _validEmail:
#             print("Pass")
#         street = input("streetname?: ")
#         if street.isalpha():
#             print("pass")
#         housenumber = input("house number?: ")
#         if housenumber.isnumeric():
#             print("pass")
#         zipcode = input("zipcode?: ").upper()
#         if zipcode[0:3].isnumeric() and zipcode[4:5].isalpha() and len(zipcode) ==6:
#             print("pass")
#         listOfCities = ["Rotterdam", "Amsterdam", "Alkmaar", "Maastricht", "Utrecht", "Almere", "Lelystad", "Maassluis", "Vlaardingen", "Schiedam"]
#         index =1
#         while index <= len(listOfCities):
#             print(f"{index}. {listOfCities[index-1]}")
#             index +=1
#         city = listOfCities[(int(input("In wich city do you live (choose from 1-10)")))-1]
#         print(city)
#         mobile_number = input("What is your mobile number?:\n31-6-")
#         if mobile_number.isnumeric() and len(mobile_number) == 8:
#             print("pass")
#         mobile_number = "31-6-" + mobile_number
#         print(mobile_number)
#         #1return Client(firstname, lastname,mail,street,housenumber,zipcode,city,mobile_number)
        
        
#         database = sqlClass.Database("analyse.db")
#         database.write('Clients', '`firstname`, `lastname`, `streetname`, `housenumber`, `zipcode`, `city`, `emailaddress`, `mobilephone`', f"'{firstname}', '{lastname}', '{street}', '{housenumber}, '{zipcode}, '{city}, '{mail}, '{mobile_number}'")
#         database.commit()
#         database.close()