from Connectdatabase import connectDB
from . import Cursor
mysql = connectDB();


def ExecuteAndResult(sql):
    mycursor = Cursor.MyCursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall();
    for x in myresult:
        print(x)

def ExecuteManyAndResult(sql, val):
    mycursor = Cursor.MyCursor()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall();
    for x in myresult:
        print(x)