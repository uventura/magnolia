"""
Main Installer class.
"""

from urllib.request import urlretrieve


# pylint: disable=too-few-public-methods
class Installer:
    """
    This part is reposible to download external
    dependencies globaly and locally from a given
    project or command line. In command line the
    download can be done with:
        magnolia install <path>/lib.zip
    """

    def __init__(self):
        pass

    def install(self, url, destiny):
        """
        Install an external library in the specific directory.
        """
        urlretrieve(url, destiny)
