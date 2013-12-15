class Light:
    def __init__(self):
        pass

    def on(self):
        print 'Light is on.'

    def off(self):
        print 'Light is off.'


class CeilingFan:
    def __init__(self):
        self._speed = 'OFF'

    def low(self):
        self._speed = 'LOW'
        print 'Ceiling fan is on low.'

    def medium(self):
        self._speed = 'MEDIUM'
        print 'Ceiling fan is on medium.'

    def high(self):
        self._speed = 'HIGH'
        print 'Ceiling fan is on high.'

    def off(self):
        self._speed = 'OFF'
        print 'Ceiling fan is off.'

    def speed(self):
        return self._speed


class GarageDoor:
    def __init__(self):
        pass

    def open(self):
        print 'Garage door is opened.'

    def close(self):
        print 'Garage door is close.'


class Stereo:
    def __init__(self):
        pass

    def on(self):
        print 'Stereo is on.'

    def off(self):
        print 'Stereo is off.'
