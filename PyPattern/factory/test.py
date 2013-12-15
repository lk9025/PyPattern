from pizzastore import *

separator = '-' * 10

NY_pizza_store = NYPizzaStore()
Chicago_pizza_store = ChicagoPizzaStore()

pizza = NY_pizza_store.order_pizza('cheese')
print separator

pizza = NY_pizza_store.order_pizza('clam')
print separator

pizza = NY_pizza_store.order_pizza('veggies')
print separator

pizza = Chicago_pizza_store.order_pizza('pepperoni')
print separator

pizza = Chicago_pizza_store.order_pizza('veggies')
