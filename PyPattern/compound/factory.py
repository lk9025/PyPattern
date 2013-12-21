from duck import *


class AbstractFactory:
    def createMallardDuck(self):
        raise NotImplementedError

    def createRedheadDuck(self):
        raise NotImplementedError

    def createDuckCall(self):
        raise NotImplementedError

    def createRubberDuck(self):
        raise NotImplementedError


class DuckFactory(AbstractFactory):
    def createMallardDuck(self):
        return MallardDuck()

    def createRedheadDuck(self):
        return RedheadDuck()

    def createDuckCall(self):
        return DuckCall()

    def createRubberDuck(self):
        return RubberDuck()


class CountingDuckFactory(AbstractFactory):
    def createMallardDuck(self):
        return QuackCounter(MallardDuck())

    def createRedheadDuck(self):
        return QuackCounter(RedheadDuck())

    def createDuckCall(self):
        return QuackCounter(DuckCall())

    def createRubberDuck(self):
        return QuackCounter(RubberDuck())
