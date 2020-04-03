---
layout: post
title:  "How To Validate IP addresses in Python"
updated: 2020-03-12 9:25
date:   2020-03-12 9:25
categories: how-to python ip
---


Validating input is always important - you don't want random errors popping up when you try to directly insert user-inputted data into your functions.

Python has lots of built-in validation. For example, if you're expecting a number, you can do something like this:

{% highlight python %}
    try:
        intVariable = int(stringVariable)
    except ValueError:
        print "That was not a number. Try again"
        
{% endhighlight %}

It's very straightforward to validate built-in types in Python, but an IP address is just a string in Python - and any string is a valid string.

We need a way to ensure that it's a valid IP address.  Here's how:

{% highlight console %}

import socket

try:
    socket.inet_aton(stringVariable)
except socket.error:
    print "That was not a valid IP address"
    
{% endhighlight %}

This is the Python 2 version of how to do it. *Apparently* Python 2 is *deprecated* or something because we have this fancy new Python 3, which, incidentally, has a built-in IP address type.

You can do the same thing in Python 3 like this:

{% highlight console %}
import ipaddress

try:
    myIpAddress = IPv4Address(stringVariable)
except ValueError:
    print "That was not a valid IP address"
    
{% endhighlight %}

## Resources ##
* [Python IP Address Library Documentation](https://docs.python.org/3/library/ipaddress.html)
* [Relevant Stackoverflow Answer](https://stackoverflow.com/a/3462840)
