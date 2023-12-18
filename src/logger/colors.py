"""
Colors class.
"""

from colorama import Fore, Style


class Colors:
    """
    This class only return colorful values.
    """

    defined_colors = {
        "red": Fore.RED + Style.BRIGHT,
        "green": Fore.GREEN + Style.BRIGHT,
        "blue": Fore.BLUE + Style.BRIGHT,
        "yellow": Fore.YELLOW + Style.BRIGHT,
        "cyan": Fore.CYAN + Style.BRIGHT,
        "reset": Style.RESET_ALL,
    }

    @classmethod
    def red(cls, message):
        """
        Returns a red message.
        """
        return f'{cls.defined_colors["red"]}{message}{cls.defined_colors["reset"]}'

    @classmethod
    def green(cls, message):
        """
        Returns a green message.
        """
        return f'{cls.defined_colors["green"]}{message}{cls.defined_colors["reset"]}'

    @classmethod
    def blue(cls, message):
        """
        Returns a blue message.
        """
        return f'{cls.defined_colors["blue"]}{message}{cls.defined_colors["reset"]}'

    @classmethod
    def yellow(cls, message):
        """
        Returns a yellow message.
        """
        return f'{cls.defined_colors["yellow"]}{message}{cls.defined_colors["reset"]}'

    @classmethod
    def cyan(cls, message):
        """
        Returns a cyan message.
        """
        return f'{cls.defined_colors["cyan"]}{message}{cls.defined_colors["reset"]}'
