import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

mycursor.execute("DROP TABLE product")
#mycursor.execute("CREATE TABLE Products (ProductID VARCHAR(20) PRIMARY KEY, ProductName VARCHAR(50), ProductStatus VARCHAR(255), Amount INT, BarCodeID VARCHAR(20), FOREIGN KEY (BarCodeID) REFERENCES BarCode(BarCodeID))")