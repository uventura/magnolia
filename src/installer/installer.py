"""
Main Installer class.
"""
import os
import requests
import json

from urllib.parse import urlparse
from pathlib import Path
from zipfile import ZipFile 

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
        for dep in dependencies:
            if dep in [name for name in os.listdir(self.cache_path) if os.path.isdir(name)]:
                print(f"Dependecy {dep} already installed!")
                continue
            dep_cache = repositories
            while (True):
                if (len(dep_cache) == 0):
                    print(f"Dependency {dep} not found in any repository.")
                    break
                rep = dep_cache.pop(0)
                
                try:
                    self.install(f"{rep}/{dep}.zip")
                    # print(f"Dependency {dep} downloaded from {rep}.")   # Decidir se esse print fica aqui ou no próprio install()
                    break
                except:
                    continue

    def install(self, url: str):
        """
        Install an external library in the specific directory.
        """
        try:
            (filename, filetype) = self._check_url(url)
            download_path = (self.cache_path + "/" + filename + "." + filetype)
            folder_path = (self.cache_path + "/" + filename)

            response = requests.get(url, stream=True)
            if (response.status_code != 200):
                if (response.status_code == 404):
                    raise ConnectionError("File not found.")
                raise ConnectionError("HTTP Error " + response.status_code)
            
            # Creates path and downloads the file
            os.makedirs(os.path.dirname(download_path), exist_ok=True)
            with open(download_path, "wb") as f:
                f.write(response.content)

            os.makedirs(os.path.dirname(folder_path), exist_ok=True)
            with ZipFile(download_path, "r") as zObject:
                zObject.extractall(folder_path)

            os.remove(download_path)

            print(f"Dep ${filename} installed succesfully")
        except Exception as err:
            print(err) # Substituir quando o logger ficar pronto!

    def _check_url(self, url: str) -> (str, str):
        """
        Checks the given URL, raising an error if its invalid or it's file type is not accepted.

        Returns (filename, filetype)
        """
        parsed_url = urlparse(url)
        if not (parsed_url.scheme or parsed_url.netloc):
            raise LookupError("URL provided is INVALID.")
        if (parsed_url.path.split(".")[-1] not in ACCEPTED_FILE_TYPES):
            raise TypeError("File type provided not accepted.")

        # Returns the name and the type of the file being downloaded (filename, filetype)
        return parsed_url.path.split("/")[-1].split(".")


installer = Installer(str(Path.home() / ".oberon" / "libs"))
installer.install_all_deps(["", "http://www.gutenberg.lib.md.us/4/8/8/2/48824"], ["48824-8"])