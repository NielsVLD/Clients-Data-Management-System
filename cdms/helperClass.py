from cdms.databaseclass import Database
import io
import sqlite3
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
        conn = sqlite3.connect(('analyse.db'))

        # Open() function
        with io.open('analyse_backup.sql', 'w') as p:
            # iterdump() function
            for line in conn.iterdump():
                p.write('%s\n' % line)

        print(' Backup performed successfully!')
        print(' Data Saved as backupdatabase_dump.sql')

        conn.close()