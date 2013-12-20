class MenuComponent:
    def add(self, menu_component):
        raise NotImplementedError

    def create_iterator(self):
        raise NotImplementedError

    def remove(self, menu_component):
        raise NotImplementedError

    def get_child(self, i):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError

    def is_vegetarian(self):
        raise NotImplementedError

    def print_(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def is_vegetarian(self):
        return self._vegetarian

    def print_(self):
        print ' ' + self.get_name(),
        print '(v)' if self.is_vegetarian() else '',
        print ', ' + str(self.get_price()),
        print '  -- ' + self.get_description()


class Menu(MenuComponent):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._menu_components = []

    def add(self, menu_component):
        self._menu_components.append(menu_component)

    def create_iterator(self):
        return CompositeIterator(MenuIterator(self._menu_components))

    def remove(self, menu_component):
        self._menu_components.remove(menu_component)

    def get_child(self, i):
        return self._menu_components[i]

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def print_(self):
        print '\n' + self.get_name(),
        print ', ' + self.get_description()
        print '-' * 15
        for menu_component in self._menu_components:
            menu_component.print_()


class Iterator:
    def has_next(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError


class MenuIterator(Iterator):
    def __init__(self, menu_components):
        self._menu_components = menu_components
        self._pos = 0

    def has_next(self):
        return self._pos < len(self._menu_components)

    def next(self):
        if self.has_next():
            menu_component = self._menu_components[self._pos]
            self._pos += 1
            return menu_component
        else:
            raise StopIteration

    def remove(self):
        self._menu_components.remove(self._pos)


class CompositeIterator(Iterator):
    def __init__(self, iterator):
        self._iterators = [iterator]

    def has_next(self):
        if len(self._iterators) == 0:
            return False
        else:
            iterator = self._iterators[-1]
            if not iterator.has_next():
                self._iterators.pop()
                return self.has_next()
            else:
                return True

    def next(self):
        if self.has_next():
            iterator = self._iterators[-1]
            component = iterator.next()
            if isinstance(component, Menu):
                self._iterators.append(component.create_iterator())
            return component
        else:
            raise StopIteration
