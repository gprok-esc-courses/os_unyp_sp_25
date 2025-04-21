#!/bin/bash

sysload=$(uptime | awk '{print $11}' | tr -d ',')
echo $sysload 

echo $(echo "$sysload > 0.2" | bc -l)

if [ $(echo "$sysload > 0.12" | bc -l) == 1 ]; then
	echo "WARNING"
else 
	echo "OK"
fi