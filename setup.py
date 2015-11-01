#!/usr/bin/env python
from setuptools import setup

setup(
    name='example',
    version='0.0.0',
    author='Mikhail Lukyanchenko',
    author_email='ml@akabos.com',
    packages=['example'],
    url='http://example.com/',
    license='LICENSE',
    description='TravisCI configuration excersises',
    install_requires=[
        "numpy",
        "scipy",
    ],
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
)
