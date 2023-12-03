"""
A new project will contain informations about
dependencies, repositories, ...

Each new project will contain a project file
to be analyzed. The project file must have
the name `.oberon.prj`.
The Oberon project file must be a json file.
"""

from pathlib import Path

PROJECT_FILENAME = ".oberon.prj"

class Project:
    def __init__(self, project_path):
        project_path = Path(project_path)
        project_file = project_path / PROJECT_FILENAME
        print(str(project_file.resolve()))
