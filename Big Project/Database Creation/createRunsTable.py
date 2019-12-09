import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="running"
)

cursor = db.cursor()
sql="CREATE TABLE runs (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, name VARCHAR(255), distance FLOAT, time FLOAT)"

cursor.execute(sql)