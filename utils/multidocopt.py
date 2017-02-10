from __future__ import print_function

import re
import sys
from inspect import getdoc

from docopt import DocoptExit, docopt


class NoSuchCommand(Exception):
    def __init__(self, command, supercommand):
        super(NoSuchCommand, self).__init__("No such command: %s" % command)

        self.command = command
        self.supercommand = supercommand


def docopt_full_help(docstring, *args, **kwargs):
    try:
        return docopt(docstring, *args, **kwargs)
    except DocoptExit:
        raise SystemExit(docstring)


class DocoptCommand(object):
    def docopt_options(self):
        return {'options_first': True}

    def sys_dispatch(self):
        self.dispatch(sys.argv[1:], None)

    def dispatch(self, argv, global_options):
        self.perform_command(*self.parse(argv, global_options))

    def perform_command(self, *args):
        raise NotImplementedError()

    def parse(self, argv, global_options):
        command_help = getdoc(self)
        options = docopt_full_help(getdoc(self), argv, **self.docopt_options())
        command = options['COMMAND']

        if command is None:
            raise SystemExit(command_help)

        handler = self.get_handler(command)
        docstring = getdoc(handler)

        if docstring is None:
            raise NoSuchCommand(command, self)

        command_options = docopt_full_help(
            docstring, options['ARGS'], options_first=True)
        return options, handler, command_options

    def get_handler(self, command):
        command = command.replace('-', '_')

        if not hasattr(self, command):
            raise NoSuchCommand(command, self)

        return getattr(self, command)


def parse_doc_section(name, source):
    pattern = re.compile('^([^\n]*' + name + '[^\n]*\n?(?:[ \t].*?(?:\n|$))*)',
                         re.IGNORECASE | re.MULTILINE)
    return [s.strip() for s in pattern.findall(source)]
