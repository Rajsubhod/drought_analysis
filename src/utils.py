from typing import List


def requirements(path:str='requirements.txt')->List[str]:
    '''
    This function reads the requirements.txt file and returns a list of the requirements
    '''
    required = []
    with open('requirements.txt') as f:
        required = f.read().splitlines()
        required = [x for x in required if x not in ['','.','-e','\n','\t','-e .']]
        return required