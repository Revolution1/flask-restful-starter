#!/usr/bin/env python
# encoding=utf-8
from __future__ import print_function

import logging
import os
import sys
from inspect import getdoc

from settings import setup_logging
from utils.multidocopt import DocoptCommand
from utils.multidocopt import NoSuchCommand
from utils.multidocopt import parse_doc_section

log = logging.getLogger(__name__)

console_handler = logging.StreamHandler(sys.stderr)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class TopLevelCommand(DocoptCommand):
    """
    Flask_restful starter

    Usage:
      cli [options] [COMMAND] [ARGS...]

    Options:
      -h, --help     Show this help information and exit.

    Commands:
      version        Print version.
      server         Start server.

    """
    base_dir = '.'

    def perform_command(self, options, handler, command_options):
        handler(command_options)
        return

    def docopt_options(self):
        options = super(TopLevelCommand, self).docopt_options()
        options['version'] = 'v0.1'
        return options

    def version(self, options):
        """
        Show the version information

        Usage: version
        """
        print('v0.1')

    def server(self, options):
        """
        Usage: server
        """
        from gunicorn_runner import run_app
        run_app()


def main():
    setup_logging('DEBUG')
    try:
        command = TopLevelCommand()
        command.sys_dispatch()
    except NoSuchCommand as e:
        commands = "\n".join(parse_doc_section("commands:", getdoc(e.supercommand)))
        log.error("No such command: %s\n\n%s", e.command, commands)
        sys.exit(1)


if __name__ == '__main__':
    main()
