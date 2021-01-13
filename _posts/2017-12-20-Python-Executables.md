---
layout: post
title:  "How To Turn Python Scripts into Windows Executables"

date:   2017-12-20 10:19
categories: how-to python exe
---

Python scripts are useful and easy - but only if you have the Python interpreter installed on your PC. If not, you can't run them. 

The first way around this that I used was called Py2Exe. It was a bit kludgy, but worked well enough at a time when there weren't many options. 

Despite my best efforts, time moved on and now we have more options for turning Python scripts into executables. 

One good such option is PyInstaller, which seems to be very straightforward and has a (so far) great one-file packaging option. It produced a ~6MB exe 
for a simple CLI script that does nothing, but who cares about disk usage these days anyway?

## PyInstaller ##

PyInstaller seems to be a much more straightforward means of getting an
exe from a Python script. I didn't have to muck around with any setup.py
files or options or anything, just a simple command line. And, I got a single
executable very easily. 

The [webpage](https://www.pyinstaller.org/) for PyInstaller has a pretty straightfoward set of instructions
for installing and using PyInstaller. It got me up and running right away.

### Installation ###

Here's what I did and what happened:

{% highlight console %}
C:\Users\sfrie\Dropbox\Projects\pyCliScript>pip install pyinstaller
Collecting pyinstaller
  Downloading pyinstaller-4.1.tar.gz (3.5 MB)
     |████████████████████████████████| 3.5 MB 3.3 MB/s
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Requirement already satisfied: pywin32-ctypes>=0.2.0 in c:\users\sfrie\appdata\local\programs\python\python38-32\lib\site-packages (from pyinstaller) (0.2.0)
Requirement already satisfied: setuptools in c:\users\sfrie\appdata\local\programs\python\python38-32\lib\site-packages (from pyinstaller) (41.2.0)
Requirement already satisfied: pefile>=2017.8.1 in c:\users\sfrie\appdata\local\programs\python\python38-32\lib\site-packages (from pyinstaller) (2019.4.18)
Requirement already satisfied: future in c:\users\sfrie\appdata\local\programs\python\python38-32\lib\site-packages (from pefile>=2017.8.1->pyinstaller) (0.18.2)
Collecting pyinstaller-hooks-contrib>=2020.6
  Downloading pyinstaller_hooks_contrib-2020.11-py2.py3-none-any.whl (172 kB)
     |████████████████████████████████| 172 kB 3.3 MB/s
Collecting altgraph
  Downloading altgraph-0.17-py2.py3-none-any.whl (21 kB)
Building wheels for collected packages: pyinstaller
  Building wheel for pyinstaller (PEP 517) ... done
  Created wheel for pyinstaller: filename=pyinstaller-4.1-py3-none-any.whl size=2790249 sha256=efab815c03c325d415b697dbe2631a2629870cd0e0b5755402bca074c6fc8c13
  Stored in directory: c:\users\sfrie\appdata\local\pip\cache\wheels\ae\7a\1e\e42202ec16f036e6c25592c6bc63d3c26e6a6addd6a25f053a
Successfully built pyinstaller
Installing collected packages: pyinstaller-hooks-contrib, altgraph, pyinstaller
Successfully installed altgraph-0.17 pyinstaller-4.1 pyinstaller-hooks-contrib-2020.11
{% endhighlight %}


### Generating an Executable ###

After that, it's a simple command-line to generate an executable:

{% highlight console %}
C:\Users\sfrie\Dropbox\Projects\pyCliScript>pyinstaller --onefile src\pyCli.py
161 INFO: PyInstaller: 4.1
161 INFO: Python: 3.8.2
165 INFO: Platform: Windows-10-10.0.18362-SP0
167 INFO: wrote C:\Users\sfrie\Dropbox\Projects\pyCliScript\pyCli.spec
172 INFO: UPX is not available.
187 INFO: Extending PYTHONPATH with paths
['C:\\Users\\sfrie\\Dropbox\\Projects\\pyCliScript\\src',
 'C:\\Users\\sfrie\\Dropbox\\Projects\\pyCliScript']
216 INFO: checking Analysis
217 INFO: Building Analysis because Analysis-00.toc is non existent
219 INFO: Initializing module dependency graph...
225 INFO: Caching module graph hooks...
255 INFO: Analyzing base_library.zip ...
4466 INFO: Processing pre-find module path hook distutils from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
4468 INFO: distutils: retargeting to non-venv dir 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib'
8048 INFO: Caching module dependency graph...
8305 INFO: running Analysis Analysis-00.toc
8335 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by c:\users\sfrie\appdata\local\programs\python\python38-32\python.exe
8483 INFO: Analyzing C:\Users\sfrie\Dropbox\Projects\pyCliScript\src\pyCli.py
8489 INFO: Processing module hooks...
8490 INFO: Loading module hook 'hook-difflib.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8493 INFO: Excluding import of doctest from module difflib
8493 INFO: Loading module hook 'hook-distutils.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8498 INFO: Loading module hook 'hook-distutils.util.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8501 INFO: Excluding import of lib2to3.refactor from module distutils.util
8501 INFO: Loading module hook 'hook-encodings.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8644 INFO: Loading module hook 'hook-heapq.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8649 INFO: Excluding import of doctest from module heapq
8650 INFO: Loading module hook 'hook-lib2to3.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8720 INFO: Loading module hook 'hook-multiprocessing.util.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8723 INFO: Excluding import of test from module multiprocessing.util
8723 INFO: Excluding import of test.support from module multiprocessing.util
8724 INFO: Loading module hook 'hook-pickle.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8727 INFO: Excluding import of argparse from module pickle
8729 INFO: Loading module hook 'hook-sysconfig.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8731 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8732 INFO: Loading module hook 'hook-xml.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
8824 INFO: Loading module hook 'hook-_tkinter.py' from 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks'...
9018 INFO: checking Tree
9018 INFO: Building Tree because Tree-00.toc is non existent
9019 INFO: Building Tree Tree-00.toc
9114 INFO: checking Tree
9115 INFO: Building Tree because Tree-01.toc is non existent
9116 INFO: Building Tree Tree-01.toc
9233 INFO: checking Tree
9233 INFO: Building Tree because Tree-02.toc is non existent
9234 INFO: Building Tree Tree-02.toc
9285 INFO: Looking for ctypes DLLs
9339 INFO: Analyzing run-time hooks ...
9344 INFO: Including run-time hook 'c:\\users\\sfrie\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_multiprocessing.py'
9357 INFO: Looking for dynamic libraries
9629 INFO: Looking for eggs
9629 INFO: Using Python library c:\users\sfrie\appdata\local\programs\python\python38-32\python38.dll
9630 INFO: Found binding redirects:
[]
9637 INFO: Warnings written to C:\Users\sfrie\Dropbox\Projects\pyCliScript\build\pyCli\warn-pyCli.txt
9747 INFO: Graph cross-reference written to C:\Users\sfrie\Dropbox\Projects\pyCliScript\build\pyCli\xref-pyCli.html
9763 INFO: checking PYZ
9764 INFO: Building PYZ because PYZ-00.toc is non existent
9765 INFO: Building PYZ (ZlibArchive) C:\Users\sfrie\Dropbox\Projects\pyCliScript\build\pyCli\PYZ-00.pyz
10541 INFO: Building PYZ (ZlibArchive) C:\Users\sfrie\Dropbox\Projects\pyCliScript\build\pyCli\PYZ-00.pyz completed successfully.
10569 INFO: checking PKG
10570 INFO: Building PKG because PKG-00.toc is non existent
10572 INFO: Building PKG (CArchive) PKG-00.pkg
12661 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
12665 INFO: Bootloader c:\users\sfrie\appdata\local\programs\python\python38-32\lib\site-packages\PyInstaller\bootloader\Windows-32bit\run.exe
12666 INFO: checking EXE
12667 INFO: Building EXE because EXE-00.toc is non existent
12668 INFO: Building EXE from EXE-00.toc
12673 INFO: Updating manifest in C:\Users\sfrie\Dropbox\Projects\pyCliScript\build\pyCli\run.exe.8k18prc5
12928 INFO: Updating resource type 24 name 1 language 0
12938 INFO: Appending archive to EXE C:\Users\sfrie\Dropbox\Projects\pyCliScript\dist\pyCli.exe
13214 INFO: Building EXE from EXE-00.toc completed successfully.
{% endhighlight %}

This produced dist/pyCli.exe - one file only!

I'm kind of sad how easy that was.

## Py2Exe - Deprecated ##

You probably shouldn't even bother reading any of this, but it's retained here for completeness. Also, maybe it'll be useful someday. Who knows.

It's worth noting that Py2Exe only works on Windows with Windows Python - not Cygwin Python.

### Installation ###

You'll need Python 2.7 for Windows installed before you can do install Py2Exe. 

Installation is as simple as opening a command prompt and typing:

> pip install py2exe

Alternately, you can go online and download it form [SourceForge](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download) and then use the installer to install it.

### Usage ###

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

### Generating a Single Executable File ###

Normally, when using Py2Exe, it will generate a big directory of miscellaneous files that are kinda messy alongside the executable you want.
There's a way you can slim it all down to just one executable file.

[This](http://www.py2exe.org/index.cgi/ListOfOptions) site discusses the options that you can pass to py2exe when you invoke it. The script that generates a single executable is here:

{% highlight python %}
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'optimize': 2,'bundle_files':1}},
    console=['src/pyCli.py']
    )
{% endhighlight %}



### Issues ###

#### Missing Modules ####

I have more complex scripts that I want to turn into executables. These scripts import Python files that are present in the same directory. Py2Exe cannot seem to find these files and include them into the executable which means that the EXE will not work. The way to fix this is to alter the system path from within the *setup.py* script to add the path to the modules you want to import. For example, if the files are in the *src* subdirectory of the project directory, then you can modify the *setup.py* script as follows:

{% highlight python %}
from distutils.core import setup
import py2exe
import sys
sys.path.insert(0,'./src')
setup(console=['src/pcApp.py'])
{% endhighlight %}

Once done, the script finds all of my custom modules, imports them and the EXE runs fine.

#### Dropbox, Virus Scanners, and WinError 110 ####

Sometimes, you'll get an error like this:

{% highlight console %}
error: [WinError 110] The system cannot open the device or file specified.
{% endhighlight %}

This sort of error is caused by another program trying to access the files that py2exe is trying to access. Usually, this is an antivirus program or (in my case) Dropbox. I remedied this error by turning off Dropbox or by moving the folder outside of my Dropbox folder.

## Resources ##

* [Py2Exe Tutorial](http://www.py2exe.org/index.cgi/Tutorial)




