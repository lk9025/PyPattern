class Duck:
    def quack(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError


class MallardDuck(Duck):
    def quack(self):
        print 'Quack'

    def fly(self):
        print "I'm flying."


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        self._turkey.fly()
