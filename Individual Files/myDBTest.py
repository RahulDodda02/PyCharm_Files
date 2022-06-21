import mysql.connector

conn = mysql.connector.connect(host = 'localhost', database = 'mydb', user = 'root', password = 'Shokugeki17Soma38')

if conn.is_connected():
    print("connection is successful")

cursor = conn.cursor()
cursor.execute("select * from Person where PersonId=1")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
