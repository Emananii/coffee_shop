import re

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
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
        from order import Order
        return [order for order in Order.get_all_orders() if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})

    