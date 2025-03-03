#!/bin/bash
params=$#

if [ $params -eq 2 ]
then
	source=$1
	destination=$2
	cp $source $destination
else
	echo "Syntax: copy_file.sh source destination"
fi