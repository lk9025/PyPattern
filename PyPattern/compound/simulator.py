from duck import Goose, GooseAdapter, QuackCounter, Flock
from quackologist import Quackologist


class DuckSimulator:
    def simulate(self, factory):
        redhead_duck = factory.createRedheadDuck()
        duck_call = factory.createDuckCall()
        rubber_duck = factory.createRubberDuck()
        goose_duck = GooseAdapter(Goose())

        print "\nDuck Simulator"

        flock_of_ducks = Flock()
        flock_of_ducks.add(redhead_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)
        flock_of_ducks.add(goose_duck)

        flock_of_mallards = Flock()
        flock_of_mallards.add(factory.createMallardDuck())
        flock_of_mallards.add(factory.createMallardDuck())
        flock_of_mallards.add(factory.createMallardDuck())
        flock_of_mallards.add(factory.createMallardDuck())

        flock_of_ducks.add(flock_of_mallards)

        quackologist = Quackologist()
        flock_of_ducks.register_observer(quackologist)

        print "\nDuck Simulator: Whole Flock Simulation"

        self._simulate(flock_of_ducks)

        print "\nDuck Simulator: Mallard Flock Simulation"

        self._simulate(flock_of_mallards)

        print "\nThe ducks quacked", str(QuackCounter.get_quacks()), "times."

    def _simulate(self, quackable):
        quackable.quack()
