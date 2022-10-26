from order import Order

class OrderLimit(Order):
    def __init__(self, type_order: str, side: str, price: int, qty: int, id: int):
        super().__init__(type_order, side, qty)
        self.price = price
        self.id = id