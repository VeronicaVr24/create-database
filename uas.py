import MySQLdb as mysql
import hashlib
import sys
import warnings

class MysqlUserDB:
    warnings.filterwarning('error')
    def  __init__(self, DBrootHost, DBrootUser,DBrootPass, DBrootdatabase):
        self.DBrootHost = DBrootHost
        self.DBrootUser = DBrootUser
        self.DBrootPass = DBrootPass
        self.DBrootDatabase = DBrootdatabase

    try:
        print("Checking connection of MYSQL....")
        self.con = mysql.connect(DBrootHost, DBrootUser, DBrootPass, DBrootDatabase)
        self.cursor =self.con.cursor()
        self.cursor.execute('Select version()')
        print("Connected to Mysql Database\n")
    
    except Warning as warn:
        print("Warning", warn)

def createDB(self, DBrootDatabase):
    print("Creating database....")
    try:
        self.cursor.execute('CREATE database if NOT exists' + DBrootDatabase)
        self.cursor.exexcute("SHOW DATABASE LIKE %S", (DBrootDatabase,))
        dbs = self.cursor.fetchone()
        print("Database created:", dbs[0])
    except warninf as warn:

        print("Warning: %s \nStopping Process.\n" %warn)
        sys.exit()
def GrantsAccess(self, DBrootDatabase):
    print("Accenssing Account....")
    try:
        self.cursor.execute("SHOW DATABASES LIKE %s", (DBrootDatabase,))
        result =self.cursor.fetchone()
        print("Access Granted for Database", result[0])
    except Warning as warn:
        print("Warning %s" % warn)

def getDB(self):
    return self.cursor

def delCon(self):
    print("Finishing operation...")
    self.cursor.close()
    self.con.close()
    print("Finished")
