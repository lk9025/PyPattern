from applience import *


class Command:
    def __init__(self):
        pass

    def excute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class NoCommand(Command):
    def __init__(self):
        Command.__init__(self)

    def __repr__(self):
        return 'NoCommand'

    def excute(self):
        print 'No command to excute.'

    def undo(self):
        print 'No command to excute.'


class LightOnCommand(Command):
    def __init__(self, light):
        Command.__init__(self)
        self._light = light

    def __repr__(self):
        return 'LightOnCommand'

    def excute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        Command.__init__(self)
        self._light = light

    def __repr__(self):
        return 'LightOffCommand'

    def excute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class CeilingFanLowCommand(Command):
    def __init__(self, ceiling_fan):
        Command.__init__(self)
        self._ceiling_fan = ceiling_fan

    def __repr__(self):
        return 'CeilingFanLowCommand'

    def excute(self):
        self._pre_speed = self._ceiling_fan.speed()
        self._ceiling_fan.low()

    def undo(self):
        if self._pre_speed == 'OFF':
            self._ceiling_fan.off()
        elif self._pre_speed == 'LOW':
            self._ceiling_fan.low()
        elif self._pre_speed == 'MEDIUM':
            self._ceiling_fan.medium()
        elif self._pre_speed == 'HIGH':
            self._ceiling_fan.high()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan):
        Command.__init__(self)
        self._ceiling_fan = ceiling_fan

    def __repr__(self):
        return 'CeilingFanMediumCommand'

    def excute(self):
        self._pre_speed = self._ceiling_fan.speed()
        self._ceiling_fan.medium()

    def undo(self):
        if self._pre_speed == 'OFF':
            self._ceiling_fan.off()
        elif self._pre_speed == 'LOW':
            self._ceiling_fan.low()
        elif self._pre_speed == 'MEDIUM':
            self._ceiling_fan.medium()
        elif self._pre_speed == 'HIGH':
            self._ceiling_fan.high()


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan):
        Command.__init__(self)
        self._ceiling_fan = ceiling_fan

    def __repr__(self):
        return 'CeilingFanHighCommand'

    def excute(self):
        self._pre_speed = self._ceiling_fan.speed()
        self._ceiling_fan.high()

    def undo(self):
        if self._pre_speed == 'OFF':
            self._ceiling_fan.off()
        elif self._pre_speed == 'LOW':
            self._ceiling_fan.low()
        elif self._pre_speed == 'MEDIUM':
            self._ceiling_fan.medium()
        elif self._pre_speed == 'HIGH':
            self._ceiling_fan.high()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan):
        Command.__init__(self)
        self._ceiling_fan = ceiling_fan

    def __repr__(self):
        return 'CeilingFanOffCommand'

    def excute(self):
        self._pre_speed = self._ceiling_fan.speed()
        self._ceiling_fan.off()

    def undo(self):
        if self._pre_speed == 'OFF':
            self._ceiling_fan.off()
        elif self._pre_speed == 'LOW':
            self._ceiling_fan.low()
        elif self._pre_speed == 'MEDIUM':
            self._ceiling_fan.medium()
        elif self._pre_speed == 'HIGH':
            self._ceiling_fan.high()


class GarageDoorUpCommand(Command):
    def __init__(self, garage_door):
        Command.__init__(self)
        self._garage_door = garage_door

    def __repr__(self):
        return 'GarageDoorUpCommand'

    def excute(self):
        self._garage_door.open()

    def undo(self):
        self._garage_door.close()


class GarageDoorDownCommand(Command):
    def __init__(self, garage_door):
        Command.__init__(self)
        self._garage_door = garage_door

    def __repr__(self):
        return 'GarageDoorDownCommand'

    def excute(self):
        self._garage_door.close()

    def undo(self):
        self._garage_door.open()


class StereoOnCommand(Command):
    def __init__(self, stereo):
        Command.__init__(self)
        self._stereo = stereo

    def __repr__(self):
        return 'StereoOnCommand'

    def excute(self):
        self._stereo.on()

    def undo(self):
        self._stereo.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        Command.__init__(self)
        self._stereo = stereo

    def __repr__(self):
        return 'StereoOffCommand'

    def excute(self):
        self._stereo.off()

    def undo(self):
        self._stereo.on()
