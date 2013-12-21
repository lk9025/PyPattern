from observable import QuackObservable


class Quackable(QuackObservable):
    def quack(self):
        raise NotImplementedError
