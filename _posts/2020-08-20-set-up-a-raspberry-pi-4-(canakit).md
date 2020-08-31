---
layout: post
title: How to Set up a Raspberry Pi 4 (Canakit)
date: 2020-08-20 12:43
categories: raspberry-pi canakit
---

## Introduction ##

I have an old laptop that downloads my torrents and serves as my Plex server. It, sadly, is dying, so I need a 
replacement. 

These days we have access to an unprecendented amount of low-power processing ability. There are any number of 
small, low-power boards you can buy that will run full distributions of Linux and give you access to everything
you ever wanted in terms of services. The workhorse of this category is the Raspberry Pi.

The latest version of the Pi is the Raspberry Pi 4. It has a 1.5GHz Quad-core ARM processor and options for RAM 
ranging from I think 1GB to 8GB. 

You can get a full loadout of everything you need for $120, and this board ( the size, roughly, of a credit card)
can be a basic Linux server for you, but also a much more advanced one if the need arises. It has power if you need
it, and with Linux behind it, there's almost nothing you can't do.

This guide will discuss how to set up a Raspberry Pi with an eye towards a few different applications/uses.

## Uses ##

While my laptop handled torrents and a Plex server, the Raspberry Pi is a Linux machine that can offer a lot
more services to me. Here's a list of the things I hope to use it for:

* Torrenting
* Plex Server
* General File Sharing
* Jenkins CI Server
* Redmine Server
* Subversion Server
* IFTTT Executor
* Wiki 
* Scanned document storage

More information/goals on some of these are below.

### General File Sharing ###

I hope to identify some sort of file sharing that will allow me to take my 750GB laptop drive that now holds all of 
my old files, attach it to the Raspberry Pi, and mount the drive seamlessly on Windows machines - so that it looks
and acts as if it is a local drive.

### IFTTT Executor ###

I'm just getting in to IFTTT for home automation. Currently, I have a Nest, remote-controlled blinds, and a whole
house fan that I hope to automate in some way.

My ultimate goal is that this system will automatically manage our home temperature - primarly through the whole
house fan. By turning on the whole house fan when the outside temperature is less than the inside temperature, you
can cheaply cool off a house. There are numerous aspects of this that must be integrated, however:

* Monitoring the inside and outside temperatures
* Monitoring whether there are any windows open
* Turning the whole house fan on and off

There are numerous sensors that can be integrated with IFTTT - I know of one in particular that has 8 temperature
sensors with humidity as well (which is always nice). Similarly, there are window sensors that can be integrated
with IFTTT as well. The only major difficulty is controlling the whole house fan, but luckily there's a potential
way that can be done.

My whole house fan has an RF controller. It should be somewhat easy to identify what frequency it uses, buy
a transceiver, and then duplicate the RF signals it produces to turn the fan on and off. If I roll this into my own 
custom PCB, I should be able to either:

1. Create a wifi-enabled board that can control the fan direclty, or 
2. Create a board that plugs into USB on the Raspberry Pi that, when paired with a Python script, will control the
fan (and the Raspberry Pi can handle the network I/O)

I will probably go with approach number 2 due to simplicity. I have the skills to write a Python script that will
have a REST-style web interface that will communicate with the board via USB to serial to control whatever is 
attached to my custom board - it needn't be just one thing at this point.

I will try to cover this approach fully in another blog post, so this is just a teaser.


### Scanned Document Storage ###

