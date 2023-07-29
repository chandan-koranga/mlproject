# useful for creating ml projects as a package (anyone can they install your package).

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


# meta data information.

setup(
    name='mlproject',
    version='0.0.1',
    author='Chandan_Singh',
    author_email='chandan.koranga07@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)