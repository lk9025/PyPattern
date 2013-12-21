from rpyc import Service
from gumballmachine import GumballMachine


class GumballService(Service):
    def exposed_get_location(self):
        return self._gumball_machine.get_location()

    def exposed_get_state(self):
        return self._gumball_machine.get_state()

    def exposed_get_n_gumballs(self):
        return self._gumball_machine.get_n_gumballs()


class GumballServiceBj(GumballService):
    def __init__(self, conn):
        self._gumball_machine = GumballMachine("Beijing", 10)


class GumballServiceSh(GumballService):
    def __init__(self, conn):
        self._gumball_machine = GumballMachine("Shanghai", 20)
