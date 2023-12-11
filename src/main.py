"""
This Main Script Loads the basic
application for Magnolia usage.
"""

import sys
from argparse import ArgumentParser

from project.project import Project
from runner.runner import Runner
from tester.tester import Tester

def get_arguments():
    """
    Get command line arguments.
    """
    parser = ArgumentParser(description="Magnolia commands.")
    parser.add_argument(
        "--install", "-i", help="Install dependencies from a given file", required=False
    )
    parser.add_argument(
        "--project",
        "-p",
        help="Project path, the default is the current path",
        default=".",
    )
    parser.add_argument(
        "--run", "-r", help="Run magnolia over a project", required=False
    )
    parser.add_argument(
        "--test", "-t", help="Run all tests of Oberon-Scala", required=False
    )

    return parser.parse_args()


def main():
    """
    Main application.
    """
    arguments = get_arguments()

    if arguments.install and arguments.run and arguments.test:
        print("ERROR: Two operations at the same time not supported.")
        exit(-1)
    elif not arguments.install and not arguments.run and not arguments.test:
        print("ERROR: An operation must be defined.")

    project = Project(arguments.project)
    print(project.cache)

    if arguments.install:
        print("Install option defined.")
    elif arguments.run:
        print("Run option enabled.")
        Runner.__init__(project)
    elif arguments.test:
        print("Running tests...")
        Tester.__init__(project)
    else:
        print("Option not defined.")


if __name__ == "__main__":
    main()
