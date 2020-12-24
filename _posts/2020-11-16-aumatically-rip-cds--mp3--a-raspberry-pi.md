---
layout: post
title: How to Automatically Rip CDs to MP3 with a Raspberry Pi
date: 2020-11-16 22:46
categories:
---

## Introduction ##

My wife has a huge, sorry, YUGE collection of CDs. She'd rather they're all MP3s or some other digital format for
easier listening. 

I was doing this on my PC, but it's cumbersome and rather manual. I have a vision that I should be able to attach
my USB CD drive to my Raspberry Pi and have the ripper automatically start when I insert a CD, then eject when it's
done. With such an approach, I could get through this task much more quickly. 


## Approach ##

Looks like we're using a package called *abcde*.

## Installation ##

I'm starting with this command line:

{% highlight console %}
sudo apt-get install abcde lame eject id3 id3v2 eyed3 normalize-audio vorbisgain mkcue mp3gain libdata-dump-perl flac
{% endhighlight %}

Okay.. things installed. The guide is a bit silent on where this configuration file is and how to use this utility

Okay, if I do this:

{% highlight console %}
pi@raspberrypi:~ $ abcde
[ERROR] abcde: CDROM has not been defined or cannot be found

{% endhighlight %}

It makes sense, I haven't attached the CDROM drive yet. But where would I define the CDROM parameter? Where's the .cfg file?

Okay, there's /etc/abcde.conf

Well it looks like all of the options are commented out so I'll have to figure out what to set for each option.

It maybe works without all the options set.

First, let's set the CDROM option.

I've attached the CDROM to the RasPi, let's see where it showed up.
Here's what I see:

{% highlight console %}
pi@raspberrypi:~ $ ls /dev/cd*
/dev/cdrom  /dev/cdrw
{% endhighlight %}

This is how I modified the configuration file:

{% highlight console %}
# CD device you want to read from
# It can be defined as a singletrack flac file, but since it might change from
# file to file it makes little sense to define it here.
CDROM=/dev/cdrom
{% endhighlight %}

Looks like you need to run nano as sudo to get this to work.

It seems that it will always output in the current directory you run it from. We should try it.

I wonder where the MP3 quality options are?

Anyway, I set the CDROM option to the CD drive, created ~/rip and then ran abcde in it.

It's starting to rip it.

It did ask a lot of questions. I'll have to automate that.

Oh how nice its default format is ogg.


## Configuration Options ##

### Interactive Options ###

{% highlight console %}
# Define if you want abcde to be non-interactive.
# Keep in mind that there is no way to deactivate it right now in the command
# line, so setting this option makes abcde to be always non-interactive.
#INTERACTIVE=n

{% endhighlight %}

Easy peasy.
### Execution Options ###
{% highlight console %}
# Actions to take
# Comma-separated list of one or more of the following:
#  cddb,cue,read,normalize,encode,tag,move,replaygain,playlist,getalbumart,embe$
#   encode implies read
#   normalize implies read
#   tag implies cddb,read,encode
#   move implies cddb,read,encode,tag
#   replaygain implies cddb,read,encode,tag,move
#   playlist implies cddb
#   embedalbumart implies getalbumart
# An action can be added to the "default" action by specifying it along with
# "default", without having to repeat the default ones:
#  ACTIONS=default,playlist
# The default action list (referenced as "default") is defined in the following
# comment:
#ACTIONS=cddb,read,encode,tag,move,clean

{% endhighlight %}

Interesting. I don't think there's much to do here yet.

### Output Options ###
{% highlight console %}
# OUTPUTTYPE can be any of a number of formats, either a single format
# (e.g. "ogg") or a combination of them separated with ","
# (e.g. "flac,mp3"). Currently recognised and supported are:
# "flac", "m4a", "mp3, "mpc", "ogg", "opus", "mka", "spx", "vorbis", "wav", "wv$
#OUTPUTTYPE=ogg

{% endhighlight %}

I'm going to say mp3.

### Maximum Processes ###

{% highlight console %}
# Define how many encoders to run at once. This makes for huge speedups
# on SMP systems. Defaults to 1. Equivalent to -j.
#MAXPROCS=2
{% endhighlight %}

I'm going to set it to 3.

### Parallelization ###

{% highlight console %}
# Support for systems with low disk space:
# n:    Default parallelization (read entire CD in while encoding)
# y:    No parallelization (rip, encode, rip, encode...)
#LOWDISK=n

