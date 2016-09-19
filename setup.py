'''Setup module for setuptools.

See:
https://github.com/janveverka/python-hello
'''

from setuptools import setup, find_packages
from codecs import open
from os import path

base = path.abspath(path.dirname(__file__))

# Read the README file contents for the long description
with open(path.join(base, 'README.rst'), encoding='utf-8') as source:
    readme = source.read()

setup(
    name='hello',
    version='0.1.1',
    description='Yet another example Python project',
    long_description=readme,
    url='https://github.com/janveverka/python-hello',
    author='Jan Veverka',
    author_email='jan.veverka@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',        
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='hello world example',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['peppercorn'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'hello=hello:main',
        ]
    }
)