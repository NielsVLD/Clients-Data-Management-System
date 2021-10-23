# CDMS: V2
# Bart Westhoff (0991807) 
# Niels Krommenhoek

import re
import sqlite3
import io
import databaseclass as sqlClass

Loginusername = ""
Loginpassword = ""











data = sqlClass.Database("analyse.db")
data.checkMigrations()
data.close()

userinterface().mainScreen()
