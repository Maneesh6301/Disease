from setuptools import find_packages,setup
from typing import List
Hypen="-e ."
def requirements(file_path:str)->List[str]:
    """
    This function require requirements

    """
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        for Hypen in requirements:
            requirements.remove(Hypen)
    return requirements


setup(
name="Disease",
version="0.0.0.1",
author="Maneesh",
author_mail="maneesh6301@gmail.com",
packages=find_packages(),
install_requires=requirements("requirements.txt")
)