"""
Main tester class.
"""
import subprocess


class Tester:
    """
    Tester will run Oberon tests and check its results.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, interpreter, file):
        
        process = subprocess.run(
            ["java", "-jar", interpreter, "interpreter", "-vi", file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True
        )
        output = str(process.stdout.decode('UTF-8')).replace("\\n", "\n").strip()

        f = open("main.test", "r")
        mainTest = f.read()
        f.close()
        
        if(mainTest == output):
            print("Test passed")
        else:
            print("Test failed")


        
        
