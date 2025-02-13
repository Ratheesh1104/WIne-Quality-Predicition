from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
  
setup( 
    name='mlproject', 
    version='0.0.1', 
    author='Ratheesh', 
    author_email='m.ratheeshmano@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
) 