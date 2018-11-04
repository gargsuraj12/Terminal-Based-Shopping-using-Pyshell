#!/usr/bin/python3

import product
import customer
import orders

global prodList
prodList = []

global custList
custList = []

global orderList
orderList = []  #list(orders.OrderDetails)

global totalOrders
totalOrders = 1

global ORDER_PENDING
ORDER_PENDING = "Pending for confirmation"

global ORDER_CONFIRMED
ORDER_CONFIRMED = "Confirmed"

global ORDER_SHIPPED
ORDER_SHIPPED = "Shipped"

global ORDER_DELIVERED
ORDER_DELIVERED = "Delivered"
