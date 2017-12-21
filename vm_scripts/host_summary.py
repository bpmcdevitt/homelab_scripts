#!/usr/bin/env python
# using the pythonl library libvirt
# this is all taken directly from the documentation here: https://libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/index.html

from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu+unix:///system?socket=/var/run/libvirt/libvirt-sock')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

#caps = conn.getCapabilities() # caps will be a string of XML
#print('Capabilities:\n'+caps)

#### some system information #####
host = conn.getHostname()
vcpus = conn.getMaxVcpus(None)
nodeinfo = conn.getInfo()

print('Hostname:'+host)
print('Model: '+str(nodeinfo[0]))
print('Memory size: '+str(nodeinfo[1])+'MB')
print('Number of CPUs: '+str(nodeinfo[2]))
print('Maximum support virtual CPUs: '+str(vcpus))
print('MHz of CPUs: '+str(nodeinfo[3]))
print('Number of NUMA nodes: '+str(nodeinfo[4]))
print('Number of CPU sockets: '+str(nodeinfo[5]))
print('Number of CPU cores per socket: '+str(nodeinfo[6]))
print('Number of CPU threads per core: '+str(nodeinfo[7]))
print('\n')

print("All (active and inactive) domain names:")
domains = conn.listAllDomains(0)
if len(domains) != 0:
    for domain in domains:
        print(domain.name())
else:
    print('  None')

conn.close()
exit(0)
