class Beverage:
    def __init__(self):
        self._description = 'Unknown Beverage'
        self._cost = 0.0

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class HouseBlend(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self._description = 'House Blend'
        self._cost = 0.5


class DarkRoast(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self._description = 'Dark Roast'
        self._cost = 0.8


class Espresso(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self._description = 'Espresso'
        self._cost = 0.7


class Condiment(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self._description = 'Unknown Condiment'
        self._cost = 0.0
        self._beverage = None

    def get_description(self):
        return ' '.join([self._beverage.get_description(), self._description])

    def get_cost(self):
        return self._beverage.get_cost() + self._cost


class Milk(Condiment):
    def __init__(self, beverage):
        Condiment.__init__(self)
        self._description = '#Milk'
        self._cost = 0.3
        self._beverage = beverage


class Mocha(Condiment):
    def __init__(self, beverage):
        Condiment.__init__(self)
        self._description = '#Mocha'
        self._cost = 0.2
        self._beverage = beverage


class Soy(Condiment):
    def __init__(self, beverage):
        Condiment.__init__(self)
        self._description = '#Soy'
        self._cost = 0.1
        self._beverage = beverage


class Whip(Condiment):
    def __init__(self, beverage):
        Condiment.__init__(self)
        self._description = '#Whip'
        self._cost = 0.2
        self._beverage = beverage
