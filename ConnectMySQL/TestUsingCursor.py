import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

print(mycursor.rowcount, "was inserted.")
print("The last record inserted has ID: ", mycursor.lastrowid)