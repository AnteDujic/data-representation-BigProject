import mysql.connector
import dbconfig as cfg

class placesDAO:
    connection = ''
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
   
    def create(self, values):
        cursor = self.getcursor()
        sql = "insert into visited (city, dov, hospitality, food, transport, attractions, entertainment) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

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

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from visited where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByCityName(self, city):
        cursor = self.getcursor()
        sql="select * from visited where id = %s"
        values = (city,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByDateVisited(self, dov):
        cursor = self.getcursor()
        sql="select * from visited where dov = %s"
        values = (dov,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByHospitalityRating(self, hospitality):
        cursor = self.getcursor()
        sql="select * from visited where hospitality = %s"
        values = (hospitality,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByFoodRating(self, food):
        cursor = self.getcursor()
        sql="select * from visited where food = %s"
        values = (food,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByTransportRating(self, transport):
        cursor = self.getcursor()
        sql="select * from visited where transport = %s"
        values = (transport,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByAttractionsRating(self, attractions):
        cursor = self.getcursor()
        sql="select * from visited where attractions = %s"
        values = (attractions,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def findByEntertainmentRating(self, entertainment):
        cursor = self.getcursor()
        sql="select * from visited where entertainment = %s"
        values = (entertainment,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue



    def update(self, values):
        cursor = self.getcursor()
        sql="update book set city= %s, dov=%s, hospitality=%s, food=%s, transport=%s, attractions=%s, enterteinment=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from visited where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("Destination deleted!")

    def convertToDictionary(self, result):
        colnames=['id','city','dov', 'hospitality', 'food', 'transport', 'attractions', 'entertainment']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
placesDAO = placesDAO()