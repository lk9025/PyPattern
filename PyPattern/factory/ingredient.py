class Dough:
    def __init__(self):
        pass

    def get_name(self):
        return self._name


class ThickCrustDough(Dough):
    def __init__(self):
        Dough.__init__(self)
        self._name = 'Thick Crust Dough'


class ThinCrustDough(Dough):
    def __init__(self):
        Dough.__init__(self)
        self._name = 'Thin Crust Dough'


class Sauce:
    def __init__(self):
        pass

    def get_name(self):
        return self._name


class PlumTomatoSauce(Sauce):
    def __init__(self):
        Sauce.__init__(self)
        self._name = 'Plum Tomato Sauce'


class MarinaraSauce(Sauce):
    def __init__(self):
        Sauce.__init__(self)
        self._name = 'Marinara Sauce'


class Cheese:
    def __init__(self):
        pass

    def get_name(self):
        return self._name


class MozzarellaCheese(Cheese):
    def __init__(self):
        Cheese.__init__(self)
        self._name = 'Mozzarella Cheese'


class ReggianoCheese(Cheese):
    def __init__(self):
        Cheese.__init__(self)
        self._name = 'Reggiano Cheese'


class Veggies:
    def __init__(self):
        pass

    def get_name(self):
        return self._name


class Garlic(Veggies):
    def __init__(self):
        Veggies.__init__(self)
        self._name = 'Garlic'


class Onion(Veggies):
    def __init__(self):
        Veggies.__init__(self)
        self._name = 'Onion'


class Mushroom(Veggies):
    def __init__(self):
        Veggies.__init__(self)
        self._name = 'Mushroom'


class RedPepper(Veggies):
    def __init__(self):
        Veggies.__init__(self)
        self._name = 'Red Pepper'


class Spinach(Veggies):
    def __init__(self):
        Veggies.__init__(self)
        self._name = 'Spinach'


class Eggplants(Veggies):
    def __init__(self):
        Veggies.__init__(self)
        self._name = 'Eggplants'


class Pepperoni:
    def __init__(self):
        pass

    def get_name(self):
        return self._name


class SlicedPepperoni(Pepperoni):
    def __init__(self):
        Pepperoni.__init__(self)
        self._name = 'Sliced Pepperoni'


class Clams:
    def __init__(self):
        pass

    def get_name(self):
        return self._name


class FreshClams(Clams):
    def __init__(self):
        Clams.__init__(self)
        self._name = 'Fresh Clams'


class FrozenClams(Clams):
    def __init__(self):
        Clams.__init__(self)
        self._name = 'Frozen Clams'
