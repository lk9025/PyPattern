from menu import MenuItem, Menu
from waitress import Waitress


pancake_house_menu = Menu('PANCAKE HOUSE MENU', 'Breakfast')
diner_menu = Menu('DINER MENU', 'Lunch')
cafe_menu = Menu('CAFE MENU', 'Dinner')
dessert_menu = Menu('DESSERT MENU', 'Dessert')

pancake_house_menu.add(MenuItem("K&B's Pancake Breakfast",
                                "Pancakes with scrambled eggs, and toast",
                                True,
                                2.99))
pancake_house_menu.add(MenuItem("Regular Pancake Breakfast",
                                "Pancakes with fried eggs, sausage",
                                False,
                                2.99))
pancake_house_menu.add(MenuItem("Blueberry Pancakes",
                                "Pancakes made with fresh blueberries",
                                True,
                                3.49))
pancake_house_menu.add(MenuItem("Waffles",
                                "Waffles, with your choice of blueberries" +
                                "or strawberries",
                                True,
                                3.59))

diner_menu.add(MenuItem("Vegetarian BLT",
                        "(Fakin') Bacon with lettuce & tomato on" +
                        "whole wheat",
                        True,
                        2.99))
diner_menu.add(MenuItem("BLT",
                        "Bacon with lettuce & tomato on whole wheat",
                        False,
                        2.99))
diner_menu.add(MenuItem("Soup of the day",
                        "Soup of the day, with a side of potato salad",
                        False,
                        3.29))
diner_menu.add(MenuItem("Hotdog",
                        "A hot dog, with saurkraut, relish, onions," +
                        "topped with cheese",
                        False,
                        3.05))

cafe_menu.add(MenuItem("Veggie Burger and Air Fries",
                       "Veggie burger on a whole wheat bun, lettuce " +
                       "tomato, and fries",
                       True,
                       3.99))
cafe_menu.add(MenuItem("Soup of the day",
                       "A cup of the soup of the day, with a side salad",
                       False,
                       3.69))
cafe_menu.add(MenuItem("Burrito",
                       "A large burrito, with whole pinto beans, salsa" +
                       ", guacamole",
                       False,
                       4.29))

dessert_menu.add(MenuItem("Apple Pie",
                          "Apple pie with flakey crust, topped with " +
                          "vanilla ice cream",
                          True,
                          1.59))

menu = Menu('ALL MENUS', 'All menus combined')
menu.add(pancake_house_menu)
menu.add(diner_menu)
menu.add(cafe_menu)
menu.add(dessert_menu)

waitress = Waitress(menu)
waitress.print_menu()
waitress.print_vegetarian_menu()
