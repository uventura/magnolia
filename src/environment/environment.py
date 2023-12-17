"""
Environment Setup Class
"""
from pathlib import Path
import os

CACHE_NAME = ".oberon"
DEFAULT_CACHE = Path.home() / CACHE_NAME

LIBRARY_CACHE = "OBERON_GLOBAL_CACHE"

INTERPRETER = "OBERON_INTERPRETER"
INTERPRETER_NAME = "oberon.jar"

class Environment:
    def __init__(self):
        if not os.path.exists(DEFAULT_CACHE):
            os.mkdir(DEFAULT_CACHE)
        if not os.path.exists(DEFAULT_CACHE / "libs"):
            os.mkdir(DEFAULT_CACHE / "libs")
        if not os.path.exists(DEFAULT_CACHE / "bin"):
            print(f'[WARNING] Error to get global interpreter. Put `oberon.jar` in {DEFAULT_CACHE / "bin"}')
            os.mkdir(DEFAULT_CACHE / "bin")
        if not (DEFAULT_CACHE / "bin" / INTERPRETER_NAME).is_file():
            print(f'[WARNING] Error to get global interpreter. Put `oberon.jar` in {DEFAULT_CACHE / "bin"}')

        os.environ[LIBRARY_CACHE] = str(DEFAULT_CACHE / "libs")
        os.environ[INTERPRETER] = str(DEFAULT_CACHE / "bin" / INTERPRETER_NAME)
