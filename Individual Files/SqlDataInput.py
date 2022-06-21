import mysql.connector
import os
conn = mysql.connector.connect(host = 'localhost', database = 'mydb', user = 'root', password = 'Shokugeki17Soma38')


print(os.getcwd())
pwd_path= os.path.dirname(os.path.abspath(__file__))
myfile = os.path.join(pwd_path, 'SQL_Data.txt')
print(myfile)
f = open(myfile, 'r')


'''
if conn.is_connected():
    print("connection is successful")

cursor = conn.cursor()

sql = "INSERT INTO person (PersonID,Name,Gender) VALUES (%s,%s,%s)"

data = f.read()
data = data.split('\n')
data = [i.split(",") for i in data]

for each_person in data:
    cursor.execute(sql, each_person)
    conn.commit()

f.close()
cursor.close()
conn.close()
'''