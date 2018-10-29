#!/usr/bin/python3

import product


class Cart:

    def __init__(self,id):
        self.id = id
        self.numOfProducts = 0
        self.prodList = []
        self.cartTotal = 0

    def addProdToCart(self, product):
        self.numOfProducts += 1
        self.prodList.append(product)
        self.cartTotal += product.getProdPrice()

    def removeProductFromCart(self, product):
        self.prodList.remove(product)
        self.numOfProducts -= 1
        self.cartTotal -= product.getProdPrice()    
