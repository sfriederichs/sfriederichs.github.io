---
layout: post
title:  "How To Turn Python Scripts into Windows Executables"
updated: 2017-12-20 10:19
date:   2017-12-20 10:19
categories: how-to python exe
---

Python scripts are useful and easy - but only if you have the Python interpreter installed on your PC. If not, you can't run them. The way around this is to turn your Python scripts into self-contained executables via Py2Exe.

It's worth noting that Py2Exe only works on Windows with Windows Python - not Cygwin Python.

## Installation ##

You'll need Python 2.7 for Windows installed before you can do install Py2Exe. 

Installation is as simple as opening a command prompt and typing:

> pip install py2exe

Alternately, you can go online and download it form [SourceForge](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download) and then use the installer to install it.

## Usage ##

First, you need a script to turn into an executable:

{% highlight python %}

print "Hello World!"

{% endhighlight %}

Well, that was easy. I'm going to store that script in a subdirectory of my project directory called 'src', so it'll be at the relative path 'src/helloWorld.py'.

This isn't the only script you need. You'll also need a *setup.py* script which has content that looks like this:

{% highlight python %}

from distutils.core import setup
import py2exe

setup(console=['src/helloWorld.py'])
{% endhighlight %}

This script acts as a wrapper which allows Py2Exe to turn your script into an executable.

On the command line, you can generate the executable by navigating to the project directory and typing:

> python setup.py py2exe

This produces a lot of output on the console, but more importantly will produce two directories: *build* and *dist*.  

*build* contains temporary and leftover files used in the build. I've had no problem deleting it after a build. The *dist* folder contains everything your EXE needs to operate. The upshot is that if you want to move the EXE to another system, you need to copy everything in the *dist* folder to the new system and keep the directory structure in that folder intact. The main output of this process is the *dist/helloWorld.exe* file: the executable name matches the name of the Python script.

Once you run that executable, you'll get the output you expect:

> Hello World!

## Issues ##

### Missing Modules ###

I have more complex scripts that I want to turn into executables. These scripts import Python files that are present in the same directory. Py2Exe cannot seem to find these files and include them into the executable which means that the EXE will not work. The way to fix this is to alter the system path from within the *setup.py* script to add the path to the modules you want to import. For example, if the files are in the *src* subdirectory of the project directory, then you can modify the *setup.py* script as follows:

{% highlight python %}
from distutils.core import setup
import py2exe
import sys
sys.path.insert(0,'./src')
setup(console=['src/pcApp.py'])
{% endhighlight %}

Once done, the script finds all of my custom modules, imports them and the EXE runs fine.
## Resources ##

* [Py2Exe Tutorial](http://www.py2exe.org/index.cgi/Tutorial)




