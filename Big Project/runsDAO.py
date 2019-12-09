import mysql.connector
class RunsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        #user="datarep",  # this is the user name on my mac
        #passwd="password" # for my mac
        database="running"
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into runs (date, name, distance, time) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from runs"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def getAllRecords(self):
        cursor = self.db.cursor()
        sql="select * from record"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDict(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from runs where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def getLeaderBoard(self):
        cursor = self.db.cursor()
        sql="select *, ROUND(SUM(distance),1) from runs group by name order by distance desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByName(self, name):
        cursor = self.db.cursor()
        sql="select * from runs where name = %s"
        values = (name,)

        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def update(self, values):
        cursor = self.db.cursor()
        sql="update runs set date= %s, name=%s, distance=%s, time=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from runs where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id', 'date', 'name','distance', 'time']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

    def convertToDict(self, result):
        colnames=['id', 'date', 'name', 'time']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    


runsDAO = RunsDAO()