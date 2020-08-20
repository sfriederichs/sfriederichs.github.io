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


## Resources ##
