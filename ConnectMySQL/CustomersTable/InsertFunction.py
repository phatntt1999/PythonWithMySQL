def InsetProductSQL():
    sql = "INSERT INTO Customers (CustomerID, name, phonenumber) VALUES (%s, %s, %s)"
    return sql

def InsetProductValue(a, b, c):
    val = [
        (a, b, c),
    ]
    return val