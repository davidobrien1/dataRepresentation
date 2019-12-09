import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="running"
)

cursor = db.cursor()
sql="insert into record (date, name, time) values (%s,%s,%s)"
values = [("04-05-31","Kenenisa BEKELE",12.623),
          ("98-06-13","Haile GEBRSELASSIE",12.657),
          ("97-08-22","Daniel KOMEN",12.65),
          ("18-08-31","Selemon BAREGA",12.717),
          ("18-18-31","Hagos GEBRHIWET",12.763),
          ("04-07-02","Eliud KIPCHOGE",12.775),
          ("18-08-31","Yomif KEJELCHA",12.78),
          ("12-07-06","Dejen GEBREMESKEL",12.78),
          ("04-07-02","Sileshi SIHINE",12.783),
          ("12-07-06","Isiah Kiplangat KOECH",12.81)]

cursor.executemany(sql, values)

db.commit()
