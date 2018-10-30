#!/usr/bin/python3

import product
import dataLists


id = 7
uname = "suraj"
password = "suraj"


def printUpdateMenu():
    print("1. Update Name")
    print("2. Update Price")
    print("3. Update Group")
    print("4. Update Subgroup")


def searchProduct(prodId):
    for product in dataLists.prodList:
        if product.pId == prodId:
            return True
    return False

def searchOrder(orderId):
    for order in dataLists.orderList:
        if order.orderId == orderId:
            return order
    return None

def addProduct():
    try:
        id = int(input("Enter the product id: "))
    except ValueError:
        print("Id must be in number format..")    
        return
    name = input("Enter the product name: ")
    try:
        price = int(input("Enter the product price: "))
    except ValueError:
        print("Price must be in number format..")
        return    
    group = input("Enter the product's group: ")
    subgroup = input("Enter the product's subgroup: ")
    if searchProduct(id) == True:
        print("Product with the entered id cannot be added as another product with same id is present in the system")
        return
    newprod = product.Product(id, name, price, group, subgroup)
    dataLists.prodList.append(newprod)
    print("Product successfully added..")


def viewProducts():
    if len(dataLists.prodList) == 0:
        print("Currently no products in the system!!")
        return

    print("Id\t\tName\t\tPrice\t\tGroup\t\tSubgroup")
    for product in dataLists.prodList:
        print(product.pId, "\t\t", product.pName, "\t\t", product.price,
              "\t\t", product.pGroup, "\t\t", product.pSubgroup)


def deleteProduct():
    if len(dataLists.prodList) == 0:
        print("Currently no products in the system to delete!!")
        return
    try:
        id = int(input("Enter the product id to be deleted: "))
    except ValueError:
        print("Id must be in number format..")    
        return
    if searchProduct(id) == False:
        print("No product is present with the entered id..")
        return
    for product in dataLists.prodList:
        if id == product.pId:
            dataLists.prodList.remove(product)
            print("Product successfully deleted..")
            break


def modifyProduct():
    if len(dataLists.prodList) == 0:
        print("Currently no products in the system to delete!!")
        return
    try:    
        id = int(input("Enter the product id to be modified: "))
    except:
        print("Id must be a number..")
        return    
    if searchProduct(id) == False:
        print("No product is present with the entered id..")
        return
    for product in dataLists.prodList:
        if id == product.pId:
            printUpdateMenu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Choice must be in number format")
                return    
            dataLists.prodList.remove(product)       
            if choice == 1:
                name = input("Enter product's new name: ")
                product.setProdName(name)
            elif choice == 2:
                try:
                    price = int(input("Enter product's new price: "))
                    product.setProdPrice(price)
                except ValueError:
                    print("Price must be in number format..")
                    return    
            elif choice == 3:
                group = input("Enter product's new group: ")
                product.setProdGroup(group)
            elif choice == 4:
                subgroup = input("Enter product's new subgroup: ")
                product.setProdSubgroup(subgroup)
            else:
                print("Innvalid choice..")
            dataLists.prodList.append(product)
            break

def viewAllOrders():
    if len(dataLists.orderList) == 0:
            print("Anybody haven't ordered anything yet..")
            return
    for order in dataLists.orderList:
        print("Order Id: ", order.orderId)
        print("Order Placed by:", order.userId)
        for product in order.prodList:
            print(product.pName,"\t", product.price)
        print("Total order amount: ", order.orderAmount)
        print("Payment made via Card num: ", order.cardNum)
        print("Delivery Address: ", order.deliveryAddress)
        print("Status of the order: ", order.status)
        print("Expected delivery date: ", order.expectedDeliveryDate)
        print("----------------------------------------------------------------------------------------")    
        

def makeShipment():
    if len(dataLists.orderList) == 0:
        print("No customer has placed any order till now..")
        return
    try:    
        orderId = int(input("Enter the order id to ship: "))
    except ValueError:
        print("Order id must be in number format..")
        return    
    order = searchOrder(orderId)
    if order == None:
        print("Nobody has placed order with entered order id...")
        return
    if order.status == dataLists.ORDER_SHIPPED:
        print("This order has already been shipped..")
        return
    if order.status == dataLists.ORDER_PENDING:
        print("This order is pending for confirmation. Please confirm it first")
        return    
    dataLists.orderList.remove(order)    
    order.status = dataLists.ORDER_SHIPPED
    dataLists.orderList.append(order)
    print("Order has been shipped successfully...")    



def confirmDelivery():
    if len(dataLists.orderList) == 0:
        print("No customer has placed any order till now..")
        return
    try:    
        orderId = int(input("Enter the order id to ship: "))
    except ValueError:
        print("Order id must be in number format..")
        return
    order = searchOrder(orderId)
    if order == None:
        print("Nobody has placed order with entered order id...")
        return
    if order.status != dataLists.ORDER_PENDING:
        print("This order has already been processed..")
        return
    dataLists.orderList.remove(order)
    deliveryDate = input("Enter the expected delivery date for this order: ")
    order.expectedDeliveryDate = deliveryDate
    order.status = dataLists.ORDER_CONFIRMED
    dataLists.orderList.append(order)

def viewAllCustomers():
    if len(dataLists.custList) == 0:
        print("No customers exist in the system..")
        return
    print("UserId\t\tPassword\t\tName\t\tAddress\t\tPhone")
    for cust in dataLists.custList:
        print(cust.userId, "\t\t", cust.password, "\t\t",
              cust.cName, "\t\t", cust.phone)
    return
