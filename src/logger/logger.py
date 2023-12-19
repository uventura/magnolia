"""
Main Logger Class.
"""

from .colors import Colors


class Logger:
    """
    The Logger class displays log messages in terminal.
    """

    @staticmethod
    def error(message):
        """
        Print a colorful error message.
        """
        prefix = Colors.red("[Magnolia Error]")
        print(f"{prefix} {message}")

    @staticmethod
    def warning(message):
        """
        Print a colorful warning message.
        """
        prefix = Colors.yellow("[Magnolia Warning]")
        print(f"{prefix} {message}")

    @staticmethod
    def success(message):
        """
        Print a colorful sucess message.
        """
        prefix = Colors.green("[Magnolia Success]")
        print(f"{prefix} {message}")

    @staticmethod
    def successfull_progress(message):
        """
        Print a colorful sucess message.
        """
        result = Colors.green(message)
        print(f"{result}")

    @staticmethod
    def error_progress(message):
        """
        Print a colorful error message.
        """
        result = Colors.red(message)
        print(f"{result}")
