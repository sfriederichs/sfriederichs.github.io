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

I followed these steps to install Win32DiskImager:

1. On the License Agreement page I accept the agreement and click 'Next'.
2. On the installation path page, I accept the default and click 'Next'.
3. I accepted the default Start Menu folder and clicked 'Next'
4. I opted not to add a Desktop shortcut and clicked 'Next'
5. I reviewed everything and clicked 'Install'
6. The program installed and on the last page I unchecked to read the 
README and allowed starting the program. Then I clicked 'Finish'

After installing, I used the program thusly:

1. Under 'Image File' I used the file dialog to identify the path I 
wanted to save the image file to
2. I set 'Device' to the USB stick that had my SD card in it.
3. I clicked the 'Read' button and it read the SD card into the image 
file I specified. It took about a half hour for a 32GB SD card.

### Shrinking the SD Card Image ###

I'm still trying to work out how to do that on Windows.

## Connecting to Your RasPi via SSH ##

You can get a full Bash terminal via SSH by following these instructions.

### Finding Your RasPi IP Address ###

First, you'll need to find your RasPi's IP address. On the RasPi
terminal, type the following:

{% highlight console %}
ifconfig
{% endhighlight %}

This will give you the network interface status. If you used wireless
to connect to the network, you'll be looking for the IP address of the
'wlan' adapter. If you're using the wired, look for 'eth0'. The IP 
address is the IP address following the 'inet' (or 'inet6' if you're using
IPv6) value. Note it so you can connect to it. 

Mine was 192.168.50.44.

### Connecting with PuTTY ###

The PuTTY client allows you to get a terminal on the RasPi via SSH. 
Here's how to use it:

1. Open PuTTY - the PuTTY Configuration window shows up
2. Enter the IP address of the RasPi under 'Host Name'
3. SSH is the default connection type - if not, switch to it (Port 22)
4. Under 'Saved Sessions', type a name for the session and click the
'Save' button 
5. Click 'Open' to initiate the connection
6. The first time you connect to the RasPi, you'll get a PUTTY Security 
Alert that the server's keys are not cached, etc. etc. Click 'Yes'
7. A login screen is presented. Login with the credentials you set
previously.

#### Setting Up an Auto-Login ####

An auto-login means you don't need to put in your username or password
when you SSH into the RasPi. It makes it easier to work with your Pi, and
when it comes to ease of use, every little bit helps. 

Look at it this way: if you use your Pi to its fullest extent, you're going
to be SSH'ing into it a lot. Thousands of times. You can save two seconds
when you connect to it by doing this. That's hours of time saved. Well worth
it. Also, by lowering the barriers to working with the Pi, you have fewer
excuses to avoid working with it.

To set up auto-login, we'll be generating an SSH key on the Pi and then 
importing it into PuTTY.

Here's what I did to generate the key

{% highlight console %}
pi@raspberrypi:/etc $ ssh-keygen -t rsa -b 4096 -C "Auto-Login 9-9-2020"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/pi/.ssh/id_rsa):
Created directory '/home/pi/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/pi/.ssh/id_rsa.
Your public key has been saved in /home/pi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:WjZxbaL2hnAbQAy/FkKMGiHYSBppfp2unbSCmva6m/U Auto-Login 9-9-2020
The key's randomart image is:
+---[RSA 4096]----+
|** ooo.          |
|Boo..o.    .     |
|+o  o = . o o    |
|.. . + + + o     |
|  . . + S        |
|     + B *       |
|  ..+ + o o      |
| +oo.+   .       |
|===..E           |
+----[SHA256]-----+

pi@raspberrypi:/etc $ cd ~/.ssh
pi@raspberrypi:~/.ssh $ cp id_rsa.pub authorized_keys

{% endhighlight %}

This generates a key in /home/pi/.ssh. We then copy the key to the 
authorized_keys folder. The next step is to save the key to the PC with 
PuTTY on it. Here's how we do that:

{% highlight console %}
pi@raspberrypi:~/.ssh $ cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
Key - no you can't see it. 
-----END OPENSSH PRIVATE KEY-----

{% endhighlight %}

I copied everything after the 'cat id_rsa' and saved it as a text file on my 
desktop: 'RasPi_Personal_Auto-Login_9_9_2020.txt'.

I need to import this key using a program on my PC called 'PuTTYGen'. 
I just type that in at the Start Menu (I have Windows 10).

It comes up. To import my key I follow these steps:

1. Click 'Load' next to 'Load an existing private key file'
2. I navigage to the Desktop where I saved my file, and switch the file type
on the dialog to 'All files' so I can see my text file. It's worth noting at
this point that my file had blank lines before the BEGIN and after the END 
and this prevented PuTTY from understanding the file the first time, until I
deleted them.
3. A dialog box pops up and tells me know that the import was successful but 
that I will have to save the key before it can be used with PuTTY. I click 'OK'.
4. Under 'Save the generated key' I click 'Save Private Key'
5. It wants me to verify that I don't want to save this with a passphrase. I
don't. So I click 'Yes'.
6. I once again save it on the desktop with the same file name, but this time
a '.ppk' extension. At this point you can close PuTTYGen.
7. Open PuTTY.
8. Start the process of generating a new connection for the RasPi by putting in
the IP address in the 'Host Name (or IP address)' box. The connection type 
should already be SSH, so you're set there.
9. On the left-hand side of the window, find the 'Connection/Auth/SSH' menu and
enter it
10. Near 'Private Key File for Authentication' click the 'Browse' button
11. Select the .ppk file you created earlier and click 'OK'
12. Now, on the left-hand side of the window find the 'Connection/Data' menu
13. In this menu, change the auto-login username to 'pi'
14. Now, on the left-hadn side of the screen, go back to the 'Session' menu 
(all the way at the top)
15. Save this connection as something readily understandable like 
'RasPi_Auto-Login'
16. The new connection will show up in the list. Double click it and 
enjoy SSH'ing into your RasPi without a password!

## Installing Docker ##

