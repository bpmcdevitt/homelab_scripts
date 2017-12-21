#!/bin/bash
# this will use qemu-img to create raw disk space for easy reproduction of vm creation
# Author: Brendan McDevitt

size="$2"
file="$1"

qemu-img create -f raw "$file" "$size"
