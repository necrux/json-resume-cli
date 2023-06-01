#!/usr/bin/env python3
"""A CLI utility for generating JSON resumes per the 1.0.0 spec."""
import argparse
import sys

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

    args = job_options.parse_args(argv)

    if args.version:
        get_version()


if __name__ == "__main__":
    main()
