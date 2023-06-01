#!/usr/bin/env python3
"""A CLI utility for generating JSON resumes per the 1.0.0 spec."""
import argparse
import sys
from schema import Schema

LOGO = """
     ██ ███████  ██████  ███    ██     ██████  ███████ ███████ ██    ██ ███    ███ ███████ 
     ██ ██      ██    ██ ████   ██     ██   ██ ██      ██      ██    ██ ████  ████ ██      
     ██ ███████ ██    ██ ██ ██  ██     ██████  █████   ███████ ██    ██ ██ ████ ██ █████   
██   ██      ██ ██    ██ ██  ██ ██     ██   ██ ██           ██ ██    ██ ██  ██  ██ ██      
 █████  ███████  ██████  ██   ████     ██   ██ ███████ ███████  ██████  ██      ██ ███████ 

"""
VERSION = "0.0.1"


def get_version():
    """Print the version and exit."""
    print(f"Version: {VERSION}")
    sys.exit(0)


def init_sub_command(args):
    """Options for the init sub-command."""
    if args.json_resume:
        Schema.get_json_sample()
    if args.yaml_resume:
        Schema.get_yaml_sample()


def main(argv=None):
    """Main entrypoint for jr."""
    print(LOGO)

    # Create the parser
    description = 'Create the perfect JSON resume!'
    job_options = argparse.ArgumentParser(description=description)

    job_options.add_argument('-v',
                             '--version',
                             default=False,
                             action='store_true',
                             help='Print the version and exit.')

    subcommand_job_options = job_options.add_subparsers(dest='command')

    # Add the 'init' sub-command.
    init_command = subcommand_job_options.add_parser('init',
                                                     help='Initialize a new resume.',
                                                     epilog='Note: All keys are optional.')

    init_command.add_argument('-j',
                              '--json',
                              default=False,
                              dest='json_resume',
                              action='store_true',
                              help='Initialize a new resume as JSON.')
    init_command.add_argument('-y',
                              '--yaml',
                              default=False,
                              dest='yaml_resume',
                              action='store_true',
                              help='Initialize a new resume as YAML.')

    args = job_options.parse_args(argv)

    if args.version:
        get_version()

    # The 'init' sub-command.
    if args.command == 'init':
        init_sub_command(args)


if __name__ == "__main__":
    main()
