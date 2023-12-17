"""
This Main Script Loads the basic
application for Magnolia usage.
"""

import sys
from argparse import ArgumentParser

from cmd_arguments.cmd_arguments import CmdArguments
from project.project import Project
from runner.runner import Runner
from tester.tester import Tester


def get_arguments():
    """
    Get command line arguments.
    """
    args = {
        "init": {"default": ".", "description": "Init a magnolia project"},
        "install": {"description": "Install a magnolia program"},
        "run": {"description": "Run an oberon program"},
        "test": {"description": "Run tests"},
    }

    return CmdArguments(args).arg


def main():
    """
    Main application.
    """
    command = get_arguments()
    print(command)


if __name__ == "__main__":
    main()
