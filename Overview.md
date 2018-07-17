
# Table of Contents

1.  [Introduction](#orgde04f70)
    1.  [Design Ideas](#orgc30b71a)
    2.  [My Lab Specs](#org7faac34)
    3.  [VMs](#org5853b24)
        1.  [VMs To Create:](#orga6c201c)
    4.  [Research](#org8901b33)
        1.  [OWASP Testing Guide - https://www.owasp.org/images/1/19/OTGv4.pdf](#org0ff9036)
        2.  [ZFS and vms? (lets not use qcow2 since we are using zfs yea?)](#org3d659b0)
        3.  [Make a script in ruby that will convert other image files to raw files. we will need to run this in bulk after dl of ova images](#org72f4bbd)
        4.  [Make a script in ruby that will download the .ova files from https://download.vulnhub.com/checksum.txt](#org2d75f4d)



<a id="orgde04f70"></a>

# Introduction


<a id="orgc30b71a"></a>

## Design Ideas

When I started my search on the internet on creating a lab environment for security research and learning the skills of penetration test, I was often frustrated. Many of the articles and how-to guides that I found were using Windows as the host operating system and/or VMware as the hypervisor. 
I like linux very much and I have grown to really enjoy using qemu/kvm. libvirt has a great community behind it that offers bindings in many different programming languages (<https://libvirt.org/bindings.html>). We can use automation to build efficient methods for spawning purposelly vulnerable systems to hack away at til our heads fall off. 

In my efforts to build a lab that will withstand the test of time, I purchased a very expensive CPU for my home system. I stacked it with RAM and lots of spinning space, and some SSD space as well. 
You do not need to go crazy like I did and buy a bunch of hardware. This will work on a laptop with a decent amount of RAM to allocate to the VMs and a modern CPU. It also needs to support VT-D. 

I am going to be primarily using ruby and bash scripting to glue everything together. I am sure it will not be the prettiest code, but it will solve the problem.

1.  TODO RESEARCH - add in the methods to check to make sure the system is ready to deploy kvm/qemu (cpu flags for vt-d/grub options/bios options&#x2026;.etc, attach or link images if neccessary)


<a id="org7faac34"></a>

## My Lab Specs

1.  Main server

    1.  OS: Archlinux
    
    2.  Motherboard - Asus X99 WS/USB 3.1
    
    3.  CPU - Intel E5-2687W v3 3.1GHZ
    
    4.  Heatsink - Noctua
    
    5.  RAM - 128GB total - 8 32GB DDR4 ECC 2300 MHZ Kingston
    
    6.  HDD - 12 HGST DeskStar NAS 7200 RPM 64MB Cache 4TB
    
    7.  SSD - 4 Intel 256GB
    
    8.  PCI-E Cards - LSI 9211-8i
    
    9.  Chassis - Rosewill 4U

2.  Router

    1.  I have an EdgeRouter lite, but honestly any modern day router will do. If you want more control over the configuration, buy a linux based router, or look into DDWRT and tomato based router firmwares and comptabile routers.

3.  Storage Chassis #1

    1.  Chassis - Supermicro 12 Bay
    
    2.  PSU - Not sure at the moment
    
    3.  Fans - 3 Noctua
    
    4.  Fan Controller - Random one on eBay or Amazon cant remember

4.  Storage Chassis #2

    1.  Chassis - Supermicro 12 Bay
    
    2.  PSU - Not sure at the moment
    
    3.  Fans - 3 Noctua
    
    4.  Fan Controller - Random one on eBay or Amazon cant remember


<a id="org5853b24"></a>

## VMs


<a id="orga6c201c"></a>

### VMs To Create:

1.  TODO Kanban board (investigate opensource JIRA alternatives)

    1.  Atlassian offers confluence, bitbucket, and jira all for $10 per year per 10 users. I like these tools, so I am more than happy to pay them for them.

2.  TODO Issue tracking (bugzilla maybe?)

3.  TODO Wiki - (as close to confluence as we can find)

4.  DONE Pentest System (Kali linux and/or pentoo)

5.  TODO Vulnerable system with multiple web apps (multidae, dvwa)

    1.  OWASP Broken Web Application Project - <https://www.owasp.org/index.php/OWASP_Broken_Web_Applications_Project#tab=Main>


<a id="org8901b33"></a>

## Research


<a id="org0ff9036"></a>

### OWASP Testing Guide - <https://www.owasp.org/images/1/19/OTGv4.pdf>


<a id="org3d659b0"></a>

### ZFS and vms? (lets not use qcow2 since we are using zfs yea?)


<a id="org72f4bbd"></a>

### TODO Make a script in ruby that will convert other image files to raw files. we will need to run this in bulk after dl of ova images

    def file_exists(filename)
      File.file?(filename) # return true if filename exists
    end
    
    def convert_file(format, filename) # needs qemu-img binary installed on the system, returns a new raw image file
      `qemu-img convert -f #{format} -O raw "#{filename}" "#{filename}.img"` 
    end 
    
    # I am using a 56MB vmdk file to test the conversion process
    def test_convert(format, filename)
      file_exists(filename)
      convert_file(format, filename)
    end
    
    test_convert('vmdk', '/storage/virtual_machines/DSL-4.4.10-disk1.vmdk')


<a id="org2d75f4d"></a>

### TODO Make a script in ruby that will download the .ova files from <https://download.vulnhub.com/checksum.txt>

    class DownloadVulnHubTorrents
      require 'csv'
    
      def initialize
        @base_url = 'https://download.vulnhub.com'
      end
    
      # get the checksum file which has checksums + urls. we can automate the check of the files and compare with the checksums to make sure everything downloaded matches
      def download_checksum
        checksum_url = "#{@base_url}/checksum.txt"
        `wget #{checksum_url}` # download the checksum file
      end
    
      def gather_urls(filename)
        urls = `awk ' { print $2 } ' #{filename} | sed 's/^\./''/g' | grep -E 'ova|torrent|zip|tar|txt|gz|gzip|iso|7z|exe|text|img|png|jpg|jpeg|md|LICENSE|README'`
        CSV.parse(urls).flatten
      end
    end
    
    vulnhubber = DownloadVulnHubTorrents.new
    vulnhubber.download_checksums
    vulnhubber.gather_urls('/home/booboy/bin/mygit/homelab_scripts/checksum.txt')

