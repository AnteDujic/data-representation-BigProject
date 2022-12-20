import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

cursor = db.cursor()

cursor.execute('create DATABASE IF NOT EXISTS places')

db.close()
cursor.close()

## now create tables