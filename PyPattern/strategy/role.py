from weapon import *


class AbstractRole:
    def __init__(self):
        pass

    def speak(self):
        raise NotImplementedError

    def fight(self):
        self._weapon.use()

    def set_weapon(self, weapon):
        self._weapon = weapon


class Knight(AbstractRole):
    def __init__(self):
        AbstractRole.__init__(self)
        self._weapon = Sword()

    def speak(self):
        print "I'm a knight."


class Robber(AbstractRole):
    def __init__(self):
        AbstractRole.__init__(self)
        self._weapon = Axe()

    def speak(self):
        print "I'm a robber."
