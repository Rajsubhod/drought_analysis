from setuptools import setup, find_packages
from src.utils import requirements

# Read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Drought Analysis',
    version='0.1.0',
    description='A machine learning project for understanding drought patterns and classifying drought severity.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=['Rajdeep Mukherjee','Srijani Dasgupta','Jitendra Kumar Bharti','Anshu Sarkar','Tomojit Bhowmick'],
    author_email=['rajdeepmukherjee721@gmail.com'],
    url='',
    packages=find_packages(),
    # include_package_data=True,
    install_requires= requirements(),
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'black',
        ],
    },
    entry_points={
        'console_scripts': [
            # To be updated
            # Add command line scripts here.
            # 'script_name = module:function',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10'
)
