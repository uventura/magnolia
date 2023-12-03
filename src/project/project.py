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

PROJECT_FILENAME = ".oberon.json"


class Project:
    def __init__(self, project_path):
        project_path = Path(project_path)
        project_file = project_path / PROJECT_FILENAME

        if not project_file.is_file():
            print(
                (
                    "ERROR: Project file not defined, please define "
                    f"a '{PROJECT_FILENAME}' file. under the project directory"
                )
            )
            sys.exit(-1)
