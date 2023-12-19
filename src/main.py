"""
This Main Script Loads the basic
application for Magnolia usage.
"""
from cmd_arguments.cmd_arguments import CmdArguments
from environment.environment import Environment
from project.project import Project
from runner.runner import Runner
from installer.installer import Installer

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
    env = Environment()
    command = get_arguments()

    if command.type == "init":
        project = Project(command.value)
        installer = Installer(env.library_cache)
        installer.install_all_deps(project.repositories, project.dependencies)
    elif command.type == "install":
        installer = Installer(env.library_cache)
        installer.install(command.value)
    elif command.type == "run":
        project = Project(".", False)
        Runner(project.interpreter, command.value)
    elif command.type == "test":
        print("Test mode")


if __name__ == "__main__":
    main()
