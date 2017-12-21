#!/bin/bash
# this will remove a virtual machine and perform cleanup on it

if [ $UID != 0 ]; then
	echo 'Are you root?'
	exit
fi


name="$1"

virsh destroy "$name"
virsh undefine "$name"

