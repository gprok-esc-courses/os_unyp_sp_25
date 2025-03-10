#!/bin/bash

used_mem=$(free -m | awk '/Mem/ {print $3}')
free_mem=$(free -m | awk '/Mem/ {print $4}')

echo $used_mem
echo $free_mem