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
    """
    Main Project Class.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, project_path):
        project_path = Path(project_path)
        self.project_file = project_path / PROJECT_FILENAME
        self.data = get_dot_oberon()

        if not project_file.is_file():
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
        cache = None
        if "cache" in project_data:
            cache = project_data["cache"]
        elif os.environ.get(CACHE_ENVIRONMENT_VAR):
            cache = os.environ[CACHE_ENVIRONMENT_VAR]
        else:
            cache = DEFAULT_CACHE

        self._create_cache_path(Path(self.project_path) / cache)
        os.environ[PROJECT_ENVIRON_CACHE_NAME] = str(Path(self.project_path) / cache)
        os.environ[PROJECT_GLOBAL_CACHE] = str(DEFAULT_CACHE)

        return cache

    def _create_cache_path(self, cache_path):
        if not os.path.exists(cache_path):
            os.mkdir(cache_path)
