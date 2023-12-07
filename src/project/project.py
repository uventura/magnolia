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

PROJECT_FILENAME = "oberon.json"

CACHE_ENVIRONMENT_VAR = "OBERON_CACHE"
DEFAULT_CACHE = Path.home() / "cache_oberon"


class Project:
    """
    Main Project Class.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, project_path):
        self.project_path = Path(project_path)
        project_file_path = self.project_path / PROJECT_FILENAME

        if not project_file_path.is_file():
            print(
                (
                    "ERROR: Project file not defined, please define "
                    f"a '{PROJECT_FILENAME}' file. under the project directory"
                )
            )
            sys.exit(-1)

        self._define_project_variables(project_file_path)

    def _define_project_variables(self, filepath):
        data = self._load_project_file(filepath)
        self.name = data["name"]
        self.version = data["version"]
        self.dependencies = data["dependencies"]
        self.repositories = data["repository"]
        self.cache = self._define_cache(data)

    def _load_project_file(self, filepath):
        with open(filepath, "r", encoding="utf8") as file:
            project_json = json.load(file)
        return project_json

    def _define_cache(self, project_data):
        if "cache" in project_data:
            return project_data["cache"]
        if os.environ.get(CACHE_ENVIRONMENT_VAR):
            return os.environ[CACHE_ENVIRONMENT_VAR]

        if not os.path.exists(DEFAULT_CACHE):
            os.mkdir(DEFAULT_CACHE)
        return DEFAULT_CACHE
