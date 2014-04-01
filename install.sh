# install.sh - installation script

BASHRC = ~/.bashrc

echo "export TEXMFHOME=\"$(pwd):$TEXMFHOME\""          >> $BASHRC
echo "export PATH=\"$(pwd)/scripts:$PATH\""            >> $BASHRC
echo "export PYTHONPATH=\"$(pwd)/python:$PYTHONPATH\"" >> $BASHRC
