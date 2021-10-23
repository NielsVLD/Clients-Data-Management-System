from CDMS.databaseclass import Database
import io

class Helper:
    def stopApp(self):
        quit()

    def Encrypt(self,name):
        encryption = ""
        for char in name:
            if char == " ":
                encryption = encryption + char
            elif char.isupper():
                encryption += chr((ord(char) + 22 - 65) % 26 + 65)
            elif char.isnumeric():
                encryption += char
            else:
                encryption += chr((ord(char) + 22 - 97) % 26 + 97)
        return encryption

    def Decrypt(self, name):


        encryption = ""
        for char in name:
            if char == " ":
                encryption = encryption + char
            elif char.isupper():
                encryption += chr((ord(char) - 22 - 65) % 26 + 65)
            elif char.isnumeric():
                encryption += char
            else:
                encryption += chr((ord(char) - 22 - 97) % 26 + 97)
        return encryption

    def nameChecker(self, name):
        # TODO: Niels even naar kijken
        flag = 0
        while True:
            if (len(name) < 20):
                flag = -1
                break
            else:
                flag = 0
                break

            if flag == 0:
                return True
            if flag == -1:
                print("Not a Valid Password")
                return False

    def usernameChecker(self, username):

        flag = 0
        while True:
            if (len(username) > 20):
                flag = -1
                break
            elif (len(username) < 5):
                flag -= 1
                break
            else:
                flag = 0
                break
            for word in username.split():
                if word[0].isdigit():
                    flag -= 1
                    break

            if flag == -1:
                print("Username is not valid!")

    def makeBackup(self):
        conn = Database("analyse.db")

        # Open() function
        with open('backupdatabase_dump.sql', 'w') as p:
            # iterdump() function
            for line in conn:
                p.write('%s\n' % line)

        print(' Backup performed successfully!')
        print(' Data Saved as backupdatabase_dump.sql')

        conn.close()