from duck import *
from turkey import *


mallard_duck = MallardDuck()
mallard_duck.quack()
mallard_duck.fly()

turkey = WildTurkey()
turkey_adapter = TurkeyAdapter(turkey)
turkey_adapter.quack()
turkey_adapter.fly()
