"""Module providing a testing framework for creating and executing Python test cases."""
import unittest
import os
import json
from project.project import Project


class TestProject(unittest.TestCase):
    """
    Test cases for the Project class.
    """

    def setUp(self):
        """
        Set up a temporary project path for testing.
        """
        self.temp_project_path = os.path.join(os.getcwd(), "temp_project_test")
        os.makedirs(self.temp_project_path, exist_ok=True)

    def tearDown(self):
        """
        Clean up the temporary project path after testing.
        """
        if os.path.exists(self.temp_project_path):
            for root, dirs, files in os.walk(self.temp_project_path, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for directory in dirs:
                    os.rmdir(os.path.join(root, directory))
            os.rmdir(self.temp_project_path)

    def test_init_with_project_file(self):
        """
        Test the initialization of Project with a project file.
        """
        project_file_path = os.path.join(self.temp_project_path, "oberon.json")
        project_content = {
            "name": "test_project",
            "version": "1.0.0",
            "dependencies": ["dep1", "dep2"],
            "repositories": ["repo1", "repo2"],
        }

        # Create a project file with specified content
        with open(project_file_path, "w", encoding="utf-8") as file:
            json.dump(project_content, file)

        # Initialize Project with the temporary project path
        project = Project(self.temp_project_path)

        # Validate project attributes match the provided content
        self.assertEqual(project.name, "test_project")
        self.assertEqual(project.version, "1.0.0")
        self.assertListEqual(project.dependencies, ["dep1", "dep2"])
        self.assertListEqual(project.repositories, ["repo1", "repo2"])

    def test_init_without_project_file(self):
        """
        Test the initialization of Project without a project file.
        """
        # Initialize Project without providing a project file
        project = Project(self.temp_project_path)

        # Validate default attribute values of an uninitialized Project instance
        self.assertEqual(project.name, "undefined")
        self.assertEqual(project.version, "undefined")
        self.assertListEqual(project.dependencies, [])
        self.assertListEqual(project.repositories, [])

    def test_create_project_file(self):
        """
        Test the creation of a project file by Project.
        """
        # Create Project instance with 'use_project_file' as True to generate a project file
        # project = Project(self.temp_project_path, use_project_file=True)
        project_file_path = os.path.join(self.temp_project_path, "oberon.json")

        # Assert that the project file has been created
        self.assertTrue(os.path.exists(project_file_path))

        # Load the content of the created project file
        with open(project_file_path, "r", encoding="utf-8") as file:
            content = json.load(file)

        # Validate the content of the created project file
        self.assertEqual(content["name"], "hello_world")
        self.assertEqual(content["version"], "0.0.1")
        self.assertListEqual(content["dependencies"], [])
        self.assertListEqual(content["repositories"], [])


if __name__ == "__main__":
    unittest.main()
