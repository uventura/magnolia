"""
Runner class.
"""

import subprocess
import os
import sys


class Runner:
    """
    Run a single oberon file. The command line will be:
        magnolia run file.oberon
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, interpreter, file):
        if not os.path.isfile(interpreter):
            print(f"[ERROR] The interpreter `{interpreter}` does not exists.")
            sys.exit(-1)
        if not os.path.isfile(file):
            print(f"The file `{file}` does not exists.")
            sys.exit(-1)

        subprocess.run(
            ["java", "-jar", interpreter, "interpreter", "-i", file], check=True
        )
