import re

class Customer:
    _all = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Customer._all.append(self)


    @property #getter method for name
    def name(self):
        return self._name

    @name.setter #setter method for name with validation
    def name(self, value):
        self._name = self._validate_name(value)
        
    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not re.fullmatch(r"[A-Za-z]{1,15}", name):
            raise ValueError("Name must be a string of 1 to 15 alphabetic characters")
        return name.strip()

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = self._validate_email(value)
        
    def _validate_email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email must be a valid email address")
        return email.strip()
        
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
        
    
    def orders(self):
        from .order import Order
        return [order for order in Order.get_all_orders() if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from .order import Order
        return Order(customer = self, coffee = coffee, price = price)
    
