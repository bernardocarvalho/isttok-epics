#!/bin/sh

PID=$(ps ax |awk '/[0-9] ..\/..\/bin\/linux-arm\/ISTTOKrpi st.cmd/ {print $1}')
QUERY=$(ps ax |awk '/[0-9] ..\/..\/bin\/linux-arm\/ISTTOKrpi st.cmd/ {print}')
echo $PID
echo $QUERY
read -p "Proceed" ANS
#if [ $ANS = y] 
#then 
	kill -9 $PID
	echo Killed
	./run-ioc.sh
	exit 0
#else
#	exit 0
#	echo abort
#fi
