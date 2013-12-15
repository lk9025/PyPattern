from chocolateboiler import ChocolateBoiler


boiler1 = ChocolateBoiler()
boiler2 = ChocolateBoiler()

print boiler1 is boiler2

boiler1.fill()
boiler2.boil()
boiler1.drain()
