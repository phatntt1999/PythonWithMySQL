# Print Amount Product were sold!!
def PopularProduct():
    sql = "SELECT \
        Products.ProductName AS Product, \
        BillProduct.SellAmount AS Amount\
        FROM Products LEFT JOIN BillProduct \
        ON Products.ProductID = BillProduct.ProductID \
        ORDER BY Amount ASC \
        "
    return sql