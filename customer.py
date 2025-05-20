import re

class Customer:
    _all = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Customer._all.append(self)

    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_spent = 0

        for customer in cls._all:
            total_spent = sum(
                order.price for order in customer.orders() if order.coffee == coffee
            )

            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer

        return top_customer if max_spent > 0 else None
    def __repr__(self):
        return f"<Customer: {self.name} - ({self.email})>"

    @property #getter method for name
    def name(self):
        return self._name

    @name.setter #setter method for name with validation
    def name(self, value):
        if isinstance(value, str):
            if re.fullmatch(r"[A-Za-z]{1,15}", value):
                self._name = value
            else:
                raise ValueError(
                    "Name must be a string of 1 to 15 alphabetic characters")
        else:
            raise TypeError("Name must be a string")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if isinstance(value, str):
            if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
                self._email = value
            else:
                raise ValueError("Email must be a valid email address")
        else:
            raise TypeError("Email must be a string")
        
    
    def orders(self):
        from .order import Order
        return [order for order in Order.get_all_orders() if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from .order import Order
        return Order(customer = self, coffee = coffee, price = price)
    
