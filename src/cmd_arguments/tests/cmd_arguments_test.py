import os
import sys

# Adjusting the sys.path to include the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import unittest
from unittest.mock import patch
from cmd_arguments import CmdArguments

class TestCmdArguments(unittest.TestCase):
    """
    Unit Test for the cmd_arguments Class.
    Tests the existence of --help, and calling of the function with valid and invalid commands.
    """

    def test_argument_existence_help(self):
        """
        Test for the case when '--help' is provided as a command.
        Ensures that the help message is printed.
        """
        # Mocking sys.argv
        with patch('sys.argv', ['magnolia.py', '--help']):
            # Mocking builtins.print to capture printed output
            with patch('builtins.print') as mock_print:
                CmdArguments({"my_argument": {"default": False, "description": "This is my argument"}})
                # Assertions
                mock_print.assert_called_with("\nEach command must be executed alone.")

    def test_argument_existence_invalid_command(self):
        """
        Test for the case when an invalid command is provided.
        Ensures that the program exits with an error code.
        """
        # Testing the case when an invalid command is given
        with patch('sys.argv', ['magnolia.py', 'another_argument']):
            with self.assertRaises(SystemExit) as cm:
                CmdArguments({"my_argument": {"default": False, "description": "This is my argument"}})
            self.assertEqual(cm.exception.code, -1)

    def test_argument_existence_missing_command(self):
        """
        Test for the case when no command is provided.
        Ensures that the program exits with an error code and prints an error message.
        """
        # Patch sys.argv to simulate the command line arguments
        with patch('sys.argv', ['magnolia.py']), \
             patch('builtins.print') as mock_print:
            
            # Use assertRaises to check if SystemExit is raised
            with self.assertRaises(SystemExit):
                CmdArguments({"my_argument": {"default": False, "description": "This is my argument"}})

            # Assertions
            mock_print.assert_called_with("[ERROR] Please choose a command.")

    def test_argument_existence_valid_command(self):
        """
        Test for the case when a valid command with parameters is provided.
        Ensures that the command and its parameters are correctly parsed.
        """
        # Testing the case when a valid command is given with parameters
        with patch('sys.argv', ['magnolia.py', 'my_argument', 'value']):
            args = CmdArguments({"my_argument": {"default": False, "description": "This is my argument"}})
            self.assertEqual(args.arg, ('my_argument', 'value'))

    def test_argument_existence_default_command(self):
        """
        Test for the case when a valid command with a default value is provided.
        Ensures that the command with the default value is correctly parsed.
        """
        # Testing the case when a valid command with default value is given
        with patch('sys.argv', ['magnolia.py', 'my_argument']):
            args = CmdArguments({"my_argument": {"default": "default_value", "description": "This is my argument"}})
            self.assertEqual(args.arg, ('my_argument', 'default_value'))

if __name__ == '__main__':
    unittest.main()