import mysql.connector

def connectDB():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Quenmenik12",
        database="MyDatabase"
    )
    return mydb