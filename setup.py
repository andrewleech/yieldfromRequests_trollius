#!/usr/bin/env python

import os
import sys

import requests

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'yieldfrom_t',
    'yieldfrom_t.requests',
]

requires = ['chardet>=2.2.1', 'certifi', 'yieldfrom_t.http.client', 'yieldfrom_t.urllib3', 'setuptools', 'trollius']

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='yieldfrom_t.requests',
    version=requests.__version__,
    description='asyncio (trollius) Python HTTP for Humans.',
    long_description=readme + '\n\n' + history,

    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    maintainer='David Keeney',
    maintainer_email='dkeeney@rdbhost.com',

    url='http://github.com/rdbhost/yieldfromrequests_trollius',

    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'yieldfrom_t.requests': ['*.pem']},
    package_dir={'yieldfrom_t': 'yieldfrom_t'},
    include_package_data=True,
    namespace_packages=['yieldfrom_t'],
    install_requires=requires,

    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
