# -*- coding: utf-8 -*-

import pycommand 
import sys

class VersionCommand(pycommand.CommandBase):
    usagestr = 'usage: full-example version'
    description = 'Show version information'

    def run(self):
        print('Python version ' + sys.version.split()[0])
        print('Fileflag = {0}'.format(self.parentFlags['file']))


class HelpCommand(pycommand.CommandBase):
    usagestr = 'usage: checker help [<command>]'
    description = 'Show help information'

    def run(self):
        if self.args and self.args[0] == 'version':
            print(VersionCommand([]).usage)
        print(cmd.usage)


class CommandArgs(pycommand.CommandBase):
  
    usagestr = 'usage: checker [-f <filename>] <command> [<args>]'
    description = (
        'Commands:\n'
        '   help         show this help information\n'
        '   version      show full version information'
    )

    # Mapping of subcommands
    commands = {
        'help': HelpCommand,
        'version': VersionCommand
    }

    optionList = (('log_path', ('l', '<log_path>', 'use specified log_path')), )

    # Optional extra usage information
    usageTextExtra = (
        "See 'checker help <command>' for more information on a "
        "specific command."
    )

    def run(self):
        '''The `run` method of the main command

        After the object has been created, there are 4 instance
        variables ready for you to use to write the flow of the program.
        In this example we use them all::

            error -- Thrown by GetoptError when parsing illegal
                     arguments

            flags -- OrderedDict of parsed options and corresponding
                     arguments, if any.

            usage -- String with usage information. The string
                     is compiled using the values found for `usagestr`,
                     `description`, `optionList` and `usageTextExtra`.

            parentFlags -- Dict of registered `flags` of another
                           `CommandBase` object.

        '''
        try:
            cmd = super(CommandArgs, self).run()
        except pycommand.CommandExit as e:
            return e.err

        # Register a flag of a parent command
        # :Parameters:
        #     - `optionName`: String. Name of option
        #     - `value`: Mixed. Value of parsed flag`
        cmd.registerParentFlag('file', self.flags.file)

        if cmd.error:
            print('checker {cmd}: {error}'
                  .format(cmd=self.args[0], error=cmd.error))
            return 1
        else:
            return cmd.run()


if __name__ == '__main__':
    # Shortcut for reading from sys.argv[1:] and sys.exit(status)
    pycommand.run_and_exit(CommandArgs)