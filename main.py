import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'Manali123hastam',
    port = '3306',
    database = 'mydb'
)

mycursor = mydb.cursor()
mycursor.execute('select * from lab')
users = mycursor.fetchall()
for user in users:
    print(user)