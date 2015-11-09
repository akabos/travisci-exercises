#!/usr/bin/env python
from setuptools import setup, Command


class RunTests(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'run_tests.py'])
        raise SystemExit(errno)


setup(
    name='example',
    version='0.0.0',
    author='Mikhail Lukyanchenko',
    author_email='ml@akabos.com',
    packages=['example'],
    url='http://example.com/',
    license='LICENSE',
    description='TravisCI configuration excersises',
    cmdclass = {'test': RunTests},
    install_requires=[
        "numpy",
        "scipy",
    ],
    tests_require=[
        'pytest',
    ],
    test_suite="tests",
)
