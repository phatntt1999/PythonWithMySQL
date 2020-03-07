import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

mycursor.execute("CREATE TABLE Customers (CustomerID VARCHAR(20) PRIMARY KEY, name VARCHAR(50), phonenumber VARCHAR(15))")

#mycursor.execute("DROP TABLE Customers")