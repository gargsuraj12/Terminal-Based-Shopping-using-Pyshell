#!/usr/bin/python3


class Product:

    def __init__(self, id, name, price, group, subgroup):
        self.pId = id
        self.pName = name
        self.price = price
        self.pGroup = group
        self.pSubgroup = subgroup

    def setProdId(self, id):
        self.pId = id

    def getProdId(self):
        return self.pId

    def setProdName(self, name):
        self.pName = name

    def getProdName(self):
        return self.pName

    def setProdPrice(self, price):
        self.price = price

    def getProdPrice(self):
        return self.price

    def setProdGroup(self, group):
        self.pGroup = group

    def getProdGroup(self):
        return self.pGroup

    def setProdSubgroup(self, subgroup):
        self.pSubgroup = subgroup

    def getProdSubgroup(self):
        return self.pSubgroup
