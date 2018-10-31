#!/usr/bin/python3

import product
import dataLists
import cart
import orders


def searchProduct(name):
    for product in dataLists.prodList:
        if product.pName == name:
            return product
    return None


def viewProdcuts():
    print("Name\t\tPrice\t\tGroup\t\tSubgroup")
    for product in dataLists.prodList:
        print(product.pName, "\t\t", product.price,
              "\t\t", product.pGroup, "\t\t", product.pSubgroup)


class Customer:

    def __init__(self, id, passwd, name, address, phone):
        self.userId = id
        self.password = passwd
        self.cName = name
        self.cAddress = address
        self.phone = phone
        self.cart = cart.Cart(id)
        self.orderList = []

class CustomerTasks:

    def __init__(self, customer: Customer):
        if customer.cart.numOfProducts > 0:
            for product in customer.cart.prodList:
                if searchProduct(product.pName) == None:
                    customer.cart.removeProductFromCart(product)
                else:
                    continue
        customer.orderList.clear()
        for order in dataLists.orderList:
            if order.userId == customer.userId:
                customer.orderList.append(order)            

    def addToCart(self, customer: Customer):
        name = input("Enter the name of the product: ")
        product = searchProduct(name)
        if product == None:
            print("product with the entered name does not exist..")
            return
        customer.cart.addProdToCart(product)
        print("Product successfully added in the cart..")

    def viewCart(self, customer: Customer):
        if customer.cart.numOfProducts == 0:
            print("Your cart is empty!! Please add some products first..")
            return
        print("Name\t\tPrice\t\tGroup\t\tSubgroup")
        for product in customer.cart.prodList:
            print(product.pName, "\t\t", product.price,
                  "\t\t", product.pGroup, "\t\t", product.pSubgroup)
        print("Items in cart: ", customer.cart.numOfProducts)
        print("Cart total: ", customer.cart.cartTotal)

    def deleteFromCart(self, customer: Customer):
        if customer.cart.numOfProducts == 0:
            print("Cart contains no products to be deleted..")
            return
        name = input("Enter the product name to be deleted: ")
        product = searchProduct(name)
        if product == None:
            print("Cart does not contain any item with the entered name!!")
            return
        customer.cart.removeProductFromCart(product)
        print("Product deleted successfully..")

    def viewOrders(self, customer: Customer):
        if len(customer.orderList) == 0:
            print("You haven't ordered anything yet..")
            return
        print("----------------------------------------------------------------------------------------------------------------")   
        for order in customer.orderList:
            for product in order.prodList:
                print(product.pName,"\t", product.price)
            print("Total order amount: ", order.orderAmount)
            print("Payment made via Card num: ", order.cardNum)
            print("Delivery Address: ", order.deliveryAddress)
            print("Status of the order: ", order.status)
            if order.expectedDeliveryDate == "":
                print("Expected delivery date: Not-Confirmed")
            else:    
                print("Expected delivery date: ", order.expectedDeliveryDate)
            print("----------------------------------------------------------------------------------------------------------------")


    def buyProducts(self, customer: Customer):
        self.addToCart(customer)    
        print("Press 1 to Make Payment")
        print("Press any key to Continue Shopping")
        choice = input("Enter your choice: ")
        if choice == 1 or choice == '1':
            self.makePayment(customer)
        else:
            return


    def makePayment(self, customer: Customer):
        if customer.cart.numOfProducts == 0:
            print("Cart is Empty!! Please first add some products in cart to make payment..")
            return
        try:
            cardNum = int(input("Enter card number: "))
        except ValueError:
            print("Card number must be an integer")
            return
        deliveryAddress = input("Enter Delivery address: ")        
        orderAmount = customer.cart.cartTotal
        prodList = []
        for product in customer.cart.prodList:
              prodList.append(product)
            #   customer.cart.removeProductFromCart(product)
        order = orders.Order(customer.userId, prodList, orderAmount, cardNum, deliveryAddress)
        customer.orderList.append(order)
        dataLists.orderList.append(order)
        customer.cart.prodList.clear()
        customer.cart.cartTotal = 0
        customer.cart.numOfProducts = 0
        print("Payment Completed. Your order is placed..")
        print("You can now check the status of the order..")
        