#!/bin/bash

python3 -m pylint --disable missing-docstring app/
python3 -m flake8
python3 -m pytest
