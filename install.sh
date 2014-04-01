# install.sh - installation script
#
# This script will echo out the commands you need to set up this repository.
# Simple redirect the output of this script into your .bashrc
#
#     ./install.sh >> ~/.bashrc

echo "export TEXMFHOME=\"$(pwd):$TEXMFHOME\"" 
echo "export PATH=\"$(pwd)/scripts:$PATH\""
echo "export PYTHONPATH=\"$(pwd)/python:$PYTHONPATH\""
echo "alias pythontex=\"python $(pwd)/pythontex/pythontex/pythontex.py\""
