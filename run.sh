#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the code
python googlechatsend/main.py "$@"
