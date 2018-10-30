#!/usr/bin/python3
import os
import pickle
import getpass

import dataLists
import admin
import customer
import guest


def loginMenu():
    print("1. Login as admin")
    print("2. Login as customer")
    print("3. Login as guest")
    print("4. Exit")


def adminMenu():
    print("-----------------------------------------------")
    print("1. View Products")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Modify Product")
    print("5. Make shipment")
    print("6. Confirm Delivery")
    print("7. View all registerd customers")
    print("8. View all orders")
    print("9. Logout")
    print("-----------------------------------------------")
    

def customerMenu():
    print("-----------------------------------------------")
    print("1. View Products")
    print("2. Add a product to cart")
    print("3. View Cart")
    print("4. Remove a product from Cart")
    print("5. Buy Products")
    print("6. Make Payment")
    print("7. View orders")
    print("8. Logout")
    print("-----------------------------------------------")
    

def guestMenu():
    print("-----------------------------------------------")
    print("1. View Products")
    print("2. Get Registered")
    print("3. Exit")
    print("-----------------------------------------------")
    

def validateAdmin():
    username = input("Enter username: ")
    passwd = getpass.getpass("Enter password: ")
    if username != admin.uname or passwd != admin.password:
        return False
    return True


def validateCustomer():
    username = input("Enter username: ")
    passwd = getpass.getpass("Enter password: ")
    for cust in dataLists.custList:
        if cust.userId == username and cust.password == passwd:
            return cust
    return None


def executeAdmin():
    print("\033[H\033[J")
    print("-----------Welcome to admin home----------")
    while True:
        adminMenu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Choice must be in number format")
            continue    
        if choice == 1:
            admin.viewProducts()
        elif choice == 2:
            admin.addProduct()
        elif choice == 3:
            admin.deleteProduct()
        elif choice == 4:
            admin.modifyProduct()
        elif choice == 5:
            admin.makeShipment()
            # print("This functionality has not been implemented yet..")
        elif choice == 6:
            admin.confirmDelivery()
            # print("This functionality has not been implemented yet..")
        elif choice == 7:
            admin.viewAllCustomers()
        elif choice == 8:
            admin.viewAllOrders()    
        elif choice == 9:
            print("\033[H\033[J")
            print("Successfully logged out..")
            break
        else:
            print("Invalid choice!! Please try again..")
    return


def executeCustomer(cust: customer.Customer):
    print("\033[H\033[J")
    print("-----------Welcome ", cust.cName," ----------")
    custObj = customer.CustomerTasks(cust)
    while True:
        customerMenu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Choice must be in number format")
            continue    
        if choice == 1:
            customer.viewProdcuts()
        elif choice == 2:
            custObj.addToCart(cust)
        elif choice == 3:
            custObj.viewCart(cust)
        elif choice == 4:
            custObj.deleteFromCart(cust)
        elif choice == 5:
            custObj.buyProducts(cust)
            # print("This functionality has not been implemented yet..")
        elif choice == 6:
            custObj.makePayment(cust)
            # print("This functionality has not been implemented yet..")
        elif choice == 7:
            custObj.viewOrders(cust)    
        elif choice == 8:
            custObj = None
            print("\033[H\033[J")
            print("Successfully logged out..")
            break
        else:
            print("Invalid choice!! Please try again..")
    return


def executeGuest():
    print("\033[H\033[J")
    print("-----------Welcome to guest home----------")
    while True:
        guestMenu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Choice must be in number format")
            continue    
        if choice == 1:
            guest.viewProducts()
        elif choice == 2:
            cust = guest.getRegistered()
            if cust != None:
                executeCustomer(cust)
                break
            else:
                continue
        elif choice == 3:
            print("\033[H\033[J")
            print("Successfully exited from guest role..")
            break
        else:
            print("Invalid choice!! Please try again later..")
    return

# Execution start from here


print("\033[H\033[J")
productFile = None
customerFile = None

if os.path.exists("productPickle") == False:
    productFile = open("productPickle", "a")
    productFile.close()

if os.path.exists("customerPickle") == False:
    customerFile = open("customerPickle", "a")
    customerFile.close()

if os.path.exists("orderPickle") == False:
    ordersFile = open("orderPickle", "a")
    ordersFile.close()

productFile = open("productPickle", "rb")
customerFile = open("customerPickle", "rb")
ordersFile = open("orderPickle", "rb")
try:
    dataLists.prodList = pickle.load(productFile)
    dataLists.custList = pickle.load(customerFile)
    dataLists.orderList = pickle.load(ordersFile)
except EOFError:
    dataLists.prodList = []
    dataLists.custList = []
    dataLists.orderList = []

productFile.close()
customerFile.close()
ordersFile.close()

while True:
    print("---------Welcome to login menu------------")
    loginMenu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Choice must be in number format")
        continue    
    if choice == 1:
        if validateAdmin() == False:
            print("Username or password incorrect!!")
            continue
        print("Admin login successful..")
        executeAdmin()

    elif choice == 2:
        if len(dataLists.custList) == 0:
            print("No users registered in the system!!")
            print("Kindly login as guest and get yourself registered first")
            continue
        cust = validateCustomer()
        if cust == None:
            print("Username or password incorrect!!")
            continue
        print("Customer login successful..")
        executeCustomer(cust)

    elif choice == 3:
        executeGuest()

    elif choice == 4:
        break

    else:
        print("Invalid choice!!! Please try again..")

productFile = open("productPickle", "wb")
pickle.dump(dataLists.prodList, productFile)
productFile.close()

customerFile = open("customerPickle", "wb")
pickle.dump(dataLists.custList, customerFile)
customerFile.close()

ordersFile = open("orderPickle", "wb")
pickle.dump(dataLists.orderList, ordersFile)
ordersFile.close()

print("\033[H\033[J")
