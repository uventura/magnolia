import os

class Runner:
    def __init__(project):
        os.system('java -jar ' + project.data['interpreter'] + ' interpreter -i ' + project.data['main'])