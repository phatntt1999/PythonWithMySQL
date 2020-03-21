from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();

# mycursor.execute("ALTER TABLE Products DROP COLUMN BarCodeID;")

# mycursor.execute("CREATE TABLE Products (ProductID VARCHAR(20) PRIMARY KEY,\
# ProductName VARCHAR(50), ProductStatus VARCHAR(255), Amount INT, BarCodeID VARCHAR(20), \
# FOREIGN KEY (BarCodeID) REFERENCES BarCode(BarCodeID))")


mycursor.execute("ALTER TABLE Products ADD BarCodeID VARCHAR(20) UNIQUE, ENGINE = InnoDB DEFAULT CHARSET = utf8;")