# helpful in making my machine learnig app as a package and deply in pipeline 
# why we use setup.py :  building the appliation as a package
# create a pyproject.toml instead of this (after the project is finished)
from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = "-e ."
# once you read this in the req.txt file it triggers the setup.py file
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return List of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements] 
        
        requirements = [req.strip() for req in requirements] 
        # the next line will cause /n to be recorded in the reqiurements list , so we need to replace it
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements
# cant use double apostrophe in this for some reason 
setup(
    name = 'ML project',
    version = '0.0.1',
    author = 'Tanmay Khanna',
    email = 'tanmay.khanna04@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)