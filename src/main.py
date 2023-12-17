"""
This Main Script Loads the basic
application for Magnolia usage.
"""
from cmd_arguments.cmd_arguments import CmdArguments
from environment.environment import Environment
from project.project import Project
from runner.runner import Runner

# from tester.tester import Tester


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
    Environment()
    command = get_arguments()

    if command.type == "init":
        Project(command.value)
    elif command.type == "install":
        print("Install mode")
    elif command.type == "run":
        project = Project(".", False)
        Runner(project.interpreter, command.value)
    elif command.type == "test":
        print("Test mode")


if __name__ == "__main__":
    main()
