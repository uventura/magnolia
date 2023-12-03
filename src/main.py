"""
This Main Script Loads the basic
application for Magnolia usage.
"""

from argparse import ArgumentParser

def get_arguments():
    """
    Get command line arguments.
    """
    parser = ArgumentParser(description="Magnolia commands.")
    parser.add_argument(
        "--install", "-i", help="Install dependencies from a given file", required=False
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
        print("ERROR: You cannot run and install at the same time.")
    if arguments.install:
        print("Install option defined.")
    elif arguments.run:
        print("Run option enabled.")
    else:
        print("Option not defined.")

if __name__ == "__main__":
    main()
