# Niels workfile

class Advisors:

    def __init__(self, name):
        self.Name = name

    def getInfo(self,Name):
        print(f"My name is {Name}")

class System_Administrators(Advisors):

    def __init__(self,name):
        super().__init__(name)



class SuperAdmin(System_Administrators,Advisors):
    
    superadmin_name = "Jeffrey"

    print(superadmin_name)

    def superadmin(self):
        return 'hello everyone'
    
    def __init__(self, newname, age):
        self.Name = newname
        self.Age = age

# info = SuperAdmin("Niels",19)
# print(info.Name)
# print(info.Age)

x = System_Administrators("Barry")
print(x.Name)
y = Advisors("Niels")
y.getInfo("Niels")
x.getInfo("Bart")

