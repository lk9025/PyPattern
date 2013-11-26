class AbstractWeapon:
    def __init__(self):
        pass

    def use(self):
        raise NotImplementedError


class NoWeapon(AbstractWeapon):
    def __init__(self):
        AbstractWeapon.__init__(self)

    def use(self):
        print 'No weapon to use.'


class Sword(AbstractWeapon):
    def __init__(self):
        AbstractWeapon.__init__(self)

    def use(self):
        print 'Use a sword to cut.'


class Axe(AbstractWeapon):
    def __init__(self):
        AbstractWeapon.__init__(self)

    def use(self):
        print 'Use an axe to chop.'
