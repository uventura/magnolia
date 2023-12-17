"""
Runner class.
"""

import subprocess


class Runner:
    """
    Run a single oberon file. The command line will be:
        magnolia run file.oberon
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, interpreter, file):
        subprocess.run(
            ["java", "-jar", interpreter, "interpreter", "-i", file], check=True
        )
