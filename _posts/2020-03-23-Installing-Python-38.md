---
layout: post
title:  "Installing Python 3.8"
updated: 2020-03-23 21:47
date:   2020-03-23 21:47
categories: how-to python python3

---

## Introduction ##

Python 2 has been discontinued. Python 3 is its replacement, and as of the writing of this article Python 3.8.2 is the latest version.

This article shows you how to install Python 3. Once this has been done to my computer, it will mark the first time in quite a while
that my computer has not had a Python 2 installation. Probably a decade at least.

Farewall Python 2.

## Downloading the Installer #

The installer for Python 3.8.2 can be found [here](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe).

The overall download page for the latest version of Python 3 is [here](https://www.python.org/downloads/).

## Installing Python 3.8.2 ##

1. On the Initial Screen, check the box labeled 'Add Python 3 to PATH'. Then click 'Install Now'
![Initial install screen]({{site.basepath}}/img/2020-03-23 22_18_34-Python 3.8.2 Setup.png)
2. If a UAC dialog shows up, allow the program to make changes
3. Wait while it installs
![Installing]({{site.basepath}}/img/2020-03-23 22_21_15-Python 3.8.2 Setup.png)
4. Once installation was finished, I opted to disable the path length limit.
![Optional PATH Modification]({{site.basepath}}/img/2020-03-23 22_22_04-Python 3.8.2 Setup.png)
5. Agree to the UAC dialog that comes up after clicking the above button.
6. That's it. Click 'Close'
![Finished]({{site.basepath}}/img/2020-03-23 22_23_34-Python 3.8.2 Setup.png)

## Installation Verification ##

To verify the install, do the following:

1. Open a Command Prompt
2. Type 'python' and verify the output below shows up:

{% highlight console %}
Microsoft Windows [Version 10.0.18362.535]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\sfrie>python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

{% endhighlight %}

## Resources ##

* [Download Python - Latest Version](https://www.python.org/downloads/)
* [Python 3.8.2 Installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)
