cd /Users/vlastimil/Coding_Projects/zk/      
python3 -m pip install virtualenv
pip3 install --upgrade pip
python3 -m venv venv
source venv/bin/activate
open -a DOCKER
cd /Users/vlastimil/Coding_Projects/zk/zuzikoko/
pip install -r requirements.txt
celery --workdir=./zuzikoko --app=web flower
echo 'flower is running'



