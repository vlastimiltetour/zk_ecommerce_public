cd /Users/vlastimil/Coding_Projects/zk/      
python3 -m pip install virtualenv
pip3 install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd /Users/vlastimil/Coding_Projects/zk/zuzikoko
celery -A web worker --loglevel=info  
echo 'celery is running'



