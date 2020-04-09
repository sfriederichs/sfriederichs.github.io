---
layout: post
title:  "How To Document Python Code With Docstrings"
updated: 2017-12-29 21:44
date:   2017-12-29 21:44
categories: how-to python dox
---

Have you ever used a tool, loved it, and even found it completely invaluable and then one day someone sees you use it and says "Why are you holding it upside down?"

It turns out that I just had a moment like that with Python. It wasn't a complete Worse Than Failure (WTF) situation, but finally seeing how I'd been misusing Python definitely made me a bit embarrassed. Luckily, no one was watching (until I posted it on the internet). To showcase my ignorance, take a look at this snippet of Python code:

{% highlight python %}

# This is a python comment, obviously.

"""
And this is also a comment... but a different one? I guess this
is just what a multi-line comment looks like in Python,
right?
"""

def thisIsTheCode():
	""" 
	I mean, I see these comments all over the place, but surely
	the difference in comment usage is just a matter of style, right?
	"""
	
	#No idea man, no idea.
	
	#Empty function 
	#(Made you look!)
	pass
	
{% endhighlight %}

It turns out that those two 'styles' of comments are not equivalent. The lines that start with the pound symbol *are* Python comments and they function just like comments do in C or C++. The ones that start with three double quotes have no direct analogue in C or C++ - they're called  [docstrings](https://en.wikipedia.org/wiki/Docstring#Python). Like comments, they aren't functional - merely informative. However, they can be accessed programmatically by the Python script itself. This means that you could, for example, document the operation of a Python script (its command-line parameters for example) within the script itself and have the script print that information to tell the user how to use the script. An example is seen below:


{% highlight python %}

"""
Python Docstring Example v0.1
Author: Stephen Friederichs
This script demonstrates the use of docstrings versus conventional Python comments.
It also has other wicked awesome things going on like automatic text wrapping and command-line argument handling
The following command-line parameters control the behavior of the script:
-h, --help - Shows this screen and exits
-a, --functiona - Shows the docstring for *funcA*
-b, --functionb - Shows the docstring for *funcB*
"""

import textwrap
import getopt
import sys

def prettyPrint(uglyString):
	"""This function properly fomats docstrings for printing on the console"""
	
	#Remove all newlines
	uglyString = uglyString.replace('\n','').replace('\r','')
	#Use textwrap module to automatically wrap lines at 79 characters of text
	print textwrap.fill(uglyString,width=79)
	

def funcA():
	"""Function A (funcA): This function accepts no inputs, returns no outputs and does no work"""
	pass

def funcB():
	"""Function B (funcB): This function is just as lazy and useless as funcA"""
	pass
	
def help():
	for line in __doc__.splitlines()[3:]:
		prettyPrint(line)
	
def version():
	for line in __doc__.splitlines()[1:3]:
		prettyPrint(line)
		
version()

try: 
	opts, args = getopt.getopt(sys.argv[1:], 'hab', ['help','functiona','functionb'])    
except getopt.GetoptError:
	print "Bad argument(s)"     
	sys.exit(2)                 

for opt, arg in opts:                 
	if opt in ('-h', '--help'):     
		help()                         
		sys.exit(2)                 
	elif opt in ('-a','--functiona'):    
		prettyPrint(funcA.__doc__)
	elif opt in ('-b','--functionb'):
		prettyPrint(funcB.__doc__)
	else: 
		help()
		sys.exit(2)

{% endhighlight %}

### Regular Output ###

If you supply no command-line switches, you get this output:

> Python Docstring Example v0.1  
> Author: Stephen Friederichs  

### Help Output ###

This is what you get when you use -h or --help on the script:

> Python Docstring Example v0.1  
> Author: Stephen Friederichs  
> This script demonstrates the use of docstrings versus conventional Python  
> comments.  
> It also has other wicked awesome things going on like automatic text wrapping  
> and command-line argument handling  
> The following command-line parameters control the behavior of the script:  
> -h, --help - Shows this screen and exits  
> -a, --functiona - Shows the docstring for *funcA*  
> -b, --functionb - Shows the docstring for *funcB*  

### Function A Output ###

Here's the output for Function A:

> Python Docstring Example v0.1  
> Author: Stephen Friederichs  
> Function A (funcA): This function accepts no inputs, returns no outputs and   
> does no work  

### Function B Output ###

This is what -b or --functionb produces:

> Python Docstring Example v0.1  
> Author: Stephen Friederichs  
> Function B (funcB): This function is just as lazy and useless as funcA  

## Docstrings and Doxygen ##

Doxygen is my go-to code documentation generator for C and C++, but I've never tried it with Python. It turns out there's one significant limitation to Doxygen with Python: it can't read all Doxygen markup from Python docstrings (it *can* read all markup within regular Python comments). It would be very desirable to be able to embed Doxygen markup in the very-useful Docstring, so luckily there's a way to do it. The [doxypy Python package](https://pypi.python.org/pypi/doxypy/) contains a script which can be used as an input filter for Doxygen and allows Doxygen markup within Docstrings. I haven't done this yet, but there are links in the Resources section below which I'm going to try out once I have the need.

## Resources ##

* [Wikipedia Docstring Article - Python](https://en.wikipedia.org/wiki/Docstring#Python)
* [Embedding Doxygen Markup in Python Docstrings](https://stackoverflow.com/a/497322)
* [doxypy Package Page](https://pypi.python.org/pypi/doxypy/)
* [Using doxypy for Python Documentation - Greg Smith's Note Magnet](http://notemagnet.blogspot.com/2009/10/using-doxypy-for-python-code.html)
* [Stackoverflow - How can I print a Python file's docstring when executing it?](https://stackoverflow.com/questions/7791574/how-can-i-print-a-python-files-docstring-when-executing-it)


