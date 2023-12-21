"""
Environment Setup Test Class
"""
import os
import sys

# Adjusting the sys.path to include the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import unittest
from pathlib import Path
from environment import Environment

class TestEnvironment(unittest.TestCase):

    def test_environment_setup(self):
        """
        Test the setup of the environment variables and directories.
        """
        # Creating the Environment instance
        env = Environment()

        # Assertions for environment variables
        self.assertEqual(os.environ['OBERON_GLOBAL_CACHE'], str(Path.home() / '.oberon/libs'))
        self.assertEqual(os.environ['OBERON_INTERPRETER'], str(Path.home() / '.oberon/bin/oberon.jar'))

        # Assertions for instance attributes
        self.assertEqual(env.library_cache, str(Path.home() / '.oberon/libs'))
        self.assertEqual(env.interpreter, str(Path.home() / '.oberon/bin/oberon.jar'))

if __name__ == '__main__':
    unittest.main()