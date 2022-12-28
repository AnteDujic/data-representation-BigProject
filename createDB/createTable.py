import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="places"
)

cursor = db.cursor()
sql="CREATE TABLE IF NOT EXISTS visited (id INT AUTO_INCREMENT PRIMARY KEY, city VARCHAR(100), dov VARCHAR(100), hospitality INT, food INT, transport INT, attractions INT, entertainment INT)"

cursor.execute(sql)

db.close()
cursor.close()