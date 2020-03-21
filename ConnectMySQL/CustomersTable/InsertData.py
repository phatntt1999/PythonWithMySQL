from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
sql = "INSERT INTO Customers (CustomerID, name, phonenumber) VALUES (%s, %s, %s)"
val = [
    ("NTTP3409", "abc", "015999999"),
    ("TLH7378", "xyz", "035999999"),
    ("NTPT4405", "egh", "045899999")
]
mycursor.executemany(sql, val)
mysql.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)