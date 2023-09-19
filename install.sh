#!/bin/bash

# Define your project folder path
project_folder="."

# Create a virtual environment (venv hidden)
python3 -m venv "$project_folder/.venv"

# Activate the venv
source "$project_folder/venv/bin/activate"

# Install requirements from requirements.txt
pip install -r "$project_folder/requirements.txt"

# Echo "Successfully installed"
echo "Successfully installed and activated project"
