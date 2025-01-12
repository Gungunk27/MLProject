from setuptools import find_packages, setup 
from typing import List
hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' 
    requirements list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        # requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Gungun',
    author_email='gungunkasera27@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)