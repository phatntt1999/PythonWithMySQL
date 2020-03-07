import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();
sql = "INSERT INTO Product (id, productName, productStatus) VALUES (%s, %s, %s)"
val = [
    ("IP11470", "Iphone X", "Full Pressure & Light scratches."),
    ("IP10780", "Iphone 8Plus Gold", "Light scratches & Cover replaced."),
    ("IP11490", "Iphone XR", "Full Pressure and Battery > 90%")
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "was inserted.")
print("The last ID inserted is: ", mycursor.lastrowid)