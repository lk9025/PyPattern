class QuackObservable:
    def register_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class Observable(QuackObservable):
    def __init__(self, observable):
        self._observable = observable
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._observable)
