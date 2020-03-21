from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
sql = "INSERT INTO Bills (BillID, CustomerID, TaxRate, Discount, BillNote) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("B159", "NTPT4405", "10","0", "None"),
    ("B160", "NTTP3409", "5", "8","Banking"),
    ("B162", "TLH7378", "10","10", "None"),
    ("B165", "NTPT4405", "5", "7", "Cash")
]
mycursor.executemany(sql, val)
mysql.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)