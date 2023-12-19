"""
Main Installer class.
"""
import os
import requests
import json
import sys

from urllib.parse import urlparse
from pathlib import Path
from zipfile import ZipFile
from collections import namedtuple

from logger.logger import Logger
from logger.colors import Colors

ACCEPTED_FILE_TYPES = ["zip", "rar"]

# pylint: disable=too-few-public-methods
class Installer:
    """
    This part is reposible for downloading external
    dependencies globally and locally from a given
    project or command line. In command line the
    download can be done with:
        magnolia install <path>/lib.zip
    """

    def __init__(self, cache_path):
        self.cache_path = cache_path
        pass

    def install_all_deps(self, repositories, dependencies):
        repositories = list(set(repositories))
        dependencies = list(set(dependencies))

        if not repositories and not dependencies:
            return

        for dep in dependencies:
            found = False
            if not repositories:
                Logger.error("Any repository defined yet.")
            for rep in repositories:
                result = self.install_dep(f"{rep}/{dep}.zip")
                if result["result"]:
                    Logger.successfull_progress(f"{dep}: Installed from {rep}")
                    found = True
                    break
            if not found:
                Logger.error_progress(f"{dep}: Not found.")

    def install(self, url):
        result = self.install_dep(url)
        if result["result"]:
            print(result["message"])
            return
        for error in result["errors"]:
            print(error)

    def install_dep(self, url):
        url_checked = self._check_url_consistency(url)
        if url_checked.errors:
            install_result = {
                "result": False,
                "errors": url_checked.errors,
                "message": None,
                "url": url
            }
            return install_result

        download_path = (self.cache_path + "/" + url_checked.filename + "." + url_checked.filetype)
        folder_path = (self.cache_path + "/" + url_checked.filename)

        errors = []
        response = requests.get(url, stream=True)
        if response.status_code == 404:
            errors.append(Colors.red("404: File not found."))
        elif response.status_code != 200:
            errors.append(Colors.red("HTTP Error " + str(response.status_code)))

        if errors:
            return {
                "result": False,
                "errors": errors,
                "message": None,
                "url": url
            }

        os.makedirs(os.path.dirname(download_path), exist_ok=True)
        with open(download_path, "wb") as f:
            f.write(response.content)

        os.makedirs(os.path.dirname(folder_path), exist_ok=True)
        with ZipFile(download_path, "r") as zObject:
            zObject.extractall(folder_path)

        os.remove(download_path)

        return {
            "result": True,
            "message": Colors.green(f"Dependency {url_checked.filename} downloaded from {url}"),
            "errors": [],
            "url": url
        }

    def _check_url_consistency(self, url):
        parsed_url = urlparse(url)
        error_type = []

        if not parsed_url.scheme:
            error_type.append(Colors.red("Wrong URL Scheme"))
        if not parsed_url.netloc:
            error_type.append(Colors.red("Wrong netlocation URL."))
        if (parsed_url.path.split(".")[-1] not in ACCEPTED_FILE_TYPES):
            error_type.append(Colors.red("File type provided not accepted."))

        url_check = namedtuple("UrlCheck", ["filename", "filetype", "errors"])
        url_split = parsed_url.path.split("/")[-1].split(".")

        return url_check(url_split[0], url_split[1], error_type)
