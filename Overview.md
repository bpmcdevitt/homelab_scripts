- [Introduction](#sec-1)
  - [Host Prep](#sec-1-1)
    - [RESEARCH: - add in the methods to check to make sure the system is ready to deploy kvm/qemu (cpu flags for vt-d/grub options/bios options&#x2026;.etc, attach or link images if neccessary)](#sec-1-1-1)
  - [My Lab Specs](#sec-1-2)
  - [VMs to build](#sec-1-3)
  - [Research Material](#sec-1-4)
    - [Filesystem specific(I used ZFS as my main FS)](#sec-1-4-1)
    - [Web Application Testing:](#sec-1-4-2)
    - [Pentest Specific:](#sec-1-4-3)
  - [Programs to write](#sec-1-5)
    - [Make a program in ruby that will convert other image files to raw files. we will need to run this in bulk after dl of ova images](#sec-1-5-1)
    - [Make a program in ruby that will download the .ova files from <https://download.vulnhub.com/checksum.txt>](#sec-1-5-2)
    - [Make a program in ruby that will generate ssh keypairs for our vms](#sec-1-5-3)
    - [Make a program that configures a static ip address for a host system in ruby (most of the vulnhub vms come configured with dhcp, but this will still be a nice tool to have for vm reconfiguring if ever needed)](#sec-1-5-4)
    - [RESEARCH: Make a program that will allow you to export an org-mode document in emacs to a pentest report.](#sec-1-5-5)


# Introduction<a id="sec-1"></a>

When I started my search on the internet on creating a lab environment for security research and learning the skills of penetration test, I was often frustrated. Many of the articles and how-to guides that I found were using Windows as the host operating system and/or VMware as the hypervisor. I like linux very much and I have grown to really enjoy using qemu/kvm. libvirt has a great community behind it that offers bindings in many different programming languages (<https://libvirt.org/bindings.html>). We can use automation to build efficient methods for spawning purposelly vulnerable systems to hack away at til our heads fall off.

In my efforts to build a lab that will withstand the test of time, I purchased a very expensive CPU for my home system. I stacked it with RAM and lots of spinning space, and some SSD space as well. You do not need to go crazy like I did and buy a bunch of hardware. This will work on a laptop with a decent amount of RAM to allocate to the VMs and a modern CPU. It also needs to support VT-D.

I am going to be primarily using ruby and bash scripting to glue everything together. I am sure it will not be the prettiest code, but it will solve the problem.

## Host Prep<a id="sec-1-1"></a>

### TODO RESEARCH: - add in the methods to check to make sure the system is ready to deploy kvm/qemu (cpu flags for vt-d/grub options/bios options&#x2026;.etc, attach or link images if neccessary)<a id="sec-1-1-1"></a>

## My Lab Specs<a id="sec-1-2"></a>

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

## VMs to build<a id="sec-1-3"></a>

1.  TODO RESEARCH: can we figure out a way to start a base template VM, and based on a set of vulns that we give the VM at deploy time, spin up the VM with those vulns?

2.  TODO OpenVas VM

3.  TODO Kanban board (investigate opensource JIRA alternatives)

    -   Atlassian offers confluence, bitbucket, and jira all for $10 per year per 10 users. I like these tools, so I am more than happy to pay them for them.

4.  TODO Issue tracking (bugzilla maybe?)

5.  TODO Wiki - (as close to confluence as we can find)

6.  DONE Pentest System (Kali linux and/or pentoo)

    -   [Build your own custom Kali iso](https://docs.kali.org/development/live-build-a-custom-kali-iso)
    -   [pentoo](https://www.pentoo.ch/download)
    -   [Blackarch](https://blackarch.org/downloads.html)
    
    CLOSED: <span class="timestamp-wrapper"><span class="timestamp">[2018-07-16 Mon 16:25]</span></span>

7.  TODO Vulnerable system with multiple web apps (multidae, dvwa)

    -   OWASP Broken Web Application Project - <https://www.owasp.org/index.php/OWASP_Broken_Web_Applications_Project#tab=Main>

## Research Material<a id="sec-1-4"></a>

### Filesystem specific(I used ZFS as my main FS)<a id="sec-1-4-1"></a>

-   [ZFS Volumes vs Raw Disk Storage Trade Offs](https://superuser.com/questions/1159116/zfs-vs-raw-disk-for-storing-virtual-machines-trade-offs)
-   [ZFS, BTRFS, XFS, EXT4, and LVM with KVM - a storage comparison](https://www.ilsistemista.net/index.php/virtualization/47-zfs-btrfs-xfs-ext4-and-lvm-with-kvm-a-storage-performance-comparison.html)

### Web Application Testing:<a id="sec-1-4-2"></a>

-   [OWASP Testing Guide](https://www.owasp.org/images/1/19/OTGv4.pdf)

### Pentest Specific:<a id="sec-1-4-3"></a>

-[ awesome-pentest GitHub](https://github.com/enaqx/awesome-pentest)

## Programs to write<a id="sec-1-5"></a>

### TODO Make a program in ruby that will convert other image files to raw files. we will need to run this in bulk after dl of ova images<a id="sec-1-5-1"></a>

```ruby
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

```

### TODO Make a program in ruby that will download the .ova files from <https://download.vulnhub.com/checksum.txt><a id="sec-1-5-2"></a>

```ruby
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

```

### TODO Make a program in ruby that will generate ssh keypairs for our vms<a id="sec-1-5-3"></a>

found a nice ruby gem [sshkey gem](https://github.com/bensie/sshkey)

```ruby
require 'sshkey'

  def gen_ssh_keypair

    k = SSHKey.generate(
      type: "DSA",
      bits: 1024,
      comment: "foo@bar.com",
      passphrase: "foobar"
    )
  end

keypair = gen_ssh_keypair

```

### TODO Make a program that configures a static ip address for a host system in ruby (most of the vulnhub vms come configured with dhcp, but this will still be a nice tool to have for vm reconfiguring if ever needed)<a id="sec-1-5-4"></a>

### TODO RESEARCH: Make a program that will allow you to export an org-mode document in emacs to a pentest report.<a id="sec-1-5-5"></a>
