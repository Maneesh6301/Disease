
from setuptools import find_packages, setup
from typing import List

HYPEN = "-e ."

def requirements(file_path: str) -> List[str]:
    """
    This function reads requirements from a file.
    """
    requirements = []

    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()

    requirements = [req.strip() for req in requirements if req.strip()]

    requirements = [req for req in requirements if req != HYPEN]

    return requirements


setup(
    name="Disease",
    version="0.0.0.1",
    author="Maneesh",
    author_email="maneesh6301@gmail.com",
    packages=find_packages(),
    install_requires=requirements("requirements.txt")
)
