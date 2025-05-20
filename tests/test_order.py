from ..customer import Customer
from ..coffee import Coffee
from ..order import Order

def test_order_creation():
    c = Customer("Zane", "zane@example.com")
    coffee = Coffee("Flat White")
    order = Order(customer=c, coffee=coffee, price=450)

    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 450
