import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();
# Print Amount Product were sold!!
sql = "SELECT \
    Products.ProductName AS Product, \
    BillProduct.SellAmount AS Amount\
    FROM Products LEFT JOIN BillProduct \
    ON Products.ProductID = BillProduct.ProductID"
    
    
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)