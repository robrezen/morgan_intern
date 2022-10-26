# %%
from exchange import *
from operation import *

def main ():
    exchange = Exchange()
    print("Enter a number or write the order")
    print("1- to exit: \n2- to read a file: \n3- to show orders in the book of orders ")

    while True:
        operation = input()
        if operation == "1":
            break
        elif operation == "2":
            print("Name of the file:")
            file_name = input()
            orders = open(file_name, 'r')
            for order in orders:
                print(f">>>{order}")
                action = Operation()
                action.action(order, exchange)
        elif operation == "3":
            buy, sell = exchange.getOrderBook("buy")

            print("\nOrders in the sell book \n Id, Price, Qty")
            for order in sell:
                print(f"[{order.id}, {order.price}, {order.qty}]")
            print("\nOrders in the buy book \n Id, Price, Qty\n")
            for order in buy:
                print(f"[{order.id}, {order.price}, {order.qty}]")
        else:
            action = Operation()
            action.action(operation, exchange)
            
if __name__ == "__main__":
    main()


# %%
