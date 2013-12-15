class Pizza:
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print 'Bake for 25 min.'

    def cut(self):
        print 'Cutting pizza into diagonal slices.'

    def box(self):
        print 'Place pizza in official PizzaStore box.'


class NYStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'NYStyleCheesePizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()


class NYStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'NYStyleClamPizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()

        print 'Adding clams...'
        self.clams = self._ingredient_factory.create_clams()
        print self.clams.get_name()


class NYStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'NYStylePepperoniPizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()

        print 'Adding pepperoni...'
        self.pepperoni = self._ingredient_factory.create_pepperoni()
        print self.pepperoni.get_name()


class NYStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'NYStyleVeggiePizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()

        print 'Adding veggies...'
        self.veggies = self._ingredient_factory.create_veggies()
        for veggies in self.veggies:
            print veggies.get_name()


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'ChicagoStyleCheesePizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()


class ChicagoStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'ChicagoStyleClamPizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()

        print 'Adding clams...'
        self.clams = self._ingredient_factory.create_clams()
        print self.clams.get_name()


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'ChicagoStylePepperoniPizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()

        print 'Adding pepperoni...'
        self.pepperoni = self._ingredient_factory.create_pepperoni()
        print self.pepperoni.get_name()


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory):
        Pizza.__init__(self, ingredient_factory)
        self._name = 'ChicagoStyleVeggiePizza'

    def prepare(self):
        print 'Preparing ' + self._name

        print 'Tossing dough...'
        self.dough = self._ingredient_factory.create_dough()
        print self.dough.get_name()

        print 'Adding sauce...'
        self.sauce = self._ingredient_factory.create_sauce()
        print self.sauce.get_name()

        print 'Adding cheese...'
        self.cheese = self._ingredient_factory.create_cheese()
        print self.cheese.get_name()

        print 'Adding veggies...'
        self.veggies = self._ingredient_factory.create_veggies()
        for veggies in self.veggies:
            print veggies.get_name()
