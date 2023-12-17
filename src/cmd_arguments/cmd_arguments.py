"""
Arguments interface for Magnolia.
"""
import sys

NUM_ARGUMENTS_IN_LINE = 3


class CmdArguments:
    """
    CmdArguments is the command line argument interface
    to use in Magnolia.
    The arguments are exclusive, and you cannot execute
    multiple argument, so you're allowed to use:
        - magnolia run <path>/file.oberon
        - magnolia init <path>
        - [...]
    With the "arguments" parameter you define which arguments
    can be executed, and its value can be:
        arguments = {
            "my_argument": {
                "default": False,
                "description": "This is my argument"
            },
            [...]
        }
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, arguments):
        self.args = arguments

        self.arg = self._argument_existence()
        if self.arg == "help":
            self._helper()

    def _argument_existence(self):
        cmd_args = sys.argv[1:]
        if len(cmd_args) == 1 and (cmd_args[0] == "-h" or cmd_args[0] == "--help"):
            return "help"

        for arg, info in self.args.items():
            if cmd_args[0] == arg and len(cmd_args) == 2:
                return (cmd_args[0], cmd_args[1])
            if cmd_args[0] == arg and "default" in info:
                return (arg, info["default"])
            if cmd_args[0] == arg:
                print("[ERROR] Missing parameters in command line.")
                sys.exit(-1)

        print("[ERROR] Wrong command line usage.")
        sys.exit(-1)

    def _helper(self):
        print("==========================================")
        print("|       Magnolia Command Interface       |")
        print("==========================================")

        for arg, info in self.args.items():
            print(f'|    {arg}: {info["description"]}')

        print("==========================================")
        print("\nEach command must be executed alone.")
