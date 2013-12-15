from pizzastore import *


seperator = '-' * 10

NY_pizza_store = NYPizzaStore()
Chicago_pizza_store = ChicagoPizzaStore()

pizza = NY_pizza_store.order_pizza('cheese')
print seperator

pizza = NY_pizza_store.order_pizza('clam')
print seperator

pizza = NY_pizza_store.order_pizza('veggies')
print seperator

pizza = Chicago_pizza_store.order_pizza('pepperoni')
print seperator

pizza = Chicago_pizza_store.order_pizza('veggies')
