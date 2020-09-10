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
pi@raspberrypi:~ $ ls /dev/sd*
ls: cannot access '/dev/sd*': No such file or directory

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

#### Automatically Mounting the Drive at Startup ####

Possible set of directions [here](https://www.raspberrypi.org/documentation/configuration/external-storage.md).

I'm starting at the 'Setting up automatic mounting' section.

I start off by doing this:
{% highlight console %}
pi@raspberrypi:~ $ sudo lsblk -o UUID,NAME,FSTYPE,PARTUUID,MOUNTPOINT
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

### Transferring Metadata From Windows to Linux ###

I have a Plex server on Windows already. I will be transferring all of the media files by attaching the external hard drive to the RasPi, but 
I need also to transfer all of the metadata such as whether or not a file has been viewed already.

[This](https://forums.plex.tv/t/how-to-transfer-plex-library-from-windows-to-linux/90633/3) is an initial guess as to how to do that.

[This](https://www.reddit.com/r/PleX/comments/7amo55/move_plex_from_windows_to_linux_while_keeping_all/) is another.

### Settings Changes ###

If I change any of the settings in the Plex server, I'll list them
here.

### Plex Plugins ###

If I add any Plex plugins I'll list them here.

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
 docker run --cap-add=NET_ADMIN -d               -v /mnt/usbdrive/torrents/:/data               -v /etc/localtime:/etc/localtime:ro               -e CREATE_TUN_DEVICE=true               -e OPENVPN_PROVIDER=PIA               -e OPENVPN_CONFIG=CA\ Denver               -e OPENVPN_USERNAME=user               -e OPENVPN_PASSWORD=pass               -e WEBPROXY_ENABLED=false               -e LOCAL_NETWORK=192.168.50.0/24               --log-driver json-file               --log-opt max-size=10m               -p 9091:9091               haugene/transmission-openvpn:latest-armhf

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



### Setting up Torrent Client to Read an RSS Feed ###

Found something [here](https://github.com/nning/transmission-rss).

## Setting up a Subversion Server on a RasPi ##

TBD

## Setting up a Jekyll Server on a RasPi ##

TBD

## Setting up a Jenkins Server on a RasPi ##

TBD

## Setting up a Redmine Server on a RasPi ##

TBD

## Setting up a NAS on a RasPi ##
TBD

   

## Resources ##
