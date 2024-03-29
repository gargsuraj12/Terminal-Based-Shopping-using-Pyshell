#!/usr/bin/python3

import getpass

import product
import dataLists
import customer


def viewProducts():
    if len(dataLists.prodList) == 0:
        print("Currently no products in the system!!")
        return
    print("Id\t\tName\t\tPrice\t\tGroup\t\tSubgroup")
    for product in dataLists.prodList:
        print(product.pId, "\t\t", product.pName, "\t\t", product.price,
              "\t\t", product.pGroup, "\t\t", product.pSubgroup)


def getRegistered():
    userid = input("Enter the username: ")
    if userid == None or userid == '':
        print("Username cannot be empty!!")
        return
    password = getpass.getpass("Enter the password: ")
    if password == None or password == '':
        print("Password cannot be empty!!")
        return 
    name = input("Enter your full name: ")
    if name == None or name == '':
        print("Name cannot be empty!!")
        return 
    address = input("Enter your full address: ")
    phone = input("Enter phone number: ")
    
    for cust in dataLists.custList:
        if cust.userId == userid:
            print(
                "Another user with same userid is present in the system!! Please choose a different userid")
            return None
    newCust = customer.Customer(userid, password, name, address, phone)
    dataLists.custList.append(newCust)
    return newCust
