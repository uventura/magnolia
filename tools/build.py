"""
    Create executable
"""

import shutil
import PyInstaller.__main__

PROJECT_NAME = "magnolia"
EXEC_OUTPUT_DIR = "bin"
CACHE_OUTPUT = "output"

PyInstaller.__main__.run(
    [
        "src/main.py",
        "--onefile",
        "--distpath",
        EXEC_OUTPUT_DIR,
        "--workpath",
        f"{CACHE_OUTPUT}/dist",
        "--name",
        PROJECT_NAME,
    ]
)

shutil.rmtree(CACHE_OUTPUT)
