#!/usr/bin/python3

import product
import dataLists
import cart


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

class CustomerTasks:

    def __init__(self,cart):
        self.cart = cart
        if self.cart.numOfProducts > 0:
            for product in self.cart.prodList:
                if searchProduct(product.pName) == None:
                    self.cart.removeProductFromCart(product)
                else:
                    continue    

    def addToCart(self):
        name = input("Enter the name of the product: ")
        product = searchProduct(name)
        if product == None:
            print("product with the entered name does not exist..")
            return
        self.cart.addProdToCart(product)
        print("Product successfully added in the cart..")

    def viewCart(self):
        if self.cart.numOfProducts == 0:
            print("Your cart is empty!! Please add some products first..")
            return
        print("Name\t\tPrice\t\tGroup\t\tSubgroup")
        for product in self.cart.prodList:
            print(product.pName, "\t\t", product.price,
                  "\t\t", product.pGroup, "\t\t", product.pSubgroup)
        print("Items in cart: ", self.cart.numOfProducts)
        print("Cart total: ", self.cart.cartTotal)

    def deleteFromCart(self):
        if self.cart.numOfProducts == 0:
            print("Cart contains no products to be deleted..")
            return
        name = input("Enter the product name to be deleted: ")
        product = searchProduct(name)
        if product == None:
            print("Cart does not contain any item with the entered name!!")
            return
        self.cart.removeProductFromCart(product)
        print("Product deleted successfully..")

    def buyProducts(self):
        if self.cart.numOfProducts == 0:
            print("Cart is currently empty!! Please add some products to cart..")
            return
        # write the info into the log and empty the cart and redirect to make payment
        pass

    def makePayment(self):
        pass
