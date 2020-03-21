from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();

mycursor.execute("CREATE TABLE Customers (CustomerID VARCHAR(20) PRIMARY KEY, name VARCHAR(50), phonenumber VARCHAR(15))")

#mycursor.execute("DROP TABLE Customers")