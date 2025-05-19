class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

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
        from order import Order
        return [order for order in Order.get_all_orders() if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

# coffee1 = Coffee("Espresso", 2.5)
# print(coffee1.name) 
# print(coffee1.price)

# coffee1.price = 3.0
# print(coffee1.price) 

# coffee1.name = "   Cappuccino   "
# print(coffee1.name)
