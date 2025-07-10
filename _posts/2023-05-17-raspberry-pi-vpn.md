---
layout: post
title: How to Set a VPN on a Raspberry Pi 4
date: 2023-05-17 12:43
categories: raspberry-pi vpn
---

## Introduction ##

I've been slowly, _slowly_ getting my Raspberry Pi set up to act as my Plex server. So far, my biggest victory other than getting the Plex server running on the RasPi is a script I made that copied, renamed and transcoded all of my existing video files on my old server to my new one. 

However, there's one problem: I still haven't set up my a VPN, torrent client and torrent RSS feed downloader on the RasPi, so the 'old' server is still responsible for downloading new episodes, which then have to be copied over to the 'new' server. 

If I can get my torrent setup running on the RasPi, then once I clean out the last of the videos from the old server, I'll be done with it completely. 

There are multiple steps to this process:

1. Connect to the VPN
2. Set up the torrent client
	a) Download and install the client
	b) Force it to use the VPN connection only
	c) Set up the scripts to access the torrent RSS feed
3. Create a script/workflow that will automatically transcode, rename and download subtitles for each downloaded episode.

Since it's always best to split tasks into smaller tasks, I will start with task one up there and see how we can get to connect to my preferred VPN of Private Internet Access .

## Googling It ##

Googling for how to setup up PIA on a RasPi brings up this [https://helpdesk.privateinternetaccess.com/guides/other-hardware/raspberry-pi/raspberry-pi-2](PIA Helpdesk) page.

Honestly, this thing doesn't even _sound_ right and I'm just going to ignore it.

Instead I'm going to work from [this](https://www.raspberrypi-spy.co.uk/2020/06/raspberry-pi-vpn-setup-guide/) page instead.

It looks like we'll be installing Open VPN and.. some other stuff. 

I've done more writing than actual work, so let's get to business here.

## Doing It ##

Okay, step 1 is updating your OS stuff with:

> sudo apt update

Which, for me has this effect:

{% highlight console %}

pi@raspberrypi:~ $ sudo apt update
Get:1 https://download.docker.com/linux/raspbian buster InRelease [33.6 kB]
Get:2 http://raspbian.raspberrypi.org/raspbian buster InRelease [15.0 kB]
Get:3 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Ign:4 https://get.filebot.net/deb universal InRelease
Get:5 https://get.filebot.net/deb universal Release [1,160 B]
Get:6 https://get.filebot.net/deb universal Release.gpg [862 B]
Get:7 https://download.docker.com/linux/raspbian buster/stable armhf Packages [31.0 kB]
Get:8 http://raspbian.raspberrypi.org/raspbian buster/main armhf Packages [13.0 MB]
Get:9 http://archive.raspberrypi.org/debian buster/main armhf Packages [400 kB]
Get:10 https://get.filebot.net/deb universal/main all Packages [575 B]
Get:11 http://raspbian.raspberrypi.org/raspbian buster/non-free armhf Packages [110 kB]
Fetched 13.6 MB in 9s (1,571 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
65 packages can be upgraded. Run 'apt list --upgradable' to see them.

{% endhighlight %}

And then, the next command is:

> sudo apt upgrade

and that produces.....

Well, it produces a *lot*. So I won't paste that.

And it's finally done, so, yay.

Now we install OpenVPN with this:

> sudo apt install openvpn

And the result:

{% highlight console %}
pi@raspberrypi:~ $ sudo apt install openvpn
Reading package lists... Done
Building dependency tree
Reading state information... Done
openvpn is already the newest version (2.4.7-1+deb10u1).
The following packages were automatically installed and are no longer required:
  libavdevice58 libavresample4 libcdio-cdda2 libcdio-paranoia2
  libcdio18 openjfx-source rpi-eeprom-images
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.

{% endhighlight %}

Of course, I do have it installed because I've tried this before. Still, doesn't hurt to try.

Next, we have to download some OpenVPN configuration files from PIA.

That involves two commands:

> cd /etc/openvpn
> sudo wget https://www.privateinternetaccess.com/openvpn/openvpn.zip

And the result:

{% highlight console %}
pi@raspberrypi:~ $ cd /etc/openvpn
pi@raspberrypi:/etc/openvpn $ sudo wget https://www.privateinternetaccess.com/openvpn/openvpn.zip
--2023-05-18 05:04:36--  https://www.privateinternetaccess.com/openvpn/openvpn.zip
Resolving www.privateinternetaccess.com (www.privateinternetaccess.com)... 104.18.14.49, 104.18.15.49
Connecting to www.privateinternetaccess.com (www.privateinternetaccess.com)|104.18.14.49|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 192173 (188K) [application/zip]
Saving to: ‘openvpn.zip’

openvpn.zip       100%[=============>] 187.67K  --.-KB/s    in 0.05s

2023-05-18 05:04:36 (3.67 MB/s) - ‘openvpn.zip’ saved [192173/192173]

{% endhighlight %}

So, that's a zip file and we have to unzip it, like this:

> sudo unzip openvpn.zip

which has the effect:

{% highlight console %}
pi@raspberrypi:/etc/openvpn $ sudo unzip openvpn.zip
Archive:  openvpn.zip
  inflating: albania.ovpn
  inflating: algeria.ovpn
  inflating: andorra.ovpn
  inflating: argentina.ovpn
  inflating: armenia.ovpn
  inflating: au_melbourne.ovpn
  inflating: au_perth.ovpn
  inflating: au_sydney.ovpn
  inflating: austria.ovpn
  inflating: bahamas.ovpn
  inflating: bangladesh.ovpn
  inflating: belgium.ovpn
  inflating: brazil.ovpn
  inflating: bulgaria.ovpn
replace ca.rsa.2048.crt? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
  inflating: ca.rsa.2048.crt
  inflating: ca_montreal.ovpn
  inflating: ca_ontario.ovpn
  inflating: ca_toronto.ovpn
  inflating: ca_vancouver.ovpn
  inflating: cambodia.ovpn
  inflating: china.ovpn
  inflating: crl.rsa.2048.pem
  inflating: cyprus.ovpn
  inflating: czech_republic.ovpn
  inflating: de_berlin.ovpn
  inflating: de_frankfurt.ovpn
  inflating: denmark.ovpn
  inflating: egypt.ovpn
  inflating: estonia.ovpn
  inflating: finland.ovpn
  inflating: france.ovpn
  inflating: georgia.ovpn
  inflating: greece.ovpn
  inflating: greenland.ovpn
  inflating: hong_kong.ovpn
  inflating: hungary.ovpn
  inflating: iceland.ovpn
  inflating: india.ovpn
  inflating: ireland.ovpn
  inflating: isle_of_man.ovpn
  inflating: israel.ovpn
  inflating: italy.ovpn
  inflating: japan.ovpn
  inflating: kazakhstan.ovpn
  inflating: latvia.ovpn
  inflating: liechtenstein.ovpn
  inflating: lithuania.ovpn
  inflating: luxembourg.ovpn
  inflating: macao.ovpn
  inflating: macedonia.ovpn
  inflating: malta.ovpn
  inflating: mexico.ovpn
  inflating: moldova.ovpn
  inflating: monaco.ovpn
  inflating: mongolia.ovpn
  inflating: montenegro.ovpn
  inflating: morocco.ovpn
  inflating: netherlands.ovpn
  inflating: new_zealand.ovpn
  inflating: nigeria.ovpn
  inflating: norway.ovpn
  inflating: panama.ovpn
  inflating: philippines.ovpn
  inflating: poland.ovpn
  inflating: portugal.ovpn
  inflating: qatar.ovpn
  inflating: romania.ovpn
  inflating: saudi_arabia.ovpn
  inflating: serbia.ovpn
  inflating: singapore.ovpn
  inflating: slovakia.ovpn
  inflating: south_africa.ovpn
  inflating: spain.ovpn
  inflating: sri_lanka.ovpn
  inflating: sweden.ovpn
  inflating: switzerland.ovpn
  inflating: taiwan.ovpn
  inflating: turkey.ovpn
  inflating: uk_london.ovpn
  inflating: uk_manchester.ovpn
  inflating: uk_southampton.ovpn
  inflating: ukraine.ovpn
  inflating: united_arab_emirates.ovpn
  inflating: us_atlanta.ovpn
  inflating: us_california.ovpn
  inflating: us_chicago.ovpn
  inflating: us_denver.ovpn
  inflating: us_east.ovpn
  inflating: us_florida.ovpn
  inflating: us_houston.ovpn
  inflating: us_las_vegas.ovpn
  inflating: us_new_york.ovpn
  inflating: us_seattle.ovpn
  inflating: us_silicon_valley.ovpn
  inflating: us_texas.ovpn
  inflating: us_washington_dc.ovpn
  inflating: us_west.ovpn
  inflating: venezuela.ovpn
  inflating: vietnam.ovpn

{% endhighlight %}

Of course, I have tried to do this before, so those files do exist. But, hey, no harm no foul here, so let's continue.

The website has me list the files next, but I can already tell which one is the one I will use:

{% highlight console %}
-rw-rw-r-- 1 root root 3169 Nov 19  2020 us_denver.ovpn

{% endhighlight %}

Yup, since I'm currently in Denver, I will use that one.

Now it wants me to verify my external IP with this command:

> curl https://api.ipify.org

When I use that command on my RasPi, the result is:

{% highlight console %}
76.155.202.9
{% endhighlight %}

Okay. Nice IP.

Now things are getting interesting and it wants me to attempt to connect to one of these VPN servers with this command:

> sudo openvpn us_denver.ovpn

It will prompt me for my username and password, which I should probably find....

Username: ********
Password: **********

so, that command provides the following:

{% highlight console %}
pi@raspberrypi:/etc/openvpn $ sudo openvpn us_denver.ovpn
Thu May 18 05:35:12 2023 OpenVPN 2.4.7 arm-unknown-linux-gnueabihf [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Apr 28 2021
Thu May 18 05:35:12 2023 library versions: OpenSSL 1.1.1n  15 Mar 2022, LZO 2.10
Enter Auth Username: ********
Enter Auth Password: **********
Thu May 18 05:35:22 2023 TCP/UDP: Preserving recently used remote address: [AF_INET]181.41.206.167:1198
Thu May 18 05:35:22 2023 UDP link local: (not bound)
Thu May 18 05:35:22 2023 UDP link remote: [AF_INET]181.41.206.167:1198
Thu May 18 05:35:22 2023 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
Thu May 18 05:35:22 2023 [denver427] Peer Connection Initiated with [AF_INET]181.41.206.167:1198
Thu May 18 05:35:23 2023 OpenVPN ROUTE6: OpenVPN needs a gateway parameter for a --route-ipv6 option and no default was specified by either --route-ipv6-gateway or --ifconfig-ipv6 options
Thu May 18 05:35:23 2023 OpenVPN ROUTE: failed to parse/resolve route for host/network: 2000::/3
Thu May 18 05:35:23 2023 TUN/TAP device tun0 opened
Thu May 18 05:35:23 2023 /sbin/ip link set dev tun0 up mtu 1500
Thu May 18 05:35:23 2023 /sbin/ip addr add dev tun0 10.1.112.251/24 broadcast 10.1.112.255
Thu May 18 05:35:23 2023 WARNING: OpenVPN was configured to add an IPv6 route over tun0. However, no IPv6 has been configured for this interface, therefore the route installation may fail or may not work as expected.
Thu May 18 05:35:23 2023 Initialization Sequence Completed

{% endhighlight %}

And that does not kick us back out to the terminal as the website suggested. So now I have to open a new terminal and try the curl command again to get the new (hoepfully) IP.

And that IP is: 181.41.206.167

Success I should say!

Now we just have to get it to tdo it automatically.

The website says that we can do that with this command:

> sudo nano auth.txt

And within auth.txt we have the following content:

{% highlight text %}
yourusername
yourpassword
{% endhighlight %}

And I do so!

Then I have to update the .ovpn files to use this auth.txt apparently, with this command:

> sudo find *.ovpn -type f -exec sed -i 's/auth-user-pass/auth-user-pass auth.txt/g' {} \;

And the effect of this is:

Well, nothing. I hope it worked.

I don't know if it worked. I tried to run openvpn as before and I was unable to curl from another terminal session.
However, I was also unable to curl once I wasn't trying to connect to the VPN. So I don't really know what's happening.

At this point I'd like to get it automatically running at startup and then reboot and see what curl says.

So I do this:

> sudo cp us_denver.ovpn autostart.conf

and change the line:
{% highlight console %}
#AUTOSTART="all"
{% endhighlight %}

to:

{% highlight console %}
AUTOSTART="autostart"
{% endhighlight %}

And I can't connect......

And now I can. Took a second. 

The IP address is:

{% highlight console %}
181.41.206.140
{% endhighlight %}

That seems right.  It's on the VPN.

I think that's it for tonight.


## Resources ##


