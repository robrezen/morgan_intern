<<<<<<< HEAD
from algorithms import *
from order import Order
from order_limit import OrderLimit
from trading import Trading

class Exchange:
    def __init__(self, id_even=0, id_odd=-1, order=0):
        self.id_even = id_even
        self.id_odd = id_odd
        self.order = order
        self.__book_orders_sell = []
        self.__book_orders_buy = []

    #set id for the order, type order buy receive id even and sell id odd
    def getId(self, side: str):
        if side == "buy":
            self.id_even = self.id_even + 2
            return self.id_even
        elif side == "sell":
            self.id_odd = self.id_odd +2
            return self.id_odd
    def getOrder(self):
        return self.order

    def createLimitOrder(self, type_order: str, side: str, price: int, qty: int, id: int):
        self.order = OrderLimit(type_order, side, price, qty, id)
        print(f"Order created: {self.order.side} {self.order.qty} @ {self.order.price} identificador_{self.order.id}")
    
    def createOrderMarket(self, type_order: str, side: str, qty: int):
        self.order = Order(type_order, side, qty)
        print(f"Order created: {self.order.type_order} {self.order.side} {self.order.qty}")

    def getOrderBook(self, side: str):
        if side == "buy":
            return self.__book_orders_buy, self.__book_orders_sell
        elif side == "sell":
            return self.__book_orders_sell, self.__book_orders_buy

    def insertOrder(self, book: list):
        my_sort(book, self.order)

    def serchOrder(self, book: list):
        return serchBinary(book, self.order)

    def findBook(self, id: int):
        if id % 2:
            return self.__book_orders_sell
        else:
            return self.__book_orders_buy

    def tradeOperation(self, order_in_book: object):
        trade = Trading()
        return trade.trade(order_in_book, self.order)
    
    def deleteOrder(self, position: int, book: list):
        del book[position]

    def changeOrder(self, id: int, new_id: int, book: list, price=0, qty=0):
        book_order, position = findOrder(id, book)
        if price != 0:
            book_order.price = price
        if qty != 0:
            book_order.qty = qty
        book_order.id = new_id
        self.order = book_order
        del book[position]
        my_sort(book, self.order)
        print(f"Order changed: {self.order.side} {self.order.qty} @ {self.order.price} identificador_{self.order.id}")

    #standard set up of operations considering the type of operation
    def constructor(self, order_str: str):
        list_order = order_str.split()
        typeOperation = list_order[0]
        if typeOperation == "cancel" or typeOperation == "change":
            id_string = list_order[2].split("_")
            id = int(id_string[1])
            if typeOperation == "change":
                if len(list_order) == 6:
                    qty = int(list_order[3])	
                    price = int(list_order[5])
                    return id, None, price, qty, typeOperation
                elif len(list_order) == 5:
                    price = int(list_order[4])
                    return id, None, price, 0, typeOperation
                elif len(list_order) == 4:
                    qty = int(list_order[3])
                    return id, None, 0, qty, typeOperation
            return id, None, None, None, typeOperation
        elif typeOperation == "limit" or typeOperation == "market":
            side = list_order[1]
            if typeOperation == "limit":
                price, qty  = int(list_order[2]),  int(list_order[3])
                return None, side, price, qty, typeOperation         
            elif typeOperation == "market":
                qty = int(list_order[2])
=======
from algorithms import Algorithms
from order import Order
from order_limit import OrderLimit
from trading import Trading

class Exchange:
    def __init__(self, id_even=0, id_odd=-1, order=0):
        self.id_even = id_even
        self.id_odd = id_odd
        self.order = order
        self.__book_orders_sell = []
        self.__book_orders_buy = []

    #set id for the order, type order buy receive id even and sell id odd
    def getId(self, side: str):
        if side == "buy":
            self.id_even = self.id_even + 2
            return self.id_even
        elif side == "sell":
            self.id_odd = self.id_odd +2
            return self.id_odd
    def getOrder(self):
        return self.order

    def createLimitOrder(self, type_order: str, side: str, price: int, qty: int, id: int):
        self.order = OrderLimit(type_order, side, price, qty, id)
        print(f"Order created: {self.order.side} {self.order.qty} @ {self.order.price} identificador_{self.order.id}")
    
    def createOrderMarket(self, type_order: str, side: str, qty: int):
        self.order = Order(type_order, side, qty)
        print(f"Order created: {self.order.type_order} {self.order.side} {self.order.qty}")

    def getOrderBook(self, side: str):
        if side == "buy":
            return self.__book_orders_buy, self.__book_orders_sell
        elif side == "sell":
            return self.__book_orders_sell, self.__book_orders_buy

    def insertOrder(self, book: list):
        sort = Algorithms()
        sort.my_sort(book, self.order)

    def serchOrder(self, book: list):
        serch = Algorithms()
        return serch.serchBinary(book, self.order)

    def findBook(self, id: int):
        if id % 2:
            return self.__book_orders_sell
        else:
            return self.__book_orders_buy

    def tradeOperation(self, order_in_book: object):
        trade = Trading()
        return trade.trade(order_in_book, self.order)
    
    def deleteOrder(self, position: int, book: list):
        del book[position]

    def changeOrder(self, id: int, new_id: int, book: list, price=0, qty=0):
        change = Algorithms()
        book_order, position = change.findOrder(id, book)
        if price != 0:
            book_order.price = price
        if qty != 0:
            book_order.qty = qty
        book_order.id = new_id
        self.order = book_order
        del book[position]
        sort = Algorithms()
        sort.my_sort(book, self.order)
        print(f"Order changed: {self.order.side} {self.order.qty} @ {self.order.price} identificador_{self.order.id}")

    #standard set up of operations considering the type of operation
    def constructor(self, order_str: str):
        list_order = order_str.split()
        typeOperation = list_order[0]
        if typeOperation == "cancel" or typeOperation == "change":
            id_string = list_order[2].split("_")
            id = int(id_string[1])
            if typeOperation == "change":
                if len(list_order) == 6:
                    qty = int(list_order[3])	
                    price = int(list_order[5])
                    return id, None, price, qty, typeOperation
                elif len(list_order) == 5:
                    price = int(list_order[4])
                    return id, None, price, 0, typeOperation
                elif len(list_order) == 4:
                    qty = int(list_order[3])
                    return id, None, 0, qty, typeOperation
            return id, None, None, None, typeOperation
        elif typeOperation == "limit" or typeOperation == "market":
            side = list_order[1]
            if typeOperation == "limit":
                price, qty  = int(list_order[2]),  int(list_order[3])
                return None, side, price, qty, typeOperation         
            elif typeOperation == "market":
                qty = int(list_order[2])
>>>>>>> b72e43e5a3b83eaaf5ee9642621dc64ffe95ec38
                return None, side, None, qty, typeOperation  