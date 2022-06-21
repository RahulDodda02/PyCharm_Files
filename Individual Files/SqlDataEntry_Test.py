import mysql.connector

conn = mysql.connector.connect(host = 'localhost', database = 'mydb', user = 'root', password = 'Shokugeki17Soma38')
cursor = conn.cursor()

sql = "INSERT INTO person (PersonID,Name,Gender) VALUES (%s,%s,%s)"


s = ''
while s != '#':
    s = input()
    cursor.execute(sql, s)
    conn.commit()
'''


f = open("SQL_User_Entry.txt", 'w')
print("Enter Users in PersonID,Name,Gender(1 = Male, 2 = Female) format, Leave a # at the end:")
s = ''

while s != '#':
    s = input()
    f.write(s + '\n')

f.close()

f = open('SQL_User_Entry.txt', 'r')
data = f.read()
data = data.split('\n')
data = [i.split(",") for i in data]
print(data)

for each_person in data:
    if each_person != '#' or each_person != '':
        cursor.execute(sql, each_person)
        conn.commit()

f.close()
'''
cursor.close()
conn.close()
