<<<<<<< HEAD
from exchange import *

class Trading():
    def trade(self, order_in_book: list, order: object ):
        balance = order_in_book.qty - order.qty
        if balance > 0:
            print(f"Trade, price: {order_in_book.price}, qty: {order.qty}")
            order_in_book.qty = balance
            return 1
        elif balance == 0:
            print(f"Trade, price: {order_in_book.price}, qty: {order.qty}")
            return 0
        elif balance < 0:
            print(f"Trade, price: {order_in_book.price}, qty: {order_in_book.qty}")
            order.qty = abs(balance)
=======
from exchange import *

class Trading():
    def trade(self, order_in_book: object, order: object ):
        balance = order_in_book.qty - order.qty
        if balance > 0:
            print(f"Trade, price: {order_in_book.price}, qty: {order.qty}")
            order_in_book.qty = balance
            return 1
        elif balance == 0:
            print(f"Trade, price: {order_in_book.price}, qty: {order.qty}")
            return 0
        elif balance < 0:
            print(f"Trade, price: {order_in_book.price}, qty: {order_in_book.qty}")
            order.qty = abs(balance)
>>>>>>> b72e43e5a3b83eaaf5ee9642621dc64ffe95ec38
            return -1