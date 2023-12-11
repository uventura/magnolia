import subprocess


class Tester:
    def __init__(project):
        process = subprocess.run(['sbt', 'test'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)

        lines = str(process.stdout).split('\\n')
        
        print("All tests completed")
        
        for i in lines:
            if i.find("All tests passed") > 0 :
                print("All tests passed")
            elif i.find("fail"):
                print(i)