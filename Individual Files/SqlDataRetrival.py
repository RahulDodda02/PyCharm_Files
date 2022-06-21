import mysql.connector

conn = mysql.connector.connect(host = 'localhost', database = 'mydb', user = 'root', password = 'Shokugeki17Soma38')
cursor = conn.cursor()

f = open('SQL_Data.txt', 'a')  #a to append, w to just write
cursor.execute("SELECT * FROM person")
result = cursor.fetchall()

for x in result:
    f.write(str(x) + "\n")
