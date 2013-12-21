from observer import Observer


class Quackologist(Observer):
    def update(self, quackable):
        print "Quackologist:", quackable, "just quacked."
