<<<<<<< HEAD
from order import Order

class OrderLimit(Order):
    def __init__(self, type_order: str, side: str, price: int, qty: int, id: int):
        super().__init__(type_order, side, qty)
        self.price = price
=======
from order import Order

class OrderLimit(Order):
    def __init__(self, type_order: str, side: str, price: int, qty: int, id: int):
        super().__init__(type_order, side, qty)
        self.price = price
>>>>>>> b72e43e5a3b83eaaf5ee9642621dc64ffe95ec38
        self.id = id