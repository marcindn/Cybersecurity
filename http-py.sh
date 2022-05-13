---CONFIG---
IP=192.168.1.4
PORT=8000
DIRECTORY=~/server/
------------

clear
echo ' _______ _______ _______ ______               '
echo '|   |   |_     _|_     _|   __ \ .-----.--.--.'
echo '|       | |   |   |   | |    __/_|  _  |  |  |'
echo '|___|___| |___|   |___| |___| |__|   __|___  |'
echo '                                 |__|  |_____|'
echo 'Starting Python3 HTTP Server'
echo 'Serving '$DIRECTORY' at '$IP:$PORT
python3 -m http.server $PORT -b $IP -d $DIRECTORY
echo 'Server has been shut down'
echo 'Clear screen [Y/n]:'
read DECISION
if [ $DECISION == 'y' ] || [ $DECISION == 'Y' ]
then
clear
fi