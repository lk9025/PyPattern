from command import *


class RemoteController:
    def __init__(self):
        self._on_commands = [NoCommand()] * 10
        self._off_commands = [NoCommand()] * 10
        self._pre_command = NoCommand()

    def __repr__(self):
        description = 'Remote Controller:\n'
        for on_command, off_command in\
                zip(self._on_commands, self._off_commands):
            description += ''.join([str(on_command), '\t' * 2,
                                    str(off_command), '\n'])
        return description

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_pushed(self, slot):
        self._on_commands[slot].excute()
        self._pre_command = self._on_commands[slot]

    def off_button_pushed(self, slot):
        self._off_commands[slot].excute()
        self._pre_command = self._off_commands[slot]

    def undo(self):
        self._pre_command.undo()
