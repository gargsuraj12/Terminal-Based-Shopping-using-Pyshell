#!/usr/bin/python3

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
    print("1. View Products")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Modify Product")
    print("5. Make shipment")
    print("6. Confirm Delivery")
    print("7. Logout")

def customerMenu():
    print("1. View Products")
    print("2. Add a product to cart")
    print("3. View Cart")
    print("4. Remove a product from Cart")
    print("5. Buy Products")
    print("6. Make Payment")
    print("7. Logout")

def guestMenu():
    print("1. View Products")
    print("2. Get Registered")
    print("3. Exit")    

def validateAdmin():
    username = input("Enter username: ")
    passwd = input("Enter password: ")
    if username != admin.uname or passwd != admin.password:
        return False
    return True    

def validateCustomer():
    username = input("Enter username: ")
    passwd = input("Enter password: ")
    for cust in dataLists.custList:
        if cust.userId == username and cust.password == passwd:
            return cust
    return False        

def executeAdmin():
    print("-----------Welcome to admin home----------")
    while True:
        adminMenu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            admin.viewProducts()
        elif choice == 2:
            admin.addProduct()
        elif choice == 3:
            admin.deleteProduct()        
        elif choice == 4:
            admin.modifyProduct()
        elif choice == 5:
            # admin.makeShipment()
            print("This functionality has not been implemented yet..")
        elif choice == 6:
            # admin.confirmDelivery()
            print("This functionality has not been implemented yet..")     
        elif choice == 7:
            print("Successfully logged out..")
            break
        else:
            print("Invalid choice!! Please try again..")    
    return        

def executeCustomer():
    print("-----------Welcome to customer home----------")
    custObj = customer.CustomerTasks()
    while True:
        customerMenu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.viewProdcuts()
        elif choice == 2:
            custObj.addToCart()
        elif choice == 3:
            custObj.viewCart()        
        elif choice == 4:
            custObj.deleteFromCart()
        elif choice == 5:
            # custObj.buyProducts()
            print("This functionality has not been implemented yet..")
        elif choice == 6:
            # custObj.makePayment()
            print("This functionality has not been implemented yet..")     
        elif choice == 7:
            custObj = None
            print("Successfully logged out..")
            break
        else:
            print("Invalid choice!! Please try again..")    
    return

def executeGuest():
    print("-----------Welcome to guest home----------")
    while True:
        guestMenu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            guest.viewProducts()
        elif choice == 2:
            if guest.getRegistered() == True:
                executeCustomer()
                break
            else:
                continue
        elif choice == 3:
            print("Successfully exited from guest role..")
            break
        else:
            print("Invalid choice!! Please try again later..")
    return


# Execution start from here
while True:
    loginMenu()
    choice = int(input("Enter your choice: "))
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
        if validateCustomer() == False:
            print("Username or password incorrect!!")
            continue
        print("Customer login successful..")
        executeCustomer()

    elif choice == 3:
        executeGuest()

    elif choice == 4:
        break

    else:
        print("Invalid choice!!! Please try again..")            
