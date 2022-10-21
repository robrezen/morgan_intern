class Order():
    def __init__(self, type_order: str, side: str, qty: int):
        self.type_order = type_order
        self.side = side
        self.qty = qty
