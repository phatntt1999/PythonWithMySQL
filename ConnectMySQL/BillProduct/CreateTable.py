import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

mycursor.execute('CREATE TABLE BillProduct (BillID VARCHAR(20), ProductID VARCHAR(20), PRIMARY KEY(BillID, ProductID), SellAmount INT, FOREIGN KEY (BillID) REFERENCES Bills(BillID), FOREIGN KEY (ProductID) REFERENCES Products(ProductID))')

# mycursor.execute('DROP TABLE BillProduct')