# Print Amount Product were sold!!
def WarehouseProduct():
    sql = "SELECT \
        Products.ProductName AS Product, \
        Products.Amount AS Amount\
        FROM Products \
        WHERE Amount > 0 \
        ORDER BY Amount DESC"
    return sql