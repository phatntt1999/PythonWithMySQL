import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

mycursor.execute("SELECT * FROM Products")
 
myresult=mycursor.fetchall();
 
for x in myresult:
    print(x)
