"""Use this file to install cfc as a module"""
import codecs
import os
from datetime import datetime
from distutils.core import setup
from setuptools import find_packages
from typing import List


def get_version(relative_path: str) -> str:
    """
    Given a relative path to an `__init__.py` inside a python package, return the version.

    :param relative_path: path to `__init__.py`
    :return: version number
    """
    with codecs.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path), "r"
    ) as fp:
        file_content = fp.read()
    for line in file_content.splitlines():
        if line.startswith("__version__"):
            return line.split('"' if '"' in line else "'")[1]
    raise RuntimeError("Unable to find version string.")


def _package_files(directory: str) -> List[str]:
    """
    Recursively walk through a directory structure pulling out all files in that directory
    hierarchy. Used to find package files/data.

    :param directory: a directory to glob
    :return: list of fully qualified paths
    """
    return [
        os.path.join("..", path, filename)
        for (path, directories, filenames) in os.walk(directory)
        for filename in filenames
    ]


def _add_version_suffix(version: str) -> str:
    """
    Add a suffix for the package that is unique to this build. Try the CircleCI build number first,
    then default to current date and time for local usage. As this value is included in a filename,
    use safe characters.

    :return: str, suitable unique suffix.
    """
    version_suffix = os.environ.get("CIRCLE_BUILD_NUM", datetime.utcnow().strftime("%Y%m%d%H%M%S"))
    return (
        version
        if (os.environ.get("CIRCLE_BRANCH") == "master")
        and (os.environ.get("CIRCLE_JOB") == "build-wheel")
        else f"{version}.{version_suffix}"
    )


def prod_dependencies() -> List[str]:
    """
    Pull the dependencies from the requirements dir
    :return: Each of the newlines, strings of the dependencies
    """
    with open("./requirements/prod.txt", "r") as file:
        return file.read().splitlines()


PACKAGE_NAME = "cfc"
PACKAGE_DATA = {PACKAGE_NAME: _package_files(PACKAGE_NAME)}

setup(
    name=PACKAGE_NAME,
    version=_add_version_suffix(get_version(f"{PACKAGE_NAME}/__init__.py")),
    description="Comunidad Familia Cristiana",
    author="Gastón Eduardo Arnau",
    author_email="gea164@gmail.com",
    packages=find_packages(**{"exclude": ["test", "test.*"]}),
    # Uncomment the below line to include additional files into the package, review the
    # implementation of _package_files first
    # package_data=PACKAGE_DATA,
    install_requires=prod_dependencies(),
)
