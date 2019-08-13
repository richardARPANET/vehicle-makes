#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
from codecs import open

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('README.rst', 'r', encoding='utf-8') as rm_file:
    readme = rm_file.read()

with open('HISTORY.rst', 'r', encoding='utf-8') as hist_file:
    history = hist_file.read()

setup(
    name='vehicle-makes',
    version='0.1.0',
    packages=find_packages('src', exclude=('tests', )),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    description=(
        'Python library to provide up-to-date vehicle make and model data'
    ),
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    url='https://code.richard.do/richardARPANET/vehicle-makes/',
    license='Apache 2.0',
    long_description=readme + '\n\n' + history,
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
