#!/bin/bash
file='data.txt'

while IFS="," read -r a b c
do 
	echo $b
done < $file