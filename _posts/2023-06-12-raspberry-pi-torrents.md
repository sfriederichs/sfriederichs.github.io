---
layout: post
title: How to Download Torrents on a Raspberry Pi 4
date: 2023-06-12 12:43
categories: raspberry-pi torrent 
---

## Introduction ##

I've been slowly, _slowly_ getting my Raspberry Pi set up to act as my Plex server. So far, my biggest victories are:

* [x] Plex server is running
* [x] Majority of legacy videos have been copied, renamed and re-encoded to standard formats
* [x] Raspberry Pi 4 is connected to VPN

But, there's still the following left to do:

* [ ] RasPi can download torrents
* [ ] RasPi can automatically download torrents from an RSS feed

Until all of this is done, the old laptop (that is literally falling apart piece by piece) must remain. And thus, I must pray that I don't need to reboot it, touch it, or somehow otherwise offend it and hasten its demise.

So, let's figure out how to download torrents.

## How to download torrents ##

You have to use a torrent client like Transmission

## How to install transmission ##

Follow these steps:
https://pimylifeup.com/raspberry-pi-transmission/

### Work Log ###

Here's what I did:
{% highlight console %}
sudo apt update
sudo apt upgrade
{% endhighlight %}

And the result:
{% highlight console %}
pi@raspberrypi:~ $ sudo apt update
Get:1 https://download.docker.com/linux/raspbian buster InRelease [33.6 kB]
Get:2 http://raspbian.raspberrypi.org/raspbian buster InRelease [15.0 kB]
Ign:3 https://get.filebot.net/deb universal InRelease
Get:4 http://archive.raspberrypi.org/debian buster InRelease [32.6 kB]
Get:5 https://get.filebot.net/deb universal Release [1,160 B]
Get:6 https://get.filebot.net/deb universal Release.gpg [862 B]
Get:7 https://download.docker.com/linux/raspbian buster/stable armhf Packages [32.6 kB]
Get:8 http://raspbian.raspberrypi.org/raspbian buster/main armhf Packages [13.0 MB]
Get:9 https://get.filebot.net/deb universal/main all Packages [575 B]
Get:10 http://archive.raspberrypi.org/debian buster/main armhf Packages [400 kB]
Fetched 13.5 MB in 1min 59s (114 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
49 packages can be upgraded. Run 'apt list --upgradable' to see them.
pi@raspberrypi:~ $ sudo apt upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  libavdevice58 libavresample4 libcdio-cdda2 libcdio-paranoia2
  libcdio18 openjfx-source rpi-eeprom-images
Use 'sudo apt autoremove' to remove them.
The following packages have been kept back:
  ffmpeg
The following packages will be upgraded:
  cpio docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin filebot imagemagick
  imagemagick-6-common imagemagick-6.q16 libavcodec58 libavdevice58
  libavfilter7 libavformat58 libavresample4 libavutil56 libc-bin
  libc-dev-bin libc-l10n libc6 libc6-dbg libc6-dev libcups2
  libcupsfilters1 libcupsimage2 libjavascriptcoregtk-4.0-18
  libmagickcore-6.q16-6 libmagickcore-6.q16-6-extra
  libmagickwand-6.q16-6 libpostproc55 libpython2.7
  libpython2.7-minimal libpython2.7-stdlib libssl1.1 libswresample3
  libswscale5 libwebkit2gtk-4.0-37 libwebp6 libwebpdemux2 libwebpmux3
  locales multiarch-support openssl python2.7 python2.7-minimal
  vim-common vim-tiny xxd
48 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.
Need to get 148 MB of archives.
After this operation, 17.2 MB disk space will be freed.
Do you want to continue? [Y/n] y
Get:1 https://download.docker.com/linux/raspbian buster/stable armhf docker-buildx-plugin armhf 0.10.5-1~raspbian.10~buster [23.6 MB]
Get:2 http://archive.raspberrypi.org/debian buster/main armhf libc6-dbg armhf 2.28-10+rpt2+rpi1+deb10u2 [10.7 MB]
Get:3 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libwebp6 armhf 0.6.1-2+deb10u2 [227 kB]
Get:4 https://get.filebot.net/deb universal/main all filebot all 5.0.3 [22.9 MB]
Get:5 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libwebpmux3 armhf 0.6.1-2+deb10u2 [94.1 kB]
Get:6 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf imagemagick-6-common all 8:6.9.10.23+dfsg-2.1+deb10u5 [202 kB]
Get:7 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libmagickcore-6.q16-6 armhf 8:6.9.10.23+dfsg-2.1+deb10u5 [1,602 kB]
Get:9 http://archive.raspberrypi.org/debian buster/main armhf libc6-dev armhf 2.28-10+rpt2+rpi1+deb10u2 [2,113 kB]
Get:11 http://archive.raspberrypi.org/debian buster/main armhf libc-dev-bin armhf 2.28-10+rpt2+rpi1+deb10u2 [267 kB]
Get:12 http://archive.raspberrypi.org/debian buster/main armhf libc6 armhf 2.28-10+rpt2+rpi1+deb10u2 [2,351 kB]
Get:14 http://archive.raspberrypi.org/debian buster/main armhf libc-bin armhf 2.28-10+rpt2+rpi1+deb10u2 [657 kB]
Get:8 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libmagickwand-6.q16-6 armhf 8:6.9.10.23+dfsg-2.1+deb10u5 [422 kB]
Get:10 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libpython2.7 armhf 2.7.16-2+deb10u2 [872 kB]
Get:13 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf python2.7 armhf 2.7.16-2+deb10u2 [306 kB]
Get:15 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libpython2.7-stdlib armhf 2.7.16-2+deb10u2 [1,846 kB]
Get:41 http://archive.raspberrypi.org/debian buster/main armhf libc-l10n all 2.28-10+rpt2+rpi1+deb10u2 [848 kB]
Get:42 http://archive.raspberrypi.org/debian buster/main armhf locales all 2.28-10+rpt2+rpi1+deb10u2 [4,061 kB]
Get:43 http://archive.raspberrypi.org/debian buster/main armhf libcupsfilters1 armhf 1.21.6-5+rpt1+deb10u1 [161 kB]
Get:44 http://archive.raspberrypi.org/debian buster/main armhf multiarch-support armhf 2.28-10+rpt2+rpi1+deb10u2 [216 kB]
Get:16 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf python2.7-minimal armhf 2.7.16-2+deb10u2 [1,093 kB]
Get:17 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libpython2.7-minimal armhf 2.7.16-2+deb10u2 [396 kB]
Get:18 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libssl1.1 armhf 1.1.1n-0+deb10u5 [1,275 kB]
Get:19 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf cpio armhf 2.12+dfsg-9+deb10u1 [208 kB]
Get:20 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf vim-tiny armhf 2:8.1.0875-5+deb10u5 [505 kB]
Get:21 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf xxd armhf 2:8.1.0875-5+deb10u5 [140 kB]
Get:22 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf vim-common all 2:8.1.0875-5+deb10u5 [196 kB]
Get:23 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf imagemagick-6.q16 armhf 8:6.9.10.23+dfsg-2.1+deb10u5 [582 kB]
Get:45 https://download.docker.com/linux/raspbian buster/stable armhf docker-ce-cli armhf 5:24.0.2-1~raspbian.10~buster [12.1 MB]
Get:24 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf imagemagick armhf 8:6.9.10.23+dfsg-2.1+deb10u5 [158 kB]
Get:25 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libavdevice58 armhf 7:4.1.11-0+deb10u1 [126 kB]
Get:26 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libavfilter7 armhf 7:4.1.11-0+deb10u1 [892 kB]
Get:27 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libswscale5 armhf 7:4.1.11-0+deb10u1 [184 kB]
Get:28 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libavformat58 armhf 7:4.1.11-0+deb10u1 [938 kB]
Get:29 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libavcodec58 armhf 7:4.1.11-0+deb10u1 [4,401 kB]
Get:46 https://download.docker.com/linux/raspbian buster/stable armhf docker-ce armhf 5:24.0.2-1~raspbian.10~buster [14.3 MB]
Get:30 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libswresample3 armhf 7:4.1.11-0+deb10u1 [109 kB]
Get:31 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libpostproc55 armhf 7:4.1.11-0+deb10u1 [91.4 kB]
Get:32 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libavresample4 armhf 7:4.1.11-0+deb10u1 [99.4 kB]
Get:33 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libavutil56 armhf 7:4.1.11-0+deb10u1 [253 kB]
Get:34 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libcupsimage2 armhf 2.2.10-6+deb10u7 [131 kB]
Get:35 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libcups2 armhf 2.2.10-6+deb10u7 [288 kB]
Get:36 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libwebpdemux2 armhf 0.6.1-2+deb10u2 [86.8 kB]
Get:37 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libwebkit2gtk-4.0-37 armhf 2.38.6-0+deb10u1+rpi1 [14.7 MB]
Get:47 https://download.docker.com/linux/raspbian buster/stable armhf docker-ce-rootless-extras armhf 5:24.0.2-1~raspbian.10~buster [8,093 kB]
Get:48 https://download.docker.com/linux/raspbian buster/stable armhf docker-compose-plugin armhf 2.18.1-1~raspbian.10~buster [9,500 kB]
Get:38 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libjavascriptcoregtk-4.0-18 armhf 2.38.6-0+deb10u1+rpi1 [2,540 kB]
Get:39 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libmagickcore-6.q16-6-extra armhf 8:6.9.10.23+dfsg-2.1+deb10u5 [202 kB]
Get:40 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf openssl armhf 1.1.1n-0+deb10u5 [819 kB]
Fetched 148 MB in 5min 1s (491 kB/s)
Reading changelogs... Done
Extracting templates from packages: 100%
Preconfiguring packages ...
(Reading database ... 71451 files and directories currently installed.)
Preparing to unpack .../libc6-dbg_2.28-10+rpt2+rpi1+deb10u2_armhf.deb ...
Unpacking libc6-dbg:armhf (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Preparing to unpack .../libc6-dev_2.28-10+rpt2+rpi1+deb10u2_armhf.deb ...
Unpacking libc6-dev:armhf (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Preparing to unpack .../libc-dev-bin_2.28-10+rpt2+rpi1+deb10u2_armhf.deb ...
Unpacking libc-dev-bin (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Preparing to unpack .../libc6_2.28-10+rpt2+rpi1+deb10u2_armhf.deb ...
Unpacking libc6:armhf (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Setting up libc6:armhf (2.28-10+rpt2+rpi1+deb10u2) ...
(Reading database ... 71460 files and directories currently installed.)
Preparing to unpack .../libc-bin_2.28-10+rpt2+rpi1+deb10u2_armhf.deb ...
Unpacking libc-bin (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Setting up libc-bin (2.28-10+rpt2+rpi1+deb10u2) ...
(Reading database ... 71460 files and directories currently installed.)
Preparing to unpack .../00-libwebp6_0.6.1-2+deb10u2_armhf.deb ...
Unpacking libwebp6:armhf (0.6.1-2+deb10u2) over (0.6.1-2+deb10u1) ...
Preparing to unpack .../01-libwebpmux3_0.6.1-2+deb10u2_armhf.deb ...
Unpacking libwebpmux3:armhf (0.6.1-2+deb10u2) over (0.6.1-2+deb10u1) ...
Preparing to unpack .../02-imagemagick-6-common_8%3a6.9.10.23+dfsg-2.1+deb10u5_all.deb ...
Unpacking imagemagick-6-common (8:6.9.10.23+dfsg-2.1+deb10u5) over (8:6.9.10.23+dfsg-2.1+deb10u4) ...
Preparing to unpack .../03-libmagickcore-6.q16-6_8%3a6.9.10.23+dfsg-2.1+deb10u5_armhf.deb ...
Unpacking libmagickcore-6.q16-6:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) over (8:6.9.10.23+dfsg-2.1+deb10u4) ...
Preparing to unpack .../04-libmagickwand-6.q16-6_8%3a6.9.10.23+dfsg-2.1+deb10u5_armhf.deb ...
Unpacking libmagickwand-6.q16-6:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) over (8:6.9.10.23+dfsg-2.1+deb10u4) ...
Preparing to unpack .../05-libpython2.7_2.7.16-2+deb10u2_armhf.deb ...
Unpacking libpython2.7:armhf (2.7.16-2+deb10u2) over (2.7.16-2+deb10u1) ...
Preparing to unpack .../06-python2.7_2.7.16-2+deb10u2_armhf.deb ...
Unpacking python2.7 (2.7.16-2+deb10u2) over (2.7.16-2+deb10u1) ...
Preparing to unpack .../07-libpython2.7-stdlib_2.7.16-2+deb10u2_armhf.deb ...
Unpacking libpython2.7-stdlib:armhf (2.7.16-2+deb10u2) over (2.7.16-2+deb10u1) ...
Preparing to unpack .../08-python2.7-minimal_2.7.16-2+deb10u2_armhf.deb ...
Unpacking python2.7-minimal (2.7.16-2+deb10u2) over (2.7.16-2+deb10u1) ...
Preparing to unpack .../09-libpython2.7-minimal_2.7.16-2+deb10u2_armhf.deb ...
Unpacking libpython2.7-minimal:armhf (2.7.16-2+deb10u2) over (2.7.16-2+deb10u1) ...
Preparing to unpack .../10-libssl1.1_1.1.1n-0+deb10u5_armhf.deb ...
Unpacking libssl1.1:armhf (1.1.1n-0+deb10u5) over (1.1.1n-0+deb10u4) ...
Preparing to unpack .../11-cpio_2.12+dfsg-9+deb10u1_armhf.deb ...
Unpacking cpio (2.12+dfsg-9+deb10u1) over (2.12+dfsg-9) ...
Preparing to unpack .../12-vim-tiny_2%3a8.1.0875-5+deb10u5_armhf.deb ...
Unpacking vim-tiny (2:8.1.0875-5+deb10u5) over (2:8.1.0875-5+deb10u4) ...
Preparing to unpack .../13-xxd_2%3a8.1.0875-5+deb10u5_armhf.deb ...
Unpacking xxd (2:8.1.0875-5+deb10u5) over (2:8.1.0875-5+deb10u4) ...
Preparing to unpack .../14-vim-common_2%3a8.1.0875-5+deb10u5_all.deb ...
Unpacking vim-common (2:8.1.0875-5+deb10u5) over (2:8.1.0875-5+deb10u4) ...
Preparing to unpack .../15-libc-l10n_2.28-10+rpt2+rpi1+deb10u2_all.deb ...
Unpacking libc-l10n (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Preparing to unpack .../16-locales_2.28-10+rpt2+rpi1+deb10u2_all.deb ...
Unpacking locales (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Preparing to unpack .../17-docker-buildx-plugin_0.10.5-1~raspbian.10~buster_armhf.deb ...
Unpacking docker-buildx-plugin (0.10.5-1~raspbian.10~buster) over (0.10.4-1~raspbian.10~buster) ...
Preparing to unpack .../18-docker-ce-cli_5%3a24.0.2-1~raspbian.10~buster_armhf.deb ...
Unpacking docker-ce-cli (5:24.0.2-1~raspbian.10~buster) over (5:24.0.0-1~raspbian.10~buster) ...
Preparing to unpack .../19-docker-ce_5%3a24.0.2-1~raspbian.10~buster_armhf.deb ...
Unpacking docker-ce (5:24.0.2-1~raspbian.10~buster) over (5:24.0.0-1~raspbian.10~buster) ...
Preparing to unpack .../20-docker-ce-rootless-extras_5%3a24.0.2-1~raspbian.10~buster_armhf.deb ...
Unpacking docker-ce-rootless-extras (5:24.0.2-1~raspbian.10~buster) over (5:24.0.0-1~raspbian.10~buster) ...
Preparing to unpack .../21-docker-compose-plugin_2.18.1-1~raspbian.10~buster_armhf.deb ...
Unpacking docker-compose-plugin (2.18.1-1~raspbian.10~buster) over (2.17.3-1~raspbian.10~buster) ...
Preparing to unpack .../22-imagemagick-6.q16_8%3a6.9.10.23+dfsg-2.1+deb10u5_armhf.deb ...
Unpacking imagemagick-6.q16 (8:6.9.10.23+dfsg-2.1+deb10u5) over (8:6.9.10.23+dfsg-2.1+deb10u4) ...
Preparing to unpack .../23-imagemagick_8%3a6.9.10.23+dfsg-2.1+deb10u5_armhf.deb ...
Unpacking imagemagick (8:6.9.10.23+dfsg-2.1+deb10u5) over (8:6.9.10.23+dfsg-2.1+deb10u4) ...
Preparing to unpack .../24-libavdevice58_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libavdevice58:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../25-libavfilter7_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libavfilter7:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../26-libswscale5_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libswscale5:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../27-libavformat58_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libavformat58:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../28-libavcodec58_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libavcodec58:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../29-libswresample3_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libswresample3:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../30-libpostproc55_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libpostproc55:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../31-libavresample4_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libavresample4:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../32-libavutil56_7%3a4.1.11-0+deb10u1_armhf.deb ...
Unpacking libavutil56:armhf (7:4.1.11-0+deb10u1) over (7:4.1.10-0+deb10u1+rpt1) ...
Preparing to unpack .../33-libcupsimage2_2.2.10-6+deb10u7_armhf.deb ...
Unpacking libcupsimage2:armhf (2.2.10-6+deb10u7) over (2.2.10-6+deb10u6) ...
Preparing to unpack .../34-libcups2_2.2.10-6+deb10u7_armhf.deb ...
Unpacking libcups2:armhf (2.2.10-6+deb10u7) over (2.2.10-6+deb10u6) ...
Preparing to unpack .../35-libcupsfilters1_1.21.6-5+rpt1+deb10u1_armhf.deb ...
Unpacking libcupsfilters1:armhf (1.21.6-5+rpt1+deb10u1) over (1.21.6-5+rpt1) ...
Preparing to unpack .../36-libwebpdemux2_0.6.1-2+deb10u2_armhf.deb ...
Unpacking libwebpdemux2:armhf (0.6.1-2+deb10u2) over (0.6.1-2+deb10u1) ...
Preparing to unpack .../37-libwebkit2gtk-4.0-37_2.38.6-0+deb10u1+rpi1_armhf.deb ...
Unpacking libwebkit2gtk-4.0-37:armhf (2.38.6-0+deb10u1+rpi1) over (2.38.5-1~deb10u1+rpi1) ...
Preparing to unpack .../38-libjavascriptcoregtk-4.0-18_2.38.6-0+deb10u1+rpi1_armhf.deb ...
Unpacking libjavascriptcoregtk-4.0-18:armhf (2.38.6-0+deb10u1+rpi1) over (2.38.5-1~deb10u1+rpi1) ...
Preparing to unpack .../39-libmagickcore-6.q16-6-extra_8%3a6.9.10.23+dfsg-2.1+deb10u5_armhf.deb ...
Unpacking libmagickcore-6.q16-6-extra:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) over (8:6.9.10.23+dfsg-2.1+deb10u4) ...
Preparing to unpack .../40-multiarch-support_2.28-10+rpt2+rpi1+deb10u2_armhf.deb ...
Unpacking multiarch-support (2.28-10+rpt2+rpi1+deb10u2) over (2.28-10+rpt2+rpi1+deb10u1) ...
Preparing to unpack .../41-openssl_1.1.1n-0+deb10u5_armhf.deb ...
Unpacking openssl (1.1.1n-0+deb10u5) over (1.1.1n-0+deb10u4) ...
Preparing to unpack .../42-filebot_5.0.3_all.deb ...
Unpacking filebot (5.0.3) over (5.0.2) ...
Setting up cpio (2.12+dfsg-9+deb10u1) ...
Setting up imagemagick-6-common (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Setting up libc-l10n (2.28-10+rpt2+rpi1+deb10u2) ...
Setting up filebot (5.0.3) ...
Setting up libssl1.1:armhf (1.1.1n-0+deb10u5) ...
Setting up libjavascriptcoregtk-4.0-18:armhf (2.38.6-0+deb10u1+rpi1) ...
Setting up locales (2.28-10+rpt2+rpi1+deb10u2) ...
Generating locales (this might take a while)...
  en_GB.UTF-8... done
Generation complete.
Setting up xxd (2:8.1.0875-5+deb10u5) ...
Setting up libavutil56:armhf (7:4.1.11-0+deb10u1) ...
Setting up libc6-dbg:armhf (2.28-10+rpt2+rpi1+deb10u2) ...
Setting up docker-buildx-plugin (0.10.5-1~raspbian.10~buster) ...
Setting up libpython2.7-minimal:armhf (2.7.16-2+deb10u2) ...
Setting up vim-common (2:8.1.0875-5+deb10u5) ...
Setting up multiarch-support (2.28-10+rpt2+rpi1+deb10u2) ...
Setting up python2.7-minimal (2.7.16-2+deb10u2) ...
Setting up libwebp6:armhf (0.6.1-2+deb10u2) ...
Setting up libpostproc55:armhf (7:4.1.11-0+deb10u1) ...
Setting up docker-compose-plugin (2.18.1-1~raspbian.10~buster) ...
Setting up libcups2:armhf (2.2.10-6+deb10u7) ...
Setting up docker-ce-cli (5:24.0.2-1~raspbian.10~buster) ...
Setting up libswscale5:armhf (7:4.1.11-0+deb10u1) ...
Setting up docker-ce-rootless-extras (5:24.0.2-1~raspbian.10~buster) ...
Setting up libc-dev-bin (2.28-10+rpt2+rpi1+deb10u2) ...
Setting up openssl (1.1.1n-0+deb10u5) ...
Setting up libwebpmux3:armhf (0.6.1-2+deb10u2) ...
Setting up libwebpdemux2:armhf (0.6.1-2+deb10u2) ...
Setting up vim-tiny (2:8.1.0875-5+deb10u5) ...
Setting up libswresample3:armhf (7:4.1.11-0+deb10u1) ...
Setting up libavresample4:armhf (7:4.1.11-0+deb10u1) ...
Setting up libcupsimage2:armhf (2.2.10-6+deb10u7) ...
Setting up libpython2.7-stdlib:armhf (2.7.16-2+deb10u2) ...
Setting up libmagickcore-6.q16-6:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Setting up docker-ce (5:24.0.2-1~raspbian.10~buster) ...
Setting up libwebkit2gtk-4.0-37:armhf (2.38.6-0+deb10u1+rpi1) ...
Setting up libc6-dev:armhf (2.28-10+rpt2+rpi1+deb10u2) ...
Setting up libmagickwand-6.q16-6:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Setting up libavcodec58:armhf (7:4.1.11-0+deb10u1) ...
Setting up libcupsfilters1:armhf (1.21.6-5+rpt1+deb10u1) ...
Setting up libpython2.7:armhf (2.7.16-2+deb10u2) ...
Setting up python2.7 (2.7.16-2+deb10u2) ...
Setting up libmagickcore-6.q16-6-extra:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Setting up libavformat58:armhf (7:4.1.11-0+deb10u1) ...
Setting up imagemagick-6.q16 (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Setting up libavfilter7:armhf (7:4.1.11-0+deb10u1) ...
Setting up libavdevice58:armhf (7:4.1.11-0+deb10u1) ...
Setting up imagemagick (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for libc-bin (2.28-10+rpt2+rpi1+deb10u2) ...
Processing triggers for systemd (241-7~deb10u9+rpi1) ...
Processing triggers for man-db (2.8.5-2) ...
sudo apt update
sudo apt upgradeProcessing triggers for shared-mime-info (1.10-1) ...
Processing triggers for mime-support (3.62) ...

{% endhighlight %}

And next:

{% highlight console %}

pi@raspberrypi:~ $ sudo apt install transmission-daemon
Reading package lists... Done
Building dependency tree
Reading state information... Done
transmission-daemon is already the newest version (2.94-2+deb10u2).
The following packages were automatically installed and are no longer required:
  libavdevice58 libavresample4 libcdio-cdda2 libcdio-paranoia2 libcdio18
  openjfx-source rpi-eeprom-images
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.

{% endhighlight %}

Then I stop the newly-activated service:

{% highlight console %}
pi@raspberrypi:~ $ sudo systemctl stop transmission-daemon.service

{% endhighlight %}

And I make torrent directories on my big hard drive: /mnt/torrents :
{% highlight console %}

pi@raspberrypi:/mnt/torrents $ sudo mkdir -p torrents-inprogress
pi@raspberrypi:/mnt/torrents $ sudo mkdir -p torrents-complete
{% endhighlight %}

Then set the owner on the new directories to 'pi' instead of root:

{% highlight console %}
pi@raspberrypi:/mnt/torrents $ sudo chown -R pi:pi /mnt/torrents/torrents-inprogress/
pi@raspberrypi:/mnt/torrents $ sudo chown -R pi:pi /mnt/torrents/torrents-complete

{% endhighlight %}

Then, we edit the configuration file, but I'm not going to tell you what I changed in favor of just pasting the whole thing here:

{% highlight console %}
pi@raspberrypi:/mnt/torrents $ sudo cat /etc/transmission-daemon/settings.json
{
    "alt-speed-down": 50,
    "alt-speed-enabled": false,
    "alt-speed-time-begin": 540,
    "alt-speed-time-day": 127,
    "alt-speed-time-enabled": false,
    "alt-speed-time-end": 1020,
    "alt-speed-up": 50,
    "bind-address-ipv4": "0.0.0.0",
    "bind-address-ipv6": "::",
    "blocklist-enabled": false,
    "blocklist-url": "http://www.example.com/blocklist",
    "cache-size-mb": 4,
    "dht-enabled": true,
    "download-dir": "/mnt/torrents/torrents-complete",
    "download-limit": 100,
    "download-limit-enabled": 0,
    "download-queue-enabled": true,
    "download-queue-size": 5,
    "encryption": 1,
    "idle-seeding-limit": 30,
    "idle-seeding-limit-enabled": false,
    "incomplete-dir": "/mnt/torrents/torrents-inprogress",
    "incomplete-dir-enabled": true,
    "lpd-enabled": false,
    "max-peers-global": 200,
    "message-level": 1,
    "peer-congestion-algorithm": "",
    "peer-id-ttl-hours": 6,
    "peer-limit-global": 200,
    "peer-limit-per-torrent": 50,
    "peer-port": 51413,
    "peer-port-random-high": 65535,
    "peer-port-random-low": 49152,
    "peer-port-random-on-start": false,
    "peer-socket-tos": "default",
    "pex-enabled": true,
    "port-forwarding-enabled": false,
    "preallocation": 1,
    "prefetch-enabled": true,
    "queue-stalled-enabled": true,
    "queue-stalled-minutes": 30,
    "ratio-limit": 2,
    "ratio-limit-enabled": false,
    "rename-partial-files": true,
    "rpc-authentication-required": false,
    "rpc-bind-address": "0.0.0.0",
    "rpc-enabled": true,
    "rpc-host-whitelist": "",
    "rpc-host-whitelist-enabled": true,
    "rpc-password": "Nope",
    "rpc-port": 9092,
    "rpc-url": "/transmission/",
    "rpc-username": "transmission",
    "rpc-whitelist": "127.0.0.1,192.168.50.*",
    "rpc-whitelist-enabled": true,
    "scrape-paused-torrents-enabled": true,
    "script-torrent-done-enabled": false,
    "script-torrent-done-filename": "",
    "seed-queue-enabled": false,
    "seed-queue-size": 10,
    "speed-limit-down": 100,
    "speed-limit-down-enabled": false,
    "speed-limit-up": 100,
    "speed-limit-up-enabled": false,
    "start-added-torrents": true,
    "trash-original-torrent-files": false,
    "umask": 18,
    "upload-limit": 100,
    "upload-limit-enabled": 0,
    "upload-slots-per-torrent": 14,
    "utp-enabled": true
}

{% endhighlight %}

And the cat command in the window shows the whole path to the file too.

Then, we have to edit one of the service files associated with transmission to change the user under which the daemon will run. This has to be done in two places: /etc/init.d/transmission-daemon and /etc/systemd/system/multi-user.target.wants/transmission-daemon.service.

Here's the (abbreviated) init.d/transmission-daemon file (onlyl the USER= line was changed, the rest is there for context)

{% highlight console %}
#!/bin/sh -e
### BEGIN INIT INFO
# Provides:          transmission-daemon
# Required-Start:    $local_fs $remote_fs $network
# Required-Stop:     $local_fs $remote_fs $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start or stop the transmission-daemon.
# Description:       Enable service provided by transmission-daemon.
### END INIT INFO

NAME=transmission-daemon
DAEMON=/usr/bin/$NAME
USER=pi
STOP_TIMEOUT=30

{% endhighlight %}

And the transmission-daemon.service file (this one's the whole thing):

{% highlight ini %}
[Unit]
Description=Transmission BitTorrent Daemon
After=network.target

[Service]
User=pi
Type=notify
ExecStart=/usr/bin/transmission-daemon -f --log-error
ExecStop=/bin/kill -s STOP $MAINPID
ExecReload=/bin/kill -s HUP $MAINPID

[Install]
WantedBy=multi-user.target


{% endhighlight %}

Then, we instruct the service manager to reload all of the configuration files:

{% highlight console %}
pi@raspberrypi:/mnt/torrents $ sudo systemctl daemon-reload
{% endhighlight %}

Now since we've changed the user that's the daemon will run under, we have to change some directory ownerships.

{% highlight console %}
pi@raspberrypi:/mnt/torrents $ sudo chown -R pi:pi /etc/transmission-daemon
{% endhighlight %}

Then we start doing some dodgy things with the configuration file?

{% highlight console %}
pi@raspberrypi:/mnt/torrents $ sudo mkdir -p /home/pi/.config/transmission-daemon
pi@raspberrypi:/mnt/torrents $ sudo ln -s /etc/transmission-daemon/settings.json /home/pi/.config/transmission-daemon
pi@raspberrypi:/mnt/torrents $ sudo chown -R pi:pi /home/pi/.config/transmission-daemon/
{% endhighlight %}

And then I start the service with this command:
{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo systemctl start transmission-daemon
{% endhighlight %}

And then I check 192.168.50.44:9092 (because apparently I changed it at some point....) and I get a transmission web interface.

I've checked my external IP with this command:

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ curl icanhazip.com
181.xx.xxx.xxx
{% endhighlight %}

And that is different than the IP on my desktop PC, so the VPN is still working, and that's great.

That means I can get right to downloading torrents.

But that requires that I get the RSS feature working somehow.

It is my birthday. Maybe I do that....


## How to Read RSS Feeds ##

I'm looking at a nice Github page for what seems to be a Ruby script: https://github.com/nning/transmission-rss

### Work Log ###

The page starts with this command:

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ gem install transmission-rss
-bash: gem: command not found
{% endhighlight %}

Oh, that's not good.

How about we try to install it:

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo apt install gem
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libavdevice58 libavresample4 libcdio-cdda2 libcdio-paranoia2
  openjfx-source rpi-eeprom-images
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  gem-doc gem-extra gem-plugin-assimp gem-plugin-gmerlin
  gem-plugin-lqt gem-plugin-magick gem-plugin-v4l2 liba52-0.7.4
  libassimp4 libftgl2 libgavl1 libglewmx1.13 libgmerlin-avdec1
  libmagick++-6.q16-8 libminizip1 libmpeg2-4 libportaudio2
  libquicktime2 puredata puredata-core puredata-dev puredata-doc
  puredata-extra puredata-gui puredata-gui-l10n puredata-utils tcl
  tcl8.6 tk tk8.6 xbitmaps xterm
Suggested packages:
  pd-zexy v4l2loopback-dkms | v4l2loopback-modules pd-aubio pd-csound
  pd-pdp multimedia-puredata tcl-tclreadline xfonts-cyrillic
The following NEW packages will be installed:
  gem gem-doc gem-extra gem-plugin-assimp gem-plugin-gmerlin
  gem-plugin-lqt gem-plugin-magick gem-plugin-v4l2 liba52-0.7.4
  libassimp4 libftgl2 libgavl1 libglewmx1.13 libgmerlin-avdec1
  libmagick++-6.q16-8 libminizip1 libmpeg2-4 libportaudio2
  libquicktime2 puredata puredata-core puredata-dev puredata-doc
  puredata-extra puredata-gui puredata-gui-l10n puredata-utils tcl
  tcl8.6 tk tk8.6 xbitmaps xterm
0 upgraded, 33 newly installed, 0 to remove and 1 not upgraded.
Need to get 14.4 MB of archives.
After this operation, 34.8 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf libftgl2 armhf 2.4.0-2.1~deb10u1 [99.3 kB]
Get:2 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf libglewmx1.13 armhf 1.13.0-4 [126 kB]
Get:3 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libportaudio2 armhf 19.6.0-1+deb10u1 [56.7 kB]
Get:4 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-core armhf 0.49.0-3 [567 kB]
Get:8 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libminizip1 armhf 1.1-8+b1 [18.3 kB]
Get:5 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem armhf 1:0.94-1 [1,294 kB]
Get:11 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libgavl1 armhf 1.4.0-5+b2 [2,772 kB]
Get:6 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-doc all 1:0.94-1 [3,945 kB]
Get:7 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-extra armhf 1:0.94-1 [160 kB]
Get:9 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf libassimp4 armhf 4.1.0~dfsg-5 [1,624 kB]
Get:10 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-plugin-assimp armhf 1:0.94-1 [131 kB]
Get:12 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf liba52-0.7.4 armhf 0.7.4-19 [29.8 kB]
Get:13 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf libmpeg2-4 armhf 0.5.1-8 [54.1 kB]
Get:14 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf libgmerlin-avdec1 armhf 1.2.0~dfsg-10 [389 kB]
Get:15 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-plugin-gmerlin armhf 1:0.94-1 [126 kB]
Get:17 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-plugin-lqt armhf 1:0.94-1 [138 kB]
Get:19 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-plugin-magick armhf 1:0.94-1 [128 kB]
Get:20 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf gem-plugin-v4l2 armhf 1:0.94-1 [143 kB]
Get:21 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-dev all 0.49.0-3 [39.6 kB]
Get:22 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-doc all 0.49.0-3 [851 kB]
Get:23 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-extra armhf 0.49.0-3 [94.4 kB]
Get:24 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf tk8.6 armhf 8.6.9-2 [71.9 kB]
Get:28 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-gui all 0.49.0-3 [105 kB]
Get:29 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-utils armhf 0.49.0-3 [25.5 kB]
Get:16 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libquicktime2 armhf 2:1.2.4-12+b2 [222 kB]
Get:30 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata all 0.49.0-3 [19.9 kB]
Get:31 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf puredata-gui-l10n all 0.49.0-3 [44.8 kB]
Get:18 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libmagick++-6.q16-8 armhf 8:6.9.10.23+dfsg-2.1+deb10u5 [255 kB]
Get:32 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf xbitmaps all 1.1.1-2 [32.1 kB]
Get:25 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf tcl8.6 armhf 8.6.9+dfsg-2 [123 kB]
Get:26 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf tcl armhf 8.6.9+1 [5,636 B]
Get:27 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf tk armhf 8.6.9+1 [5,676 B]
Get:33 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf xterm armhf 344-1+deb10u2 [718 kB]
Fetched 14.4 MB in 15s (979 kB/s)
Extracting templates from packages: 100%
Selecting previously unselected package libftgl2:armhf.
(Reading database ... 71442 files and directories currently installed.)
Preparing to unpack .../00-libftgl2_2.4.0-2.1~deb10u1_armhf.deb ...
Unpacking libftgl2:armhf (2.4.0-2.1~deb10u1) ...
Selecting previously unselected package libglewmx1.13:armhf.
Preparing to unpack .../01-libglewmx1.13_1.13.0-4_armhf.deb ...
Unpacking libglewmx1.13:armhf (1.13.0-4) ...
Selecting previously unselected package libportaudio2:armhf.
Preparing to unpack .../02-libportaudio2_19.6.0-1+deb10u1_armhf.deb ...
Unpacking libportaudio2:armhf (19.6.0-1+deb10u1) ...
Selecting previously unselected package puredata-core.
Preparing to unpack .../03-puredata-core_0.49.0-3_armhf.deb ...
Unpacking puredata-core (0.49.0-3) ...
Selecting previously unselected package gem.
Preparing to unpack .../04-gem_1%3a0.94-1_armhf.deb ...
Unpacking gem (1:0.94-1) ...
Selecting previously unselected package gem-doc.
Preparing to unpack .../05-gem-doc_1%3a0.94-1_all.deb ...
Unpacking gem-doc (1:0.94-1) ...
Selecting previously unselected package gem-extra.
Preparing to unpack .../06-gem-extra_1%3a0.94-1_armhf.deb ...
Unpacking gem-extra (1:0.94-1) ...
Selecting previously unselected package libminizip1:armhf.
Preparing to unpack .../07-libminizip1_1.1-8+b1_armhf.deb ...
Unpacking libminizip1:armhf (1.1-8+b1) ...
Selecting previously unselected package libassimp4:armhf.
Preparing to unpack .../08-libassimp4_4.1.0~dfsg-5_armhf.deb ...
Unpacking libassimp4:armhf (4.1.0~dfsg-5) ...
Selecting previously unselected package gem-plugin-assimp.
Preparing to unpack .../09-gem-plugin-assimp_1%3a0.94-1_armhf.deb ...
Unpacking gem-plugin-assimp (1:0.94-1) ...
Selecting previously unselected package libgavl1:armhf.
Preparing to unpack .../10-libgavl1_1.4.0-5+b2_armhf.deb ...
Unpacking libgavl1:armhf (1.4.0-5+b2) ...
Selecting previously unselected package liba52-0.7.4:armhf.
Preparing to unpack .../11-liba52-0.7.4_0.7.4-19_armhf.deb ...
Unpacking liba52-0.7.4:armhf (0.7.4-19) ...
Selecting previously unselected package libmpeg2-4:armhf.
Preparing to unpack .../12-libmpeg2-4_0.5.1-8_armhf.deb ...
Unpacking libmpeg2-4:armhf (0.5.1-8) ...
Selecting previously unselected package libgmerlin-avdec1:armhf.
Preparing to unpack .../13-libgmerlin-avdec1_1.2.0~dfsg-10_armhf.deb ...
Unpacking libgmerlin-avdec1:armhf (1.2.0~dfsg-10) ...
Selecting previously unselected package gem-plugin-gmerlin.
Preparing to unpack .../14-gem-plugin-gmerlin_1%3a0.94-1_armhf.deb ...
Unpacking gem-plugin-gmerlin (1:0.94-1) ...
Selecting previously unselected package libquicktime2:armhf.
Preparing to unpack .../15-libquicktime2_2%3a1.2.4-12+b2_armhf.deb ...
Unpacking libquicktime2:armhf (2:1.2.4-12+b2) ...
Selecting previously unselected package gem-plugin-lqt.
Preparing to unpack .../16-gem-plugin-lqt_1%3a0.94-1_armhf.deb ...
Unpacking gem-plugin-lqt (1:0.94-1) ...
Selecting previously unselected package libmagick++-6.q16-8:armhf.
Preparing to unpack .../17-libmagick++-6.q16-8_8%3a6.9.10.23+dfsg-2.1+deb10u5_armhf.deb ...
Unpacking libmagick++-6.q16-8:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Selecting previously unselected package gem-plugin-magick.
Preparing to unpack .../18-gem-plugin-magick_1%3a0.94-1_armhf.deb ...
Unpacking gem-plugin-magick (1:0.94-1) ...
Selecting previously unselected package gem-plugin-v4l2.
Preparing to unpack .../19-gem-plugin-v4l2_1%3a0.94-1_armhf.deb ...
Unpacking gem-plugin-v4l2 (1:0.94-1) ...
Selecting previously unselected package puredata-dev.
Preparing to unpack .../20-puredata-dev_0.49.0-3_all.deb ...
Unpacking puredata-dev (0.49.0-3) ...
Selecting previously unselected package puredata-doc.
Preparing to unpack .../21-puredata-doc_0.49.0-3_all.deb ...
Unpacking puredata-doc (0.49.0-3) ...
Selecting previously unselected package puredata-extra.
Preparing to unpack .../22-puredata-extra_0.49.0-3_armhf.deb ...
Unpacking puredata-extra (0.49.0-3) ...
Selecting previously unselected package tk8.6.
Preparing to unpack .../23-tk8.6_8.6.9-2_armhf.deb ...
Unpacking tk8.6 (8.6.9-2) ...
Selecting previously unselected package tcl8.6.
Preparing to unpack .../24-tcl8.6_8.6.9+dfsg-2_armhf.deb ...
Unpacking tcl8.6 (8.6.9+dfsg-2) ...
Selecting previously unselected package tcl.
Preparing to unpack .../25-tcl_8.6.9+1_armhf.deb ...
Unpacking tcl (8.6.9+1) ...
Selecting previously unselected package tk.
Preparing to unpack .../26-tk_8.6.9+1_armhf.deb ...
Unpacking tk (8.6.9+1) ...
Selecting previously unselected package puredata-gui.
Preparing to unpack .../27-puredata-gui_0.49.0-3_all.deb ...
Unpacking puredata-gui (0.49.0-3) ...
Selecting previously unselected package puredata-utils.
Preparing to unpack .../28-puredata-utils_0.49.0-3_armhf.deb ...
Unpacking puredata-utils (0.49.0-3) ...
Selecting previously unselected package puredata.
Preparing to unpack .../29-puredata_0.49.0-3_all.deb ...
Unpacking puredata (0.49.0-3) ...
Selecting previously unselected package puredata-gui-l10n.
Preparing to unpack .../30-puredata-gui-l10n_0.49.0-3_all.deb ...
Unpacking puredata-gui-l10n (0.49.0-3) ...
Selecting previously unselected package xbitmaps.
Preparing to unpack .../31-xbitmaps_1.1.1-2_all.deb ...
Unpacking xbitmaps (1.1.1-2) ...
Selecting previously unselected package xterm.
Preparing to unpack .../32-xterm_344-1+deb10u2_armhf.deb ...
Unpacking xterm (344-1+deb10u2) ...
Setting up tk8.6 (8.6.9-2) ...
Setting up libportaudio2:armhf (19.6.0-1+deb10u1) ...
Setting up tcl8.6 (8.6.9+dfsg-2) ...
Setting up libminizip1:armhf (1.1-8+b1) ...
Setting up libgavl1:armhf (1.4.0-5+b2) ...
Setting up puredata-doc (0.49.0-3) ...
Setting up libftgl2:armhf (2.4.0-2.1~deb10u1) ...
Setting up libquicktime2:armhf (2:1.2.4-12+b2) ...
Setting up libmpeg2-4:armhf (0.5.1-8) ...
Setting up puredata-utils (0.49.0-3) ...
Setting up liba52-0.7.4:armhf (0.7.4-19) ...
Setting up gem-doc (1:0.94-1) ...
Setting up libassimp4:armhf (4.1.0~dfsg-5) ...
Setting up tcl (8.6.9+1) ...
Setting up libglewmx1.13:armhf (1.13.0-4) ...
Setting up libmagick++-6.q16-8:armhf (8:6.9.10.23+dfsg-2.1+deb10u5) ...
Setting up tk (8.6.9+1) ...
Setting up puredata-core (0.49.0-3) ...
update-alternatives: using /usr/bin/puredata to provide /usr/bin/pd (pd) in auto mode
Setting up xbitmaps (1.1.1-2) ...
Setting up puredata-dev (0.49.0-3) ...
Setting up gem (1:0.94-1) ...
update-alternatives: using /usr/lib/pd/extra/Gem/gemdefaultwindow-glx.pd to provide /usr/lib/pd/extra/Gem/gemdefaultwindow.pd (gemdefaultwindow.pd) in auto mode
Setting up puredata-extra (0.49.0-3) ...
Setting up gem-plugin-v4l2 (1:0.94-1) ...
Setting up gem-plugin-lqt (1:0.94-1) ...
Setting up libgmerlin-avdec1:armhf (1.2.0~dfsg-10) ...
Setting up gem-plugin-magick (1:0.94-1) ...
Setting up gem-plugin-assimp (1:0.94-1) ...
Setting up puredata-gui (0.49.0-3) ...
Setting up gem-extra (1:0.94-1) ...
Setting up xterm (344-1+deb10u2) ...
update-alternatives: using /usr/bin/xterm to provide /usr/bin/x-terminal-emulator (x-terminal-emulator) in auto mode
update-alternatives: using /usr/bin/lxterm to provide /usr/bin/x-terminal-emulator (x-terminal-emulator) in auto mode
Setting up puredata-gui-l10n (0.49.0-3) ...
Setting up gem-plugin-gmerlin (1:0.94-1) ...
Setting up puredata (0.49.0-3) ...
Processing triggers for mime-support (3.62) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for libc-bin (2.28-10+rpt2+rpi1+deb10u2) ...
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for shared-mime-info (1.10-1) ...

{% endhighlight %}

But then...

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ gem install transmission-rss
-bash: gem: command not found
{% endhighlight %}

Oh well:

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo apt remove gem
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gem-doc liba52-0.7.4 libassimp4 libavdevice58 libavresample4
  libcdio-cdda2 libcdio-paranoia2 libcdio18 libftgl2 libgavl1
  libglewmx1.13 libgmerlin-avdec1 libmagick++-6.q16-8 libminizip1
  libmpeg2-4 libquicktime2 openjfx-source puredata puredata-core
  puredata-dev puredata-doc puredata-extra puredata-gui
  puredata-gui-l10n puredata-utils rpi-eeprom-images tcl tk
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  gem gem-extra gem-plugin-assimp gem-plugin-gmerlin gem-plugin-lqt
  gem-plugin-magick gem-plugin-v4l2
0 upgraded, 0 newly installed, 7 to remove and 1 not upgraded.
After this operation, 6,202 kB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 72967 files and directories currently installed.)
Removing gem-extra (1:0.94-1) ...
Removing gem-plugin-v4l2 (1:0.94-1) ...
Removing gem-plugin-assimp (1:0.94-1) ...
Removing gem-plugin-gmerlin (1:0.94-1) ...
Removing gem-plugin-lqt (1:0.94-1) ...
Removing gem-plugin-magick (1:0.94-1) ...
Removing gem (1:0.94-1) ...
Processing triggers for man-db (2.8.5-2) ...
{% endhighlight %}

Let's just try installing ruby:

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo apt install ruby
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gem-doc liba52-0.7.4 libassimp4 libavdevice58 libavresample4
  libcdio-cdda2 libcdio-paranoia2 libcdio18 libftgl2 libgavl1
  libglewmx1.13 libgmerlin-avdec1 libmagick++-6.q16-8 libminizip1
  libmpeg2-4 libquicktime2 openjfx-source puredata puredata-core
  puredata-dev puredata-doc puredata-extra puredata-gui
  puredata-gui-l10n puredata-utils rpi-eeprom-images tcl tk
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  fonts-lato libruby2.5 libyaml-0-2 rake ruby-did-you-mean
  ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit
  ruby-xmlrpc ruby2.5 rubygems-integration zip
Suggested packages:
  ri ruby-dev bundler
The following NEW packages will be installed:
  fonts-lato libruby2.5 libyaml-0-2 rake ruby ruby-did-you-mean
  ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit
  ruby-xmlrpc ruby2.5 rubygems-integration zip
0 upgraded, 14 newly installed, 0 to remove and 1 not upgraded.
Need to get 6,773 kB of archives.
After this operation, 27.9 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf fonts-lato all 2.0-2 [2,698 kB]
Get:2 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf rubygems-integration all 1.11+deb10u1 [5,212 B]
Get:3 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf ruby2.5 armhf 2.5.5-3+deb10u6 [401 kB]
Get:4 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf ruby armhf 1:2.5.1+b1 [11.6 kB]
Get:5 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf rake all 12.3.1-3+deb10u1 [67.1 kB]
Get:6 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf ruby-did-you-mean all 1.2.1-1 [14.4 kB]
Get:7 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf ruby-minitest all 5.11.3-1 [54.8 kB]
Get:8 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf ruby-net-telnet all 0.1.1-2 [12.5 kB]
Get:9 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf ruby-power-assert all 1.1.1-1 [10.9 kB]
Get:10 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf ruby-test-unit all 3.2.8-1 [72.4 kB]
Get:11 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf ruby-xmlrpc all 0.3.0-2 [23.7 kB]
Get:12 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf libyaml-0-2 armhf 0.2.1-1 [38.8 kB]
Get:13 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf libruby2.5 armhf 2.5.5-3+deb10u6 [3,151 kB]
Get:14 http://mirrors.gigenet.com/raspbian/raspbian buster/main armhf zip armhf 3.0-11 [212 kB]
Fetched 6,773 kB in 9s (737 kB/s)                                      j
Selecting previously unselected package fonts-lato.
(Reading database ... 72654 files and directories currently installed.)
Preparing to unpack .../00-fonts-lato_2.0-2_all.deb ...
Unpacking fonts-lato (2.0-2) ...
Selecting previously unselected package rubygems-integration.
Preparing to unpack .../01-rubygems-integration_1.11+deb10u1_all.deb ...
Unpacking rubygems-integration (1.11+deb10u1) ...
Selecting previously unselected package ruby2.5.
Preparing to unpack .../02-ruby2.5_2.5.5-3+deb10u6_armhf.deb ...
Unpacking ruby2.5 (2.5.5-3+deb10u6) ...
Selecting previously unselected package ruby.
Preparing to unpack .../03-ruby_1%3a2.5.1+b1_armhf.deb ...
Unpacking ruby (1:2.5.1+b1) ...
Selecting previously unselected package rake.
Preparing to unpack .../04-rake_12.3.1-3+deb10u1_all.deb ...
Unpacking rake (12.3.1-3+deb10u1) ...
Selecting previously unselected package ruby-did-you-mean.
Preparing to unpack .../05-ruby-did-you-mean_1.2.1-1_all.deb ...
Unpacking ruby-did-you-mean (1.2.1-1) ...
Selecting previously unselected package ruby-minitest.
Preparing to unpack .../06-ruby-minitest_5.11.3-1_all.deb ...
Unpacking ruby-minitest (5.11.3-1) ...
Selecting previously unselected package ruby-net-telnet.
Preparing to unpack .../07-ruby-net-telnet_0.1.1-2_all.deb ...
Unpacking ruby-net-telnet (0.1.1-2) ...
Selecting previously unselected package ruby-power-assert.
Preparing to unpack .../08-ruby-power-assert_1.1.1-1_all.deb ...
Unpacking ruby-power-assert (1.1.1-1) ...
Selecting previously unselected package ruby-test-unit.
Preparing to unpack .../09-ruby-test-unit_3.2.8-1_all.deb ...
Unpacking ruby-test-unit (3.2.8-1) ...
Selecting previously unselected package ruby-xmlrpc.
Preparing to unpack .../10-ruby-xmlrpc_0.3.0-2_all.deb ...
Unpacking ruby-xmlrpc (0.3.0-2) ...
Selecting previously unselected package libyaml-0-2:armhf.
Preparing to unpack .../11-libyaml-0-2_0.2.1-1_armhf.deb ...
Unpacking libyaml-0-2:armhf (0.2.1-1) ...
Selecting previously unselected package libruby2.5:armhf.
Preparing to unpack .../12-libruby2.5_2.5.5-3+deb10u6_armhf.deb ...
Unpacking libruby2.5:armhf (2.5.5-3+deb10u6) ...
Selecting previously unselected package zip.
Preparing to unpack .../13-zip_3.0-11_armhf.deb ...
Unpacking zip (3.0-11) ...
Setting up fonts-lato (2.0-2) ...
Setting up ruby-power-assert (1.1.1-1) ...
Setting up libyaml-0-2:armhf (0.2.1-1) ...
Setting up rubygems-integration (1.11+deb10u1) ...
Setting up ruby-minitest (5.11.3-1) ...
Setting up zip (3.0-11) ...
Setting up ruby-test-unit (3.2.8-1) ...
Setting up ruby-net-telnet (0.1.1-2) ...
Setting up ruby-did-you-mean (1.2.1-1) ...
Setting up ruby-xmlrpc (0.3.0-2) ...
Setting up ruby2.5 (2.5.5-3+deb10u6) ...
Setting up ruby (1:2.5.1+b1) ...
Setting up rake (12.3.1-3+deb10u1) ...
Setting up libruby2.5:armhf (2.5.5-3+deb10u6) ...
Processing triggers for libc-bin (2.28-10+rpt2+rpi1+deb10u2) ...
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for fontconfig (2.13.1-2) ...
{% endhighlight %}

Okay, looks like success. Now can I install the thing?
{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ gem install transmission-rss



Fetching: ffi-1.15.5.gem (100%)
ERROR:  While executing gem ... (Gem::FilePermissionError)
    You don't have write permissions for the /var/lib/gems/2.5.0 directory.
{% endhighlight %}

Okay, as sudo?

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo gem install transmission-rss
Fetching: ffi-1.15.5.gem (100%)
Building native extensions. This could take a while...
ERROR:  Error installing transmission-rss:
        ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/2.5.0/gems/ffi-1.15.5/ext/ffi_c
/usr/bin/ruby2.5 -r ./siteconf20230619-14897-ik14ug.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.5.0/gems/ffi-1.15.5 for inspection.
Results logged to /var/lib/gems/2.5.0/extensions/arm-linux/2.5.0/ffi-1.15.5/gem_make.out

{% endhighlight %}

I know I need to download more ruby stuff - development stuff. Let's try a random package:

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo apt install ruby-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gem-doc liba52-0.7.4 libassimp4 libavdevice58 libavresample4
  libcdio-cdda2 libcdio-paranoia2 libcdio18 libftgl2 libgavl1
  libglewmx1.13 libgmerlin-avdec1 libmagick++-6.q16-8 libminizip1
  libmpeg2-4 libquicktime2 openjfx-source puredata puredata-core
  puredata-dev puredata-doc puredata-extra puredata-gui
  puredata-gui-l10n puredata-utils rpi-eeprom-images tcl tk
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  ruby2.5-dev ruby2.5-doc
The following NEW packages will be installed:
  ruby-dev ruby2.5-dev ruby2.5-doc
0 upgraded, 3 newly installed, 0 to remove and 1 not upgraded.
Need to get 2,578 kB of archives.
After this operation, 19.3 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf ruby2.5-dev armhf 2.5.5-3+deb10u6 [416 kB]
Get:2 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf ruby-dev armhf 1:2.5.1+b1 [10.4 kB]
Get:3 http://mirror.pit.teraswitch.com/raspbian/raspbian buster/main armhf ruby2.5-doc all 2.5.5-3+deb10u6 [2,151 kB]
Fetched 2,578 kB in 5s (534 kB/s)
Selecting previously unselected package ruby2.5-dev:armhf.
(Reading database ... 73952 files and directories currently installed.)
Preparing to unpack .../ruby2.5-dev_2.5.5-3+deb10u6_armhf.deb ...
Unpacking ruby2.5-dev:armhf (2.5.5-3+deb10u6) ...
Selecting previously unselected package ruby-dev:armhf.
Preparing to unpack .../ruby-dev_1%3a2.5.1+b1_armhf.deb ...
Unpacking ruby-dev:armhf (1:2.5.1+b1) ...
Selecting previously unselected package ruby2.5-doc.
Preparing to unpack .../ruby2.5-doc_2.5.5-3+deb10u6_all.deb ...
Unpacking ruby2.5-doc (2.5.5-3+deb10u6) ...
Setting up ruby2.5-dev:armhf (2.5.5-3+deb10u6) ...
Setting up ruby2.5-doc (2.5.5-3+deb10u6) ...
Setting up ruby-dev:armhf (1:2.5.1+b1) ...
{% endhighlight %}

Okay, something happened. Let's see if we can do the gem install now.

{% highlight console %}
pi@raspberrypi:~/.config/transmission-daemon $ sudo gem install transmission-rss
Building native extensions. This could take a while...
Successfully installed ffi-1.15.5
Fetching: rb-inotify-0.10.1.gem (100%)
Successfully installed rb-inotify-0.10.1
Fetching: open_uri_redirections-0.2.1.gem (100%)
Successfully installed open_uri_redirections-0.2.1
Fetching: rexml-3.2.5.gem (100%)
Successfully installed rexml-3.2.5
Fetching: rss-0.2.9.gem (100%)
Successfully installed rss-0.2.9
Fetching: transmission-rss-1.2.3.gem (100%)
Successfully installed transmission-rss-1.2.3
Parsing documentation for ffi-1.15.5
Installing ri documentation for ffi-1.15.5
Parsing documentation for rb-inotify-0.10.1
Installing ri documentation for rb-inotify-0.10.1
Parsing documentation for open_uri_redirections-0.2.1
Installing ri documentation for open_uri_redirections-0.2.1
Parsing documentation for rexml-3.2.5
Installing ri documentation for rexml-3.2.5
Parsing documentation for rss-0.2.9
Installing ri documentation for rss-0.2.9
Parsing documentation for transmission-rss-1.2.3
Installing ri documentation for transmission-rss-1.2.3
Done installing documentation for ffi, rb-inotify, open_uri_redirections, rexml, rss, transmission-rss after 91 seconds
6 gems installed

{% endhighlight %}

Okay, that's good. What's next?

I need to create a config dir and a config file, like this:

{% highlight console %}
pi@raspberrypi:~ $ mkdir -p ~/.config/transmission-rss
pi@raspberrypi:~ $ nano ~/.config/transmission-rss/config.yml
pi@raspberrypi:~ $ cat ~/.config/transmission-rss/config.yml
feeds:
    - url: http://showrss.info/user/127411.rss?magnets=true&namespaces=true&name=null&quality=null&re=null

{% endhighlight %}

Okay, did that. What's next?

I can configure it to download the .torrent files to a specific directory. Then transmission can look there.

I need to get that feature working on transmission. I'd better look at the configuration file again.

For later, two options stand out at me:

{% highlight console %}
    "script-torrent-done-enabled": false,
    "script-torrent-done-filename": "",
{% endhighlight %}

I think there is no such feature. I tried this:

{% highlight console %}
pi@raspberrypi:~/temp-rss $ transmission-rss -s
2023-06-19 06:55:16 (error) /etc/transmission-rss.conf not found
2023-06-19 06:55:16 (debug) loading user config /home/pi/.config/transmission-rss/config.yml
2023-06-19 06:55:16 (info) transmission-rss 1.2.3
2023-06-19 06:55:16 (debug) {"feeds"=>[{"url"=>"http://showrss.info/user/127411.rss?magnets=true&namespaces=true&name=null&quality=null&re=null"}], "update_interval"=>600, "add_paused"=>false, "server"=>{"host"=>"localhost", "port"=>9091, "tls"=>false, "rpc_path"=>"/transmission/rpc"}, "login"=>nil, "log"=>{"target"=>#<IO:<STDERR>>, "level"=>:debug}, "fork"=>false, "single"=>false, "pid_file"=>false, "privileges"=>{}, "seen_file"=>nil}
2023-06-19 06:55:16 (debug) no privilege dropping, running as user pi
2023-06-19 06:55:16 (debug) 0 uris from seenfile
2023-06-19 06:55:16 (debug) aggregator start
2023-06-19 06:55:16 (debug) aggregate http://showrss.info/user/127411.rss?magnets=true&namespaces=true&name=null&quality=null&re=null
2023-06-19 06:55:16 (debug) on_new_item event magnet:?xt=urn:btih:40D5C6748A31F8A0E03A03BE9E712FFDF07C9293&dn=Outlander+S07E01+720p+WEB+h264+EDITH&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2F9.rarbg.me%3A2960&tr=udp%3A%2F%2F9.rarbg.to%3A2980
2023-06-19 06:55:16 (debug) request localhost:9091
Traceback (most recent call last):
        37: from /usr/local/bin/transmission-rss:23:in `<main>'
        36: from /usr/local/bin/transmission-rss:23:in `load'
        35: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/bin/transmission-rss:189:in `<top (required)>'
        34: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:43:in `run'
        33: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:43:in `loop'
        32: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:44:in `block in run'
        31: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:44:in `each'
        30: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:64:in `block (2 levels) in run'
        29: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:64:in `each'
        28: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:65:in `block (3 levels) in run'
        27: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/aggregator.rb:131:in `process_link'
        26: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/callback.rb:12:in `block (3 levels) in callback'
        25: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/bin/transmission-rss:161:in `block in <top (required)>'
        24: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:59:in `add_torrent'
        23: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:29:in `rpc'
        22: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:96:in `get_session_id'
        21: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:131:in `request'
        20: from /usr/lib/ruby/2.5.0/timeout.rb:108:in `timeout'
        19: from /usr/lib/ruby/2.5.0/timeout.rb:33:in `catch'
        18: from /usr/lib/ruby/2.5.0/timeout.rb:33:in `catch'
        17: from /usr/lib/ruby/2.5.0/timeout.rb:33:in `block in catch'
        16: from /usr/lib/ruby/2.5.0/timeout.rb:93:in `block in timeout'
        15: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:133:in `block in request'
        14: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:123:in `http_request'
        13: from /usr/lib/ruby/2.5.0/net/http.rb:609:in `start'
        12: from /usr/lib/ruby/2.5.0/net/http.rb:910:in `start'
        11: from /var/lib/gems/2.5.0/gems/transmission-rss-1.2.3/lib/transmission-rss/client.rb:124:in `block in http_request'
        10: from /usr/lib/ruby/2.5.0/net/http.rb:1467:in `request'
         9: from /usr/lib/ruby/2.5.0/net/http.rb:1494:in `transport_request'
         8: from /usr/lib/ruby/2.5.0/net/http.rb:1494:in `catch'
         7: from /usr/lib/ruby/2.5.0/net/http.rb:1497:in `block in transport_request'
         6: from /usr/lib/ruby/2.5.0/net/http/response.rb:29:in `read_new'
         5: from /usr/lib/ruby/2.5.0/net/http/response.rb:40:in `read_status_line'
         4: from /usr/lib/ruby/2.5.0/net/protocol.rb:167:in `readline'
         3: from /usr/lib/ruby/2.5.0/net/protocol.rb:157:in `readuntil'
         2: from /usr/lib/ruby/2.5.0/net/protocol.rb:175:in `rbuf_fill'
         1: from /usr/lib/ruby/2.5.0/socket.rb:452:in `read_nonblock'
/usr/lib/ruby/2.5.0/socket.rb:452:in `__read_nonblock': Connection reset by peer (Errno::ECONNRESET)

{% endhighlight %}

Right, so it's trying to access the rpc interface of transmission to do its dirty work. I've got to configure that because it can't get to the one on 9092 right now.

Here's my updated config file:

{% highlight yaml %}
feeds:
    - url: http://showrss.info/user/127411.rss?magnets=true&namespaces=true&name=null&quality=null&re=null

server:
  host: localhost
  port: 9092
  tls: false
  rpc_path: /transmission/rpc

login:
  username: transmission
  password: nope
{% endhighlight %}

And if I try to run it again with transmission-rss -s....

It works!

I think I'll add this as a cron job, like so:

{% highlight console %}
pi@raspberrypi:~/temp-rss $ sudo crontab -e
crontab: installing new crontab
{% endhighlight %}

My crontab now looks like this:

{% highlight console %}
0 * * * * sudo filebot -non-strict -rename --db TheTVDB --action move --output /mnt/torrents/tv /mnt/torrents/temp
15 * * * * sudo filebot -non-strict -get-subtitles --db TheTVDB /mnt/torrents/tv
*/10 * * * * /usr/local/bin/transmission-rss -s

{% endhighlight %}

Okay, so currently I'm:

* Having filebot rename files in the 'temp' directory and moving them into the 'tv' directory at the top of the hour
* Downloading subtitles for all the files in the 'tv' directory at 15 after the hour
* Every 10 minutes, add new torrents to transmission

So, the process will be:

1. Torrent gets added from RSS feed (every 10 minutes)
2. Torrent finishes downloading - creates video file
3. Video file gets re-encoded into 'temp' directory
4. Original video file is deleted
5. at the top of the hour, the video file will be renamed and moved into the 'tv' directory (the video can now be watched on Plex)
6. Subtitles will be downloaded at 15 after the hour

So, unless I miss my mark, all I need to do is use the feature of transmission where I run a command after the torrent downloads. 
I've disabled the torrents downloading for the moment by pausing all of the existing ones and then changing the settings to not start added torrents automatically. They'll keep piling up, but everything is still downloading on the old laptop, so I don't need the new downloading to start and I'm not ready to re-encode them yet.

#### 7/8/23 ####

So, where I currently am with my setup:

1. VPN is connected
2. Transmission is installed and running
3. Torrents are being added from an RSS feed
4. Torrents are downloaded and placed into a 'torrents-complete' directory
5. Transmission will call a script I've made once the torrent is completed, which will:
    a) Rename/Copy all video files in 'torrents-complete' to a 'torrents-renamed' directory. The original file are left in 'torrents-complete' to allow for seeding, the copied files are renamed to a standard format via Filebot
	b) Re-encode all videos files in 'torrents-renamed' to a standard format and place it in the 'tv' directory - Plex will serve the video from this directory
	c) Download the subtitles for the videos to the 'tv' directory
	d) Remove the video files from 'torrents-renamed'
	
There are a few issues with this process though, mainly associated with my desire to seed the torrents. Take a look at step 5a above: it specifies that it will copy ALL video files from the 'torrents-complete' directory to 'torrents-renamed'. However, it is possible that this will include videos that have already been processed via the script, but haven't finished seeding and thus, haven't been removed. It's a waste of time to re-encode videos I've already re-encoded. That'd be re-re-encoding. It's just silly.

There's a few potential ways around this:

1. Delete the original file in 'torrents-complete' once it's been re-encoded. The downside of this is that I'd have to stop seeding. That's not *awful* but it's not *neighborly*. I'd feel a little bad if I did this.
2. Check to see if the video is in the 'tv' directory before re-encoding. This would require a bit more smarts in the script, but that's no big deal. It also would mean copying all of the videos from 'torrents-complete' every time you ran the script. That'd be wasteful of disk space, but it gets worse when I realize I still haven't figured out how to stop torrents that are done.

Okay, number 2 above is the best way of doing this, but it means we have to fix all of the other problems I thought up:

1. Need a way to clear out the torrents that have finished seeding
2. Need a way to determine if a file in 'torrents-complete' has been processed without copying gigs and gigs of data

These are independent problems. I must resist the urge to bundle their solutions together for no good reason.  

For example, I know I can solve number 1 above because I've found out there's a python library that will interface with transmission and allow me to programatically evaluate which torrents should be removed. That can be run in a cron job every hour or so. If I keep the script light and fast, I can run it more often and everything will feel more responsive. If I weight the script down with more features, I run the risk of introducing delays, complexity and bugs. If the script just does one thing, we can debug it, streamline it and *finish* it sooner. And then forget about it.

So, how can I solve number 2? Well, I've found another idea. The biggest difficulty for determining if a file has already been processed is that we rename the video file to a standard naming format, but keep the original name in 'torrents-complete'. Thus, we have to figure out what the standardized name of the each video file in 'torrents-complete' so we can determine if it already is in the 'tv' directory. Filebot can rename the file and copy, move, or do weird symlink stuff. It can also run custom scripts, to which it passes the original file name and the new file name as arguments. 

If I have filebot call a custom bash script of mine and read those file names, I can see if the file has already been processed.

I can start off this process by having Transmission call filebot with the proper command-line parameters. Transmission will create an environment variable with the path to the directory the torrent was downloaded in. I can tell Filebot to look in that directory and then

Question 1: Do I have to process the downloaded torrent directory recursively with Filebot? I need to know if that directory is just 'torrents-complete' or if there'll be a subdirectory. There's not always a subdirectory with these torrents.

I think I had another question but I've forgotten it. I just keep getting hung up on potential issues.

I've been taking a look around the Transmission interface and I think I'm settling on something here. It is centered around the 'Set Location' feature.

If I were to set the location of the torrent to 'torrents-seeding' - would that copy all of the data? I can try that right now.

Yes, that does in fact happen.

Okay, so maybe Transmission calls filebot to rename, which I have call my script with the two paths. My script can do the copy/rename for Filebot, then use transmission-rpc to talk to the Transmission and do a Set Location on the torrent (which it can identify via environmental variables which Python can access as described [here](https://stackoverflow.com/a/4907053) ). 

Filebot environmental variables available to scripts can be found [here](https://github.com/transmission/transmission/blob/main/docs/Scripts.md) 
## Resources ##


