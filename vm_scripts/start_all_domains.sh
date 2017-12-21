#!/bin/bash
# this will use virsh to start all domains

for domain in $(virsh list --all | awk ' { print $2 }' | grep -v Name); 
do 
	virsh start $domain ;
done 