{% endhighlight %}

I'm going to set it to 'n'.

### MP3 Encoder Syntax ###

I think I'll be able to set the quality options I want here:

{% highlight console %}
#MP3ENCODERSYNTAX=default
{% endhighlight %}

And the MP3 encoder is...
 
LAME

So, I make the option 
{% highlight console %}
MP3ENCODERSYNTAX=lame
{% endhighlight %}

And for the encoder options:
{% highlight console %}
# MP3:
# For the best LAME encoder options have a look at:
# <http://wiki.hydrogenaudio.org/index.php?title=LAME#Recommended_encoder_setti$
# A good option is '-V 0' which gives Variable Bitrate Rate (VBR) recording
# with a target bitrate of ~245 Kbps and a bitrate range of 220...260 Kbps.
#LAMEOPTS=

{% endhighlight %}

I think I'll go with -V 0 then, like this:

{% highlight console %}

# MP3:
# For the best LAME encoder options have a look at:
# <http://wiki.hydrogenaudio.org/index.php?title=LAME#Recommended_encoder_setti$
# A good option is '-V 0' which gives Variable Bitrate Rate (VBR) recording
# with a target bitrate of ~245 Kbps and a bitrate range of 220...260 Kbps.
LAMEOPTS='-V 0'

{% endhighlight %}

### CD Database Options ###

# CDDB options

# Choose whether you want to use "cddb", "musicbrainz" and/or
# "cdtext". Default is "musicbrainz", but all can be specified in a
# comma delimited list to be tried sequentially. All the results will
# be displayed ready for user choice.
#CDDBMETHOD=musicbrainz
{% endhighlight %}

Maybe if I set this, it won't ask for which data source to use.  I set it to musicbrainz.


### MP3 Naming Options ###

{% highlight console %}
# Output filename format - change this to reflect your inner desire to
# organize things differently than everyone else :)
# You have the following variables at your disposal:
# OUTPUT, GENRE, ALBUMFILE, ARTISTFILE, TRACKFILE, TRACKNUM and YEAR.
# Make sure to single-quote this variable. abcde will automatically create
# the directory portion of this filename.
# NOTICE: OUTPUTTYPE has been deprecated in the OUTPUTFORMAT string.
# Since multiple-output was integrated we always append the file type
# to the files. Remove it from your user defined string if you are getting
# files like ".ogg.ogg".
#OUTPUTFORMAT='${ARTISTFILE}-${ALBUMFILE}/${TRACKNUM}.${TRACKFILE}'

{% endhighlight %}

So, what I have now is one folder for artists with multiple albums under it, so I'm going to do this:

{% highlight console %}
OUTPUTFORMAT='${ARTISTFILE}/${ALBUMFILE}/${TRACKNUM}.${TRACKFILE}'
{% endhighlight %}

### Album Art ###

I want album art to be downloaded and saved as folder.jpg. Here's what I have so far:

{% highlight console %}
# album art download options (see glyrc's help for details with more detailed
# examples here: https://github.com/sahib/glyr/wiki/Commandline-arguments).
# For example use '--formats jpg;jpeg' to only search for JPEG images
# These options: '--from <provider>' and '--lang <langcode>' might also be usef$
#GLYRCOPTS=
ALBUMARTFILE="folder.jpg"
ALBUMARTTYPE="JPEG"
{% endhighlight %}

Then, adding getting album art as a step here:

{% highlight console %}
# Actions to take
# Comma-separated list of one or more of the following:
#  cddb,cue,read,normalize,encode,tag,move,replaygain,playlist,getalbumart,embe$
#   encode implies read
#   normalize implies read
#   tag implies cddb,read,encode
#   move implies cddb,read,encode,tag
#   replaygain implies cddb,read,encode,tag,move
#   playlist implies cddb
#   embedalbumart implies getalbumart
# An action can be added to the "default" action by specifying it along with
# "default", without having to repeat the default ones:
#  ACTIONS=default,playlist
# The default action list (referenced as "default") is defined in the following
# comment:
ACTIONS=default,getalbumart
{% endhighlight %}
## Creating a RAM Drive for the WAV Output ##

I added this line to my /etc/fstab:

{% highlight console %}
tmpfs /var/tmp tmpfs nodev,nosuid,size=825M 0 0
{% endhighlight %}

Then, I did this:

{% highlight console %}
pi@raspberrypi:~/rip $ sudo mount -a
{% endhighlight %}

