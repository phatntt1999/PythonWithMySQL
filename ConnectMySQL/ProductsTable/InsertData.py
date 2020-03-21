from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
sql = "INSERT INTO Products (ProductID, ProductName, ProductStatus, Amount, BarCodeID) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("IP8M001", "Iphone 8Plus", "Light scratches.", "20", "147852369"),
    ("IP8M015", "Iphone 8Plus Gold", "Light scratches & Cover replaced.", "12","147852369"),
    ("IPXM001", "Iphone X", "Full Pressure & Light scratches.", "2","123456789"),
    ("IPXM015", "Iphone XR", "Full Pressure and Battery > 90%", "11","123456789"),
    ("IPXM019", "Iphone Xs", "Full Pressure.", "5","123456789"),
    ("IP7M091", "Iphone 7Plus", "Full Pressure and Battery > 90%", "9","abcddghyh"),
    ("IP7M001", "Iphone 7", "Screen replaced!", "6","abcddghyh")
]

mycursor.executemany(sql, val)
mysql.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)