from ..coffee import Coffee
from ..customer import Customer

def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_num_orders_and_avg_price():
    coffee = Coffee("Cappuccino")
    c1 = Customer("Leo", "leo@example.com")
    c2 = Customer("Mia", "mia@example.com")

    c1.create_order(coffee, 300)
    c2.create_order(coffee, 500)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 400.0
