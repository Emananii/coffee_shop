from datetime import datetime
from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []
    def __init__(self, customer, coffee, price=None):
        self.customer = customer
        self.coffee = coffee
        self.price = price if price is not None else coffee.price
        self.timestamp = datetime.now()
        Order._all_orders.append(self)

    def __repr__(self):
        return f"<Order: {self.customer.name} ordered {self.coffee.name} for Ksh{self.price}>"
    @classmethod
    def get_all_orders(cls):
        return cls._all_orders

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise TypeError("customer must be an instance of the Customer class.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise TypeError("coffee must be an instance of the Coffee class.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._price = float(value)
        else:
            raise ValueError("Price must be a positive number.")


# c1 = Customer("Emmanuel", "emmanuelwambugu5@gmail.com")
# coffee1 = Coffee("Latte", 4.5)

# order1 = Order(c1, coffee1)
# print(order1.customer.name)   # Alice
# print(order1.coffee.name)     # Latte
# print(order1.price)           # 4.5
# print(order1.timestamp)       # Current datetime

# print("All orders:", Order.get_all_orders())
# print("Customer's coffees:", c1.coffees())
# print("Coffee's customers:", coffee1.customers())
