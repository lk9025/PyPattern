from role import *


if __name__ == '__main__':
    knight = Knight()
    knight.speak()
    knight.fight()

    robber = Robber()
    robber.speak()
    robber.fight()

    print 'Robber was disarmed.'

    robber.set_weapon(NoWeapon())
    robber.fight()
