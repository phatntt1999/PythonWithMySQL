def InsetProductSQL():
    sql = "INSERT INTO Products (ProductID, ProductName, ProductStatus, Amount, BarCodeID) VALUES (%s, %s, %s, %s, %s)"
    return sql

def InsetProductValue(a, b, c, d, e):
    val = [
        (a, b, c, d, e),
    ]
    return val