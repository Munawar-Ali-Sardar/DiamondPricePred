from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(path:str)->List[str]:
    with open(path) as file_obj:
        requirement = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirement]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements

setup(
    name="Diamond Price Prediction",
    author="Munawar ali sardar",
    author_email="me.munawar@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)