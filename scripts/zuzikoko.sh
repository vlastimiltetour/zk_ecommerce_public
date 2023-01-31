#!/bin/sh
open -a DOCKER
sleep 15
osascript -e 'tell app "Terminal"
	do script "/Users/vlastimil/Coding_Projects/zk/scripts/flower.sh"
	do script "/Users/vlastimil/Coding_Projects/zk/scripts/rabbitmq.sh"
	do script "/Users/vlastimil/Coding_Projects/zk/scripts/redis.sh"
	do script "/Users/vlastimil/Coding_Projects/zk/scripts/stripe.sh"
	do script "/Users/vlastimil/Coding_Projects/zk/scripts/celery.sh"


end tell'






echo 'all files run'
