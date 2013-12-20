from gumballmachine import GumballMachine


machine = GumballMachine(3)

print machine, '\n'

machine.insert_quarter()
machine.turn_crank()
print machine, '\n'

machine.insert_quarter()
machine.eject_quarter()
machine.insert_quarter()
machine.turn_crank()
print machine, '\n'

machine.turn_crank()
print machine, '\n'

machine.insert_quarter()
machine.turn_crank()
print machine, '\n'

machine.eject_quarter()
machine.insert_quarter()
machine.turn_crank()
print machine, '\n'
