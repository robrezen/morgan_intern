<<<<<<< HEAD
def my_sort(book: list, order: object):
    start, end = 0, len(book)
    while start < end:
        half = (start + end) // 2
        if order.price < book[half].price:
            end = half
        else:
            start = half + 1
    book.insert(start, order)
    return

def serchBinary(book: list, order: object):
    start, end = 0, len(book)-1
    while start <= end:
        half = (start + end) // 2
        if order.price == book[half].price:
            return half
        elif order.price < book[half].price:
            end = half - 1
        else: 
            start = half + 1
    return "Not found"
    
#finds the order with the highest priority in the book considering the price of the order
def HigherPriority(book: list, order: object):
    position = len(book)-1
    if position > 0:
        prevPriceBook = book[position-1].price
        while  prevPriceBook == order.price and position >= 1:
            position = position -1
            prevPriceBook = book[position].price
    return position 

def findOrder(id: int, book: list):
    for position,orderBook in enumerate(book):
        if orderBook.id == id:
            return orderBook, position
    return "Not found", print("Invalid ID or Order is not in the book anymore") 
=======
class Algorithms():
    def my_sort(self, book: object, order: object):
        start, end = 0, len(book)
        while start < end:
            half = (start + end) // 2
            if order.price < book[half].price:
                end = half
            else:
                start = half + 1
        book.insert(start, order)
        return

    def serchBinary(self, book: object, order: object):
        start, end = 0, len(book)-1
        while start <= end:
            half = (start + end) // 2
            if order.price == book[half].price:
                return half
            elif order.price < book[half].price:
                end = half - 1
            else: 
                start = half + 1
        return "Not found"
        
    #finds the order with the highest priority in the book considering the price of the order
    def HigherPriority(self, book: object, order: object):
        position = len(book)-1
        if position > 0:
            prevPriceBook = book[position-1].price
            while  prevPriceBook == order.price and position >= 1:
                position = position -1
                prevPriceBook = book[position].price
        return position 

    def findOrder(self, id: int, book: object):
        for position,orderBook in enumerate(book):
            if orderBook.id == id:
                return orderBook, position
        return "Not found", print("Invalid ID or Order is not in the book anymore") 
>>>>>>> b72e43e5a3b83eaaf5ee9642621dc64ffe95ec38
