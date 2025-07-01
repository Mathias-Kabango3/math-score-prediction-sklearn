from setuptools import find_packages,setup
from typing import List


def get_requirements(filename:str)->list[str]:
    requirements = []
    with open(filename) as f:
        requirements = f.read().splitlines()
        if "-e." in requirements:
            requirements.remove("-e.")
    return requirements

setup(
    name="mlproject1",
    version="0.0.1",
    author="Mathias Kabango",
    author_email="kabangomathias0@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)