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
import json

PROJECT_FILENAME = "oberon.json"

CACHE_NAME = ".cache_oberon"
PROJECT_ENVIRON_CACHE_NAME = "OBERON_DEPS_CACHE"


class Project:
    """
    Main Project Class.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, project_path, use_project_file=True):
        self.project_path = Path(project_path)
        project_file_path = self.project_path / PROJECT_FILENAME

        if use_project_file and not project_file_path.is_file():
            self._create_project_file(project_file_path)
        elif project_file_path.is_file():
            use_project_file = True

        if use_project_file:
            self._define_project_variables_file(project_file_path)
        else:
            self._define_project_varibles_empty()

    def _define_project_variables_file(self, filepath):
        data = self._load_project_file(filepath)
        self.name = data["name"]
        self.version = self._get_optional_key("version", data)
        self.dependencies = self._get_optional_key("dependencies", data)
        self.repositories = self._get_optional_key("repositories", data)
        self.cache = self._define_cache()
        self.interpreter = self._get_interpreter(data)

    def _define_project_varibles_empty(self):
        self.name = "undefined"
        self.version = "undefined"
        self.dependencies = []
        self.repositories = []
        self.cache = self._define_cache()
        self.interpreter = self._get_interpreter()

    def _create_project_file(self, filepath):
        project_content = {
            "name": "hello_world",
            "version": "0.0.1",
            "dependencies": [],
            "repositories": [],
        }
        json_object = json.dumps(project_content, indent=4)
        with open(filepath, "w", encoding="utf8") as oberon_project:
            oberon_project.write(json_object)

    def _load_project_file(self, filepath):
        with open(filepath, "r", encoding="utf8") as file:
            project_json = json.load(file)
        return project_json

    def _define_cache(self):
        cache_path = Path(self.project_path) / CACHE_NAME
        self._create_cache_path(cache_path)

        return cache_path

    def _create_cache_path(self, cache_path):
        if not os.path.exists(cache_path):
            os.mkdir(cache_path)

    # pylint: disable=dangerous-default-value
    def _get_interpreter(self, data={}):
        if "interpreter" in data:
            return data["interpreter"]
        return os.environ.get("OBERON_INTERPRETER")

    def _get_optional_key(self, key, data):
        if key in data:
            return data[key]
        return None
