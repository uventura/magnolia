"""
Main tester class.
"""
import subprocess


class Tester:
    """
    Tester will run Oberon tests and check its results.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self):
        process = subprocess.run(
            ["sbt", "test"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )

        lines = str(process.stdout).split("\\n")

        print("All tests completed")

        for i in lines:
            if i.find("All tests passed") > 0:
                print("All tests passed")
            elif i.find("fail"):
                print(i)
