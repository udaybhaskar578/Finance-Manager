# -*- coding: utf-8 -*-
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

requires = ['pandas']
tests_require = ['pytest', 'pytest-cache', 'pytest-cov']


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="finance manager",
    version='0.0.1',
    description="Finance manager",
    long_description="\n\n".join([open("README.md").read()]),
    license='MIT',
    author="Naren Mudivarthy",
    author_email="narenuday595@gmail.com",
    install_requires=requires,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers', 'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    extras_require={'test': tests_require},
    cmdclass={'test': PyTest})
