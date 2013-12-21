from factory import CountingDuckFactory
from simulator import DuckSimulator


simulator = DuckSimulator()
simulator.simulate(CountingDuckFactory())
