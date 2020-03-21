from Connectdatabase import connectDB

mysql = connectDB();

def MyCursor():
    cursor = mysql.cursor();
    return cursor