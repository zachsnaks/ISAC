#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "Creating Python 3.11.5 virtual environment..."

# Check if Python 3.11.5 is installed
if ! command -v python3.11 &> /dev/null; then
    echo -e "${RED}Python 3.11 not found. Installing via Homebrew...${NC}"
    brew install python@3.11
fi

# Create the virtual environment
python3.11 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Verify Python version
PYTHON_VERSION=$(python --version)
if [[ $PYTHON_VERSION == *"3.11.5"* ]]; then
    echo -e "${GREEN}Successfully created virtual environment with Python $PYTHON_VERSION${NC}"
    echo -e "To activate the environment:"
    echo -e "${GREEN}source .venv/bin/activate${NC}"
else
    echo -e "${RED}Warning: Python version is $PYTHON_VERSION, not 3.11.5${NC}"
fi

# Print environment information
echo -e "\nEnvironment Information:"
echo "Python Path: $(which python)"
python --version
pip --version