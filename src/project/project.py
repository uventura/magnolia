"""
A new project will contain informations about
dependencies, repositories, ...

Each new project will contain a project file
to be analyzed. The project file must have
the name `.oberon.json`.
The Oberon project file must be a json file.
"""

from pathlib import Path
import os
import sys
import json

PROJECT_FILENAME = ".oberon.json"

def get_dot_oberon():
    """
    Get .oberon.json content.
    """
    f = open(PROJECT_FILENAME)
    data = json.load(f)
    f.close()
    return data

class Project:
    def __init__(self, project_path):
        project_path = Path(project_path)
        self.project_file = project_path / PROJECT_FILENAME
        self.data = get_dot_oberon()

        if not self.project_file.is_file():
            print(
                (
                    "ERROR: Project file not defined, please define "
                    f"a '{PROJECT_FILENAME}' file. under the project directory"
                )
            )
            sys.exit(-1)
