#!/bin/bash
# this script will install a new virtual machine using virt-install
# Author: Brendan McDevitt

### idea is to create functions for each different type of OS ###

#function tests()
#
#{
#
#if [ $UID ! = 0 ]; then 
#	echo 'Are you root?' 
#	usage
#fi

#}

### main variables passed as arguments ###
name="$1"
distro_type="$2"
size="$3"
install_path="$4"

### the ip location of the webserver where OS img & automated install files are held ###
webserver_ip="192.168.1.15"

#function usage() 
#
#{
#echo "usage: $(basename $0) [name] [distro_type] [size] [/path/to/install.img]" 
#}


function centos() 

	{

	#centos_installer="http://${webserver_ip}/centos7_x64_minimal/CentOS-7-x86_64-Minimal-1511.iso"
	centos_installer="http://${webserver_ip}/centos7_x64_minimal"

		#function pxe() 
			#{
			#}
	virt-install \
	--name="$name" \
	--ram 2048 \
	--os-type=Linux \
	--os-variant=rhel7.0
	--vcpus 2 \
	--disk-path="${install_path},size=${size},bus=virtio" \
	--network bridge:br0 \
	--graphics none \
	--location $centos_installer \
	#--pxe \
 	-x "ks=http://192.168.15/bootstrap/ks.cfg"
	}

#function debian() 
#{
#
#}

#function ubuntu() {
#}
#
#function arch() {
#}
#
#function freebsd() {
#}
#
#function windows_server() {
#}

if "$2" ! = 'centos'; then 
	exit
fi
centos
