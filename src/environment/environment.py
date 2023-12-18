"""
Environment Setup Class
"""
from pathlib import Path
import os

from logger.logger import Logger

CACHE_NAME = ".oberon"
DEFAULT_CACHE = Path.home() / CACHE_NAME

LIBRARY_CACHE = "OBERON_GLOBAL_CACHE"

INTERPRETER = "OBERON_INTERPRETER"
INTERPRETER_NAME = "oberon.jar"


class Environment:
    """
    This class does the environment setup. Including the
    definition of some environment variables.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self):
        if not os.path.exists(DEFAULT_CACHE):
            os.mkdir(DEFAULT_CACHE)
        if not os.path.exists(DEFAULT_CACHE / "libs"):
            os.mkdir(DEFAULT_CACHE / "libs")
        if not os.path.exists(DEFAULT_CACHE / "bin"):
            Logger.warning(
                "[WARNING] Error to get global interpreter. Put `oberon.jar` "
                f'in {DEFAULT_CACHE / "bin"}'
            )
            os.mkdir(DEFAULT_CACHE / "bin")

        os.environ[LIBRARY_CACHE] = str(DEFAULT_CACHE / "libs")
        os.environ[INTERPRETER] = str(DEFAULT_CACHE / "bin" / INTERPRETER_NAME)
