---
layout: post
title:  "How to Wipe a Hard Drive Before Selling it"
date:   2020-07-01 8:58
updated: 2020-07-01 8:58
categories: how-to hdd ssd
---


## Introduction ##

It's time to clear out a bunch of old stuff from my basement. Among this stuff is a bunch of laptops and SSDs. It's rather surprising that a few years ago, a 256GB SSD was a good and useful thing to have, and now even 512GB is looking pretty anemic. I've got quite a few 256GB SSDs and even a 128GB one sitting around. I need to wipe these so that I can sell them.


## Potential Tools ##

There's a wide variety of tools that will wipe drives for you, but for my purposes, I'm looking for something that is:

* Free
* Open source
* Has special SSD-wiping ability (stretch)

The 'special SSD wiping ability' one is interesting. Basically, SSDs use flash memory which can only be written to a certain number of times before
it doesn't work anymore. To lengthen the useful life of the drive, there is actually more storage available on the drive than they tell you. The drive keeps track of how many times an area of flash has been written to, and if one area starts to get more used than another, it will write the data to a different area to ensure that all of the areas have roughly similar use. Using these wear-leveling algorithms and the 'phantom' extra space, the drives are calculated to last for acceptable amounts of time given standard usage for the given application (i.e., server, home, gaming, etc.). 

What this means when you're wiping the drive is that even if you delete a file, that file (or at least, a potentially older version of that file) might be sitting somewhere in another flash memory area that has been written too many times. Technically, even platter hard drives have this issue, but they don't have the 'phantom' space and don't really have issues with wear-leveling, so you can just write a bunch of 0's to the drive repeatedly and you're pretty sure to clear all of the data without ruining the useful life of the drive. With SSDs, you need special tools that help to actually wipe it and not leave any stray data around. Alternately, the drive may have a Secure Erase command which takes the guesswork out of the process, but you may need a special manufacturer's tool to access that command.

The first tool I'm looking at to do this wipe is a utility called Darik's Boot and Nuke (DBAN). It meets my first two criteria easily and I know it has been around for a while.

### DBAN ### 

You can find DBAN's website [here](https://dban.org/). This website is confusing. It looks like an advertisement. It *IS* an advertisement actually. 
It's an advertisement for a, let's say, 'qualified' data erasure tool. You know, one that conforms to standards and produces a report that you can take to someone who cares about these things and they'll say "Mmm, mmmm, yes. This report has the i's dotted and the t's crossed and has license numbers and such. I can trust this for legal purposes." Then, if something goes wrong, you get to sue them. You don't get to sue anyone with DBAN, but I'm not looking to do that. I'm looking to prevent casual data thieves from stealing my account numbers and passwords and such. 

I thought for sure this couldn't be the site for DBAN, but honestly I can't find another one. I don't know if DBAN isn't being maintained anymore or maybe its creators made this paid utility or what's going on, but this is where you download DBAN. Well, technically you can get it right [here](https://sourceforge.net/projects/dban/files/dban/dban-2.3.0/dban-2.3.0_i586.iso/download) too, directly from Sourceforge.

DBAN is free for personal use, which is what I'm doing. It does NOT have special SSD wiping abilities.

I'm going to do a first-pass using DBAN since I can't get the manufacturer's tool to work.

#### Creating a Bootable DBAN USB Drive ####

