from exchange import Exchange
from algorithms import *
from order import Order

class Operation(Exchange):
    def action(self, order: object, exchange):
        id, side, price, qty, typeOperation = exchange.constructor(order)

        if typeOperation == "cancel" or typeOperation == "change":
            order_book = exchange.findBook(id)
            book_order, position = findOrder(id, order_book)
         
        if typeOperation == "cancel":
            if position != None:
                exchange.deleteOrder(position, order_book)
                return print("Order cancelled")
            else:
                return

        elif typeOperation == "change":
            if position != None:
                new_id = exchange.getId(order_book[0].side)
                exchange.changeOrder(id, new_id, order_book, price, qty)
            else:
                return
        
        elif typeOperation == "limit" or typeOperation == "market":
            left_order, position = 0, 0
            book_write, book_read = exchange.getOrderBook(side)

            #create the order and verify if it is possible to trade
            if typeOperation == "limit":
                id = exchange.getId(side)
                exchange.createLimitOrder(typeOperation, side, price, qty, id)
                position = exchange.serchOrder(book_read)
                #verify if the main order is in the book
                if position != "Not found":
                    order = exchange.getOrder()
                    position = HigherPriority(book_read, order)
                else:
                    #put order in book, if not possible to trade
                    book_write = exchange.insertOrder(book_write)
                    return
                
            elif typeOperation == "market":
                if len(book_read) > 0:
                    exchange.createOrderMarket(typeOperation, side, qty)
                    order = exchange.getOrder()
                elif len(book_read) == 0:
                    return print("No orders to trade")
            
            #makes the trade, if the system has found an order with the same price in the book or if the order is of the Market type
            if len(book_read) > 0:
                situation = exchange.tradeOperation(book_read[position])
                #if the system has not reached the amount of shares requested by the order, try to trade with the next order
                while True:
                    if situation == 0:
                        exchange.deleteOrder(position, book_read)
                        break
                    elif situation == -1:
                        exchange.deleteOrder(position, book_read)
                        if len(book_read) > 0:
                            situation = exchange.tradeOperation(book_read[position])
                        else:
                            break
                    elif len(book_read) == 0:
                        exchange.deleteOrder(position, book_read)
                        order = exchange.getOrder()
                        left_order = order.qty
                        break
                    elif situation == 1:
                        break
            #place the order in the book if the system has made the full trade or there is any share left
            if position == "Not found" or left_order > 0:
                book_write = exchange.insertOrder(book_write)
        return
