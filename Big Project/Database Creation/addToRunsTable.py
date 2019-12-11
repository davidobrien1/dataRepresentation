import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="running"
)

cursor = db.cursor()
sql="insert into runs (date, name, distance, time) values (%s,%s,%s,%s)"
values = [("19-05-20","David", 5.5, 25.1),
          ("19-05-15","Amy", 11.1, 55.2),
          ("19-06-01","Padraic", 10.2, 49.2),
          ("19-07-03","Una", 7.6, 35.6),
          ("19-07-27","David", 13.1, 60.5),
          ("19-05-13","Una", 8, 39.5),
          ("19-06-22","Padraic", 7.1, 32.0),
          ("19-07-17","Padraic", 5.5, 24.5),
          ("19-06-30","Amy", 4, 19.7),
          ("19-05-29","David", 6.3, 32.1)]

cursor.executemany(sql, values)

db.commit()
