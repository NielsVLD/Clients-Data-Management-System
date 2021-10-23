import sqlite3

class Database:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None
        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database!")
            print(e)

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()
    
    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        self.close()

    def get(self,table,columns,limit=None,where=1):

        query = "SELECT {0} from {1} WHERE {2};".format(columns,table,where)
        #print(query)
        self.cursor.execute(query)

        # fetch data
        rows = self.cursor.fetchall()

        return rows[len(rows)-limit if limit else 0:]

    def getLast(self,table,columns):
        
        return self.get(table,columns,limit=1)[0]

    def write(self,table,columns,data):
        
        query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table,columns,data)

        self.cursor.execute(query)

    def delete(self,table,colums,data):

        query = "DELETE FROM {0} WHERE id = {2} ;".format(table,colums,data)

        self.cursor.execute(query)

    def updatePassword(self,table,password,username):

            try:
                query = "UPDATE {0} SET password = {1} WHERE id = 1;".format(table,password,username)
                self.cursor.execute(query)
            except:
                print("something went wrong")
                return


    def query(self,sql,values=None):
        if values == None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, values)
        # self.conn.commit()
    
    # Check if all required tables are avalible
    def checkMigrations(self):

       
        try: self.query("CREATE TABLE 'SystemAdmins' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'username' VARCHAR(128) NOT NULL, 'password' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'Advisors' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'username' VARCHAR(128) NOT NULL, 'password' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'Clients' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'streetname' VARCHAR(128) NOT NULL, 'housenumber' INTEGER NOT NULL, 'zipcode' VARCHAR(128) NOT NULL, 'city' VARCHAR(128) NOT NULL, 'emailaddress' VARCHAR(128) NOT NULL, 'mobilephone' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'SuperAdmin' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'username' VARCHAR(128) NOT NULL, 'password' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'Logging' ('number' INTEGER PRIMARY KEY AUTOINCREMENT, 'username' VARCHAR(128) NOT NULL, 'datetime' VARCHAR(128) NOT NULL, 'description' VARCHAR(128) NOT NULL, 'suspicious' VARCHAR(128) NOT NULL)")
        except: pass
        self.open("analyse.db")
        self.commit()


