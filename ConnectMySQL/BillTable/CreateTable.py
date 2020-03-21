from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
mycursor.execute("CREATE TABLE Bills (BillID VARCHAR(20) PRIMARY KEY, CustomerID VARCHAR(20), TaxRate SMALLINT(2) ZEROFILL, Discount SMALLINT(2) ZEROFILL, BillNote VARCHAR(255), FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID))")

#mycursor.execute("DROP TABLE Bills")