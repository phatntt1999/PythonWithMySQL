import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();
#Select name of customers have discount
sql = "SELECT \
  Bills.Discount AS Discount, \
   Customers.name AS LuckyCustomer \
   FROM Bills INNER JOIN Customers ON Bills.CustomerID = Customers.CustomerID"
  
# sql = "SELECT Discount from bills"
  
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
