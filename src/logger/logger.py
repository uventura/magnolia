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