[This](https://www.pendrivelinux.com/install-dban-to-a-usb-flash-drive-using-windows/) site is the one that I'm using to create the bootable DBAN thumb drive. It looks easy - you just download a utility that will download DBAN and put it on a thumb drive. I do not know if the thumb drive will be wiped but I'm using one that I don't care about, so we'll see.

All you have to do here is download [this](https://www.pendrivelinux.com/downloads/Universal-USB-Installer/Universal-USB-Installer-1.9.9.0.exe) to get started.

Prerequisites:
* Thumb drive (> 32MB)
* DBAN ISO (from above)

Then I followed these steps:

1. Run the Universal USB Installer
2. Click 'I agree' on the license agreement page.
3. Under 'Step 1 - Select a Distribution' enter the drop-down and keep hitting 'd' until DBAN is highlighted.
4. Aaaand.. you still have to download the ISO even though it's very familiar with DBAN. odd. Use the download link above to get it, then, under 'Step 2' select the ISO you downloaded.
5. Under 'Step 3' select the drive letter of the USB drive. Make sure it's right. You can select to format or wipe the drive. I did not. Mine remains a FAT32 formatted USB with files already on it.
6. Click the 'Create' button.
7. It will tell you what it's about to do. Click 'Yes' if you're brave.
8. It performs these actions...
9. It took about a minute on my PC and then was done. The program exits when complete.

#### Wiping a Drive With DBAN ####

Now I'm going to try to wipe the drive with DBAN. Here's how I did it.

1. Put the USB drive into a USB port on the target computer.
2. Rebooted
3. Brought up the boot menu and selected the USB stick.
4. DBAN boots and I have several options:
* F2 to learn about DBAN
* F3 for a list of quick commands
* F4 to read the RAID disclaimer
* ENTER to start in interactive mode
* autonuke to start in automatic mode.
I'm going for interactive mode, so I press ENTER.
5. DBAN loads and starts initializing - it takes a while on my PC.
6. Then it shows me a list of the drives attached to the PC - I made sure NOT to select the USB drive and instead did the SSD
7. Then, I press 'M' to mess around with the method of wiping. There's one called 'Gutmann Wipe' which claims to be an implementation of a method described in a paper that will securely delete from both magnetic and solid-state media. Looks good.
8. I'm having fun fooling around, so I press 'R' to control the number of rounds of wiping. It was at 1, so I raised it to 2 for no good reason.
9. I could mess around with the PRNG (random number generator) which fills the drive with 'random' data (spoiler alert, it's always semi-random, never really random). I don't care about that, so I don't press 'P'
10. With my drive selected and my method set, I press F10 to start the process.

Oh, there are 35 passes in each round. That may have been overkill.
Uh, this is going to take 52 hours or more.
Hours? Yeah... seconds, minutes... *hours*....
Now it's up to 65 hours.
Probably will go up even more.

No, this isn't really great.

Now we find out if restarting in the middle of this process is really bad for the drive or not (don't worry, I have more 256GB SSDs!).

Haha now it's up to 93 hours....

Okay I restarted. So far so good.

Okay, I tried again with the Gutmann wipe and it became a whole lot more reasonable: 17 hours for the 500GB SDD and 8.5 hours for the 250GB SDD.

### Manufacturer's Tools ###

Another good option is a manufacturer-specific tool to wipe your drive. [This](https://www.makeuseof.com/tag/securely-erase-ssd-without-destroying/)
site has a list of several manufacturers and their specific utilities for managing their SSDs (including wiping).

Honestly, I think this might be the best way to go. It seems as if these drives have a built-in Secure Erase feature that takes the guesswork out of ensuring that everything is actually deleted. This could be good. My drives are Samsung, so I'm going to download that one.

#### Samsung Magician ####

[Here](https://www.samsung.com/semiconductor/minisite/ssd/download/tools/) is the download site for Samsung Magician and [here](https://s3.ap-northeast-2.amazonaws.com/global.semi.static/SAMSUNG_SSD_v6_1_0_200310/SW/675B9E5CD0C5F99B41D766B27C8E0055C3909ECE3AA2FB6B74A2A1EAC1BAC402/Samsung_Magician_Installer.zip) is the direct link to the software.

It seems to want to install itself on Windows which is interesting because I want to wipe the hard drive that has Windows on it. Let's see how this works out.

It may or may not be compatible with my SSD which is an 840 series SSD. 

Well. I can't even install it on this Windows installation because it's so messed up. I'll probably have to remove the drive from the PC and hook it up externally to use this software.

Which I don't want to do right now.

### What I Actually Did ###

I ended up using DBAN and doing the Gutmann wipe - after a brief startup period of confusion, the process settled down to a reasonable wipe time of about 17 hours for a 500GB SDD.

Here's the steps:

1. Put the USB drive into a USB port on the target computer.
2. Rebooted
3. Brought up the boot menu and selected the USB stick.
4. DBAN boots and I have several options:
* F2 to learn about DBAN
* F3 for a list of quick commands
* F4 to read the RAID disclaimer
* ENTER to start in interactive mode
* autonuke to start in automatic mode.
I'm going for interactive mode, so I press ENTER.
5. DBAN loads and starts initializing - it takes a while on my PC.
6. Then it shows me a list of the drives attached to the PC - I made sure NOT to select the USB drive and instead did the SSD
7. Then, I press 'M' to mess around with the method of wiping. There's one called 'Gutmann Wipe' which claims to be an implementation of a method described in a paper that will securely delete from both magnetic and solid-state media. Looks good.
8. I'm having fun fooling around, so I press 'R' to control the number of rounds of wiping. It was at 1, and I leave it there as one pass of Gutmann is sufficient.
9. I could mess around with the PRNG (random number generator) which fills the drive with 'random' data (spoiler alert, it's always semi-random, never really random). I don't care about that, so I don't press 'P'
10. With my drive selected and my method set, I press F10 to start the process.
11. After 17 hour or so, the process is complete. It offers to save logs - I either ignore the prompts or type '0' to ignore them.
12. The process ends up on an advertisement page and stays there. You can safely restart the computer or do whatever now.

## Resources ##

* [Installing and running DBAN from a thumb drive](https://www.pendrivelinux.com/install-dban-to-a-usb-flash-drive-using-windows/)
* [Guide to Wiping SSDs](https://www.makeuseof.com/tag/securely-erase-ssd-without-destroying/)
* [Samsung Magician](https://www.samsung.com/semiconductor/minisite/ssd/download/tools/)