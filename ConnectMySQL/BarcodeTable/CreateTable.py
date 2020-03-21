from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();
# mycursor.execute("CREATE TABLE BarCode (BarCodeID VARCHAR(20) PRIMARY KEY UNIQUE)")
mycursor.execute("CREATE TABLE BarCodes (ID INT NOT NULL AUTO_INCREMENT, \
BarCodeID VARCHAR(20), PRIMARY KEY (ID), FOREIGN KEY (BarCodeID) REFERENCES Products(BarCodeID)) ENGINE = InnoDB DEFAULT CHARSET = utf8;")