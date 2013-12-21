class Monitor:
    def __init__(self, gumball_machine):
        self._gumball_machine = gumball_machine

    def report(self):
        print "Gumball Machine:", self._gumball_machine.get_location()
        print "Current Inventory:", self._gumball_machine.get_n_gumballs()
        print "Current State:", self._gumball_machine.get_state()
