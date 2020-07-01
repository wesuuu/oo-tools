#!/bin/bash

python3 setup.py bdist_wheel sdist
python3 -m twine upload --repository oo-tools --repository-url https://upload.pypi.org/legacy/ dist/*