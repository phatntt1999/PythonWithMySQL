import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

#Select record(s) that the Amount < 7
# sql = "SELECT * FROM Product WHERE Amount < 7"

#Select records that have the Status contains the word "full"
sql = "SELECT * FROM Product WHERE productStatus LIKE '%full%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)