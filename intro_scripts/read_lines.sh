#!/bin/bash
file='data.txt' 

while read line
do 
	echo $line
done < $file
