class Waitress:
    def __init__(self, all_menus):
        self._all_menus = all_menus

    def print_menu(self):
        self._all_menus.print_()

    def print_vegetarian_menu(self):
        print '\nVEGETARIAN MENU'
        print '-' * 15
        iterator = self._all_menus.create_iterator()
        while iterator.has_next():
            component = iterator.next()
            try:
                if component.is_vegetarian():
                    component.print_()
            except NotImplementedError:
                pass
