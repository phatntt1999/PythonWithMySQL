from Connectdatabase import connectDB
from . import Cursor
mysql = connectDB();


def ExecuteAdd(sql, val):
    mycursor = Cursor.MyCursor()
    mycursor.executemany(sql, val)
    mysql.commit()
    print(mycursor.rowcount, "was inserted.")
