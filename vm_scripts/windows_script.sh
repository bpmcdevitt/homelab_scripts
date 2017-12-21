#!/bin/bash 

# QEMU name and PID
OPTS="-name windows-10-pro"
OPTS="$OPTS -pidfile /tmp/windows-10-pro.pid"
 
 
# Processor core2duo qemu64 host
OPTS="$OPTS -cpu qemu64,kvm=off"
OPTS="$OPTS -smp 8,sockets=1,cores=4,threads=2"
OPTS="$OPTS -enable-kvm"
 
 
# Machine
OPTS="$OPTS -machine type=pc-i440fx-2.1,accel=kvm"
#OPTS="$OPTS -machine type=q35,accel=kvm"
 
 
# The following setting enables S3 (suspend to RAM). OVMF supports S3
# suspend/resume. Disable when using Q35
OPTS="$OPTS -global PIIX4_PM.disable_s3=0"
 
 
# Memory
OPTS="$OPTS -m 8G"
#OPTS="$OPTS -mem-path /dev/hugepages"
OPTS="$OPTS -mem-prealloc"
OPTS="$OPTS -balloon none"
 
 
# Hardware clock
OPTS="$OPTS -rtc clock=host,base=utc"
 
 
# Sound hardware
QEMU_PA_SAMPLES=128
export QEMU_AUDIO_DRV=pa
OPTS="$OPTS -soundhw hda"
 
 
# Graphic card passthrough (Gigabyte GeForce GTX 970)
OPTS="$OPTS -device vfio-pci,host=09:00.0,multifunction=on"
OPTS="$OPTS -device vfio-pci,host=09:00.1"
 
 
# USB 3.0 passthrough (NEC/Renesas)
#OPTS="$OPTS -usb -usbdevice host:0x03f0:0xd407"
#OPTS="$OPTS -usb -usbdevice host:0x1d6b:0x0003"
#OPTS="$OPTS -usb -usbdevice host:0x1a40:0x0101"
 
#OPTS="$OPTS -device vfio-pci,host=03:00.0"
 
 
# Keyboard layout
OPTS="$OPTS -k en-us"
 
 
# Boot priority
OPTS="$OPTS -boot order=c"
 
 
# OVMF
cp /usr/share/edk2/ovmf-x64/OVMF_VARS-pure-efi.fd /usr/vms/image_files/windows_10_vars.fd
OPTS="$OPTS -drive if=pflash,format=raw,readonly,file=/usr/share/edk2/ovmf-x64/OVMF_CODE-pure-efi.fd"
OPTS="$OPTS -drive if=pflash,format=raw,file=/usr/vms/image_files/windows_10_vars.fd"
 
 
# System drive
OPTS="$OPTS -drive id=disk0,if=none,cache=unsafe,format=raw,file=/usr/vms/windows_10.image"
OPTS="$OPTS -device driver=virtio-scsi-pci,id=scsi0"
OPTS="$OPTS -device scsi-hd,drive=disk0"
 
 
# Other drive
#OPTS="$OPTS -drive id=disk1,if=none,cache=none,aio=native,format=raw,file=/dev/disk/by-id/ata-Hitachi_HDS721050CLA660_JP1570FR1ZWP7K"
#OPTS="$OPTS -device driver=virtio-scsi-pci,id=scsi1"
#OPTS="$OPTS -device scsi-hd,drive=disk1"
 
 
# Other drive 2
#OPTS="$OPTS -drive id=disk2,if=none,cache=none,aio=native,format=raw,file=/dev/disk/by-id/ata-Hitachi_HDS5C3020ALA632_ML0220F30NX2DD"
#OPTS="$OPTS -device driver=virtio-scsi-pci,id=scsi2"
#OPTS="$OPTS -device scsi-hd,drive=disk2"
 
 
# Windows 10 Pro installer
OPTS="$OPTS -drive id=cd0,if=none,format=raw,readonly,file=/usr/vms/image_files/win10.iso"
OPTS="$OPTS -device driver=ide-cd,bus=ide.0,drive=cd0"
 
 
# Virtio driver
OPTS="$OPTS -drive id=virtiocd,if=none,format=raw,file=/usr/vms/image_files/virtio-win-0.1.102.iso"
OPTS="$OPTS -device driver=ide-cd,bus=ide.1,drive=virtiocd"
 
 
# OVMF emits a number of info / debug messages to the QEMU debug console, at
# ioport 0x402. We configure qemu so that the debug console is indeed
# available at that ioport. We redirect the host side of the debug console to
# a file.
#OPTS="$OPTS -global isa-debugcon.iobase=0x402 -debugcon file:/tmp/windows_10_pro.ovmf.log"
 
 
# QEMU accepts various commands and queries from the user on the monitor
# interface. Connect the monitor with the qemu process's standard input and
# output.
#OPTS="$OPTS -monitor stdio"
 
 
# A USB tablet device in the guest allows for accurate pointer tracking
# between the host and the guest.
#OPTS="$OPTS -device piix3-usb-uhci -device usb-tablet"
 
 
# Network
#OPTS="$OPTS -netdev tap,vhost=on,ifname=$VM,script=/usr/local/bin/vm_ifup_brlan,id=brlan"
#OPTS="$OPTS -device virtio-net-pci,mac=52:54:00:xx:xx:xx,netdev=brlan"
 
# Disable display
#OPTS="$OPTS -vga qxl"
#OPTS="$OPTS -vga none"
#OPTS="$OPTS -serial null"
#OPTS="$OPTS -parallel null"
#OPTS="$OPTS -monitor none"
#OPTS="$OPTS -display none"
#OPTS="$OPTS -daemonize"
 
 
# QEMU Guest Agent
#OPTS="$OPTS -chardev socket,path=/tmp/qga.sock,server,nowait,id=qga0"
#OPTS="$OPTS -device virtio-serial"
#OPTS="$OPTS -device virtserialport,chardev=qga0,name=org.qemu.guest_agent.0"
 
sudo taskset -c 0-7 qemu-system-x86_64 $OPTS