Right now, I scan documents directly to my PC one at a time, rename them, and then store them in an encrypted volume.
There are utilities out there that will handle many of the difficult aspects of this process. One of them I know is
[PaperMerge](https://github.com/ciur/papermerge). With PaperMerge, I imagine I can just scan a bunch of pages,
sort them into individual documents, OCR them, align them, etc, and store them in a document management system.

## Unboxing ##

I bought a kit that has all of the stuff you'd need to get a Raspberry Pi 4 up and running:

* Raspberry Pi 4
* Power adapter
* Heat sinks
* Case
* SD card
* Power Switch
* HDMI Cable

The power supply, I will note, is a beast. It's a 5V/3A adapter that will trigger the Turbo Charge on my phone. It's
pretty worth getting a few of them for general use if you have a phone that has a USB-C charging port.

I will say something about the heatsinks: I have not experienced this, but I have been told that the heatsinks
are *not* optional. It's true, you may get by without them, but they will ceratinly add to the overall stability
of the board. And, for a board that supposed to sit in a corner, be powerful and not make waves, stability is 
paramount - especially if you need the power this board offers. Bottom line: USE THE HEATSINKS.

I am unsure right now of the power switch - it's an on/off that goes inline withe the USB-C connection. It might 
very well be useful - we'll see.

The HDMI cable, it should be noted, is a mini (or is it micro?) HDMI to regular HDMI. Very useful.

The case just makes everything neat. Highly recommended.

So, if you're unboxing, all of the stuff removed from the box looks like this:

Photo missing :(

The first thing I'm going to do is to put the heatsinks on. These heatsinks are great because they are just 
stick-ons: peel off the backing and then attach to the appropriate chip. The question is: which chip is the 
appropriate one?

These are the heat sinks:

Photo missing :(

There's three of them, all different sizes, so this should be straightforward, right?

The biggest one goes on the processor: the metal-topped largest chip on the board.

This is a pic of the largest heatsink attached:

Photo missing :(

The second-largest one goes on the SDRAM chip, as seen below:

Photo missing :(

And the final, smallest one, goes on the USB 3.0 controller, as seen below:

Photo missing :(

The other cooling aspect is the fan that came with my kit. You can connect it to 5V for fast operation, or 3.3V for
slower (quieter) operation. Given that I think, after the heatsinks, the fan is kinda overkill, I'll leave it on 3.3V

That configuration looks like this:

Photo missing :(

And then, the fan gets shoved into the case - but how? There's two ways: label up or label down. Label up, I think,
will pull air through the case and blow it out the top. The other way will push it out.

At [this](https://www.raspberrypi.org/forums/viewtopic.php?t=146272) forum post they discuss how to do it. I put it 
with the label facing up in the top cover of the case:

Photo missing :(

Then, to get the case on, I kinda slid the end with the HDMI connector under the tabs on that end of the base. The 
next step should be to put the top piece (not cover) on, but I had to disconnect the fan wires and then route them
through the top piece:

Photo missing :(

Then, I put the top cover on:

Photo missing :(

And now it is a single unit - ready for power.

So, I then plug in the power adapter and hope to see a light. I do, in fact, see a light:

Photo missing :(

So, now I have a nearly fully assembled board.
Nearly.


## SD Card Image Generation ##

The next step in this process is to generate an SD card image that can boot the 
Raspberry Pi to Linux.

Now, technically, the Canakit comes with a pre-imaged SD card that already has Linux
on it. You could just use that, but I'd like to generate one from scratch so that I
know I'm getting the newest software and that I can reproduce the image if needs be.

I'm going to use a variant of Linux called Raspbian Lite because I've used it before.

I will generally be following the steps found [here](https://thisdavej.com/create-a-lightweight-raspberry-pi-system-with-raspbian-lite/).

### Balena Etcher Installation ###

Balena Etcher can be found [here](https://www.balena.io/etcher).

On that page is a download button which I can't get the URL of, but I clicked it and 
downloaded the installer.

I doubled clicked it to start and did the following:

1. On the first balenaEtcher setup screen, agreed to the license by clicking 'I agree'.
2. It installed. That was pretty much it. The program starts.

It already identified the SD card attached via the USB stick, so all I need now is 
the image to burn to it.

### Raspbian Lite ###

The latest Raspbian Lite image can be found [here](https://downloads.raspberrypi.org/raspbian_lite_latest). It will download a zip file
of the latest image.

Inside of the zip is the .img file.

### Burning the Image to the SD Card ###

These are the steps I followed:

1. In balenaEtcher, select the 'Flash from File' option
2. I found the file that I took out of the .zip file and selected it.
3. I clicked the Flash! button.
4. A UAC warning came up and I allowed the operation
5. For a 32GB card, it took a minute or so.

### Using the SD Card ###

To start using the card, insert it into the micro-SD card slot on the 
Raspberry Pi and power it.

I did so, and the first thing I noticed is that a screen came up that said it resized the root partition, then it rebooted.

It booted up and then presented a login screen. This is the default 
login:

Username: pi
Password: raspberry

Now you're in!

The first thing to do is to get it on a network. I'm going to start with
my wireless network for simplicity.

### Initial Setup ###

I have in my previous notes a few things that I did previously.

1. Run the following commands:
{% highlight console %}
cd /etc/default
sudo cp keyboard keyboard.'date +%d%b%y'.org
sudo nano keyboard
{% endhighlight %}
2. Within the 'key' file change the XKBLAYOUT option to "us" and save the file. 

### Raspi-Config ###

Raspi-Config is the top-level configuration utility for the Raspberry Pi.

You access it by typing:
{% highlight console %}
sudo raspi-config
{% endhighlight %}

It presents several options. The first option is to change the password
for the 'pi' user to something other than the default. This is, of 
course, good security policy, so go ahead and do it.

Option 2 is to set network options. Beneath it, option 2 is for wireless
networks, which I then set up.

The first step is to select the country you're using it in - United 
States for me.

Then, you have to type the SSID in manually. Maybe a search box would
have come up if I had put nothing into the text box, but I typed it in 
manually, then typed in the passphrase.

Next, under Interface Options, we can turn on the SSH server.

Under Interface Options, the SSH server is option P2. Then, I selected
to enable the SSH server. THen, it told me it was enabled and that was it.

At this point, the image is pretty much ready for use. I'm going to save it on my PC so I can just revert back to a clean install whenever I 
need.

One good thing to set up now is an SSH key that allows automatic SSH 
login to the Raspberry Pi.

### Saving the SD Card Image to a File ###

I found a guide to create an image from an SD card [here](https://www.howtogeek.com/341944/how-to-clone-your-raspberry-pi-sd-card-for-foolproof-backup/).

The relevant program to use here is Win32DiskImager, which can be 
downloaded [here](https://sourceforge.net/projects/win32diskimager/).



#### SD Cards ####

1. Default RaspPi install - maybe, this one or #13
2. Configured RaspPi install.
3. Default RaspPi install - maybe, this one or #1

#### SD Card Preparation ####

Raspbian Lite

etcher to write to the SD card: https://www.balena.io/etcher/

1. Download Rasbpian Lite from [here](https://downloads.raspberrypi.org/raspbian_lite_latest)
2. Run balena Etcher
3. Burn the zip file to the SD card
4. Remove SD card.
5. Insert microsd card
6. insert HDMI
7. Apply power. - It will resize the image to the full size of the disk and then restart the pi
8. It restarts and does linuxy startup things.
9. Now I have a login screen - 
    * User: pi
    * Password raspberry
10. You're in. It is currently not on any network.
11. Run 'ifconfig' to get the MAC address out of there. The WiFi one for this pi is dc:a6:32:27:9b:83
12. cd /etc/default
13. sudo cp keyboard keyboard.'date +%d%b%y'.org - This backs up the config file
14. sudo vi key (it has nano too)
15. Change XKBLAYOUT="us". Save and exit.
16. sudo raspi-config Top level configuration utility
17. Change the default password to something else. Password for user 'pi' changed to 'moog'
18. Now do 2. Network options
19. Set a hostname - we have no idea what to do, but we'll do that later.
20. Set up the WiFi settings
21. Set to US, set up Wifi network and password.
22. Go to Interface options
23. Turn on SSH server
24. Then we're done.
25. You can set all of the options that you want - we can clone this image after the fact for use on later Pis
26. Reboot it for everything to take effect.
27. Once rebooted and re-logged in, run:
    > sudo apt update
And this will update all of the packages on the Pi
28. Generate some SSH keys:
    > ssh-keygen -t rs -b 4096 -C "Common MOOG logn - Jan2020"
29. The pair generates. Save it in the default place. We probably want passphrases.
30. Do this:
    > cp ~/.ssh
    > cp id_rsa.pub authorized_keys
31. We can copy down the SSH key via copy/paste of the ascii:
    > cd ~/.ssh
    > cat id_rsa
32. Copy the text that comes up to a file on the desktop - I called it  RaspPi_1_RSA_kEY.txt
33. Open PuttyKeygen
34. Load the text file
35. Save Private Key once loaded - you can use a passphrase if you want
36. This process converts the OpenSSH private key to a PuTTY key.
37. Open Putty.
38. Enter the IP address and such for the RaspPi, then on the left go to SSH/Auth
39. Load private key file for authentication and load the file we just created.
40. Go to Connection/Data
41. Set the autologin username to 'pi'
42. The first time, save this information to the RaspPi session.
43. Then click open and you're automatically in.
44. You can also use pagent: start menu->pagent
45. A new tray icon shows up, right click and select View Keys
46. Add the key that you created - if you used a passphrase, you'd enter it here once instead of every time you used putty.

47. When you're fully done with the the RaspPi, shut it down properly with:
    > sudo shutdown -h now
   

## Resources ##
