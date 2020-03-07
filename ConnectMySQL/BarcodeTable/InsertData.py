import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();
sql = "INSERT INTO BarCode (BarCodeID) VALUES ('147852369')"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)