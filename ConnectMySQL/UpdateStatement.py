import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Quenmenik12",
    database="MyDatabase"
)

mycursor = mydb.cursor();

sql = "UPDATE Product SET Amount = %s where id = %s"
val = (20, 'IP11470');


mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected.")