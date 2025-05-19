# main.py
from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Emmanuel", "emmanuel@gmail.com")
coffee1 = Coffee("Latte", 450)

order1 = Order(c1, coffee1)

print(c1.name)
print(coffee1.name)
print(order1.price)
print(order1.timestamp)

print("All orders:", Order.get_all_orders())

print("Customer's coffees:", c1.coffees())
print("Coffee's customers:", coffee1.customers())
