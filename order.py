from datetime import datetime
from .customer import Customer
from .coffee import Coffee


class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.timestamp = datetime.now()
        Order._all_orders.append(self)

    @classmethod
    def get_all_orders(cls):
        return cls._all_orders

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError(
                "customer must be an instance of the Customer class.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of the Coffee class.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = self._validate_price(value)

    def _validate_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number (int or float).")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        return float(price)

    def __repr__(self):
        return f"<Order: {self.customer.name} ordered {self.coffee.name} for Ksh{self.price}>"
