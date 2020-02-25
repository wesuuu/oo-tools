#!/bin/bash

docker run -v $(pwd):/opt/oo-tools -t oo-tools python3 setup.py test