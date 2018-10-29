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


def addProduct():
    id = int(input("Enter the product id: "))
    name = input("Enter the product name: ")
    price = int(input("Enter the product price: "))
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

    id = int(input("Enter the product id to be deleted: "))
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
    id = int(input("Enter the product id to be modified: "))
    if searchProduct(id) == False:
        print("No product is present with the entered id..")
        return
    for product in dataLists.prodList:
        if id == product.pId:
            dataLists.prodList.remove(product)
            printUpdateMenu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter product's new name: ")
                product.setProdName(name)
            elif choice == 2:
                price = int(input("Enter product's new price: "))
                product.setProdPrice(price)
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


def makeShipment():
    pass


def confirmDelivery():
    pass


def viewAllCustomers():
    if len(dataLists.custList) == 0:
        print("No customers exist in the system..")
        return
    print("UserId\t\tPassword\t\tName\t\tAddress\t\tPhone")
    for cust in dataLists.custList:
        print(cust.userId, "\t\t", cust.password, "\t\t",
              cust.cName, "\t\t", cust.phone)
    return
