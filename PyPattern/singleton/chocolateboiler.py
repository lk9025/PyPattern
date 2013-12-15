from singleton import singleton


@singleton
class ChocolateBoiler(object):
    def __init__(self):
        self._empty = True
        self._boiled = False

    def fill(self):
        if self._empty:
            self._empty = False
            self._boiled = False
            print 'ChocolateBoiler is full now.'

    def drain(self):
        if not self._empty and self._boiled:
            self._empty = True
            print 'ChocolateBoiler is empty now.'

    def boil(self):
        if not self._empty and not self._boiled:
            self._boiled = True
            print 'Chocolate and milk are boiled now.'

    def is_empty(self):
        return self._empty

    def is_boiled(self):
        return self._boiled
