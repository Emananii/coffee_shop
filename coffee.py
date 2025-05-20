class Coffee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Coffee: {self.name} - Ksh{self.price}>"
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value.strip()
        else:
            raise ValueError("Coffee name must be a non-empty string.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._price = float(value)
        else:
            raise ValueError("Price must be a positive number.")
        
    def orders(self):
        from .order import Order
        return [order for order in Order.get_all_orders() if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        from .order import Order
        return len([order for order in Order.get_all_orders() if order.coffee == self])
    
    def average_price(self):
        from .order import Order
        prices = [order.price for order in Order.get_all_orders() if order.coffee == self]
        if prices:
            return round(sum(prices) / len(prices), 2)
        else:
            return print("No orders for this coffee yet: ", 0.0)
        