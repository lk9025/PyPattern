from quackable import Quackable
from observable import Observable


class MallardDuck(Quackable):
    def __init__(self):
        self._observable = Observable(self)

    def __repr__(self):
        return "MallardDuck"

    def quack(self):
        print "Quack"
        self.notify_observers()

    def register_observer(self, observer):
        self._observable.register_observer(observer)

    def notify_observers(self):
        self._observable.notify_observers()


class RedheadDuck(Quackable):
    def __init__(self):
        self._observable = Observable(self)

    def __repr__(self):
        return "RedheadDuck"

    def quack(self):
        print "Quack"
        self.notify_observers()

    def register_observer(self, observer):
        self._observable.register_observer(observer)

    def notify_observers(self):
        self._observable.notify_observers()


class DuckCall(Quackable):
    def __init__(self):
        self._observable = Observable(self)

    def __repr__(self):
        return "DuckCall"

    def quack(self):
        print "Kwak"
        self.notify_observers()

    def register_observer(self, observer):
        self._observable.register_observer(observer)

    def notify_observers(self):
        self._observable.notify_observers()


class RubberDuck(Quackable):
    def __init__(self):
        self._observable = Observable(self)

    def __repr__(self):
        return "RubberDuck"

    def quack(self):
        print "Squeak"
        self.notify_observers()

    def register_observer(self, observer):
        self._observable.register_observer(observer)

    def notify_observers(self):
        self._observable.notify_observers()


class Goose:
    def __repr__(self):
        return "Goose"

    def honk(self):
        print "Honk"


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self._goose = goose
        self._observable = Observable(self)

    def __repr__(self):
        return repr(self._goose)

    def quack(self):
        self._goose.honk()
        self.notify_observers()

    def register_observer(self, observer):
        self._observable.register_observer(observer)

    def notify_observers(self):
        self._observable.notify_observers()


class QuackCounter(Quackable):

    number_of_quacks = 0

    def __init__(self, quackable):
        self._quackable = quackable
        self._observable = Observable(self)

    def __repr__(self):
        return repr(self._quackable)

    def quack(self):
        self._quackable.quack()
        QuackCounter.number_of_quacks += 1
        self.notify_observers()

    def register_observer(self, observer):
        self._observable.register_observer(observer)

    def notify_observers(self):
        self._observable.notify_observers()

    @classmethod
    def get_quacks(cls):
        return cls.number_of_quacks


class Flock(Quackable):
    def __init__(self):
        self._quackers = []

    def add(self, quacker):
        self._quackers.append(quacker)

    def quack(self):
        for quacker in self._quackers:
            quacker.quack()

    def register_observer(self, observer):
        for quacker in self._quackers:
            quacker.register_observer(observer)

    def notify_observers(self):
        for quacker in self._quackers:
            quacker.notify_observers()
