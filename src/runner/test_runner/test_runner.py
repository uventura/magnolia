"""Module providing a testing framework for creating and executing Python test cases."""
import unittest
from unittest.mock import patch
from logger.logger import Logger
from runner.runner import Runner


class TestRunner(unittest.TestCase):
    """
    Test cases for the Runner class.
    """

    def test_runner_with_existing_files(self):
        """
        Tests the behavior of Runner class when given existing files.
        """
        with patch("subprocess.run") as mock_subprocess_run, patch(
            "os.path.isfile", side_effect=[True, True]
        ), patch("sys.exit") as mock_sys_exit:
            interpreter = "../../../data/project_examples/project02/interpreter/oberon.jar"
            file =  "../../../data/project_examples/project02/main.oberon"

            Runner(interpreter, file)

            mock_subprocess_run.assert_called_once_with(
                ["java", "-jar", interpreter, "interpreter", "-i", file], check=True
            )
            mock_sys_exit.assert_not_called()

    def test_runner_with_non_existing_interpreter(self):
        """
        Tests the behavior of Runner when given a non-existing interpreter.
        """
        with patch("os.path.isfile", side_effect=[False, True]), patch.object(
            Logger, "error"
        ) as mock_logger_error, patch("sys.exit") as mock_sys_exit:
            interpreter = "non_existing_interpreter.jar"
            file =  "../../../data/project_examples/project02/main.oberon"

            Runner(interpreter, file)

            mock_logger_error.assert_called_once_with(
                f"The interpreter `{interpreter}` does not exist."
            )
            mock_sys_exit.assert_called_once_with(-1)

    def test_runner_with_non_existing_file(self):
        """
        Tests the behavior of Runner when given a non-existing file.
        """
        with patch("os.path.isfile", side_effect=[True, False]), patch.object(
            Logger, "error"
        ) as mock_logger_error, patch("sys.exit") as mock_sys_exit:
            interpreter = "../../../data/project_examples/project02/interpreter/oberon.jar"
            file = "non_existing_file.oberon"

            Runner(interpreter, file)

            mock_logger_error.assert_called_once_with(
                f"The file `{file}` does not exist."
            )
            mock_sys_exit.assert_called_once_with(-1)


if __name__ == "__main__":
    unittest.main()
