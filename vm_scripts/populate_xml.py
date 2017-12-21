#!/usr/bin/env python
# this will populate the xml template file used to integrate into the python library for libvirt domain creation

import sys
import uuid
import xml.etree.ElementTree as ET

domain = ET.Element('domain')
name = ET.SubElement(domain, 'name')
uuid = ET.SubElement(domain, 'uuid')
memory = ET.SubElement(domain, 'memory', unit='Kib')
ET.dump(domain)


#<domain type='' id=''>
#  <name>host.changeme123</name>
#  <uuid>uuid.uuid4()</uuid>
#  <memory unit='KiB'>4194304</memory>
#  <currentMemory unit='KiB'>4194304</currentMemory>
#  <vcpu placement='static'>4</vcpu>
#  <resource>
#    <partition>/machine</partition>
#  </resource>
#  <os>
#    <type arch='x86_64' machine='pc-i440fx-2.6'>hvm</type>
#    <boot dev='hd'/>
#  </os>
#  <features>
#    <acpi/>
#    <apic/>
#    <vmport state='off'/>
#  </features>
#  <cpu mode='custom' match='exact'>
#    <model fallback='allow'>Haswell-noTSX</model>
#  </cpu>
#  <clock offset='utc'>
#    <timer name='rtc' tickpolicy='catchup'/>
#    <timer name='pit' tickpolicy='delay'/>
#    <timer name='hpet' present='no'/>
#  </clock>
#  <on_poweroff>destroy</on_poweroff>
#  <on_reboot>restart</on_reboot>
#  <on_crash>restart</on_crash>
#  <pm>
#    <suspend-to-mem enabled='no'/>
#    <suspend-to-disk enabled='no'/>
#  </pm>
#  <devices>
#    <emulator>/usr/sbin/qemu-system-x86_64</emulator>
#    <disk type='file' device='disk'>
#      <driver name='qemu' type='raw'/>
#      <source file='/home/booboy/vms/booboy.openbsd'/>
#      <backingStore/>
#      <target dev='hda' bus='ide'/>
#      <alias name='ide0-0-0'/>
#      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
#    </disk>
#    <disk type='file' device='cdrom'>
#      <driver name='qemu' type='raw'/>
#      <backingStore/>
#      <target dev='hdb' bus='ide'/>
#      <readonly/>
#      <alias name='ide0-0-1'/>
#      <address type='drive' controller='0' bus='0' target='0' unit='1'/>
#    </disk>
#    <controller type='usb' index='0' model='ich9-ehci1'>
#      <alias name='usb'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x7'/>
#    </controller>
#    <controller type='usb' index='0' model='ich9-uhci1'>
#      <alias name='usb'/>
#      <master startport='0'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0' multifunction='on'/>
#    </controller>
#    <controller type='usb' index='0' model='ich9-uhci2'>
#      <alias name='usb'/>
#      <master startport='2'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x1'/>
#    </controller>
#    <controller type='usb' index='0' model='ich9-uhci3'>
#      <alias name='usb'/>
#      <master startport='4'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x2'/>
#    </controller>
#    <controller type='pci' index='0' model='pci-root'>
#      <alias name='pci.0'/>
#    </controller>
#    <controller type='ide' index='0'>
#      <alias name='ide'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
#    </controller>
#    <controller type='virtio-serial' index='0'>
#      <alias name='virtio-serial0'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
#    </controller>
#    <interface type='bridge'>
#      <mac address='52:54:00:35:c6:0d'/>
#      <source bridge='br0'/>
#      <target dev='vnet1'/>
#      <model type='rtl8139'/>
#      <alias name='net0'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
#    </interface>
#    <serial type='pty'>
#      <source path='/dev/pts/1'/>
#      <target port='0'/>
#      <alias name='serial0'/>
#    </serial>
#    <console type='pty' tty='/dev/pts/1'>
#      <source path='/dev/pts/1'/>
#      <target type='serial' port='0'/>
#      <alias name='serial0'/>
#    </console>
#    <channel type='spicevmc'>
#      <target type='virtio' name='com.redhat.spice.0' state='disconnected'/>
#      <alias name='channel0'/>
#      <address type='virtio-serial' controller='0' bus='0' port='1'/>
#    </channel>
#    <input type='mouse' bus='ps2'>
#      <alias name='input0'/>
#    </input>
#    <input type='keyboard' bus='ps2'>
#      <alias name='input1'/>
#    </input>
#    <graphics type='spice' port='5901' autoport='yes' listen='127.0.0.1'>
#      <listen type='address' address='127.0.0.1'/>
#      <image compression='off'/>
#    </graphics>
#    <video>
#      <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>
#      <alias name='video0'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
#    </video>
#    <redirdev bus='usb' type='spicevmc'>
#      <alias name='redir0'/>
#      <address type='usb' bus='0' port='1'/>
#    </redirdev>
#    <redirdev bus='usb' type='spicevmc'>
#      <alias name='redir1'/>
#      <address type='usb' bus='0' port='2'/>
#    </redirdev>
#    <memballoon model='virtio'>
#      <alias name='balloon0'/>
#      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
#    </memballoon>
#  </devices>
#  <seclabel type='none' model='none'/>
#  <seclabel type='dynamic' model='dac' relabel='yes'>
#    <label>+1000:+1000</label>
#    <imagelabel>+1000:+1000</imagelabel>
#  </seclabel>
#</domain>
#
