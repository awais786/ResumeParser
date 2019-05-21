#!/usr/bin/env python

import sys
from setuptools import find_packages, setup


setup(
    name='resume_parser',
    version='0.0.1',
    description='A utility to make parse data from resumes.',
    packages=['resumeparser'],
    install_requires=[
        'gensim==3.7.1',
        'pandas==0.24.2',
        'pdfminer.six==20181108',
        'spacy==2.1.3',
        'PyYAML==5.1'
    ],
)
