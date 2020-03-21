from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
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
