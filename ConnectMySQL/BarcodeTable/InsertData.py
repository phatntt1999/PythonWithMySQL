from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
sql = "INSERT INTO BarCodes (BarCodeID) VALUES ('QR04')"
mycursor.execute(sql)
mysql.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)