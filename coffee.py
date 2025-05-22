class Coffee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Coffee: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_name(value)

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if not name.strip():
            raise ValueError("Coffee name must be a non-empty string.")
        if len(name.strip()) > 30:
            raise ValueError("Coffee name must be 30 characters or fewer.")
        return name.strip()
    
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
        prices = [order.price for order in Order.get_all_orders()
                  if order.coffee == self]
        if prices:
            return round(sum(prices) / len(prices), 2)
        else:
            return print("No orders for this coffee yet: ", 0.0)
