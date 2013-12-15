from ingredientfactory import *
from pizza import *


class PizzaStore:
    def __init__(self):
        pass

    def _create_pizza(self, pizza_type):
        raise NotImplementedError

    def order_pizza(self, pizza_type):
        pizza = self._create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    def __init__(self):
        PizzaStore.__init__(self)
        self._ingredient_factory = NYPizzaIngredientFactory()

    def _create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return NYStyleCheesePizza(self._ingredient_factory)
        elif pizza_type == 'veggies':
            return NYStyleVeggiePizza(self._ingredient_factory)
        elif pizza_type == 'clam':
            return NYStyleClamPizza(self._ingredient_factory)
        elif pizza_type == 'pepperoni':
            return NYStylePepperoniPizza(self._ingredient_factory)
        else:
            return None


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        PizzaStore.__init__(self)
        self._ingredient_factory = ChicagoPizzaIngredientFactory()

    def _create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza(self._ingredient_factory)
        elif pizza_type == 'veggies':
            return ChicagoStyleVeggiePizza(self._ingredient_factory)
        elif pizza_type == 'clam':
            return ChicagoStyleClamPizza(self._ingredient_factory)
        elif pizza_type == 'pepperoni':
            return ChicagoStylePepperoniPizza(self._ingredient_factory)
        else:
            return None
