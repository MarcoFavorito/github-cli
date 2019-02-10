#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import distutils.cmd
import distutils.log
import fileinput
import re

from setuptools import setup, find_packages

PACKAGE_NAME="github_cli"

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, PACKAGE_NAME, '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name=about['__title__'],
    description=about['__description__'],
    version=about['__version__'],
    author=about['__author__'],
    url=about['__url__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT Software License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[],
    tests_require=["tox"],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': ["github-cli=github_cli.__main__"],
    },
    include_package_data=False,
    zip_safe = False,
    license=about['__license__'],
)

