#!/bin/bash
# this will work on a linux machine to test the drives sequential read speeds.
# https://wiki.archlinux.org/index.php/Benchmarking/Data_storage_devices 
# ^ this is a good writeup. in this script we will run the hdparm -Tt command 6 times and avg out the results 

if [ "$(id -u)" != "0" ]; then
	echo 'please run the script as root' 2>&1
	exit 1
fi

drive_list=() # initialize empty array of drives
count=0

# exit if not root

function usage() {
	
	echo "usage: $(basename $0) /dev/sd[a-z]"

}

function get_drives() {
	
	for drive in /dev/sd[a-z]; do
		drive_list[count]=$(echo  $drive)
		count=$((count +1))
	done		
	no_of_drives="${#drive_list[@]}"

}

function list_drives() {
	
	get_drives # this allows access to the drive_list array
	echo "# of detected drives: $no_of_drives" 
	printf "%s\n" "${drive_list[@]}"

}

function hdparm_test() {
	
	get_drives 
	
	for ((i=${no_of_drives}-1; i>=0; i--)); do
		for num in {1..6}; do 
			hdparm -Tt "${drive_list[$i]}" \
			| awk '/[0-9]{4}/{ print $10 }'   
		done 
	done 
		
}

function main() {
	
	#list_drives 
	hdparm_test 

}

main
