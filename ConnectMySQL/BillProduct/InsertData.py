import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();
sql = "INSERT INTO BillProduct (BillID, ProductID, SellAmount) VALUES (%s, %s, %s)"
val = [
    ("B159", "IP8M001", 1),
    ("B159", "IPXM001", 1),
    ("B162", "IP8M015", 5),
    ("B165", "IPXM019", 3)
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)