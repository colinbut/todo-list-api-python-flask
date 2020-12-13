#!/bin/bash

python3 -m venv env
cd env/lib/python3.9/site-packages/
. ../../../bin/activate
cd ../../../../
pip3 install -qr requirements.txt