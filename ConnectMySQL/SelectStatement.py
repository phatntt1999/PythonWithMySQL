from Connectdatabase import connectDB

mysql = connectDB();

mycursor = mysql.cursor();

mycursor.execute("SELECT * FROM Products")
 
myresult=mycursor.fetchall();

for x in myresult:
    print(x)