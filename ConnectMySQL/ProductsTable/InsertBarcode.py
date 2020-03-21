from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
sql = "UPDATE Products SET BarCodeID = %s where ProductID = %s"
val = [
    ("QR05", "IP8M017"),
    ("QR04", "IP8M015")
]

mycursor.executemany(sql, val)
mysql.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)