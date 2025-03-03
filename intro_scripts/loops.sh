#!/bin/bash
echo "While Loop"
i=0
while [ $i < 5 ]
do
	echo $i 
	((i++))
done

echo "For Loop"
for((i=0; i < 5; i++))
do
	echo $i
done