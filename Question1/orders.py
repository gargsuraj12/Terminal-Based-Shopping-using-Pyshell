#!/usr/bin/python3

import product
import customer
import dataLists


class Order:
    totalOrders = int(1)

    def __init__(self, userId, prodList, orderAmount, cardNum, address):
        self.orderId = Order.totalOrders
        self.userId = userId
        self.prodList = prodList
        self.orderAmount = orderAmount
        self.cardNum = cardNum
        self.deliveryAddress = address
        self.status = dataLists.ORDER_PENDING
        self.expectedDeliveryDate = ""
        Order.totalOrders += 1

    def updateOrderStatus(self, newStatus):
        self.status = newStatus

    def updateDeliveryDate(self, newDate):
        self.expectedDeliveryDate = newDate