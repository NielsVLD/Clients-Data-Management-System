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


    def query(self,sql,values=None):
        if values == None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, values)
        # self.conn.commit()
    
    # Check if all required tables are avalible
    def checkMigrations(self):

        # Books table
        # try:
        #     data = self.get('books','id')
        # except:
        #     self.query("CREATE TABLE `books` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `author` VARCHAR(256) NOT NULL , `country` VARCHAR(256) NOT NULL , `imageLink` TEXT NOT NULL , `language` VARCHAR(256) NOT NULL , `link` VARCHAR(256) NOT NULL , `pages` INT NOT NULL , `title` VARCHAR(256) NOT NULL , `year` YEAR NOT NULL )")
        #
        #
        # # Credentials table
        # try:
        #     data = self.get('credentials', 'id')
        # except:
        #     self.query("CREATE TABLE `credentials` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT , `persons_id` INT NOT NULL , `password` VARCHAR(128) NOT NULL , `is_admin` BOOLEAN DEFAULT(FALSE) )")
        #
        # # Persons table
        # try:
        #     data = self.get('persons', 'id')
        # except:
        #     self.query("CREATE TABLE `persons` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT , `gender` VARCHAR(128) NOT NULL , `nameset` VARCHAR(128) NOT NULL , `givenname` VARCHAR(128) NOT NULL , `surname` VARCHAR(128) NOT NULL , `streetaddress` VARCHAR(256) NOT NULL , `zipcode` VARCHAR(10) NOT NULL , `city` VARCHAR(128) NOT NULL , `emailaddress` VARCHAR(256) NOT NULL , `telephonenumber` VARCHAR(128) NOT NULL, `username` VARCHAR(128) NOT NULL );")
        #     self.query("INSERT INTO `persons` (`gender`, `nameset`, `givenname`, `surname`, `streetaddress`, `zipcode`, `city`, `emailaddress`, `telephonenumber`, `username`) VALUES ('male', 'dutch', 'admin', 'user', 'adminstreet 5', '2550PK', 'admincity', 'admin@gmail.com', '0653839238', 'admin')")
        #     self.commit()
        #     lastPerson = self.getLast('persons', 'id')
        #     self.query(f"INSERT INTO `credentials` (`persons_id`, `password`, `is_admin`) VALUES ({lastPerson[0]}, 'password', 1)")
        #     self.commit()
        #
        # # Catalogs table
        # try:
        #     data = self.get('catalogs', 'id')
        # except:
        #     self.query("CREATE TABLE `catalogs` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT , `books_id` INT NOT NULL , `amount` INT NOT NULL)")
        #
        # # Catalogs table
        # try:
        #     data = self.get('loan_items', 'id')
        # except:
        #     self.query("CREATE TABLE `loan_items` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT , `books_id` INT NOT NULL , `user_id` INT NOT NULL)")
        #
        #pass
        try: self.query("CREATE TABLE 'SystemAdmins' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'username' VARCHAR(128) NOT NULL, 'password' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'Advisors' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'username' VARCHAR(128) NOT NULL, 'password' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'Clients' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'streetname' VARCHAR(128) NOT NULL, 'housenumber' INTEGER NOT NULL, 'zipcode' VARCHAR(128) NOT NULL, 'city' VARCHAR(128) NOT NULL, 'emailaddress' VARCHAR(128) NOT NULL, 'mobilephone' VARCHAR(128) NOT NULL)")
        except: pass
        try: self.query("CREATE TABLE 'SuperAdmin' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'firstname' VARCHAR(128) NOT NULL, 'lastname' VARCHAR(128) NOT NULL, 'username' VARCHAR(128) NOT NULL, 'password' VARCHAR(128) NOT NULL)")
        except: pass
