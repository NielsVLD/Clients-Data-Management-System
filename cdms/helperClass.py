from cdms.databaseclass import Database
import io
import sqlite3
import json
class Helper:
    def stopApp(self):
        quit()

    def Encrypt(self,name):
        message = name.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        key = 4
        for letter in message:
            if letter in alpha:  # if the letter is actually a letter
                # find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) + key) % len(alpha)

                result = result + alpha[letter_index]
            if letter.isnummeric():
                result = result + alpha[letter]
            else:
                result = result + letter

        return result

    def Decrypt(self, name):

        message = name.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        key =4
        for letter in message:
            if letter in alpha:  # if the letter is actually a letter
                # find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) - key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter

        return result



    def passwordChecker(self, password):
            #What will be ur password? Min length of 8, no longer than 30 characters, MUST have at least one lowercase letter, one uppercase letter, one digit and one special character
            #password = input('please enter password')
            nums = '0123456789'
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alpha_lower = "abcdefghijklmnopqrstuvwxyz"
            special = "~!@#$%^&*_-+=`|{\()}[]:;'<>,.?/"
            x=0
            y=0
            z=0
            w=0

            while len(password) < 8 or len(password) > 30:
                password=input('\n Please enter correct password. Min length of 8, no longer than 30 characters, MUST have at least one lowercase letter, one uppercase letter, one digit and one special character : ')

            for i in range(len(password)):
                if password[i] in nums:
                    x=1
                elif password[i] in alpha:
                    y=1
                elif password[i] in alpha_lower:
                    z=1
                elif password[i] in special:
                    w=1
            sum = x+y+z+w
            if sum != 4:
                password=input('\n Please enter correct password. Min length of 8, no longer than 30 characters, MUST have at least one lowercase letter, one uppercase letter, one digit and one special character :')
            else:
                print('\n Password is accepted.')
                return password

            
        





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
            while len(username) < 5 or len(username) > 20:
                username=input('\n Please enter correct username, name needs to be between 5 and 20 characters : ')
            return username
            

            
            
      
    def makeBackup(self):
        conn = sqlite3.connect(('analyse.db'))

        # Open() function
        with io.open('analyse_backup.sql', 'w') as p:
            # iterdump() function
            for line in conn.iterdump():
                p.write('%s\n' % line)

        print(' Backup performed successfully!')
        print(' Data Saved as backupdatabase_dump.sql')

        conn.close()
    def logUsername(self, username):
        _dict = {"username": username}
        with open("username.json", "w+") as f:
            json.dump(_dict, f)

    def checkLoggedIn(self):
        with open("username.json", "r") as f:
            _dict = json.load(f)
        return _dict["username"]