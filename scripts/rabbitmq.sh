cd /Users/vlastimil/Coding_Projects/zk/      
python3 -m pip install virtualenv
pip3 install --upgrade pip
python3 -m venv venv
source venv/bin/activate
cd /Users/vlastimil/Coding_Projects/zk/zuzikoko/
pip install -r requirements.txt
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
echo 'docker is running'



