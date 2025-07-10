---
layout: post
title: How to Repair Filesystems on a Raspberry Pi
date: 2025-03-30 20:34
categories: raspberry-pi fsck filesystem 
---



## Running fsck ##

1. Unmount the filesystem to be checked. The only way I was able to do this was to remove the disk from the fstab and then reboot
2. Run the command on your hard drive (/dev/sdd1 for me). The -C 0 option prints a progress bar. The -y option answers yes to all questions. This will auto-fix:
> sudo sudo fsck.ext4 -C 0 -f -v -y /dev/sdd1

Breakdown:
* -C 0 - Shows a progress bar on the terminal
* -f - Force checking even if filesystem is clean
* -v - Be verbose
* -y - Assume yes to all questions (automatically fix errors)
* /dev/sdd1 - The target filesystem

## Forcing a Filesystem Check At Startup ##

Use this command:
> sudo touch /forcefsck; sudo reboot

Breakdown:

* sudo touch /forcefsck - Creates a an empty file called 'forcefsck' at the root of the filesystem ('/')
* sudo reboot - Reboots in order to effect the changes

Note: The first time that I did this an interactive prompt came up that I need to clear from a local terminal (i.e., using a monitor and keyboard)


## Resources ##

[Stackoverflow answer - How do you get e2fsck to show progress information?](https://serverfault.com/questions/118791/how-do-you-get-e2fsck-to-show-progress-information)