From [this](https://hub.docker.com/r/jaymoulin/plex/) site, Docker can
be installed in one command, like this:
{% highlight console %}
curl -sSL "https://gist.githubusercontent.com/jaymoulin/e749a189511cd965f45919f2f99e45f3/raw/0e650b38fde684c4ac534b254099d6d5543375f1/ARM%2520(Raspberry%2520PI)%2520Docker%2520Install" | sudo sh && sudo usermod -aG docker $USER
{% endhighlight %}

I pasted that into PuTTY and a whole bunch of stuff started happening, 
but it ended up with this:

{% highlight console %}
 Failed to fetch http://raspbian.raspberrypi.org/raspbian/pool/main/p/python3.7/python3.7-dev_3.7.3-2+deb10u1_armhf.deb  404  Not Found [IP: 93.93.128.193 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?

{% endhighlight %}

I did, indeed need to do an update on apt-get considering I had never
done one before. So, I typed:

{% highlight console %}
sudo apt-get-update
{% endhighlight %}

I let it run to completion (which took a bit of time).

Once it finished, I returned to the original command and ran it.
It also took a while. Then it ended with this error:

{% highlight console %}
Command "/usr/bin/python3 -m pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-agngpakf --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple --extra-index-url https://www.piwheels.org/simple -- setuptools>=40.8.0 wheel "cffi>=1.1; python_implementation != 'PyPy'"" failed with error code 1 in None

{% endhighlight %}

I'm trying a different approach from [here](https://dev.to/rohansawant/installing-docker-and-docker-compose-on-the-raspberry-pi-in-5-simple-steps-3mgl).

Doing this:

{% highlight console %}
curl -sSL https://get.docker.com | sh
{% endhighlight %}

It gave me a warning about already having Docker installed, but I 
just let it do its thing anyway. Nonetheless, it seems to have 
worked just fine.

Then, I followed it up with this:

{% highlight console %}
sudo usermod -aG docker pi
sudo docker run hello-world
{% endhighlight %}

This successfully ran the Docker hello-world. This is, by the way, a 
feature every piece of software should have.

## Removing Docker Containers for a Fresh Re-Install ##

More than once here I've had to completely wipe away and re-download a fresh Docker container. I figured I might as well document the steps so I know how to
do it when I need to again.


## Setting up a Plex Server via Docker ##

Apparently this should be somewhat straightforward.

I'm using directions from [here](https://hub.docker.com/r/jaymoulin/plex/).

First, I need a USB drive for some external storage. I've found an old
8GB stick that seems rediculously slow. I hope it doesn't hurt anything.

### Mounting a USB Drive ###

I plugged my drive in - it should be recognized. I can figure that out
by listing the hard drives on the RasPi. I did this twice - once with
the drive plugged in, and then again without it:

{% highlight console %}
pi@raspberrypi:~ $ ls /dev/sd*
/dev/sda  /dev/sda1

{% endhighlight %}

Seems pretty safe to bet that's the USB stick. I can mount it like
this:

{% highlight console %}
pi@raspberrypi:~ $ sudo mount /dev/sda1 /mnt/usbdrive
mount: /mnt/usbdrive: mount point does not exist.
{% endhighlight %}

Oops. I have to make that directory first:

{% highlight console %}
pi@raspberrypi:/ $ sudo mkdir /mnt/usbdrive
pi@raspberrypi:/ $ sudo mount /dev/sda1 /mnt/usbdrive
{% endhighlight %}

Then it mounts fine.


#### Adding exFAT Support ####

One of my external drives is exFAT-formatted. My RasPi can't mount
that. 

I've found a page [here](https://pimylifeup.com/raspberry-pi-exfat/).

{% highlight console %}

pi@raspberrypi:~ $ sudo apt-get update
Hit:1 https://download.docker.com/linux/raspbian buster InRelease
Get:2 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Get:3 http://raspbian.raspberrypi.org/raspbian buster InRelease [15.0 kB]
Get:4 http://raspbian.raspberrypi.org/raspbian buster/main armhf Packages [13.0 MB]
Get:5 http://archive.raspberrypi.org/debian buster/main armhf Packages [330 kB]
Fetched 13.4 MB in 8s (1,681 kB/s)
Reading package lists... Done
pi@raspberrypi:~ $ sudo apt-get upgrade

---Waaaay too much to retain here---

pi@raspberrypi:~ $ sudo apt-get install exfat-fuse
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  exfat-utils
The following NEW packages will be installed:
  exfat-fuse exfat-utils
0 upgraded, 2 newly installed, 0 to remove and 5 not upgraded.
Need to get 67.7 kB of archives.
After this operation, 260 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf exfat-fuse armhf 1.3.0-1 [27.5 kB]
Get:2 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf exfat-utils armhf 1.3.0-1 [40.3 kB]
Fetched 67.7 kB in 1s (57.7 kB/s)
Selecting previously unselected package exfat-fuse.
(Reading database ... 41633 files and directories currently installed.)
Preparing to unpack .../exfat-fuse_1.3.0-1_armhf.deb ...
Unpacking exfat-fuse (1.3.0-1) ...
Selecting previously unselected package exfat-utils.
Preparing to unpack .../exfat-utils_1.3.0-1_armhf.deb ...
Unpacking exfat-utils (1.3.0-1) ...
Setting up exfat-utils (1.3.0-1) ...
Setting up exfat-fuse (1.3.0-1) ...
Processing triggers for man-db (2.8.5-2) ...
pi@raspberrypi:~ $ sudo apt-get install exfat-utils
Reading package lists... Done
Building dependency tree
Reading state information... Done
exfat-utils is already the newest version (1.3.0-1).
exfat-utils set to manually installed.
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.

pi@raspberrypi:/mnt/usbdrive $ sudo mount /dev/sda1 /mnt/usbdrive
FUSE exfat 1.3.0
WARN: volume was not unmounted cleanly.
fuse: device not found, try 'modprobe fuse' first
pi@raspberrypi:/mnt/usbdrive $ modprobe fuse
modprobe: ERROR: ../libkmod/libkmod.c:586 kmod_search_moddep() could not open moddep file '/lib/modules/4.19.97-v7l+/modules.dep.bin'
modprobe: FATAL: Module fuse not found in directory /lib/modules/4.19.97-v7l+
pi@raspberrypi:/mnt/usbdrive $ sudo mount -t exfat /dev/sda1 /mnt/usbdrive/
FUSE exfat 1.3.0
WARN: volume was not unmounted cleanly.
fuse: device not found, try 'modprobe fuse' first

{% endhighlight %}

Turns out you need to restart the Raspberry Pi after you do all that.

Then, theoretically it could mount the drive, but I started having
difficulties with my USB drive adapters.

9/23/2020

Okay, I finally fixed this problem by ordering a [powered USB 3.0 hub](https://www.amazon.com/gp/product/B00TPMEOYM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) to attach both drives to.

The RasPi could power one drive on its own, but never two, so I needed the powered hub to attach them both at once.

Now, I have both attached and mounted - the exFAT support works great.

9/24/20
Ha ha! Did you think a powered hub would solve my problems? YOU WERE WRONG!

Turns out my powered hub is trying to feed power into my RasPI and IT DOESN'T LIKE IT!

I need a different hub that won't backpower the RasPi.

[Here](https://elinux.org/RPi_Powered_USB_Hubs) is a site that discusses the issue and provides some potentially compatible hubs.

Really, after not looking too hard at the site, [this](https://www.amazon.com/Anker-7-Port-Adapter-Charging-iPhone/dp/B014ZQ07NE/ref=sr_1_1?dchild=1&keywords=anker+AH221&qid=1600991156&sr=8-1) is the only one that will suffice for me.
s
#### Automatically Mounting the Drive at Startup ####

Possible set of directions [here](https://www.raspberrypi.org/documentation/configuration/external-storage.md).

I'm starting at the 'Setting up automatic mounting' section.

I start off by doing this:
{% highlight console %}
pi@raspberrypi:~ $ blk
UUID                                 NAME        FSTYPE PARTUUID                             MOUNTPOINT
                                     sda
16E1-2724                            └─sda1      vfat   ed9bf8d7-01
                                     mmcblk0
4BBD-D3E7                            ├─mmcblk0p1 vfat   738a4d67-01                          /boot
45e99191-771b-4e12-a526-0779148892cb └─mmcblk0p2 ext4   738a4d67-02                          /
{% endhighlight %}

This gives me both the filesystem type and the PARTUUID which I need for the next step. I'm looking at the /dev/sda1 
drive for my information.

For reference, that information is:
* Filesystem Type: vfat
* PARTUUID: ed9bf8d7-01

I copy PARTUUID to the clipboard.

I use this command line to edit the /etc/fstab file:

{% highlight console %}
/
pi@raspberrypi:~ $ sudo nano /etc/fstab

{% endhighlight %}

And at the end I add this line:

{% highlight console %}

PARTUUID=ed9bf8d7-01  /mnt/usbdrive   vfat    defaults,auto,users,rw,nofail 0 0
{% endhighlight %}

Theoretically, that's it. I'm testing it by doing a reboot, like this:

{% highlight console %}
pi@raspberrypi:~ $ sudo reboot

{% endhighlight %}

And, lo and behold, it's fairly non-responsive. The website did suggest that the modifications I made to /etc/fstab would 
cause the startup to take an additional 90 seconds.

I suppose that's accurate.

But, after it's all started up, I run this command and  see this result, and it tells me that all is as it should be:

{% highlight console %}

pi@raspberrypi:~ $ sudo lsblk -o UUID,NAME,FSTYPE,PARTUUID,MOUNTPOINT
UUID                                 NAME        FSTYPE PARTUUID                             MOUNTPOINT
                                     sda
16E1-2724                            └─sda1      vfat   ed9bf8d7-01                          /mnt/usbdrive
                                     mmcblk0
4BBD-D3E7                            ├─mmcblk0p1 vfat   738a4d67-01                          /boot
45e99191-771b-4e12-a526-0779148892cb └─mmcblk0p2 ext4   738a4d67-02                          /

{% endhighlight %}

Yes, the MOUNTPOINT for the /dev/sda1 device is as it should be.

Muy. Bueno.

#### Formatting a New Drive ####

I've recently bought a new external drive since my media server drive is
getting full. So I need to get it ready to work with Plex on the 
Raspberry Pi. It came formatted as NTFS but I don't really want that.
I need to figure out what filesystem I should use and how to forma tit.

Several people on [this](https://serverfault.com/questions/14235/best-file-system-for-media-server) thread are suggesting XFS. They say it's good for large files.

Okay, [this](https://raspberrytips.com/format-mount-usb-drive/) site
suggests that all I need to do is to is this:
{% highlight console %}
sudo mkfs.xfs /dev/sdc1
{% endhighlight %}

Let's try it.

Well it does not have mkfs.xfs. Here's what I think I have to install 
to get that:

{% highlight console %}
pi@raspberrypi:~ $ sudo apt-get install xfsprogs
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libreadline5
Suggested packages:
  xfsdump acl quota
The following NEW packages will be installed:
  libreadline5 xfsprogs
0 upgraded, 2 newly installed, 0 to remove and 29 not upgraded.
Need to get 912 kB of archives.
After this operation, 3,388 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://raspbian.mirror.axinja.net/raspbian buster/main armhf libreadline5 armhf 5.2+dfsg-3 [103 kB]
Get:2 http://raspbian.mirror.axinja.net/raspbian buster/main armhf xfsprogs armhf 4.20.0-1 [809 kB]
Fetched 912 kB in 2s (451 kB/s)
Selecting previously unselected package libreadline5:armhf.
(Reading database ... 52676 files and directories currently installed.)
Preparing to unpack .../libreadline5_5.2+dfsg-3_armhf.deb ...
Unpacking libreadline5:armhf (5.2+dfsg-3) ...
Selecting previously unselected package xfsprogs.
Preparing to unpack .../xfsprogs_4.20.0-1_armhf.deb ...
Unpacking xfsprogs (4.20.0-1) ...
Setting up libreadline5:armhf (5.2+dfsg-3) ...
Setting up xfsprogs (4.20.0-1) ...
update-initramfs: deferring update (trigger activated)
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for libc-bin (2.28-10+rpi1) ...
Processing triggers for initramfs-tools (0.133+deb10u1) ...

{% endhighlight %}

So, now I try this:
{% highlight console %}
pi@raspberrypi:~ $ sudo mkfs.xfs /dev/sdc1
mkfs.xfs: /dev/sdc1 appears to contain an existing filesystem (ntfs).

{% endhighlight %}

Okay, makes sense. Let's try this:

### USB Drive Mounting Configuration ###

Here's the fstab I'm using to mount both of my drives at once:

{% highlight console %}
proc            /proc           proc    defaults          0       0
PARTUUID=738a4d67-01  /boot           vfat    defaults          0       2
PARTUUID=738a4d67-02  /               ext4    defaults,noatime  0       1
PARTUUID=4aaed96b-01  /mnt/nas        vfat    defaults,auto,users,rw,nofail 0 0
PARTUUID=1de59ff2-01  /mnt/torrents   exfat   defaults,auto,users,rw,nofail 0 0

{% endhighlight %}

### Installing Plex via Docker ###

Now, I have a Docker command-line to run:

{% highlight console %}
pi@raspberrypi:/ $ docker run -d --restart=always --name plex -v /mnt/usbdrive:/media --net=host jaymoulin/plex
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/create?name=plex: dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
pi@raspberrypi:/ $ sudo docker run -d --restart=always --name plex -v /mnt/usbdrive:/media --net=host jaymoulin/plex

{% endhighlight %}

Well, that first error is because I forgot to use sudo since I didn't
reboot before I did all this. It ran fine after using sudo.

Then, I go to http://192.168.50.44:32400/manage to manage it...

And it works.

Wow. That was straightforward.

### Running Plex With External HD ###

Okay, so I've got my media drive connected to the RasPi now. How do I re-run Plex with the new configuration?

{% highlight console %}
pi@raspberrypi:~ $ docker stop plex
plex
pi@raspberrypi:~ $ docker ps
CONTAINER ID        IMAGE                                       COMMAND                  CREATED             STATUS                    PORTS                    NAMES
d8d39033ecc1        haugene/transmission-openvpn:latest-armhf   "/usr/bin/entry.sh d…"   10 days ago         Up 14 minutes (healthy)   0.0.0.0:9091->9091/tcp   angry_goldstine
pi@raspberrypi:~ $ docker run -d --restart=always --name plex -v /mnt/torrents:/media --net=host jaymoulin/plex
docker: Error response from daemon: Conflict. The container name "/plex" is already in use by container "c2065d31b4f0ca3e740315a06b9535748bd947baa58acba46f1e91626732f298". You have to remove (or rename) that container to be able to reuse that name.

{% endhighlight %}

Okay.. that wasn't correct...

{% highlight console %}
pi@raspberrypi:~ $ docker run -d --restart=always -v /mnt/torrents:/media jaymoulin/plex
1a0600f158d30e6ee35c7342f5995bc97b213982c96e13a3a087ad2f43e54aff

{% endhighlight %}

Okay! That worked!

Except that I can't access the server from my laptop. Is it running?

{% highlight console %}
pi@raspberrypi:~ $ docker ps
CONTAINER ID        IMAGE                                       COMMAND                  CREATED             STATUS                    PORTS                    NAMES
1a0600f158d3        jaymoulin/plex                              "daemon-pms"             3 minutes ago       Up 3 minutes              32400/tcp                serene_goldberg
d8d39033ecc1        haugene/transmission-openvpn:latest-armhf   "/usr/bin/entry.sh d…"   10 days ago         Up 22 minutes (healthy)   0.0.0.0:9091->9091/tcp   angry_goldstine

{% endhighlight %}

It's running. Is the port forwarding working correctly? Why don't I try adding the port forwarding explicitly to the command line?

{% highlight console %}
docker run -d --restart=always -v /mnt/torrents:/media jaymoulin/plex -p 32400:32400
{% endhighlight %}

{% highlight console %}
pi@raspberrypi:~ $ docker run -d --restart=always -v /mnt/torrents:/media -p 32400:32400 jaymoulin/plex
dad08c59e0f66764b8aa4a7c7dddbae98e1d6938acc7e2ade8eb3d483c1e8163

{% endhighlight %}

THAT worked.

Except...

There must be more. I can't make a proper connection to the Plex server. I can go to http://192.168.50.44:32400/manage and it loads, but it also claims it can't contact my Raspberry Pi.  I'm missing something else here.

What if I remove that container and reinstall it?

{% highlight console %}
pi@raspberrypi:~ $ docker images
REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
jaymoulin/plex                 latest              5eb3d5ff1080        3 weeks ago         202MB
haugene/transmission-openvpn   latest-armhf        2adda52281cd        4 weeks ago         309MB
haugene/transmission-openvpn   latest              ee7968739e88        4 weeks ago         434MB
jaymoulin/transmission         latest              b023adfd1e43        5 months ago        18.4MB
hello-world                    latest              851163c78e4a        8 months ago        4.85kB
pi@raspberrypi:~ $ docker rm
cranky_gauss      focused_wiles     laughing_villani  plex              quirky_bhabha     serene_goldberg   stupefied_jones   zealous_gauss
pi@raspberrypi:~ $ docker rm plex
plex
pi@raspberrypi:~ $ sudo docker run -d --restart=always --name plex -v /mnt/torrents:/media --net=host jaymoulin/plex
c125429ff26e7c9a65d6ba1c190b95b00a09011f49ac780a8a8bb0efaf13d995

{% endhighlight %}

Mmmm, no dice. It's the same behavior.

Maybe I didn't delete it correctly. I'm trying this:

{% highlight console %}
pi@raspberrypi:~ $ docker rmi jaymoulin/plex -f
Untagged: jaymoulin/plex:latest
Untagged: jaymoulin/plex@sha256:53abfee666150e18a4ca6a49e14942b7b93f18984d410fa98ee3a05bc45b03e3
Deleted: sha256:5eb3d5ff108078e2dd8f32b61f58f262c0edd1574fd03fa9cb60a02e54466e5d
pi@raspberrypi:~ $ sudo docker run -d --restart=always --name plex -v /mnt/torrents:/media --net=host jaymoulin/plex
Unable to find image 'jaymoulin/plex:latest' locally
latest: Pulling from jaymoulin/plex
e68f2aaec91c: Already exists
adbe693323bb: Already exists
18214b7504c5: Already exists
c2974ca466f5: Already exists
9e99806a6d24: Already exists
Digest: sha256:53abfee666150e18a4ca6a49e14942b7b93f18984d410fa98ee3a05bc45b03e3
Status: Downloaded newer image for jaymoulin/plex:latest
docker: Error response from daemon: Conflict. The container name "/plex" is already in use by container "c125429ff26e7c9a65d6ba1c190b95b00a09011f49ac780a8a8bb0efaf13d995". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.

{% endhighlight %}

Oof it just doesn't get easier does it?

Looking up that error [here](https://stackoverflow.com/questions/31697828/docker-error-name-is-already-in-use-by-container).

Okay, let's see what its steps do:

{% highlight console %}
pi@raspberrypi:~ $ docker ps -a
CONTAINER ID        IMAGE                                       COMMAND                  CREATED             STATUS                      PORTS                    NAMES
c125429ff26e        jaymoulin/plex                              "daemon-pms"             11 minutes ago      Exited (0) 9 minutes ago                             plex
dad08c59e0f6        jaymoulin/plex                              "daemon-pms"             19 minutes ago      Exited (0) 10 minutes ago                            ecstatic_hamilton
40235647b1c2        jaymoulin/plex                              "-p 32400:32400"         21 minutes ago      Created                     32400/tcp                quirky_bhabha
1a0600f158d3        jaymoulin/plex                              "daemon-pms"             29 minutes ago      Exited (0) 22 minutes ago                            serene_goldberg
d8d39033ecc1        haugene/transmission-openvpn:latest-armhf   "/usr/bin/entry.sh d…"   10 days ago         Up 48 minutes (healthy)     0.0.0.0:9091->9091/tcp   angry_goldstine
5a31a1162635        haugene/transmission-openvpn:latest-armhf   "/usr/bin/entry.sh d…"   2 weeks ago         Exited (0) 11 days ago                               zealous_gauss
adbe9ba4ac34        ee7968739e88                                "dumb-init /etc/open…"   2 weeks ago         Exited (1) 2 weeks ago                               cranky_gauss
858aef494521        ee7968739e88                                "dumb-init /etc/open…"   2 weeks ago         Exited (1) 2 weeks ago                               laughing_villani
883598a1c459        ee7968739e88                                "dumb-init /etc/open…"   2 weeks ago         Exited (1) 2 weeks ago                               focused_wiles
a6193863727c        hello-world                                 "/hello"                 3 weeks ago         Exited (0) 3 weeks ago                               stupefied_jones

{% endhighlight %}

Okay, I need to remove all of the containers associated with jaymoulin/plex.

Then I re-run the command:

{% highlight console %}
pi@raspberrypi:~ $ sudo docker run -d --restart=always --name plex -v /mnt/torrents:/media --net=host jaymoulin/plex
edfb618a400520b0ebd234d957beb78fead1e867733536b083ed59a4523895e0

{% endhighlight %}

And I go to 192.168.50.44:32400/manage....

And it's the initial setup again!

### Transferring Metadata From Windows to Linux ###

I have a Plex server on Windows already. I will be transferring all of the media files by attaching the external hard drive to the RasPi, but 
I need also to transfer all of the metadata such as whether or not a file has been viewed already.

[This](https://forums.plex.tv/t/how-to-transfer-plex-library-from-windows-to-linux/90633/3) is an initial guess as to how to do that.

[This](https://www.reddit.com/r/PleX/comments/7amo55/move_plex_from_windows_to_linux_while_keeping_all/) is another.

[here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)

Ok, the first thing I need to do is identify where on the plex container I need to copy these files.

I can get a shell on the plex container with this command:

{% highlight console %}
pi@raspberrypi:~ $ docker exec -it plex /bin/sh
/ # ls
bin    dev    etc    home   lib    media  mnt    proc   root   run    sbin   srv    sys    tmp    usr    var

{% endhighlight %}

Okie dokie....

It's late. TIme to stop for tonight.

I found them. Not where anyone said they'd be, but here:

{% highlight console %}
/Library/Application Support/Plex Media Server
{% endhighlight %}

On the topic of gathering the files from my current Plex server, I've hit something
that's not a snag, but a difficulty.

You're supposed to zip up the whole Plex directory - maybe without the Cache folder.
My problem is that the Updates folder is liek 6GB. Huge. It will take 20 hours to zip that so I can send it to the hard drive. Some people (in the Reddit thread) say
that you don't even need all of those folders, you can get by with one. 

Sooo.... maybe I don't have to copy the Updates folder.

It's worth a shot.

Heck, my Linux Plex server doesn't even have an Updates folder.

So, how do I stop the Plex server on the Docker?

I listed the processes on a hunch:

{% highlight console %}
~/Library/Application Support/Plex Media Server # ps
PID   USER     TIME   COMMAND
    1 root       0:00 {daemon-pms} /bin/sh /usr/sbin/daemon-pms
    7 root       0:00 {start_pms} /bin/sh /usr/sbin/start_pms
    8 root       1:53 ./Plex Media Server
   22 root       0:21 {Plex Script Hos} Plex Plug-in [com.plexapp.system] /usr/
   68 root       0:00 /usr/lib/plexmediaserver/Plex Tuner Service /usr/lib/plex
 7478 root       0:00 /bin/sh
 7492 root       0:00 ps

{% endhighlight %}

So, I'll kill those.

Here's how I'm going to do this:

1. Zip the Plex config directories on my current server into a zip
2. Put the zip on the external hard drive
3. Attach the external hard drive to the RasPi
4. Reboot the RasPi
5. SSH into the RasPi
6. Get a shell on the Plex Docker
7. Kill Plex on the Docker
8. Unzip the files from the external hard drive to the Plex config directory
9. Restart the RasPi or at least the Plex docker container
10. Verify that I can see the new Plex server on all of my TVs and that the watched status looks the same as on my previous server.

Then, I just have to get torrents working from RSS and I can get rid of that old computer.

I... cannot kill Plex on the Docker with ps alone. 

I will have to find another way.

Every time that I try to kill the Plex process, ALL of my shell sessions on the Docker are ended.

Okay... how is it started at startup?

Nothing in init.d.

This is my /etc/inittab:

{% highlight console %}
# /etc/inittab

::sysinit:/sbin/openrc sysinit
::sysinit:/sbin/openrc boot
::wait:/sbin/openrc default

# Set up a couple of getty's
tty1::respawn:/sbin/getty 38400 tty1
tty2::respawn:/sbin/getty 38400 tty2
tty3::respawn:/sbin/getty 38400 tty3
tty4::respawn:/sbin/getty 38400 tty4
tty5::respawn:/sbin/getty 38400 tty5
tty6::respawn:/sbin/getty 38400 tty6

# Put a getty on the serial port
#ttyS0::respawn:/sbin/getty -L ttyS0 115200 vt100

# Stuff to do for the 3-finger salute
::ctrlaltdel:/sbin/reboot

# Stuff to do before rebooting
::shutdown:/sbin/openrc shutdown

{% endhighlight %}

Nothing Plex in there...

Here's something:
{% highlight console %}

/usr/sbin # cat start_pms
#!/bin/sh

#change these parameters in /etc/default/plexmediaserver
export PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS=6
export PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver
export PLEX_MEDIA_SERVER_MAX_STACK_SIZE=3000
export PLEX_MEDIA_SERVER_TMPDIR=/tmp
export PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR="${HOME}/Library/Application Support"

test -f /etc/default/plexmediaserver && . /etc/default/plexmediaserver

if [ ! -d "$PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR" ]
then
  mkdir -p "$PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR"
  if [ ! $? -eq 0 ]
  then
    echo "WARNING COULDN'T CREATE $PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR, MAKE SURE I HAVE PERMISSON TO DO THAT!"
    exit 1
  fi
fi

export LD_LIBRARY_PATH="${PLEX_MEDIA_SERVER_HOME}/lib"
export TMPDIR="${PLEX_MEDIA_SERVER_TMPDIR}"

echo $PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS $PLEX_MEDIA_SERVER_MAX_STACK_SIZE $PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR

ulimit -s $PLEX_MAX_STACK_SIZE

(cd /usr/lib/plexmediaserver; ./Plex\ Media\ Server)

{% endhighlight %}

This looks like the important line:

{% highlight console %}
(cd /usr/lib/plexmediaserver; ./Plex\ Media\ Server)
{% endhighlight %}

That's the executable. It must start the others. It's definitely the one to kill.

Maybe I can just comment out that line in the script and then restart the docker and then copy everything.

Well, I did the edit and now the container is stuck in a restart loop.

*Sigh* Time to wipe it out and start over.

Okay, I'm wiping it out and starting over with a twist: I'm going to map the configuration directory in the Plex Docker to a local folder where I unzipped the zip file of my
old Plex server's configuration.

I started it with this line:

{% highlight console %}
docker run -d --restart=always --name plex -v /mnt/torrents:/media --net=host -v /mnt/torrents/PlexLib:/root/Library jaymoulin/plex
{% endhighlight %}

And I'm going through initial setup again. Fingers crossed.

And it doesn't look like it took. I'm going to stop the Docker and unzip the zip file back where I mapped the paths, then start it again.

Tried that. No dice.

I went on to the Docker and couldn't even find the configuration library where I left it last time.

It's late. I have to put this to bed.

9/30/20

Okay, I've realized something: I cannot work with the entire Plex metadata directory. It's just too damn large, even without some of the suspicious folders in there. It takes forever to zip, unzip, transfer, etc.
I just can't do it. It won't work.

All I need is the watched status. Plugins? I probably chose the wrong ones last time. I'll get new ones. Logs? No. Settings? Probably not.

I just want watched status, nothing else. How?

[This](https://support.plex.tv/articles/201154527-move-viewstate-ratings-from-one-install-to-another/) maybe.

I needed to download the sqlite command line tools [here](https://sqlite.org/2020/sqlite-tools-win32-x86-3330000.zip).

Then I've done this:

{% highlight console %}
echo ".dump metadata_item_settings" | sqlite3 com.plexapp.plugins.library.db | grep -v TABLE | grep -v INDEX > settings.sql
{% endhighlight %}

That seems to have done it. I now have a settings.sql file.

Now I have to get sqlite3 on the RasPi?

I do this:

{% highlight console %}
pi@raspberrypi:~ $ sudo apt-get install sqlite3
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  sqlite3
0 upgraded, 1 newly installed, 0 to remove and 17 not upgraded.
Need to get 839 kB of archives.
After this operation, 2,278 kB of additional disk space will be used.
Get:1 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf sqlite3 armhf 3.27.2-3 [839 kB]
Fetched 839 kB in 1s (855 kB/s)
Selecting previously unselected package sqlite3.
(Reading database ... 43130 files and directories currently installed.)
Preparing to unpack .../sqlite3_3.27.2-3_armhf.deb ...
Unpacking sqlite3 (3.27.2-3) ...
Setting up sqlite3 (3.27.2-3) ...
Processing triggers for man-db (2.8.5-2) ...
pi@raspberrypi:~ $ sqlite3
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
{% endhighlight %}

That looks like it works.

So I should be able to do this:

{% highlight console %}
cat settings.sql | sqlite3 com.plexapp.plugins.library.db
{% endhighlight %}



### Settings Changes ###

If I change any of the settings in the Plex server, I'll list them
here.

### Plex Plugins ###

If I add any Plex plugins I'll list them here.

### Impressions of Plex on the RasPi ###

I got my Plex server set up and am trying out a movie right now. 

I'm looking at the output of top and the processor sure is pegged. However, it's running the media scanner and that's what's taking most of the CPU.

It must take a long while to download the episode descriptions and cover art and such. The TV shows are taking forever.

Only certain movies are working. The broken ones just say that the movie isn't available. It's not predicated on the playback mode.

Maybe it will even out.

It's playing HD just fine. No long loading times or anything.

Once the cover art is downloaded it seems that when browsing the movies everything loads pretty quickly.

TV art and descriptions are starting to come in. 

Missing sound on a couple of new downloads. Older TV shows are working fine though.

## Setting up VPN on a RasPi ##

[Here](https://gist.github.com/superjamie/ac55b6d2c080582a3e64) is a 
good starting point for my application.

### NTP Setup ###

I'm starting off with the NTP section.

The steps claim I probably won't have to do anything - it should be set up
already.

I do this command line to verify that NTP is installed and working:

{% highlight console %}
pi@raspberrypi:/ $ ntpq -p
-bash: ntpq: command not found
{% endhighlight %}

Hmmmm, that's not comforting.

Looking around on the internet, I find a thread that may help [here](https://www.raspberrypi.org/forums/viewtopic.php?t=192020).

I run this command as suggested:

{% highlight console %}
sudo apt-get update && sudo apt-get -y install ntp
{% endhighlight %}

And when I do that, it installs - it involves a lot of scrolling but there's no 
errors. When I try the verification step again, I get this:

{% highlight console %}
pi@raspberrypi:/ $ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 0.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.001
 1.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.001
 2.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.001
 3.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.001
 tick.chi1.ntfo. 206.55.64.76     3 u    1   64    1   36.594   -5.182   0.372
*logiplex.net    18.26.4.105      2 u    2   64    1   55.960   -0.119   0.452
 darwin.kenyonra 80.72.67.48      3 u    1   64    1   39.756   -2.509   1.550
 B1-66ER.matrix. 129.6.15.30      2 u    2   64    1   54.886   -1.254   0.524
 srcf-ntp.stanfo 171.64.7.105     2 u    2   64    1   37.839   -0.233   0.168
 t2.time.bf1.yah 129.6.15.28      2 u    2   64    1   71.870    1.917   0.410
 ns2.nuso.cloud  142.66.101.13    2 u    2   64    1   28.342   -0.186   0.717
 las1.cdn.doridi 141.57.74.83     3 u    1   64    1   39.951   -5.965   0.799
+karhu.miuku.net 207.197.87.124   4 u    -   64    1   38.363   -1.599   1.145
 t1.time.bf1.yah 129.6.15.28      2 u    1   64    1   72.448   -2.741   0.731
 ntp.xtom.com    204.123.2.5      2 u    -   64    1   38.231   -2.628   2.101
-50-205-244-109- 50.205.244.27    2 u    1   64    1   41.924   -0.940   0.915
 mis.wci.com     216.218.192.202  2 u    -   64    1   61.305   10.074   0.895
 clock.fmt.he.ne .CDMA.           1 u    1   64    1   37.733   -2.424   0.973
 tick.sol.net    206.55.64.77     3 u    -   64    1   89.365   11.456   3.823
 time.cloudflare 10.98.8.8        3 u    -   64    1    9.788   -1.072   0.596

{% endhighlight %}

That looks right.

### Installing OpenVPN ###

This is how I attempt to install OpenVPN via apt-get:

{% highlight console %}
pi@raspberrypi:/ $ sudo apt-get install openvpn
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  easy-rsa libccid liblzo2-2 libpkcs11-helper1 opensc opensc-pkcs11 pcscd
Suggested packages:
  pcmciautils openvpn-systemd-resolved
The following NEW packages will be installed:
  easy-rsa libccid liblzo2-2 libpkcs11-helper1 opensc opensc-pkcs11 openvpn pcscd
0 upgraded, 8 newly installed, 0 to remove and 66 not upgraded.
Need to get 1,958 kB of archives.
After this operation, 5,437 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf easy-rsa all 3.0.6-1 [37.9 kB]
Get:2 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libccid armhf 1.4.30-1 [328 kB]
Get:3 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf liblzo2-2 armhf 2.10-0.1 [48.4 kB]
Get:4 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libpkcs11-helper1 armhf 1.25.1-1 [41.9 kB]
Get:5 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf opensc-pkcs11 armhf 0.19.0-1 [718 kB]
Get:6 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf opensc armhf 0.19.0-1 [274 kB]
Get:7 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf openvpn armhf 2.4.7-1 [426 kB]
Get:8 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf pcscd armhf 1.8.24-1 [84.8 kB]
Fetched 1,958 kB in 3s (645 kB/s)
Preconfiguring packages ...
Selecting previously unselected package easy-rsa.
(Reading database ... 41325 files and directories currently installed.)
Preparing to unpack .../0-easy-rsa_3.0.6-1_all.deb ...
Unpacking easy-rsa (3.0.6-1) ...
Selecting previously unselected package libccid.
Preparing to unpack .../1-libccid_1.4.30-1_armhf.deb ...
Unpacking libccid (1.4.30-1) ...
Selecting previously unselected package liblzo2-2:armhf.
Preparing to unpack .../2-liblzo2-2_2.10-0.1_armhf.deb ...
Unpacking liblzo2-2:armhf (2.10-0.1) ...
Selecting previously unselected package libpkcs11-helper1:armhf.
Preparing to unpack .../3-libpkcs11-helper1_1.25.1-1_armhf.deb ...
Unpacking libpkcs11-helper1:armhf (1.25.1-1) ...
Selecting previously unselected package opensc-pkcs11:armhf.
Preparing to unpack .../4-opensc-pkcs11_0.19.0-1_armhf.deb ...
Unpacking opensc-pkcs11:armhf (0.19.0-1) ...
Selecting previously unselected package opensc.
Preparing to unpack .../5-opensc_0.19.0-1_armhf.deb ...
Unpacking opensc (0.19.0-1) ...
Selecting previously unselected package openvpn.
Preparing to unpack .../6-openvpn_2.4.7-1_armhf.deb ...
Unpacking openvpn (2.4.7-1) ...
Selecting previously unselected package pcscd.
Preparing to unpack .../7-pcscd_1.8.24-1_armhf.deb ...
Unpacking pcscd (1.8.24-1) ...
Setting up libccid (1.4.30-1) ...
Setting up pcscd (1.8.24-1) ...
Created symlink /etc/systemd/system/sockets.target.wants/pcscd.socket → /lib/systemd/system/pcscd.socket.
Setting up liblzo2-2:armhf (2.10-0.1) ...
Setting up libpkcs11-helper1:armhf (1.25.1-1) ...
Setting up opensc-pkcs11:armhf (0.19.0-1) ...
Setting up easy-rsa (3.0.6-1) ...
Setting up openvpn (2.4.7-1) ...
[ ok ] Restarting virtual private network daemon.:.
Created symlink /etc/systemd/system/multi-user.target.wants/openvpn.service → /lib/systemd/system/openvpn.service.
Setting up opensc (0.19.0-1) ...
Processing triggers for systemd (241-7~deb10u2+rpi1) ...

{% endhighlight %}

So it looks like that worked.

### Downloading the PIA OpenVPN Profiles ###

Next, i follow the steps to download and uncompress the PIA OpenVPN profiles:

{% highlight console %}
pi@raspberrypi:/ $ sudo wget https://www.privateinternetaccess.com/openvpn/openvpn.zip
--2020-09-04 03:17:11--  https://www.privateinternetaccess.com/openvpn/openvpn.zip
Resolving www.privateinternetaccess.com (www.privateinternetaccess.com)... 69.192.206.86
Connecting to www.privateinternetaccess.com (www.privateinternetaccess.com)|69.192.206.86|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 131897 (129K) [application/zip]
Saving to: ‘openvpn.zip’

openvpn.zip             100%[============================>] 128.81K  --.-KB/s    in 0.1s

2020-09-04 03:17:11 (1.11 MB/s) - ‘openvpn.zip’ saved [131897/131897]

pi@raspberrypi:/ $ sudo apt-get install unzip
Reading package lists... Done
Building dependency tree
Reading state information... Done
unzip is already the newest version (6.0-23+deb10u1).
0 upgraded, 0 newly installed, 0 to remove and 66 not upgraded.
pi@raspberrypi:/ $ unzip openvpn.zip -d openvpn
Archive:  openvpn.zip
checkdir:  cannot create extraction directory: openvpn
           Permission denied
pi@raspberrypi:/ $ sudo unzip openvpn.zip -d openvpn
Archive:  openvpn.zip
  inflating: openvpn/AU Melbourne.ovpn
  inflating: openvpn/AU Perth.ovpn
  inflating: openvpn/AU Sydney.ovpn
  inflating: openvpn/Albania.ovpn
  inflating: openvpn/Argentina.ovpn
  inflating: openvpn/Austria.ovpn
  inflating: openvpn/Belgium.ovpn
  inflating: openvpn/Bosnia and Herzegovina.ovpn
  inflating: openvpn/Bulgaria.ovpn
  inflating: openvpn/CA Montreal.ovpn
  inflating: openvpn/CA Ontario.ovpn
  inflating: openvpn/CA Toronto.ovpn
  inflating: openvpn/CA Vancouver.ovpn
  inflating: openvpn/Czech Republic.ovpn
  inflating: openvpn/DE Berlin.ovpn
  inflating: openvpn/DE Frankfurt.ovpn
  inflating: openvpn/Denmark.ovpn
  inflating: openvpn/Estonia.ovpn
  inflating: openvpn/Finland.ovpn
  inflating: openvpn/France.ovpn
  inflating: openvpn/Greece.ovpn
  inflating: openvpn/Hungary.ovpn
  inflating: openvpn/Iceland.ovpn
  inflating: openvpn/India.ovpn
  inflating: openvpn/Ireland.ovpn
  inflating: openvpn/Israel.ovpn
  inflating: openvpn/Italy.ovpn
  inflating: openvpn/Japan.ovpn
  inflating: openvpn/Latvia.ovpn
  inflating: openvpn/Lithuania.ovpn
  inflating: openvpn/Luxembourg.ovpn
  inflating: openvpn/Moldova.ovpn
  inflating: openvpn/Netherlands.ovpn
  inflating: openvpn/New Zealand.ovpn
  inflating: openvpn/North Macedonia.ovpn
  inflating: openvpn/Norway.ovpn
  inflating: openvpn/Poland.ovpn
  inflating: openvpn/Portugal.ovpn
  inflating: openvpn/Romania.ovpn
  inflating: openvpn/Serbia.ovpn
  inflating: openvpn/Singapore.ovpn
  inflating: openvpn/Slovakia.ovpn
  inflating: openvpn/South Africa.ovpn
  inflating: openvpn/Spain.ovpn
  inflating: openvpn/Sweden.ovpn
  inflating: openvpn/Switzerland.ovpn
  inflating: openvpn/Turkey.ovpn
  inflating: openvpn/UAE.ovpn
  inflating: openvpn/UK London.ovpn
  inflating: openvpn/UK Manchester.ovpn
  inflating: openvpn/UK Southampton.ovpn
  inflating: openvpn/US Atlanta.ovpn
  inflating: openvpn/US California.ovpn
  inflating: openvpn/US Chicago.ovpn
  inflating: openvpn/US Dallas.ovpn
  inflating: openvpn/US Denver.ovpn
  inflating: openvpn/US East.ovpn
  inflating: openvpn/US Florida.ovpn
  inflating: openvpn/US Houston.ovpn
  inflating: openvpn/US Las Vegas.ovpn
  inflating: openvpn/US New York City.ovpn
  inflating: openvpn/US Seattle.ovpn
  inflating: openvpn/US Silicon Valley.ovpn
  inflating: openvpn/US Washington DC.ovpn
  inflating: openvpn/US West.ovpn
  inflating: openvpn/Ukraine.ovpn
  inflating: openvpn/ca.rsa.2048.crt
  inflating: openvpn/crl.rsa.2048.pem

{% endhighlight %}

Then, I copy the certificates and profiles:

{% highlight console %}
pi@raspberrypi:/ $ sudo cp openvpn/ca.rsa.2048.crt openvpn/crl.rsa.2048.pem /etc/openvpn/
pi@raspberrypi:/ $ sudo cp openvpn/US\ Denver.ovpn  /etc/openvpn/US\ Denver.conf

{% endhighlight %}

### Setting Up a Password File ###

Here's what I did:

{% highlight console %}

pi@raspberrypi:~ $ sudo nano /etc/openvpn/login
pi@raspberrypi:~ $ sudo chmod 600 /etc/openvpn/login

{% endhighlight %}

And, of course, in the *login* file I put my username on the first name, and my
password on the second line. The second command changed the permissions on the 
file so only the root user can read it.

Next, I need to configure the VPN to use that file.

I need to edit the '/etc/openvpn/US\ Denver.conf' file. I changed this line:

{% highlight console %}
auth-user-pass
{% endhighlight %}

to this:

{% highlight console %}
auth-user-pass /etc/openvpn/login
{% endhighlight %}

This configured OpenVPN to use that password file.

### Testing the VPN ###

Here's the command line I used to test the VPN as well as the result:

{% highlight console %}
pi@raspberrypi:~ $ sudo openvpn --config /etc/openvpn/US\ Denver.conf
Mon Sep  7 04:12:45 2020 OpenVPN 2.4.7 arm-unknown-linux-gnueabihf [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Feb 20 2019
Mon Sep  7 04:12:45 2020 library versions: OpenSSL 1.1.1d  10 Sep 2019, LZO 2.10
Mon Sep  7 04:12:45 2020 TCP/UDP: Preserving recently used remote address: [AF_INET]174.128.242.226:1198
Mon Sep  7 04:12:45 2020 UDP link local: (not bound)
Mon Sep  7 04:12:45 2020 UDP link remote: [AF_INET]174.128.242.226:1198
Mon Sep  7 04:12:45 2020 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
Mon Sep  7 04:12:45 2020 [7b0c1628f354dbacdcc3d98ef26163] Peer Connection Initiated with [AF_INET]174.128.242.226:1198
Mon Sep  7 04:12:47 2020 TUN/TAP device tun0 opened
Mon Sep  7 04:12:47 2020 /sbin/ip link set dev tun0 up mtu 1500
Mon Sep  7 04:12:47 2020 /sbin/ip addr add dev tun0 local 10.7.11.6 peer 10.7.11.5
Mon Sep  7 04:12:47 2020 Initialization Sequence Completed

{% endhighlight %}

This is a successful result. Ctrl+C exits this. 

## Setting up a Torrent Client on RasPi ##

[This](https://hub.docker.com/r/jaymoulin/transmission/) seems to be
a great Docker-ish way to get a torrent client.

First, I created folders on my USB drive for torrentFiles and for torrent downlodads.

Then, I ran this:

{% highlight console %}

pi@raspberrypi:~ $ docker run -d --restart=always --name transmission -u $(id -u) -v /mnt/usbdrive/torrentFiles/ -v /mnt/usbdrive/torrents -p 9091:80 -p 51413:51413 -p 51413:51413/udp -e PORT=80 jaymoulin/transmission
Unable to find image 'jaymoulin/transmission:latest' locally
latest: Pulling from jaymoulin/transmission
0776aeec3430: Pull complete
04dcf910c102: Pull complete
5e175c9477f5: Pull complete
1cc20c3a8ea5: Pull complete
f01a37760413: Pull complete
Digest: sha256:acfc58e4229522b728c2be41be44de7ff73729da5e05fbd0bf31b45e69e1f92a
Status: Downloaded newer image for jaymoulin/transmission:latest
d5061c55932a9eb2852d0f5a3b4ac91f5718d244cfc4419e8f57caf96413151d9

{% endhighlight %}

That seems to have worked splendidly. Let's see what we have to do to verify
the installation.

Ah, I made a mistake. I didn't configure the paths correctly. But I had to
remove the transmssion Docker and then re-download it again, with these commands:

{% highlight console %}
pi@raspberrypi:~ $ docker stop transmission
transmission
pi@raspberrypi:~ $ docker rm transmission
transmission
pi@raspberrypi:~ $ docker run -d --restart=always --name transmission -u $(id -u) -v /path/to/incoming/torrents:/mnt/usbdrive/torrentFiles/ -v /path/to/downloaded/files:/mnt/usbdrive/torrents -p 9091:80 -p 51413:51413 -p 51413:51413/udp -e PORT=80 jaymoulin/transmission
f2dc5fcfe9e08b96e55ff71158d0457e7beb9294c5c2585ff6b580d2659f3926

{% endhighlight %}

Now, at this point I should be able to go to 192.168.50.44:9091 with a web 
browser and you should see the Transmission web interface.

I do not.

This saddens me.

How can I fix this?

### Transmission and OpenVPN in One Docker ###

I've found a website [here](https://hub.docker.com/r/haugene/transmission-openvpn)

It says I should install it with this command line:

{% highlight console %}
$ docker run --cap-add=NET_ADMIN -d \
              -v /your/storage/path/:/data \
              -v /etc/localtime:/etc/localtime:ro \
              -e CREATE_TUN_DEVICE=true \
              -e OPENVPN_PROVIDER=PIA \
              -e OPENVPN_CONFIG=CA\ Toronto \
              -e OPENVPN_USERNAME=user \
              -e OPENVPN_PASSWORD=pass \
              -e WEBPROXY_ENABLED=false \
              -e LOCAL_NETWORK=192.168.0.0/16 \
              --log-driver json-file \
              --log-opt max-size=10m \
              -p 9091:9091 \
              haugene/transmission-openvpn
{% endhighlight %}

What would I need to change that to for my setup?

{% highlight console %}
$ docker run --cap-add=NET_ADMIN -d \
              -v /mnt/usbdrive/torrents/:/data \
              -v /etc/localtime:/etc/localtime:ro \
              -e CREATE_TUN_DEVICE=true \
              -e OPENVPN_PROVIDER=PIA \
              -e OPENVPN_CONFIG=CA\ Denver \
              -e OPENVPN_USERNAME=user \
              -e OPENVPN_PASSWORD=pass \
              -e WEBPROXY_ENABLED=false \
              -e LOCAL_NETWORK=192.168.50.0/24 \
              --log-driver json-file \
              --log-opt max-size=10m \
              -p 9091:9091 \
              haugene/transmission-openvpn
{% endhighlight %}

I'm also looking at the list of environment variables from [here](https://haugene.github.io/docker-transmission-openvpn/arguments/).

I'm particularly interested in the LOCAL_NETWORK option. I want the value to 
encompass everything in the 192.168.50.xxx which is my local LAN.

I'm using [this](http://jodies.de/ipcalc?host=192.168.50.0&mask1=24&mask2=) site 
to calculate the proper value. Turns out that it's "192.168.50.0/24".

So, I ran the above, and got this result:

{% highlight console %}

Unable to find image 'haugene/transmission-openvpn:latest' locally
latest: Pulling from haugene/transmission-openvpn
3f2411103a12: Pull complete
4da04088b2c2: Pull complete
ab1184837b6f: Pull complete
354c6da61dcc: Pull complete
faed08aca42b: Pull complete
d7c7f0b89ec9: Pull complete
f206b2064c44: Pull complete
85d221ac7edf: Pull complete
9d3429593a91: Pull complete
Digest: sha256:56177b53358134f4d1b5ecab999d982a34fdb741fe7cbf9bef48efcfbb017a11
Status: Downloaded newer image for haugene/transmission-openvpn:latest
883598a1c45969cc21365928b29282a1d4fb509a3d9cad7ac414d407463d191a

{% endhighlight %}

But I still don't get a web interface.

So I try this:

{% highlight console %}
pi@raspberrypi:~ $ docker run haugene/transmission-openvpn
standard_init_linux.go:211: exec user process caused "exec format error"

{% endhighlight %}

What does that even mean?

It might mean that Docker container isn't meant for this architecture.

So I'll use this command to pull the correct Docker container:



{% highlight console %}
 docker run --cap-add=NET_ADMIN -d               		\
            -v /mnt/usbdrive/torrents/:/data        	\       
			-v /etc/localtime:/etc/localtime:ro      	\	         
			-e CREATE_TUN_DEVICE=true               	\
			-e OPENVPN_PROVIDER=PIA               		\
			-e OPENVPN_CONFIG=CA\ Denver           		\    
			-e OPENVPN_USERNAME=user               		\
			-e OPENVPN_PASSWORD=pass               		\
			-e WEBPROXY_ENABLED=false               	\	
			-e LOCAL_NETWORK=192.168.50.0/24         	\      
			--log-driver json-file               		\
			--log-opt max-size=10m               		\
			-p 9091:9091               					\
			haugene/transmission-openvpn:latest-armhf

Unable to find image 'haugene/transmission-openvpn:latest-armhf' locally
latest-armhf: Pulling from haugene/transmission-openvpn
770c4d307a2e: Pull complete
0b233ee442e0: Pull complete
3a9ab8cba906: Pull complete
85d08d01a9ef: Pull complete
29c792061d71: Pull complete
fedbfe21d473: Pull complete
af93c37ed24c: Pull complete
b3bae2cc3e34: Pull complete
9e02f8493f06: Pull complete
eb2f72d6761c: Pull complete
fe524bef95e5: Pull complete
8c1d821b314a: Pull complete
910247dcf4fc: Pull complete
8ace303956b5: Pull complete
e97232dee793: Pull complete
c4e62d28fe61: Pull complete
dab34ad90a69: Pull complete
82a4a95e2c78: Pull complete
5f15f9ab2f3c: Pull complete
bf388eb360ba: Pull complete
f96e0c5e7936: Pull complete
fe1e7300c139: Pull complete
49dafb91bee7: Pull complete
1d6d8f0bed77: Pull complete
e5b177c0172c: Pull complete
eede4bbb4adc: Pull complete
0e77e9ff87a9: Pull complete
420926a0a652: Pull complete
Digest: sha256:dc1b6a7c8b59ac806cae791c976efdd224c51de09f1a2b82ce85d61a8944d40b
Status: Downloaded newer image for haugene/transmission-openvpn:latest-armhf
5a31a1162635ae7e64b4e0bea3c82dc19c9064981f486288b77726e927307452

{% endhighlight %}

Now a docker ps shows its running. Is the web interface running?

Yes, in fact, it is.

Success!

However, I had no idea whether it is connected to the internet via VPN or not.
And I see no mention of an RSS option.

### Testing the Torrent Client to Make Sure It's Using VPN ###

I'm going to try downloading a [slackware ISO](http://www.slackware.com/torrents/slackware-14.2-install-d1.torrent) torrent first for a few reasons:

1. It's legal so I won't get into any trouble if the VPN isn't working
2. It will show if Bittorrent is working at all
3. I will hopefully be able to see where the data is being routed (hopefully the
VPN)

Sadly, once I start trying to download something, everything slows to a crawl.
I can't even get the web interface to come back up.

I *think* it's my USB drive. I think it's so slow that it sucks.

I think I need to try another USB drive.

Oh look I waited a bit and it is in fact working.

So, to get a terminal *inside* the Docker container running Transmission, I do 
this:

{% highlight console %}
pi@raspberrypi:~ $ docker exec -it zealous_gauss /bin/bash
root@5a31a1162635:/# 

{% endhighlight %}

And then, since my torrent is running, I will use netstat to show me the traffic
into and out of the Docker container:

{% highlight console %}
root@5a31a1162635:/# netstat
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp   119678      0 10.15.11.6:50113        189.115.109.112.s:54912 ESTABLISHED
tcp        0      0 10.15.11.6:50869        i19-les01-ntr-176:28552 ESTABLISHED
tcp        0      0 10.15.11.6:56221        cpe-24-209-179-35:63550 ESTABLISHED
tcp        0      0 10.15.11.6:44717        104-163-137-251.q:37040 TIME_WAIT
tcp   496963      0 10.15.11.6:44703        S0106105611beaa18:42067 ESTABLISHED
tcp        0      1 10.15.11.6:60537        114.234.81.95.cht:40618 SYN_SENT
tcp        1      0 10.15.11.6:58217        praetorian.stealth:8082 CLOSE_WAIT
tcp        0      0 10.15.11.6:40471        192-3-206-204-hos:53517 ESTABLISHED
tcp        0      0 10.15.11.6:42341        thisis.feralhosti:17007 ESTABLISHED
tcp        0      0 5a31a1162635:9091       DESKTOP-NE76661:57823   ESTABLISHED
tcp        0      0 10.15.11.6:57791        095160201134.ostr:47852 ESTABLISHED
tcp        0      0 10.15.11.6:40471        pool-100-16-217-22:5752 ESTABLISHED
tcp        0      0 10.15.11.6:51691        pool-108-41-37-223:1198 ESTABLISHED
tcp   2492400      0 10.15.11.6:59299        udp069456uds.hawai:6881 ESTABLISHED
tcp      644      0 5a31a1162635:9091       DESKTOP-NE76661:57825   ESTABLISHED
tcp        0      1 10.15.11.6:40471        174-23-172-136.sl:32935 LAST_ACK
tcp        0      1 10.15.11.6:48933        hosted-by.leasewe:52822 LAST_ACK
tcp       95      0 10.15.11.6:39363        net-2-35-125-79.c:37563 ESTABLISHED
tcp        0      0 10.15.11.6:33795        ifconfig.com.ua:6981    ESTABLISHED
tcp   1096669      0 10.15.11.6:45365        136.56.33.112:51414     ESTABLISHED
tcp        0      0 10.15.11.6:44771        125-237-50-253-fi:36881 TIME_WAIT
tcp     1060      0 5a31a1162635:9091       DESKTOP-NE76661:57824   ESTABLISHED
tcp        0      1 10.15.11.6:42801        cpc114408-walt26-:61325 SYN_SENT
tcp        0      0 10.15.11.6:40471        unn-195-181-170-2:33393 ESTABLISHED
tcp        0      0 10.15.11.6:40471        41.60.172.170:21799     ESTABLISHED
tcp       88      0 10.15.11.6:40471        lfbn-ren-1-1726-4:63602 ESTABLISHED
tcp        0      0 10.15.11.6:45225        p5b053575.dip0.t-:36011 ESTABLISHED
tcp        0      0 10.15.11.6:49847        hosted-by.leasewe:52822 ESTABLISHED
tcp        0     87 10.15.11.6:60847        i19-les01-ntr-176:28552 LAST_ACK
tcp        0      0 10.15.11.6:60219        94-209-171-232.cab:6890 ESTABLISHED
tcp    49349      0 10.15.11.6:50601        540035A4.dsl.pool:49409 ESTABLISHED
tcp        0      0 10.15.11.6:52659        p54bde485.dip0.t-:51413 ESTABLISHED
tcp        0      1 10.15.11.6:57631        ns3043883.ip-94-2:50000 LAST_ACK
tcp        0   2469 10.15.11.6:46235        37-146-254-56.bro:45536 ESTABLISHED
tcp        0      0 10.15.11.6:40471        45.162.228.187:44717    ESTABLISHED
tcp        0      0 10.15.11.6:40471        93-143-149-148.ad:49708 ESTABLISHED
tcp        0      0 10.15.11.6:54213        ns383199.ip-46-10:51413 ESTABLISHED
tcp        0      0 10.15.11.6:50625        ns3043883.ip-94-2:50000 ESTABLISHED
tcp     1060      0 5a31a1162635:9091       DESKTOP-NE76661:57821   ESTABLISHED
tcp    65588      0 10.15.11.6:55003        udp099529uds.hawai:6881 ESTABLISHED
tcp        0      0 10.15.11.6:40471        5-13-122-102.resi:60226 ESTABLISHED
tcp        0      0 5a31a1162635:9091       DESKTOP-NE76661:57822   ESTABLISHED
tcp        0      0 10.15.11.6:42243        173.44.55.179:8589      ESTABLISHED
tcp   667441      0 10.15.11.6:42321        d207-81-235-198.b:14956 ESTABLISHED
tcp        0      0 10.15.11.6:35693        c-73-137-224-199.:22223 ESTABLISHED
tcp        0      0 10.15.11.6:52651        a23-48-11-96.deplo:http ESTABLISHED
tcp        0      0 5a31a1162635:9091       DESKTOP-NE76661:57826   ESTABLISHED
tcp        0      1 10.15.11.6:49695        unn-212-102-33-167:8297 SYN_SENT
tcp    65588      0 10.15.11.6:40471        5-13-122-102.resi:60226 ESTABLISHED
tcp        0      0 5a31a1162635:9091       DESKTOP-NE76661:57822   ESTABLISHED
tcp        1      0 10.15.11.6:42243        173.44.55.179:8589      CLOSE_WAIT
tcp   585345    216 10.15.11.6:42321        d207-81-235-198.b:14956 ESTABLISHED
tcp        0      0 10.15.11.6:35693        c-73-137-224-199.:22223 ESTABLISHED
tcp        0      0 10.15.11.6:52651        a23-48-11-96.deplo:http ESTABLISHED
tcp        0      0 5a31a1162635:9091       DESKTOP-NE76661:57826   ESTABLISHED
tcp        0      1 10.15.11.6:49695        unn-212-102-33-167:8297 SYN_SENT
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
root@5a31a1162635:/# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
        RX packets 230732  bytes 278810967 (265.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 72343  bytes 10895658 (10.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 80  bytes 11827 (11.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 80  bytes 11827 (11.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.15.11.6  netmask 255.255.255.255  destination 10.15.11.5
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 100  (UNSPEC)
        RX packets 195063  bytes 256756956 (244.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 62520  bytes 3979045 (3.7 MiB)
        TX errors 0  dropped 821 overruns 0  carrier 0  collisions 0

{% endhighlight %}

So, the 10.x.x.x activity is all over the VPN (as we can see from the ifconfig
showing that the tun0 address is 10.15.11.6). The other IPV6 activity is 
the web interface for Transmission (you can see it's on the 9091 port).

With my configuration, the .torrent file I uploaded via the web interface is 
placed into '/mnt/usbdrive/torrents/transmission-home/torrents'.  The actual 
file is downloaded (temporarily) to '/mnt/usbdrive/torrents/transmission-home/resume'
and will be copied when it's finished to...?

### Getting the Torrent Docker Container to Start Automatically ###

Turns out my docker container is not starting automatically. Let's figure out how 
to do that.

I'm working from instructions [here](https://docs.docker.com/config/containers/start-containers-automatically/).

Turns out all you need to do is add -restart always to the command

{% highlight console %}
docker run --restart always --cap-add=NET_ADMIN -d     	\
            -v /mnt/usbdrive/torrents/:/data        	\       
			-v /etc/localtime:/etc/localtime:ro      	\	         
			-e CREATE_TUN_DEVICE=true               	\
			-e OPENVPN_PROVIDER=PIA               		\
			-e OPENVPN_CONFIG=CA\ Denver           		\    
			-e OPENVPN_USERNAME=user               		\
			-e OPENVPN_PASSWORD=pass               		\
			-e WEBPROXY_ENABLED=false               	\	
			-e LOCAL_NETWORK=192.168.50.0/24         	\      
			--log-driver json-file               		\
			--log-opt max-size=10m               		\
			-p 9091:9091               					\
			haugene/transmission-openvpn:latest-armhf
{% endhighlight %}

### Setting up Torrent Client to Read an RSS Feed ###

Found something [here](https://github.com/nning/transmission-rss).

Okay, from that page I *want* to do the Docker setup, but I have a sneaking suspicion that will create a whole new Docker container that will
include Transmission as well.  I just want to download RSS feeds into the directory that my existing Transmission-VPN.

Maybe I can use one of the other set of steps.

Okay, I will need ruby within the transmission docker

so I do this:

{% highlight console %}
pi@raspberrypi:/etc $ docker exec -it angry_goldstine /bin/bash
root@d8d39033ecc1:/# ls
bin  boot  config  data  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@d8d39033ecc1:/# gem
bash: gem: command not found
root@d8d39033ecc1:/# apt-get
apt 1.8.2.1 (armhf)
Usage: apt-get [options] command
       apt-get [options] install|remove pkg1 [pkg2 ...]
       apt-get [options] source pkg1 [pkg2 ...]

apt-get is a command line interface for retrieval of packages
and information about them from authenticated sources and
for installation, upgrade and removal of packages together
with their dependencies.

Most used commands:
  update - Retrieve new lists of packages
  upgrade - Perform an upgrade
  install - Install new packages (pkg is libc6 not libc6.deb)
  reinstall - Reinstall packages (pkg is libc6 not libc6.deb)
  remove - Remove packages
  purge - Remove packages and config files
  autoremove - Remove automatically all unused packages
  dist-upgrade - Distribution upgrade, see apt-get(8)
  dselect-upgrade - Follow dselect selections
  build-dep - Configure build-dependencies for source packages
  clean - Erase downloaded archive files
  autoclean - Erase old downloaded archive files
  check - Verify that there are no broken dependencies
  source - Download source archives
  download - Download the binary package into the current directory
  changelog - Download and display the changelog for the given package

See apt-get(8) for more information about the available commands.
Configuration options and syntax is detailed in apt.conf(5).
Information about how to configure sources can be found in sources.list(5).
Package and version choices can be expressed via apt_preferences(5).
Security details are available in apt-secure(8).
                                        This APT has Super Cow Powers.
root@d8d39033ecc1:/# apt-get install ruby
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package ruby
root@d8d39033ecc1:/# apt-get update
Get:1 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Get:2 http://archive.raspbian.org/raspbian buster InRelease [15.0 kB]
Get:3 http://archive.raspbian.org/raspbian buster/main armhf Packages [18.3 MB]
Get:4 http://archive.raspberrypi.org/debian buster/main armhf Packages [331 kB]
Get:5 http://archive.raspbian.org/raspbian buster/rpi armhf Packages [1299 B]
Get:6 http://archive.raspbian.org/raspbian buster/non-free armhf Packages [126 kB]
Get:7 http://archive.raspbian.org/raspbian buster/firmware armhf Packages [1201 B]
Get:8 http://archive.raspbian.org/raspbian buster/contrib armhf Packages [68.6 kB]
Fetched 18.9 MB in 4min 40s (67.4 kB/s)
Reading package lists... Done
root@d8d39033ecc1:/# apt-get install ruby
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libruby2.5 libyaml-0-2 rake ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby-xmlrpc ruby2.5 rubygems-integration
Suggested packages:
  ri ruby-dev bundler
Recommended packages:
  zip fonts-lato libjs-jquery
The following NEW packages will be installed:
  libruby2.5 libyaml-0-2 rake ruby ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby-xmlrpc ruby2.5 rubygems-integration
0 upgraded, 12 newly installed, 0 to remove and 4 not upgraded.
Need to get 3858 kB of archives.
After this operation, 15.3 MB of additional disk space will be used.
Get:1 http://archive.raspbian.org/raspbian buster/main armhf rubygems-integration all 1.11+deb10u1 [5212 B]
Get:2 http://archive.raspbian.org/raspbian buster/main armhf ruby2.5 armhf 2.5.5-3+deb10u2 [400 kB]
Get:3 http://archive.raspbian.org/raspbian buster/main armhf ruby armhf 1:2.5.1+b1 [11.6 kB]
Get:4 http://archive.raspbian.org/raspbian buster/main armhf rake all 12.3.1-3+deb10u1 [67.1 kB]
Get:5 http://archive.raspbian.org/raspbian buster/main armhf ruby-did-you-mean all 1.2.1-1 [14.4 kB]
Get:6 http://archive.raspbian.org/raspbian buster/main armhf ruby-minitest all 5.11.3-1 [54.8 kB]
Get:7 http://archive.raspbian.org/raspbian buster/main armhf ruby-net-telnet all 0.1.1-2 [12.5 kB]
Get:8 http://archive.raspbian.org/raspbian buster/main armhf ruby-power-assert all 1.1.1-1 [10.9 kB]
Get:9 http://archive.raspbian.org/raspbian buster/main armhf ruby-test-unit all 3.2.8-1 [72.4 kB]
Get:10 http://archive.raspbian.org/raspbian buster/main armhf ruby-xmlrpc all 0.3.0-2 [23.7 kB]
Get:11 http://archive.raspbian.org/raspbian buster/main armhf libyaml-0-2 armhf 0.2.1-1 [38.8 kB]
Get:12 http://archive.raspbian.org/raspbian buster/main armhf libruby2.5 armhf 2.5.5-3+deb10u2 [3146 kB]
Fetched 3858 kB in 28s (138 kB/s)
Selecting previously unselected package rubygems-integration.
(Reading database ... 11950 files and directories currently installed.)
Preparing to unpack .../00-rubygems-integration_1.11+deb10u1_all.deb ...
Unpacking rubygems-integration (1.11+deb10u1) ...
Selecting previously unselected package ruby2.5.
Preparing to unpack .../01-ruby2.5_2.5.5-3+deb10u2_armhf.deb ...
Unpacking ruby2.5 (2.5.5-3+deb10u2) ...
Selecting previously unselected package ruby.
Preparing to unpack .../02-ruby_1%3a2.5.1+b1_armhf.deb ...
Unpacking ruby (1:2.5.1+b1) ...
Selecting previously unselected package rake.
Preparing to unpack .../03-rake_12.3.1-3+deb10u1_all.deb ...
Unpacking rake (12.3.1-3+deb10u1) ...
Selecting previously unselected package ruby-did-you-mean.
Preparing to unpack .../04-ruby-did-you-mean_1.2.1-1_all.deb ...
Unpacking ruby-did-you-mean (1.2.1-1) ...
Selecting previously unselected package ruby-minitest.
Preparing to unpack .../05-ruby-minitest_5.11.3-1_all.deb ...
Unpacking ruby-minitest (5.11.3-1) ...
Selecting previously unselected package ruby-net-telnet.
Preparing to unpack .../06-ruby-net-telnet_0.1.1-2_all.deb ...
Unpacking ruby-net-telnet (0.1.1-2) ...
Selecting previously unselected package ruby-power-assert.
Preparing to unpack .../07-ruby-power-assert_1.1.1-1_all.deb ...
Unpacking ruby-power-assert (1.1.1-1) ...
Selecting previously unselected package ruby-test-unit.
Preparing to unpack .../08-ruby-test-unit_3.2.8-1_all.deb ...
Unpacking ruby-test-unit (3.2.8-1) ...
Selecting previously unselected package ruby-xmlrpc.
Preparing to unpack .../09-ruby-xmlrpc_0.3.0-2_all.deb ...
Unpacking ruby-xmlrpc (0.3.0-2) ...
Selecting previously unselected package libyaml-0-2:armhf.
Preparing to unpack .../10-libyaml-0-2_0.2.1-1_armhf.deb ...
Unpacking libyaml-0-2:armhf (0.2.1-1) ...
Selecting previously unselected package libruby2.5:armhf.
Preparing to unpack .../11-libruby2.5_2.5.5-3+deb10u2_armhf.deb ...
Unpacking libruby2.5:armhf (2.5.5-3+deb10u2) ...
Setting up ruby-power-assert (1.1.1-1) ...
Setting up libyaml-0-2:armhf (0.2.1-1) ...
Setting up rubygems-integration (1.11+deb10u1) ...
Setting up ruby-minitest (5.11.3-1) ...
Setting up ruby-test-unit (3.2.8-1) ...
Setting up ruby-net-telnet (0.1.1-2) ...
Setting up ruby-did-you-mean (1.2.1-1) ...
Setting up ruby-xmlrpc (0.3.0-2) ...
Setting up ruby2.5 (2.5.5-3+deb10u2) ...
Setting up ruby (1:2.5.1+b1) ...
Setting up rake (12.3.1-3+deb10u1) ...
Setting up libruby2.5:armhf (2.5.5-3+deb10u2) ...
Processing triggers for libc-bin (2.28-10+rpi1) ...
root@d8d39033ecc1:/#
root@d8d39033ecc1:/# gem install transmission-rss
Fetching: open_uri_redirections-0.2.1.gem (100%)
Successfully installed open_uri_redirections-0.2.1
Fetching: ffi-1.13.1.gem (100%)
Building native extensions. This could take a while...
ERROR:  Error installing transmission-rss:
        ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/2.5.0/gems/ffi-1.13.1/ext/ffi_c
/usr/bin/ruby2.5 -r ./siteconf20201012-350-1cfd7g5.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.5.0/gems/ffi-1.13.1 for inspection.
Results logged to /var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.13.1/gem_make.out

{% endhighlight %}

Okay, that's fun.

Regardless, I have some work to do with my /etc/ folder.

I need to create a configuration file with the proper RSS feed URLs in it.

It will look like this:

{% highlight text %}
feeds:
  - url: http://example.com/feed1
    download_path: /home/user/Downloads
{% endhighlight %}


and this file will be called....

/etc/transmission-rss.conf

Okie. Let's do it.
And thank God this Docker has nano.

One of the questions is... where are the paths that map to my drive supposed to be?

So, I check this file: /data/transmission-home/transmission-log

And I see this:

{% highlight console %}
[2020-10-12 03:32:38.135] watchdir Failed to open directory "/data/watch" (2): No such file or directory (watchdir.c:354)

{% endhighlight %}

This tells me that, perhaps, my directoreis are not properly configured for mapping.
Indeed, poking around the Docker, I do not see a damn thing in the folders that should contain my TV shows do not... contain any shows.

So, I've done something wrong.....

Okay, I've updated my command line for running docker to this:

{% highlight console %}
docker run --restart always --cap-add=NET_ADMIN -d -v /mnt/torrents/:/data -v /mnt/torrents/torrentFiles:/data/watch -v /etc/localtime:/etc/localtime:ro -e CREATE_TUN_DEVICE=true -e OPENVPN_PROVIDER=PIA -e OPENVPN_CONFIG=CA\ Denver -e OPENVPN_USERNAME=uname -e OPENVPN_PASSWORD=pass -e WEBPROXY_ENABLED=false -e LOCAL_NETWORK=192.168.50.0/24 --log-driver json-file --log-opt max-size=10m -p 9091:9091 haugene/transmission-openvpn:latest-armhf
{% endhighlight %}
And.. it seems to work. I see the file where they're supposed to be. And I see where the watch files are supposed to be.

So, what about that error we found?

Okay, I found [this](https://stackoverflow.com/questions/20559255/error-while-installing-json-gem-mkmf-rb-cant-find-header-files-for-ruby).

It wants me to do this sort of thing:

{% highlight console %}
sudo apt-get install ruby2.0-dev
sudo apt-get install ruby2.2-dev
sudo apt-get install ruby2.3-dev
{% endhighlight %}

But sadly, it doesn't recognize any of those packages.

So I'm stuck.
Wait, I had to do another apt-get update
Then, it recognized ruby-dev

And it installed. What next?

We try the gem install transmission-rss again - and watch it fail again like this:

{% highlight console %}
root@72d64126b585:/data/watch# apt-get install ruby-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package ruby-dev
root@72d64126b585:/data/watch# apt-get install ruby-dev2.0
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package ruby-dev2.0
E: Couldn't find any package by glob 'ruby-dev2.0'
E: Couldn't find any package by regex 'ruby-dev2.0'
root@72d64126b585:/data/watch# apt-get install ruby2.0-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package ruby2.0-dev
E: Couldn't find any package by glob 'ruby2.0-dev'
E: Couldn't find any package by regex 'ruby2.0-dev'
root@72d64126b585:/data/watch# apt-get update
Get:1 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Get:2 http://archive.raspbian.org/raspbian buster InRelease [15.0 kB]
Get:3 http://archive.raspberrypi.org/debian buster/main armhf Packages [331 kB]
Get:4 http://archive.raspbian.org/raspbian buster/rpi armhf Packages [1299 B]
Get:5 http://archive.raspbian.org/raspbian buster/contrib armhf Packages [68.6 kB]
Get:6 http://archive.raspbian.org/raspbian buster/non-free armhf Packages [126 kB]
Get:7 http://archive.raspbian.org/raspbian buster/firmware armhf Packages [1201 B]
Get:8 http://archive.raspbian.org/raspbian buster/main armhf Packages [18.3 MB]
Fetched 18.9 MB in 3min 35s (87.7 kB/s)
Reading package lists... Done
root@72d64126b585:/data/watch# apt-get install rubydev
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package rubydev
root@72d64126b585:/data/watch# apt-get install ruby-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libgmp-dev libgmpxx4ldbl libruby2.5 libyaml-0-2 rake ruby ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby-xmlrpc ruby2.5 ruby2.5-dev
  rubygems-integration
Suggested packages:
  gmp-doc libgmp10-doc libmpfr-dev ri bundler
Recommended packages:
  zip fonts-lato libjs-jquery ruby2.5-doc
The following NEW packages will be installed:
  libgmp-dev libgmpxx4ldbl libruby2.5 libyaml-0-2 rake ruby ruby-dev ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby-xmlrpc ruby2.5 ruby2.5-dev
  rubygems-integration
0 upgraded, 16 newly installed, 0 to remove and 4 not upgraded.
Need to get 4875 kB of archives.
After this operation, 17.5 MB of additional disk space will be used.
Get:1 http://archive.raspbian.org/raspbian buster/main armhf libgmpxx4ldbl armhf 2:6.1.2+dfsg-4 [21.8 kB]
Get:2 http://archive.raspbian.org/raspbian buster/main armhf libgmp-dev armhf 2:6.1.2+dfsg-4 [570 kB]
Get:3 http://archive.raspbian.org/raspbian buster/main armhf rubygems-integration all 1.11+deb10u1 [5212 B]
Get:4 http://archive.raspbian.org/raspbian buster/main armhf ruby2.5 armhf 2.5.5-3+deb10u2 [400 kB]
Get:5 http://archive.raspbian.org/raspbian buster/main armhf ruby armhf 1:2.5.1+b1 [11.6 kB]
Get:6 http://archive.raspbian.org/raspbian buster/main armhf rake all 12.3.1-3+deb10u1 [67.1 kB]
Get:7 http://archive.raspbian.org/raspbian buster/main armhf ruby-did-you-mean all 1.2.1-1 [14.4 kB]
Get:8 http://archive.raspbian.org/raspbian buster/main armhf ruby-minitest all 5.11.3-1 [54.8 kB]
Get:9 http://archive.raspbian.org/raspbian buster/main armhf ruby-net-telnet all 0.1.1-2 [12.5 kB]
Get:10 http://archive.raspbian.org/raspbian buster/main armhf ruby-power-assert all 1.1.1-1 [10.9 kB]
Get:11 http://archive.raspbian.org/raspbian buster/main armhf ruby-test-unit all 3.2.8-1 [72.4 kB]
Get:12 http://archive.raspbian.org/raspbian buster/main armhf ruby-xmlrpc all 0.3.0-2 [23.7 kB]
Get:13 http://archive.raspbian.org/raspbian buster/main armhf libyaml-0-2 armhf 0.2.1-1 [38.8 kB]
Get:14 http://archive.raspbian.org/raspbian buster/main armhf libruby2.5 armhf 2.5.5-3+deb10u2 [3146 kB]
Get:15 http://archive.raspbian.org/raspbian buster/main armhf ruby2.5-dev armhf 2.5.5-3+deb10u2 [415 kB]
Get:16 http://archive.raspbian.org/raspbian buster/main armhf ruby-dev armhf 1:2.5.1+b1 [10.4 kB]
Fetched 4875 kB in 1min 25s (57.4 kB/s)
Selecting previously unselected package libgmpxx4ldbl:armhf.
(Reading database ... 11950 files and directories currently installed.)
Preparing to unpack .../00-libgmpxx4ldbl_2%3a6.1.2+dfsg-4_armhf.deb ...
Unpacking libgmpxx4ldbl:armhf (2:6.1.2+dfsg-4) ...
Selecting previously unselected package libgmp-dev:armhf.
Preparing to unpack .../01-libgmp-dev_2%3a6.1.2+dfsg-4_armhf.deb ...
Unpacking libgmp-dev:armhf (2:6.1.2+dfsg-4) ...
Selecting previously unselected package rubygems-integration.
Preparing to unpack .../02-rubygems-integration_1.11+deb10u1_all.deb ...
Unpacking rubygems-integration (1.11+deb10u1) ...
Selecting previously unselected package ruby2.5.
Preparing to unpack .../03-ruby2.5_2.5.5-3+deb10u2_armhf.deb ...
Unpacking ruby2.5 (2.5.5-3+deb10u2) ...
Selecting previously unselected package ruby.
Preparing to unpack .../04-ruby_1%3a2.5.1+b1_armhf.deb ...
Unpacking ruby (1:2.5.1+b1) ...
Selecting previously unselected package rake.
Preparing to unpack .../05-rake_12.3.1-3+deb10u1_all.deb ...
Unpacking rake (12.3.1-3+deb10u1) ...
Selecting previously unselected package ruby-did-you-mean.
Preparing to unpack .../06-ruby-did-you-mean_1.2.1-1_all.deb ...
Unpacking ruby-did-you-mean (1.2.1-1) ...
Selecting previously unselected package ruby-minitest.
Preparing to unpack .../07-ruby-minitest_5.11.3-1_all.deb ...
Unpacking ruby-minitest (5.11.3-1) ...
Selecting previously unselected package ruby-net-telnet.
Preparing to unpack .../08-ruby-net-telnet_0.1.1-2_all.deb ...
Unpacking ruby-net-telnet (0.1.1-2) ...
Selecting previously unselected package ruby-power-assert.
Preparing to unpack .../09-ruby-power-assert_1.1.1-1_all.deb ...
Unpacking ruby-power-assert (1.1.1-1) ...
Selecting previously unselected package ruby-test-unit.
Preparing to unpack .../10-ruby-test-unit_3.2.8-1_all.deb ...
Unpacking ruby-test-unit (3.2.8-1) ...
Selecting previously unselected package ruby-xmlrpc.
Preparing to unpack .../11-ruby-xmlrpc_0.3.0-2_all.deb ...
Unpacking ruby-xmlrpc (0.3.0-2) ...
Selecting previously unselected package libyaml-0-2:armhf.
Preparing to unpack .../12-libyaml-0-2_0.2.1-1_armhf.deb ...
Unpacking libyaml-0-2:armhf (0.2.1-1) ...
Selecting previously unselected package libruby2.5:armhf.
Preparing to unpack .../13-libruby2.5_2.5.5-3+deb10u2_armhf.deb ...
Unpacking libruby2.5:armhf (2.5.5-3+deb10u2) ...
Selecting previously unselected package ruby2.5-dev:armhf.
Preparing to unpack .../14-ruby2.5-dev_2.5.5-3+deb10u2_armhf.deb ...
Unpacking ruby2.5-dev:armhf (2.5.5-3+deb10u2) ...
Selecting previously unselected package ruby-dev:armhf.
Preparing to unpack .../15-ruby-dev_1%3a2.5.1+b1_armhf.deb ...
Unpacking ruby-dev:armhf (1:2.5.1+b1) ...
Setting up ruby-power-assert (1.1.1-1) ...
Setting up libyaml-0-2:armhf (0.2.1-1) ...
Setting up rubygems-integration (1.11+deb10u1) ...
Setting up ruby-minitest (5.11.3-1) ...
Setting up libgmpxx4ldbl:armhf (2:6.1.2+dfsg-4) ...
Setting up ruby-test-unit (3.2.8-1) ...
Setting up ruby-net-telnet (0.1.1-2) ...
Setting up ruby-did-you-mean (1.2.1-1) ...
Setting up ruby-xmlrpc (0.3.0-2) ...
Setting up libgmp-dev:armhf (2:6.1.2+dfsg-4) ...
Setting up ruby2.5 (2.5.5-3+deb10u2) ...
Setting up ruby (1:2.5.1+b1) ...
Setting up rake (12.3.1-3+deb10u1) ...
Setting up libruby2.5:armhf (2.5.5-3+deb10u2) ...
Setting up ruby2.5-dev:armhf (2.5.5-3+deb10u2) ...
Setting up ruby-dev:armhf (1:2.5.1+b1) ...
Processing triggers for libc-bin (2.28-10+rpi1) ...
root@72d64126b585:/data/watch# apt-get install ruby
Reading package lists... Done
Building dependency tree
Reading state information... Done
ruby is already the newest version (1:2.5.1+b1).
ruby set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.
root@72d64126b585:/data/watch# gem install transmission-rss
Fetching: open_uri_redirections-0.2.1.gem (100%)
Successfully installed open_uri_redirections-0.2.1
Fetching: ffi-1.13.1.gem (100%)
Building native extensions. This could take a while...
ERROR:  Error installing transmission-rss:
        ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/2.5.0/gems/ffi-1.13.1/ext/ffi_c
/usr/bin/ruby2.5 -r ./siteconf20201012-459-7qd6op.rb extconf.rb
checking for ffi.h... *** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
        --with-opt-dir
        --without-opt-dir
        --with-opt-include
        --without-opt-include=${opt-dir}/include
        --with-opt-lib
        --without-opt-lib=${opt-dir}/lib
        --with-make-prog
        --without-make-prog
        --srcdir=.
        --curdir
        --ruby=/usr/bin/$(RUBY_BASE_NAME)2.5
        --with-ffi_c-dir
        --without-ffi_c-dir
        --with-ffi_c-include
        --without-ffi_c-include=${ffi_c-dir}/include
        --with-ffi_c-lib
        --without-ffi_c-lib=${ffi_c-dir}/lib
        --enable-system-libffi
        --disable-system-libffi
        --with-libffi-config
        --without-libffi-config
        --with-pkg-config
        --without-pkg-config
/usr/lib/ruby/2.5.0/mkmf.rb:456:in `try_do': The compiler failed to generate an executable file. (RuntimeError)
You have to install development tools first.
        from /usr/lib/ruby/2.5.0/mkmf.rb:590:in `try_cpp'
        from /usr/lib/ruby/2.5.0/mkmf.rb:1098:in `block in have_header'
        from /usr/lib/ruby/2.5.0/mkmf.rb:948:in `block in checking_for'
        from /usr/lib/ruby/2.5.0/mkmf.rb:350:in `block (2 levels) in postpone'
        from /usr/lib/ruby/2.5.0/mkmf.rb:320:in `open'
        from /usr/lib/ruby/2.5.0/mkmf.rb:350:in `block in postpone'
        from /usr/lib/ruby/2.5.0/mkmf.rb:320:in `open'
        from /usr/lib/ruby/2.5.0/mkmf.rb:346:in `postpone'
        from /usr/lib/ruby/2.5.0/mkmf.rb:947:in `checking_for'
        from /usr/lib/ruby/2.5.0/mkmf.rb:1097:in `have_header'
        from extconf.rb:10:in `system_libffi_usable?'
        from extconf.rb:42:in `<main>'

To see why this extension failed to compile, please check the mkmf.log which can be found here:

  /var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.13.1/mkmf.log

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.5.0/gems/ffi-1.13.1 for inspection.
Results logged to /var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.13.1/gem_make.out

{% endhighlight %}

Oof. Da. 

I have been working for 2.5 hours now. How usually effective is my time In 2.5 hours I can break apart a logjam that has afflicated a 100 million dollar project. Or I can fail to correct something that costs $0.

Well, those $100 million folks are just plain wrong about the valuation of their project.

Mine is much more important.

And more expensive.

Am I going to have fun at any point here?

Anyway, the log file they want me to look at (mkmf.log) looks like this:

{% highlight console %}
package configuration for libffi is not found
"gcc -o conftest -I/usr/include/arm-linux-gnueabihf/ruby-2.5.0 -I/usr/include/ruby-2.5.0/ruby/backward -I/usr/include/ruby-2.5.0 -I. -Wdate-time -D_FORTIFY_SOURCE=2 -D_FILE_OFFSET_BITS=64  -g -O2 -fdebug-prefix-map=/build/ruby2.5-cMKrLr/ruby2.5-2.5.5=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC conftest.c  -L. -L/usr/lib/arm-linux-gnueabihf -L. -Wl,-z,relro -Wl,-z,now -fstack-protector -rdynamic -Wl,-export-dynamic     -lruby-2.5  -lpthread -lgmp -ldl -lcrypt -lm   -lc"
checked program was:
/* begin */
1: #include "ruby.h"
2:
3: int main(int argc, char **argv)
4: {
5:   return 0;
6: }
/* end */

{% endhighlight %}

At least one link says to install gcc
So I do
apt-get install gcc

It's always something, now this:

{% highlight console %}
ERROR: Failed to build gem native extension.
{% endhighlight %}

so what now?

Supposedly, I should install ruby-dev, then maybe make.

So I do this:

{% highlight console %}
root@72d64126b585:/var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.13.1# apt-get install make
Reading package lists... Done
Building dependency tree
Reading state information... Done
Suggested packages:
  make-doc
The following NEW packages will be installed:
  make
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 321 kB of archives.
After this operation, 1279 kB of additional disk space will be used.
Get:1 http://archive.raspbian.org/raspbian buster/main armhf make armhf 4.2.1-1.2 [321 kB]
Fetched 321 kB in 2s (156 kB/s)
sh: 0: getcwd() failed: No such file or directory
Selecting previously unselected package make.
(Reading database ... 13749 files and directories currently installed.)
Preparing to unpack .../make_4.2.1-1.2_armhf.deb ...
Unpacking make (4.2.1-1.2) ...
Setting up make (4.2.1-1.2) ...
root@72d64126b585:/var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.13.1# gem install transmission-rss
ERROR:  While executing gem ... (Errno::ENOENT)
    No such file or directory - getcwd
root@72d64126b585:/var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.13.1#

{% endhighlight %}

And... I got nothing here.

I'm just rebooting.

Nope. Same thing. It just won't install.

okay, i'm installing build-essential

then i'm trying to install the gem again.

it DOESN'T IMMEDIATELY FAIL.
And it doesn't fail at all.

Do I just need that configuration file now?

It will look like this:

{% highlight text %}
feeds:
  - url: http://showrss.info/user/127411.rss?magnets=true&namespaces=true&name=null&quality=null&re=null
    download_path: /data/torrents
{% endhighlight %}


and this file will be called....

/etc/transmission-rss.conf


But... I have no clue whether this is working or not.

Time to put this HD babck on the other laptop.

I have utterly failed to get this working again.





## Setting up a Subversion Server on a RasPi ##

TBD

## Setting up a Jekyll Server on a RasPi ##

TBD

## Setting up a Jenkins Server on a RasPi ##

TBD

## Setting up a Redmine Server on a RasPi ##

TBD

## Setting up a NAS on a RasPi ##

I've got an old hard drive that I'd like access to from my network. At this point, I sadly think Samba sharing may be the best option for file sharing with
Windows 10.  I wonder if I'm right?

[This](https://www.fosslinux.com/19265/how-to-share-and-transfer-files-between-linux-and-windows.htm) site offers some alternatives.

1. SSH Sharing - This looks to be pretty command-line oriented. Not really what I'm looking for.
2. Samba - This is what I'm assuming I'll have to use
3. Shared Folders - This... looks like Samba again to me...

So, it's Samba for me.

I'm using [this](https://magpi.raspberrypi.org/articles/samba-file-server) site
for instructions on installing Samba.

### Installing Samba ###

Here's what I do:

{% highlight console %}
pi@raspberrypi:~ $ sudo apt-get update
Get:1 https://download.docker.com/linux/raspbian buster InRelease [29.7 kB]
Get:2 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Get:3 http://raspbian.raspberrypi.org/raspbian buster InRelease [15.0 kB]
Get:4 https://download.docker.com/linux/raspbian buster/stable armhf Packages [7,361 B]
Get:5 http://raspbian.raspberrypi.org/raspbian buster/main armhf Packages [13.0 MB]
Get:6 http://archive.raspberrypi.org/debian buster/main armhf Packages [331 kB]
Fetched 13.4 MB in 13s (1,071 kB/s)
Reading package lists... Done
pi@raspberrypi:~ $ sudo apt-get install samba samba-common-bin
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  attr ibverbs-providers libavahi-client3 libboost-atomic1.67.0 libboost-iostreams1.67.0
  libboost-regex1.67.0 libboost-system1.67.0 libboost-thread1.67.0 libcephfs2 libcups2 libgfapi0
  libgfrpc0 libgfxdr0 libglusterfs0 libgpgme11 libibverbs1 libjansson4 libldb1 libnspr4 libnss3
  libpython2.7 librados2 libtdb1 libtevent0 python-crypto python-dnspython python-gpg python-ldb
  python-samba python-talloc python-tdb samba-common samba-dsdb-modules samba-libs samba-vfs-modules
  tdb-tools
Suggested packages:
  cups-common python-crypto-doc bind9 bind9utils ctdb ldb-tools smbldap-tools ufw winbind heimdal-clients
The following NEW packages will be installed:
  attr ibverbs-providers libavahi-client3 libboost-atomic1.67.0 libboost-iostreams1.67.0
  libboost-regex1.67.0 libboost-system1.67.0 libboost-thread1.67.0 libcephfs2 libcups2 libgfapi0
  libgfrpc0 libgfxdr0 libglusterfs0 libgpgme11 libibverbs1 libjansson4 libldb1 libnspr4 libnss3
  libpython2.7 librados2 libtdb1 libtevent0 python-crypto python-dnspython python-gpg python-ldb
  python-samba python-talloc python-tdb samba samba-common samba-common-bin samba-dsdb-modules samba-libs
  samba-vfs-modules tdb-tools
0 upgraded, 38 newly installed, 0 to remove and 17 not upgraded.
Need to get 26.8 MB of archives.
After this operation, 101 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-dnspython all 1.16.0-1 [90.1 kB]
Get:2 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-crypto armhf 2.6.1-9+b1 [248 kB]
Get:3 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libtdb1 armhf 1.3.16-2+b1 [39.0 kB]
Get:4 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libtevent0 armhf 0.9.37-1 [27.6 kB]
Get:5 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libldb1 armhf 2:1.5.1+really1.4.6-3 [109 kB]
Get:6 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libpython2.7 armhf 2.7.16-2+deb10u1 [873 kB]
Get:7 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-ldb armhf 2:1.5.1+really1.4.6-3 [33.1 kB]
Get:8 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-tdb armhf 1.3.16-2+b1 [16.0 kB]
Get:9 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libavahi-client3 armhf 0.7-4+b1 [54.0 kB]
Get:10 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libcups2 armhf 2.2.10-6+deb10u3 [287 kB]
Get:11 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libjansson4 armhf 2.12-1 [34.6 kB]
Get:12 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-talloc armhf 2.1.14-2 [12.3 kB]
Get:13 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf samba-libs armhf 2:4.9.5+dfsg-5+deb10u1+rpi1 [4,700 kB]
Get:14 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-samba armhf 2:4.9.5+dfsg-5+deb10u1+rpi1 [1,794 kB]
Get:15 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf samba-common all 2:4.9.5+dfsg-5+deb10u1+rpi1 [170 kB]
Get:16 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf samba-common-bin armhf 2:4.9.5+dfsg-5+deb10u1+rpi1 [570 kB]
Get:17 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf tdb-tools armhf 1.3.16-2+b1 [26.9 kB]
Get:18 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf samba armhf 2:4.9.5+dfsg-5+deb10u1+rpi1 [1,010 kB]
Get:19 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf attr armhf 1:2.4.48-4 [39.4 kB]
Get:20 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libibverbs1 armhf 22.1-1 [43.5 kB]
Get:21 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf ibverbs-providers armhf 22.1-1 [20.2 kB]
Get:22 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libboost-atomic1.67.0 armhf 1.67.0-13+deb10u1 [226 kB]
Get:23 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libboost-iostreams1.67.0 armhf 1.67.0-13+deb10u1 [245 kB]
Get:24 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libboost-regex1.67.0 armhf 1.67.0-13+deb10u1 [430 kB]
Get:25 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libboost-system1.67.0 armhf 1.67.0-13+deb10u1 [229 kB]
Get:26 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libboost-thread1.67.0 armhf 1.67.0-13+deb10u1 [260 kB]
Get:27 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libnspr4 armhf 2:4.20-1 [89.6 kB]
Get:28 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libnss3 armhf 2:3.42.1-1+deb10u3 [944 kB]
Get:29 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf librados2 armhf 12.2.11+dfsg1-2.1+rpi1 [2,337 kB]
Get:30 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libcephfs2 armhf 12.2.11+dfsg1-2.1+rpi1 [380 kB]
Get:31 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libglusterfs0 armhf 5.5-3 [2,724 kB]
Get:32 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libgfxdr0 armhf 5.5-3 [2,488 kB]
Get:33 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libgfrpc0 armhf 5.5-3 [2,506 kB]
Get:34 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libgfapi0 armhf 5.5-3 [2,524 kB]
Get:35 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libgpgme11 armhf 1.12.0-6 [230 kB]
Get:36 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf python-gpg armhf 1.12.0-6 [275 kB]
Get:37 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf samba-dsdb-modules armhf 2:4.9.5+dfsg-5+deb10u1+rpi1 [345 kB]
Get:38 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf samba-vfs-modules armhf 2:4.9.5+dfsg-5+deb10u1+rpi1 [400 kB]
Fetched 26.8 MB in 36s (739 kB/s)
Extracting templates from packages: 100%
Preconfiguring packages ...
Selecting previously unselected package python-dnspython.
(Reading database ... 41657 files and directories currently installed.)
Preparing to unpack .../00-python-dnspython_1.16.0-1_all.deb ...
Unpacking python-dnspython (1.16.0-1) ...
Selecting previously unselected package python-crypto.
Preparing to unpack .../01-python-crypto_2.6.1-9+b1_armhf.deb ...
Unpacking python-crypto (2.6.1-9+b1) ...
Selecting previously unselected package libtdb1:armhf.
Preparing to unpack .../02-libtdb1_1.3.16-2+b1_armhf.deb ...
Unpacking libtdb1:armhf (1.3.16-2+b1) ...
Selecting previously unselected package libtevent0:armhf.
Preparing to unpack .../03-libtevent0_0.9.37-1_armhf.deb ...
Unpacking libtevent0:armhf (0.9.37-1) ...
Selecting previously unselected package libldb1:armhf.
Preparing to unpack .../04-libldb1_2%3a1.5.1+really1.4.6-3_armhf.deb ...
Unpacking libldb1:armhf (2:1.5.1+really1.4.6-3) ...
Selecting previously unselected package libpython2.7:armhf.
Preparing to unpack .../05-libpython2.7_2.7.16-2+deb10u1_armhf.deb ...
Unpacking libpython2.7:armhf (2.7.16-2+deb10u1) ...
Selecting previously unselected package python-ldb.
Preparing to unpack .../06-python-ldb_2%3a1.5.1+really1.4.6-3_armhf.deb ...
Unpacking python-ldb (2:1.5.1+really1.4.6-3) ...
Selecting previously unselected package python-tdb.
Preparing to unpack .../07-python-tdb_1.3.16-2+b1_armhf.deb ...
Unpacking python-tdb (1.3.16-2+b1) ...
Selecting previously unselected package libavahi-client3:armhf.
Preparing to unpack .../08-libavahi-client3_0.7-4+b1_armhf.deb ...
Unpacking libavahi-client3:armhf (0.7-4+b1) ...
Selecting previously unselected package libcups2:armhf.
Preparing to unpack .../09-libcups2_2.2.10-6+deb10u3_armhf.deb ...
Unpacking libcups2:armhf (2.2.10-6+deb10u3) ...
Selecting previously unselected package libjansson4:armhf.
Preparing to unpack .../10-libjansson4_2.12-1_armhf.deb ...
Unpacking libjansson4:armhf (2.12-1) ...
Selecting previously unselected package python-talloc:armhf.
Preparing to unpack .../11-python-talloc_2.1.14-2_armhf.deb ...
Unpacking python-talloc:armhf (2.1.14-2) ...
Selecting previously unselected package samba-libs:armhf.
Preparing to unpack .../12-samba-libs_2%3a4.9.5+dfsg-5+deb10u1+rpi1_armhf.deb ...
Unpacking samba-libs:armhf (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Selecting previously unselected package python-samba.
Preparing to unpack .../13-python-samba_2%3a4.9.5+dfsg-5+deb10u1+rpi1_armhf.deb ...
Unpacking python-samba (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Selecting previously unselected package samba-common.
Preparing to unpack .../14-samba-common_2%3a4.9.5+dfsg-5+deb10u1+rpi1_all.deb ...
Unpacking samba-common (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Selecting previously unselected package samba-common-bin.
Preparing to unpack .../15-samba-common-bin_2%3a4.9.5+dfsg-5+deb10u1+rpi1_armhf.deb ...
Unpacking samba-common-bin (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Selecting previously unselected package tdb-tools.
Preparing to unpack .../16-tdb-tools_1.3.16-2+b1_armhf.deb ...
Unpacking tdb-tools (1.3.16-2+b1) ...
Selecting previously unselected package samba.
Preparing to unpack .../17-samba_2%3a4.9.5+dfsg-5+deb10u1+rpi1_armhf.deb ...
Unpacking samba (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Selecting previously unselected package attr.
Preparing to unpack .../18-attr_1%3a2.4.48-4_armhf.deb ...
Unpacking attr (1:2.4.48-4) ...
Selecting previously unselected package libibverbs1:armhf.
Preparing to unpack .../19-libibverbs1_22.1-1_armhf.deb ...
Unpacking libibverbs1:armhf (22.1-1) ...
Selecting previously unselected package ibverbs-providers:armhf.
Preparing to unpack .../20-ibverbs-providers_22.1-1_armhf.deb ...
Unpacking ibverbs-providers:armhf (22.1-1) ...
Selecting previously unselected package libboost-atomic1.67.0:armhf.
Preparing to unpack .../21-libboost-atomic1.67.0_1.67.0-13+deb10u1_armhf.deb ...
Unpacking libboost-atomic1.67.0:armhf (1.67.0-13+deb10u1) ...
Selecting previously unselected package libboost-iostreams1.67.0:armhf.
Preparing to unpack .../22-libboost-iostreams1.67.0_1.67.0-13+deb10u1_armhf.deb ...
Unpacking libboost-iostreams1.67.0:armhf (1.67.0-13+deb10u1) ...
Selecting previously unselected package libboost-regex1.67.0:armhf.
Preparing to unpack .../23-libboost-regex1.67.0_1.67.0-13+deb10u1_armhf.deb ...
Unpacking libboost-regex1.67.0:armhf (1.67.0-13+deb10u1) ...
Selecting previously unselected package libboost-system1.67.0:armhf.
Preparing to unpack .../24-libboost-system1.67.0_1.67.0-13+deb10u1_armhf.deb ...
Unpacking libboost-system1.67.0:armhf (1.67.0-13+deb10u1) ...
Selecting previously unselected package libboost-thread1.67.0:armhf.
Preparing to unpack .../25-libboost-thread1.67.0_1.67.0-13+deb10u1_armhf.deb ...
Unpacking libboost-thread1.67.0:armhf (1.67.0-13+deb10u1) ...
Selecting previously unselected package libnspr4:armhf.
Preparing to unpack .../26-libnspr4_2%3a4.20-1_armhf.deb ...
Unpacking libnspr4:armhf (2:4.20-1) ...
Selecting previously unselected package libnss3:armhf.
Preparing to unpack .../27-libnss3_2%3a3.42.1-1+deb10u3_armhf.deb ...
Unpacking libnss3:armhf (2:3.42.1-1+deb10u3) ...
Selecting previously unselected package librados2:armhf.
Preparing to unpack .../28-librados2_12.2.11+dfsg1-2.1+rpi1_armhf.deb ...
Unpacking librados2:armhf (12.2.11+dfsg1-2.1+rpi1) ...
Selecting previously unselected package libcephfs2:armhf.
Preparing to unpack .../29-libcephfs2_12.2.11+dfsg1-2.1+rpi1_armhf.deb ...
Unpacking libcephfs2:armhf (12.2.11+dfsg1-2.1+rpi1) ...
Selecting previously unselected package libglusterfs0:armhf.
Preparing to unpack .../30-libglusterfs0_5.5-3_armhf.deb ...
Unpacking libglusterfs0:armhf (5.5-3) ...
Selecting previously unselected package libgfxdr0:armhf.
Preparing to unpack .../31-libgfxdr0_5.5-3_armhf.deb ...
Unpacking libgfxdr0:armhf (5.5-3) ...
Selecting previously unselected package libgfrpc0:armhf.
Preparing to unpack .../32-libgfrpc0_5.5-3_armhf.deb ...
Unpacking libgfrpc0:armhf (5.5-3) ...
Selecting previously unselected package libgfapi0:armhf.
Preparing to unpack .../33-libgfapi0_5.5-3_armhf.deb ...
Unpacking libgfapi0:armhf (5.5-3) ...
Selecting previously unselected package libgpgme11:armhf.
Preparing to unpack .../34-libgpgme11_1.12.0-6_armhf.deb ...
Unpacking libgpgme11:armhf (1.12.0-6) ...
Selecting previously unselected package python-gpg.
Preparing to unpack .../35-python-gpg_1.12.0-6_armhf.deb ...
Unpacking python-gpg (1.12.0-6) ...
Selecting previously unselected package samba-dsdb-modules:armhf.
Preparing to unpack .../36-samba-dsdb-modules_2%3a4.9.5+dfsg-5+deb10u1+rpi1_armhf.deb ...
Unpacking samba-dsdb-modules:armhf (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Selecting previously unselected package samba-vfs-modules:armhf.
Preparing to unpack .../37-samba-vfs-modules_2%3a4.9.5+dfsg-5+deb10u1+rpi1_armhf.deb ...
Unpacking samba-vfs-modules:armhf (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Setting up python-crypto (2.6.1-9+b1) ...
Setting up libibverbs1:armhf (22.1-1) ...
Setting up libpython2.7:armhf (2.7.16-2+deb10u1) ...
Setting up libboost-regex1.67.0:armhf (1.67.0-13+deb10u1) ...
Setting up ibverbs-providers:armhf (22.1-1) ...
Setting up attr (1:2.4.48-4) ...
Setting up libtdb1:armhf (1.3.16-2+b1) ...
Setting up samba-common (2:4.9.5+dfsg-5+deb10u1+rpi1) ...

Creating config file /etc/samba/smb.conf with new version
Setting up libgpgme11:armhf (1.12.0-6) ...
Setting up libjansson4:armhf (2.12-1) ...
Setting up libglusterfs0:armhf (5.5-3) ...
Setting up libtevent0:armhf (0.9.37-1) ...
Setting up libnspr4:armhf (2:4.20-1) ...
Setting up tdb-tools (1.3.16-2+b1) ...
update-alternatives: using /usr/bin/tdbbackup.tdbtools to provide /usr/bin/tdbbackup (tdbbackup) in auto mode
Setting up libboost-iostreams1.67.0:armhf (1.67.0-13+deb10u1) ...
Setting up python-tdb (1.3.16-2+b1) ...
Setting up libboost-atomic1.67.0:armhf (1.67.0-13+deb10u1) ...
Setting up python-dnspython (1.16.0-1) ...
Setting up libboost-system1.67.0:armhf (1.67.0-13+deb10u1) ...
Setting up python-gpg (1.12.0-6) ...
Setting up python-talloc:armhf (2.1.14-2) ...
Setting up libavahi-client3:armhf (0.7-4+b1) ...
Setting up libgfxdr0:armhf (5.5-3) ...
Setting up libldb1:armhf (2:1.5.1+really1.4.6-3) ...
Setting up libboost-thread1.67.0:armhf (1.67.0-13+deb10u1) ...
Setting up libnss3:armhf (2:3.42.1-1+deb10u3) ...
Setting up python-ldb (2:1.5.1+really1.4.6-3) ...
Setting up libcups2:armhf (2.2.10-6+deb10u3) ...
Setting up libgfrpc0:armhf (5.5-3) ...
Setting up librados2:armhf (12.2.11+dfsg1-2.1+rpi1) ...
Setting up samba-libs:armhf (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Setting up libcephfs2:armhf (12.2.11+dfsg1-2.1+rpi1) ...
Setting up libgfapi0:armhf (5.5-3) ...
Setting up samba-dsdb-modules:armhf (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Setting up python-samba (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Setting up samba-vfs-modules:armhf (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Setting up samba-common-bin (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Checking smb.conf with testparm
Load smb config files from /etc/samba/smb.conf
Loaded services file OK.
Server role: ROLE_STANDALONE

Done
Setting up samba (2:4.9.5+dfsg-5+deb10u1+rpi1) ...
Adding group `sambashare' (GID 116) ...
Done.
Samba is not being run as an AD Domain Controller: Masking samba-ad-dc.service
Please ignore the following error about deb-systemd-helper not finding those services.
(samba-ad-dc.service masked)
Created symlink /etc/systemd/system/multi-user.target.wants/nmbd.service → /lib/systemd/system/nmbd.service.
Failed to preset unit: Unit file /etc/systemd/system/samba-ad-dc.service is masked.
/usr/bin/deb-systemd-helper: error: systemctl preset failed on samba-ad-dc.service: No such file or directory
Created symlink /etc/systemd/system/multi-user.target.wants/smbd.service → /lib/systemd/system/smbd.service.
Processing triggers for systemd (241-7~deb10u4+rpi1) ...
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for libc-bin (2.28-10+rpi1) ...

{% endhighlight %}

It's worth noting that in the middle of this, a screen came up offering to change 
my configuration to allow my DHCP server to populate the WINS server address for
my network.

I'm fairly sure that I don't have one of those, but I allowed it.

The next step from that website is to create the directory that I will share things
from and to set its permissions to '1777'. That would allow everyone full access.

I don't think I want that, and anyway, my directory already exists, so I'm somewhat
unsure of just what to do in this situation. What I will do is ignore this part
of the instructions, try to share my hard drive and then see if I have permissions
issues regarding it later.

### Configuring Samba ###

There's a text file that holds the settings for Samba and will allow us to define 
a new share. Here's the command I used to edit the file:

{% highlight console %}

pi@raspberrypi:~ $ sudo nano /etc/samba/smb.conf

{% endhighlight %}
   
Then, I add the following lines at the end of the file:

{% highlight console %}
[share]
Comment = NAS Files
Path = /mnt/nas
Browseable = yes
Writeable = no
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest ok = yes

{% endhighlight %}

Next, apparently I have to create a user and start Samba.

### Creating a User and Starting Samba ###

I start off by doing the same thing that they do on the website:

{% highlight console %}
pi@raspberrypi:/mnt/nas $ sudo smbpasswd -a pi
New SMB password: xxxx 
Retype new SMB password: xxxx
Added user pi.
pi@raspberrypi:/mnt/nas $ sudo /etc/init.d/samba restart
sudo: /etc/init.d/samba: command not found

{% endhighlight %}

Hmm, that last bit is interesting. Do I need a reboot?

Let's try!

Hmm, no, that didn't help either.

Let's see if we can access the share....

Yes, in fact I can. I log in with my pi username.  

The share is at \\192.168.50.44\share

And I can transfer at about 2MB/s.

I've seen worse.  

Okay.... I don't really want to be logging in to the share with the admin password for my RasPi.  I'll need to create another user and give it access to the
share.

Also, I need to change the name from [share].

Hmm, in other bad news, I detect a slowdown in the terminal while I'm transferring
this file. Interesting....

Here's how I added the user:

{% highlight console %}
pi@raspberrypi:/mnt/nas $ sudo adduser smbuser
Adding user `smbuser' ...
Adding new group `smbuser' (1001) ...
Adding new user `smbuser' (1001) with group `smbuser' ...
Creating home directory `/home/smbuser' ...
Copying files from `/etc/skel' ...
New password:
Retype new password:
No password supplied
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for smbuser
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n]

{% endhighlight %}

I used a password of 'guest' since I couldn't do blank.

And... I'm not sure that I want to go much further here. I'm not sure I want to make the share writeable at all. 

I think for now I can hold off on this.

## Setting up a Scans Folder ##

1. Make a folder on the NAS called 'Scans'
{% highlight console %}
pi@raspberrypi:~ $ cd /mnt/nas
pi@raspberrypi:/mnt/nas $ sudo mkdir Scans
{% endhighlight %}
2. Change the permissions of the directory to allow the smbuser to write to it
{% highlight console %}
pi@raspberrypi:/mnt/nas $ sudo chown smbuser: Scans
chown: changing ownership of 'Scans': Operation not permitted
{% endhighlight %}

It's possible we can't do this with an exFAT formatted hard drive.

Let's just try adding a new share that is writeable for the smbuser.

I added this to /etc/samba/smb.conf:

{% highlight console %}
[Scans]
Path = /mnt/nas/Scans
Browseable = yes
Writeable = yes
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest ok = yes

{% endhighlight %}

Then I reboot the RasPi.

But sadly, I can't create a file from Windows when I log in as smbuser.

Working from a website [here](https://www.raspberrypi.org/forums/viewtopic.php?t=109428).

First thing I do is try to add a read only field, so it looks like this:

{% highlight console %}
[Scans]
Path = /mnt/nas/Scans
Browseable = yes
Writeable = yes
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest ok = yes
read only = no

{% endhighlight %}

Nope, doesn't work.

Okay, what next?

I'd really like to fix the exFAT user permissions issue. [This](https://raspberrypi.stackexchange.com/a/81989) says it should do the trick.

Okay... doing that doesn't immediately solve the problem. Can I chown now?

No, it does not

Okay, I think we want to mount the drive as smbuser, then it should be writeable.

Okay, usmbuser is uid 1001.

My fstab now looks like this:

{% highlight console %}

proc            /proc           proc    defaults          0       0
PARTUUID=738a4d67-01  /boot           vfat    defaults          0       2
PARTUUID=738a4d67-02  /               ext4    defaults,noatime  0       1
PARTUUID=4aaed96b-01  /mnt/nas        vfat    defaults,auto,users,rw,nofail 0 0
PARTUUID=1de59ff2-01  /mnt/torrents   exfat   defaults,auto,users,rw,nofail,uid=1001,gid=1001,umask=022 0 0

# a swapfile is not a swap partition, no line here
#   use  dphys-swapfile swap[on|off]  for that

{% endhighlight %}

I ended up just using force user = root in the smb.conf file. 

Feels like defeat.

Anyway, now I need a document management system.

I'm going with [Paperless](https://github.com/the-paperless-project/paperless).

I start it off like this:

First, I needed to install git and for that I needed up do an apt-get update.

So I did both of those...

{% highlight console %}
pi@raspberrypi:~ $ sudo apt-get install git
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  git-man libcurl3-gnutls liberror-perl
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git git-man libcurl3-gnutls liberror-perl
0 upgraded, 4 newly installed, 0 to remove and 17 not upgraded.
Need to get 6,137 kB of archives.
After this operation, 32.9 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf libcurl3-gnutls armhf 7.64.0-4+deb10u1 [292 kB]
Get:2 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf liberror-perl all 0.17027-2 [30.9 kB]
Get:3 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf git-man all 1:2.20.1-2+deb10u3 [1,620 kB]
Err:4 http://raspbian.raspberrypi.org/raspbian buster/main armhf git armhf 1:2.20.1-2+deb10u3
  Connection failed [IP: 93.93.128.193 80]
Fetched 1,943 kB in 2min 34s (12.7 kB/s)
E: Failed to fetch http://raspbian.raspberrypi.org/raspbian/pool/main/g/git/git_2.20.1-2+deb10u3_armhf.deb  Connection failed [IP: 93.93.128.193 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
pi@raspberrypi:~ $ sudo apt-get update
Get:1 http://raspbian.raspberrypi.org/raspbian buster InRelease [15.0 kB]
Get:2 https://download.docker.com/linux/raspbian buster InRelease [29.7 kB]
Get:3 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Get:4 http://archive.raspberrypi.org/debian buster/main armhf Packages [331 kB]
Get:5 http://raspbian.raspberrypi.org/raspbian buster/main armhf Packages [13.0 MB]
Get:6 http://raspbian.raspberrypi.org/raspbian buster/contrib armhf Packages [58.7 kB]
Fetched 13.5 MB in 2min 54s (77.4 kB/s)
Reading package lists... Done
pi@raspberrypi:~ $ sudo apt-get install git
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  rpi-eeprom-images
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  git-man libcurl3-gnutls liberror-perl
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git git-man libcurl3-gnutls liberror-perl
0 upgraded, 4 newly installed, 0 to remove and 29 not upgraded.
Need to get 4,194 kB/6,137 kB of archives.
After this operation, 32.9 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://mirror.sjc02.svwh.net/raspbian/raspbian buster/main armhf git armhf 1:2.20.1-2+deb10u3 [4,194 kB]
Fetched 4,194 kB in 18s (233 kB/s)
Selecting previously unselected package libcurl3-gnutls:armhf.
(Reading database ... 43138 files and directories currently installed.)
Preparing to unpack .../libcurl3-gnutls_7.64.0-4+deb10u1_armhf.deb ...
Unpacking libcurl3-gnutls:armhf (7.64.0-4+deb10u1) ...
Selecting previously unselected package liberror-perl.
Preparing to unpack .../liberror-perl_0.17027-2_all.deb ...
Unpacking liberror-perl (0.17027-2) ...
Selecting previously unselected package git-man.
Preparing to unpack .../git-man_1%3a2.20.1-2+deb10u3_all.deb ...
Unpacking git-man (1:2.20.1-2+deb10u3) ...
Selecting previously unselected package git.
Preparing to unpack .../git_1%3a2.20.1-2+deb10u3_armhf.deb ...
Unpacking git (1:2.20.1-2+deb10u3) ...
Setting up libcurl3-gnutls:armhf (7.64.0-4+deb10u1) ...
Setting up liberror-perl (0.17027-2) ...
Setting up git-man (1:2.20.1-2+deb10u3) ...
Setting up git (1:2.20.1-2+deb10u3) ...
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for libc-bin (2.28-10+rpi1) ...
{% endhighlight %}

{% highlight console %}
pi@raspberrypi:~ $ git clone https://github.com/the-paperless-project/paperless.git
{% endhighlight %}

This creates a 'paperless' folder into which I change the working directory.

Then, I try to follow these directions [here](https://paperless.readthedocs.io/en/latest/setup.html#setup-installation-docker).

Step 3 is what I'm on considering that I already have Docker installed and Docker-Compose installed.

So, luckily in the paperless folder there are the two basic files that I need to create and customize.

So I follow its advice.

I'm to modify docker-compose.yml to my liking. My likings are:

* Modified restart to always: restart: always
* Left the web server port as was: 8000
* The healthcheck stuff looks interesting, but I'll leave it as is

Now, we get into something actionable: volumes.

There's a data and media folder and a consume folder. What do they do?
The website says that the only thing I need to change is the consume directory - I'll set it to /mnt/nas/Scans
Apparently I had to do this in two places: under webserver and consumer.

So I did that. Then I saved the file as docker-compose.yml.

Next, on to Docker-compose.env

I didn't change anything there.

Now, I do this:

{% highlight console %}
docker-compose up -d
{% endhighlight %}

And, ha! I don't have docker-compose installed. I guess I was wrong.

So I did this:

{% highlight console %}
pi@raspberrypi:~/paperless $ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100     9  100     9    0     0     31      0 --:--:-- --:--:-- --:--:--    31
pi@raspberrypi:~/paperless $ sudo chmod +x /usr/local/bin/docker-compose
pi@raspberrypi:~/paperless $ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

{% endhighlight %}

Yeah... that didn't work. The download specifically.

Turns out the Raspberyy Pi doesn't have a ready-made version of Compose on the official site.
So I try this [here](https://dev.to/rohansawant/installing-docker-and-docker-compose-on-the-raspberry-pi-in-5-simple-steps-3mgl)

So I try:
{% highlight console %}
sudo pip3 -v install docker-compose
{% endhighlight %}

And it does stuff for a while...
Okay, doesn't look like it failed anywhere.

Time to try the Docker command again.

And it works!

Working for a while....

Okay, what's the next step?

{% highlight console %}
docker-compose run --rm webserver createsuperuser
{% endhighlight %}

It makes me put in a password, so I do.

Now I can log into the web interface on port 8000 @ http://192.168.50.44:8000

Well, what do I do with this?

It doesn't specify what formats it can ingest.  My scanner can do JPEG.

Okay, I have a JPEG there, I had to do some messing to get the consume directory - my source and dest were switched. Once I fixed my docker-compose file and restarted I was able to get a shell on the paperless consumer docker and cd to './consume' and see the files I expected.

I even saw unpaper running via top

But I dont' see any documents.

I look in /usr/src/paperless/media/documents/originals and I see a PDF.  You'd think that was it.

But it's not even unskewed or anything. Doesn't look complete by any means.

I'm wondering if my files are crashing the script?

It might be the JPEG. I removed everything except it and I still get kicked out of the consumer docker shell.

tesseract is always the last thing to run.

It looks like it finished. There's a new .jpg in the originals folder. But no, it's not fixed. And somehow the old pdf showed up again.

Oof. All my projects end up like this.


## Encoding Video to x264 for Plex Using Hardware Acceleration ##

{% highlight console %}
ffmpeg -i <input> -c:v h264_v4l2m2m -preset superfast -crf 23 -tune film -b:v 8M -maxrate:v 8M -bufsize:v 8M -c:a aac -ac 2 -ab 256K -strict experimental -threads 4 -loglevel info -y <output>.mp4
{% endhighlight %}


## Mounting a Remote Samba Share to a Local Path ##

[Thread](https://forums.raspberrypi.com/viewtopic.php?t=276537).

His final solution:
{% highlight console %}
//192.168.2.7/Videos /mnt/Videos cifs _netdev,credentials=/home/pi/.andycreds,uid=pi,gid=pi,x-systemd.automount 0 0
{% endhighlight %}

His initial solution:
{% highlight console %}
//PC/Share /mnt/share cifs username=username,password=password 0 0
{% endhighlight %}

An intermediate solution:
{% highlight console %}
//PC/Share /mnt/share cifs _netdev,username=username,password=password 0 0
{% endhighlight %}

So if I had to guess I'd say that my fstab entry would be:

{% highlight console %}
//192.168.50.122/Torrents /mnt/remote-torrents cifs _netdev,username=guest,password= 0 0
{% endhighlight %}

## Resources ##

