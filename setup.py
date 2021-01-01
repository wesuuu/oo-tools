import setuptools
import os
import codecs

from setuptools import setup

# https://packaging.python.org/guides/single-sourcing-package-version/
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="oo-tools",
    version=get_version("oo_tools/__init__.py"),
    url="",
    author="Wesley Uykimpang",
    description="Some object-oriented classes + utilities for python",
    packages=setuptools.find_packages(),
    install_requires=['pyyaml', 'requests'],
    python_requires = ">=3.6",
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    package_data={'oo_tools': ['*.py']}
)
