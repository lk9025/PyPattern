class Turkey:
    def gobble(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError


class WildTurkey(Turkey):
    def gobble(self):
        print 'Gobble gobble.'

    def fly(self):
        print "I'm flying a short distance."