Then, I changed this line in the abcde config file:
{% highlight console %}
# Or if you'd just like to put the temporary .wav files somewhere else
# you can specify that here
WAVOUTPUTDIR=/var/tmp
{% endhighlight %}

Now, I'm going to see if this speeds things up by doing this:

{% highlight console %}
pi@raspberrypi:~/rip $ time abcde
{% endhighlight %}

Before and after the change to see the difference.

Using the RAM FS for WAV output:

{% highlight console %}
real    8m14.335s
user    3m25.624s
sys     0m24.581s
{% endhighlight %}

And without:

{% highlight console %}
real    8m18.065s
user    3m25.997s
sys     0m26.399s
{% endhighlight %}

Well, no real difference for a loss of about 800MB of RAM.

## Fingerprinting MP3 Files ##

I've got a lot of CDs that are copies and it just can't figure out what they are.

Maybe an MP3 fingerprinting utility can help?

I'm looking [here](https://github.com/d99kris/idntag).

To install it I try the following:

{% highlight console %}
sudo apt install git cmake mp3info python3-pip libtag1-dev libchromaprint-dev ffmpeg
{% endhighlight %}

Which works, and installs a lot of stuff...

Then I do this:
{% highlight console %}
pip3 install pyacoustid pytaglib
{% endhighlight %}

Now this:

{% highlight console %}
git clone https://github.com/d99kris/idntag && cd idntag
{% endhighlight %}

And this:

{% highlight console %}
mkdir -p build && cd build && cmake .. && make -s
{% endhighlight %}

and then this:

{% highlight console %}
ctest --output-on-failure
{% endhighlight %}

Which produces this:
{% highlight console %}
Test project /home/pi/idntag/build
    Start 1: test001
1/4 Test #1: test001 ..........................   Passed    5.43 sec
    Start 2: test002
2/4 Test #2: test002 ..........................   Passed   12.81 sec
    Start 3: test003
3/4 Test #3: test003 ..........................***Failed    1.86 sec
"FAIL" != "OK"
"web service error (response is not valid JSON)" != "/tmp/tmp.qtvGtcv8WR/song.mp3"

    Start 4: test004
4/4 Test #4: test004 ..........................   Passed   17.86 sec

75% tests passed, 1 tests failed out of 4

Total Test time (real) =  37.98 sec

The following tests FAILED:
          3 - test003 (Failed)
Errors while running CTest
{% endhighlight %}

Eh, I'm going to ignore it.

Finally this:

{% highlight console %}
sudo make install
{% endhighlight %}

Then, I find an unknown MP3 and:
{% highlight console %}
pi@raspberrypi:/mnt/nas/Tessa CD Imports/Unknown_Artist/Unknown_Album $ idntag 01.Track_1.mp3
/mnt/nas/Tessa CD Imports/Unknown_Artist/Unknown_Album/01.Track_1.mp3 : Traceback (most recent call last):
  File "/usr/local/bin/idntag", line 94, in <module>
    main()
  File "/usr/local/bin/idntag", line 90, in main
    identify_and_update_file(path, args.keepname)
  File "/usr/local/bin/idntag", line 53, in identify_and_update_file
    song.save()
  File "src/taglib.pyx", line 122, in taglib.File.save
OSError: Unable to save tags: file is read-only
{% endhighlight %}

Oops, trying sudo...
{% highlight console %}
pi@raspberrypi:/mnt/nas/Tessa CD Imports/Unknown_Artist/Unknown_Album $ sudo idntag 01.Track_1.mp3
Traceback (most recent call last):
  File "/usr/local/bin/idntag", line 8, in <module>
    import acoustid
ModuleNotFoundError: No module named 'acoustid'

{% endhighlight %}

Hmm, maybe sudo pip3 install acoustid?

Maybe, but I copied the file and got it to work. Sadly, pyacoustid (the library we
use to identify songs) doesn't return the album as well.

Maybe I can figure out what the album is from the artist and song, then copy and rename the thing to a proper directory structure and completely fill out the ID3 tags.

## Resources ##

[SteveB's Guide](http://www.questions4steveb.co.uk/html/Raspberry_Pi/Pi-CD-auto-Rip)
[Peter Saffrey's Attempt](https://psaffrey.wordpress.com/2013/03/27/media-server-odyssey-part-4-autorip/)
[Creating a RAM drive on a Raspberry Pi](https://www.domoticz.com/wiki/Setting_up_a_RAM_drive_on_Raspberry_Pi)

