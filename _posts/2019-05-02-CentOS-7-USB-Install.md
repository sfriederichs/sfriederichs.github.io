---
layout: post
title:  "How To Create CentOS7 Install Media on a usb"

date:   2019-05-02 11:39
categories: how-to centos
---

Bossman wants me to make a CentOS 7 installer USB drive.

Let's do this.

First attempt, [this](https://linoxide.com/how-tos/centos-7-step-by-step-screenshots/) website.

For Windows 10, says I need [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/).

Then I need the [install media](http://mirrors.ocf.berkeley.edu/centos/7.6.1810/isos/x86_64/CentOS-7-x86_64-Everything-1810.iso).
I chose the 'everything' ISO because why not? Get everything and it's only 10G, the drive is 60G.

Says it's going to take 3-4 hours to download though...

## Installing Win32DiskImager ##

1. Double click the downloaded install file
2. Accept the License agreement
3. Accept the default installation path of  C:\\Program Files (x86)\\ImageWriter
4. Accept the default start menu folder of Image Writer
5. Opt to create a desktop shortcut
6. Click 'Install'
7. Opt to start the program when install has finished

## Creating the Bootable USB Drive ##

Win32DiskImager has started as per the last step in the previous section. These are the steps to create the bootable USB drive:

1. Select the image file (Note, I had to change the filter to all files to find the .iso)
2. Ensure the Device is the correct drive.
3. Click Write and see what happens

Spoiler: It wrote.

## Installing CentOS 7 ##

Dave gave me a laptop to install CentOS 7 on.

I am doing that.

F11 brings up the boot menu - it booted from the USB just fine.
Defaults for most of the installation were good - I had to delete the existing partitions on the hard drive.

Root password: <redacted>

I made no new users. 

## Getting a GUI on the PC ##

Turns out we need a GUI.
So I'm reinstalling.

Changes I made:
* Under 'Software Selection' I've changed it to 'GNOME Desktop. I had added on (because it seemed like a good idea):
    * Compatibility libraries
    * Development Tools
    * Security Tools
    * System Administration Tools
    
Same root password... trying again...

Seems to work this time.

I've created a new user:
* Username: sfrieder
* Password: <redacted>

## Resources ##
* [Linoxide USB Install Media Creation Steps](https://linoxide.com/how-tos/centos-7-step-by-step-screenshots/)
* [Win32DiskImager Download](https://sourceforge.net/projects/win32diskimager/files/latest/download)
* [CentOS7 Install ISO]()

