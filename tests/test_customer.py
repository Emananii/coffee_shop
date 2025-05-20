import pytest
from ..customer import Customer
from ..coffee import Coffee
from ..order import Order

def test_customer_creation():
    customer = Customer("Alice", "alice@example.com")
    assert customer.name == "Alice"
    assert customer.email == "alice@example.com"

def test_invalid_customer_name():
    with pytest.raises(ValueError):
        Customer("1234", "bad@example.com")

def test_invalid_email():
    with pytest.raises(ValueError):
        Customer("Bob", "bad-email")

def test_create_order_and_orders():
    customer = Customer("John", "john@example.com")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 400)

    assert order in customer.orders()
    assert coffee in customer.coffees()

def test_most_aficionado():
    c1 = Customer("Anna", "anna@example.com")
    c2 = Customer("Beth", "beth@example.com")
    latte = Coffee("Latte")

    c1.create_order(latte, 500)
    c2.create_order(latte, 400)
    c1.create_order(latte, 300)

    assert Customer.most_aficionado(latte) == c1
