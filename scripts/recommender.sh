#!/bin/sh
cd /Users/vlastimil/Coding_Projects/zk/      
python3 -m pip install virtualenv
pip3 install --upgrade pip
python3 -m venv venv
source venv/bin/activate
cd /Users/vlastimil/Coding_Projects/zk/zuzikoko/
pip install -r requirements.txt