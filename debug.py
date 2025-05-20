from .customer import Customer
from .coffee import Coffee
from .order import Order

c1 = Customer("Emmanuel", "emmanuel@gmail.com")
c2 = Customer("Sarah", "sarah@gmail.com")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

c1.create_order(latte, 450)
c1.create_order(latte, 500)
c2.create_order(espresso, 300)

top = Customer.most_aficionado(latte)

print(f"{latte.name} was ordered {latte.num_orders()} times.")
print(f"Average price of {latte.name}: ksh{latte.average_price()}")

if top:
    print(f"The top aficionado for {latte.name} is {top.name}")
else:
    print(f"No aficionados yet for {latte.name}")

print(f"\nOrders by {c1.name}:")
for order in c1.orders():
    print(f"  - {order.coffee.name} at Ksh{order.price} on {order.timestamp}")
