#!/bin/bash -e
 
export PYTHONPATH=$PYTHONPATH:$(pwd)/notebook/:$(pwd)/diary/:$(pwd)/utils/
export PATH=$PATH:$(pwd)/notebook/:$(pwd)/diary:$(pwd)/utils/
echo "Prepending PATH"
