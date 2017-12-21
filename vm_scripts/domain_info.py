#!/usr/bin/env python
# this will fetch the domain name information for the arg given

from __future__ import print_function
import sys 
import libvirt
from xml.dom import minidom

domName = sys.argv[1]

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

name = dom.name()
print('The name of the domain is "' + name +'".')

flag = dom.isActive()
if flag == True:
    print('The domain is active.')
else:
    print('The domain is not active.')

id = dom.ID()
if id == -1:
    print('The domain is not running so has no ID.')
else:
    print('The ID of the domain is ' + str(id))

flag2 = dom.isPersistent()
if flag2 == 1:
    print('The domain is persistent.')
elif flag2 == 0:
    print('The domain is not persistent.')
else:
    print('There was an error.')

uuid = dom.UUIDString()
print('The UUID of the domain is ' + uuid)

type = dom.OSType()
print('The OS type of the domain is "' + type + '"')

flag = dom.hasCurrentSnapshot() #https://libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/libvirt_application_development_guide_using_python-Guest_Domains-Information-HasCurrentSnapshot.html
print('The value of the current snapshot flag is ' + str(flag))

flag = dom.hasManagedSaveImage()
print('The value of the manaed save images flag is ' + str(flag))

state, maxmem, mem, cpus, cput = dom.info()
print('The state is ' + str(state))
print('The max memory is ' + str(maxmem))
print('The memory is ' + str(mem))
print('The number of cpus is ' + str(cpus))
print('The cpu time is ' + str(cput))
print('\n')

### the state ###
state, reason = dom.state()

if state == libvirt.VIR_DOMAIN_NOSTATE:
    print('The state is VIR_DOMAIN_NOSTATE')
elif state == libvirt.VIR_DOMAIN_RUNNING:
    print('The state is VIR_DOMAIN_RUNNING')
elif state == libvirt.VIR_DOMAIN_BLOCKED:
    print('The state is VIR_DOMAIN_BLOCKED')
elif state == libvirt.VIR_DOMAIN_PAUSED:
    print('The state is VIR_DOMAIN_PAUSED')
elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
    print('The state is VIR_DOMAIN_SHUTDOWN')
elif state == libvirt.VIR_DOMAIN_SHUTOFF:
    print('The state is VIR_DOMAIN_SHUTOFF')
elif state == libvirt.VIR_DOMAIN_CRASHED:
    print('The state is VIR_DOMAIN_CRASHED')
elif state == libvirt.VIR_DOMAIN_PMSUSPENDED:
    print('The state is VIR_DOMAIN_PMSUSPENDED')
else:
    print(' The state is unknown.')
print('The reason code is ' + str(reason))

conn.close()
exit(0)
