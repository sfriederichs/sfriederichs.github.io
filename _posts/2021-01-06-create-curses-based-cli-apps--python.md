---
layout: post
title: How to Create Curses-Based CLI Apps With Python
date: 2021-01-06 22:30
categories: how-to cli python3 curses

---

## Introduction ##

I've been writing a lot of CLI-based Python apps lately, but they rely on 'print' statements and 'input' statements. This means there's lots of scrolling.
If you've ever used CLI programs before such as vi or nano, you don't see that sort of scrolling: the cursor just moves around the screen cleanly.
That's because they're written with a library called curses, or maybe ncurses. Understanding this dark magic will allow you to write similar applications
that look a bit more professional than the scrolly ones that I make.

## Installation ##

I'm starting off with the curses tutorial by DevDungeon found [here](https://www.devdungeon.com/content/curses-programming-python).

It tells me that on Windows I need to install the curses library by doing this:

{% highlight console %}

C:\Users\sfrie\Dropbox\Projects\pyCurses>python -m pip install windows-curses
Collecting windows-curses
  Downloading windows_curses-2.2.0-cp38-cp38-win32.whl (75 kB)
     |████████████████████████████████| 75 kB 5.5 MB/s
Installing collected packages: windows-curses
Successfully installed windows-curses-2.2.0

{% endhighlight %}


That was easy enough.


## Basic Curses Script ##

This is the most basic curses script that the tutorial uses:

{% highlight python %}

import curses

print("Preparing to initialize screen...")
screen = curses.initscr()
print("Screen initialized.")
screen.refresh()

curses.napms(2000)
curses.endwin()

print("Window ended.")
{% endhighlight %}

All this does is show a blank window for a few seconds, but it's a start!


## Resources ##

* [Python curses library documentation](https://docs.python.org/3/library/curses.html)
* [DevDungeon curses tutorial](https://www.devdungeon.com/content/curses-programming-python)
