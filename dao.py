# Module: Data Representation
# Author: Ante Dujic

import mysql.connector
import dbconfig as cfg

# Class to access database
class PlacesDAO:
    connection = ''
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    # Initiate database
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    # Get cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # Close connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
   
    # Add data to database
    def create(self, values):
        cursor = self.getcursor()
        sql = "insert into visited (city, dov, hospitality, food, transport, attractions, entertainment) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    # Retreive all data from database
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from visited"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    # Retreive data with specified id
    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from visited where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    # Update data with specified id
    def update(self, values):
        cursor = self.getcursor()
        sql="update visited set city= %s, dov=%s, hospitality=%s, food=%s, transport=%s, attractions=%s, entertainment=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # Delete data with specified id  
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from visited where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("Destination deleted!")

    # Convert from tuple to dict
    def convertToDictionary(self, result):
        colnames=['id','city','dov', 'hospitality', 'food', 'transport', 'attractions', 'entertainment']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

# Create instance
placesDAO = PlacesDAO()