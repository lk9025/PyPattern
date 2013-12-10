from beverage import *

milk_houseblend = Milk(HouseBlend())
print 'Beverage:', milk_houseblend.get_description()
print 'price:', '$' + str(milk_houseblend.get_cost())

mocha_darkroast = Mocha(DarkRoast())
print 'Beverage:', mocha_darkroast.get_description()
print 'price:', '$' + str(mocha_darkroast.get_cost())

soy_whip_espresso = Soy(Whip(Espresso()))
print 'Beverage:', soy_whip_espresso.get_description()
print 'price:', '$' + str(soy_whip_espresso.get_cost())

milk_soy_whip_mocha_houseblend = Milk(Soy(Whip(Mocha(HouseBlend()))))
print 'Beverage:', milk_soy_whip_mocha_houseblend.get_description()
print 'price:', '$' + str(milk_soy_whip_mocha_houseblend.get_cost())
