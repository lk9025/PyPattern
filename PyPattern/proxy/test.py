from gumballmachine import GumballMachineProxy
from gumballmonitor import Monitor


machine_bj = GumballMachineProxy('localhost', 9999)
machine_sh = GumballMachineProxy('localhost', 9998)

monitors = {'Beijing': Monitor(machine_bj), 'Shanghai': Monitor(machine_sh)}

monitors['Beijing'].report()
monitors['Shanghai'].report()
