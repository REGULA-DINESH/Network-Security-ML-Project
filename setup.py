from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    try:
        requirement_list = []
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found.")
    return requirement_list
setup(
    name="Network_Security_ML_Project",
    version = "0.0.1",
    author = "Dinesh",
    author_email = "dineshregula001@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)