# Database
import sqlite3

conn = sqlite3.connect('CDMS.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS advisors (
                advisorName text,
                advisorPassword text,

 b  
)""")