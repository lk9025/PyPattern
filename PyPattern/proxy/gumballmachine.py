import random
import rpyc


class State:
    def insert_quarter(self):
        raise NotImplementedError

    def eject_quarter(self):
        raise NotImplementedError

    def turn_crank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError


class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self._gumball_machine = gumball_machine

    def __repr__(self):
        return "NoQuarterState"

    def insert_quarter(self):
        print 'You inserted a quarter.'
        self._gumball_machine.set_state(self._gumball_machine
                                        .get_has_quarter_state())

    def eject_quarter(self):
        print "You haven't inserted a quarter"

    def turn_crank(self):
        print "You turned, but there's no quarter."

    def dispense(self):
        print "You need to pay first."


class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self._gumball_machine = gumball_machine

    def __repr__(self):
        return "HasQuarterState"

    def insert_quarter(self):
        print "You can't insert another quarter."

    def eject_quarter(self):
        print "Quarter returned."
        self._gumball_machine.set_state(self._gumball_machine
                                        .get_no_quarter_state())

    def turn_crank(self):
        print "You turned..."
        if random.randint(1, 10) % 10 == 0 and\
                self._gumball_machine.get_n_gumballs() > 1:
            self._gumball_machine.set_state(self._gumball_machine
                                            .get_winner_state())
        else:
            self._gumball_machine.set_state(self._gumball_machine
                                            .get_sold_state())

    def dispense(self):
        print "No gumball dispensed."


class SoldState(State):
    def __init__(self, gumball_machine):
        self._gumball_machine = gumball_machine

    def __repr__(self):
        return "SoldState"

    def insert_quarter(self):
        print "Please wait, we're already giving you a gumball."

    def eject_quarter(self):
        print "Sorry, you already turned the crank."

    def turn_crank(self):
        print "Turning twice doesn't give you another gumball!"

    def dispense(self):
        self._gumball_machine.release_ball()
        if self._gumball_machine.get_n_gumballs() > 0:
            self._gumball_machine.set_state(self._gumball_machine
                                            .get_no_quarter_state())
        else:
            print "Oops, out of gumballs!"
            self._gumball_machine.set_state(self._gumball_machine
                                            .get_sold_out_state())


class WinnerState(State):
    def __init__(self, gumball_machine):
        self._gumball_machine = gumball_machine

    def __repr__(self):
        return "WinnerState"

    def insert_quarter(self):
        print "Please wait, we're already giving you a gumball."

    def eject_quarter(self):
        print "Sorry, you already turned the crank."

    def turn_crank(self):
        print "Turning twice doesn't give you another gumball!"

    def dispense(self):
        print "YOU'RE A WINNER! You get two gumballs for your quarter."
        self._gumball_machine.release_ball()
        if self._gumball_machine.get_n_gumballs() == 0:
            print "Oops, out of gumballs!"
            self._gumball_machine.set_state(self._gumball_machine
                                            .get_sold_out_state())
        else:
            self._gumball_machine.release_ball()
            if self._gumball_machine.get_n_gumballs() > 0:
                self._gumball_machine.set_state(self._gumball_machine
                                                .get_no_quarter_state())
            else:
                print "Oops, out of gumballs!"
                self._gumball_machine.set_state(self._gumball_machine
                                                .get_sold_out_state())


class SoldOutState(State):
    def __init__(self, gumball_machine):
        self._gumball_machine = gumball_machine

    def __repr__(self):
        return "SoldOutState"

    def insert_quarter(self):
        print "You can't insert a quarter, the machine is sold out."

    def eject_quarter(self):
        print "You can't eject, you haven't insert a quarter."

    def turn_crank(self):
        print "You turned, but there are no gumballs."

    def dispense(self):
        print "No gumballs dispensed."


class AbstractGumballMachine:
    def insert_quarter(self):
        raise NotImplementedError

    def eject_quarter(self):
        raise NotImplementedError

    def turn_crank(self):
        raise NotImplementedError

    def set_state(self, state):
        raise NotImplementedError

    def get_state(self):
        raise NotImplementedError

    def get_no_quarter_state(self):
        raise NotImplementedError

    def get_has_quarter_state(self):
        raise NotImplementedError

    def get_sold_state(self):
        raise NotImplementedError

    def get_winner_state(self):
        raise NotImplementedError

    def get_sold_out_state(self):
        raise NotImplementedError

    def get_location(self):
        raise NotImplementedError

    def get_n_gumballs(self):
        raise NotImplementedError

    def release_ball(self):
        raise NotImplementedError


class GumballMachine(AbstractGumballMachine):
    def __init__(self, location, n_gumballs):
        self._location = location
        self._n_gumballs = n_gumballs
        self._no_quarter_state = NoQuarterState(self)
        self._has_quarter_state = HasQuarterState(self)
        self._sold_state = SoldState(self)
        self._winner_state = WinnerState(self)
        self._sold_out_state = SoldOutState(self)
        self._current_state = self._no_quarter_state

    def __repr__(self):
        return "Mighty Gumball, Inc.\n" +\
               "Python enabled Standing Gumball Model\n" +\
               "Inventory: " +\
               str(self.get_n_gumballs()) + "\n" +\
               "Machine is waiting for quarter"

    def insert_quarter(self):
        self._current_state.insert_quarter()

    def eject_quarter(self):
        self._current_state.eject_quarter()

    def turn_crank(self):
        self._current_state.turn_crank()
        self._current_state.dispense()

    def set_state(self, state):
        self._current_state = state

    def get_state(self):
        return self._current_state

    def get_no_quarter_state(self):
        return self._no_quarter_state

    def get_has_quarter_state(self):
        return self._has_quarter_state

    def get_sold_state(self):
        return self._sold_state

    def get_winner_state(self):
        return self._winner_state

    def get_sold_out_state(self):
        return self._sold_out_state

    def get_location(self):
        return self._location

    def get_n_gumballs(self):
        return self._n_gumballs

    def release_ball(self):
        print "A gumball comes rolling out the slot..."
        if self._n_gumballs > 0:
            self._n_gumballs -= 1


class GumballMachineProxy(AbstractGumballMachine):
    def __init__(self, address, port):
        self._address = address
        self._port = port
        self._conn = rpyc.connect(address, port)

    def __repr__(self):
        return "Mighty Gumball, Inc.\n" +\
               "Python enabled Standing Gumball Model\n" +\
               "Inventory: " +\
               str(self.get_n_gumballs()) + "\n" +\
               "Machine is waiting for quarter"

    def get_state(self):
        return self._conn.root.get_state()

    def get_location(self):
        return self._conn.root.get_location()

    def get_n_gumballs(self):
        return self._conn.root.get_n_gumballs()
