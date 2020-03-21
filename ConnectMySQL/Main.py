from builtins import input
from ProductsTable.InsertFunction import InsetProductSQL, InsetProductValue
from Views.LeflJoinSelect import PopularProduct
from Views.ProductInWareHouse import WarehouseProduct
from Views.ShowProduct import ListProduct
from Views.ShowCustomer import ListCustomers
from SQLStatement.ExcuteSQLVariable import ExecuteAndResult
from SQLStatement.ExecuteAddSQL import ExecuteAdd


print('This is a management application.')
print('What do you want?')
print('1. Add product')
print('2. Add customer')
print('3. List customer')
print('4. List product')
print('5. List the popular product')
print('6. List product in warehouse')
print('-------------------')
print('Enter the number here: ')
#Execute the SELECT products SQL
prds = ListProduct()
ctms = ListCustomers() 

#Wait the input from users
strInput = input()
choice = int(strInput)

#Choice conditions
if(choice == 1):
    print('Enter product id: ')
    productID = input()
    print('Enter product Name: ')
    productName = input()
    print('Enter product Status: ')
    productStatus = input()
    print('Enter product amount: ')
    var1 = input()
    amount = str(var1)
    print('Enter barcode id: ')
    barcodeID = input()
    var2 = InsetProductSQL()
    var3 = InsetProductValue(productID, productName, productStatus, amount, barcodeID)
    ExecuteAdd(var2, var3)
    print('List products after imported:')
    ExecuteAndResult(prds)
    
elif (choice == 2):
    print('Enter customer id: ')
    cusID = input()
    print('Enter customer Name: ')
    cusName = input()
    print('Enter customer number phone: ')
    var1 = input()
    cusPhonenumber = str(var1)
    var4 = InsetProductSQL()
    var5 = InsetProductValue(cusID, cusName, cusPhonenumber)
    ExecuteAdd(var4, var5)
    print('List customers after imported:')
    ExecuteAndResult(ctms)
    
elif (choice == 3):
    ExecuteAndResult(ctms)
elif (choice == 4):
    ExecuteAndResult(prds)
    
elif (choice == 5):
    print('The top 3 product was interested the most: ')
    var6 = PopularProduct()
    ExecuteAndResult(var6)
    
elif (choice == 6):
    print('The list of product that are in warehouse: ')
    var7 = WarehouseProduct()
    ExecuteAndResult(var7)
else:
    print('Your choice was invalid!')
print('------------------------')
print('Finish')