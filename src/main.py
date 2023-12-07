"""
This Main Script Loads the basic
application for Magnolia usage.
"""

import sys
from argparse import ArgumentParser

from project.project import Project


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

    return parser.parse_args()


def main():
    """
    Main application.
    """
    arguments = get_arguments()

    if arguments.install and arguments.run:
        print("ERROR: Two operations at the same time not supported.")
        sys.exit(-1)
    elif not arguments.install and not arguments.run:
        print("ERROR: An operation must be defined.")

    project = Project(arguments.project)

    if arguments.install:
        print("Install option defined.")
    elif arguments.run:
        print("Run option enabled.")
    else:
        print("Option not defined.")


if __name__ == "__main__":
    main()
