import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

cursor = db.cursor()
#sql = "create database if not exists" + self.database (to take from config)
# self.blabla
cursor.execute('create DATABASE IF NOT EXISTS places')

db.close()
cursor.close()

## now create tables