---
layout: post
title:  "How-to Access the Windows Clipboard with Python"
date:   2020-07-14 8:58
updated: 2020-07-14 8:58
categories: how-to python3 clipboard
---

## Introduction ##

I'm writing a script to generate some text that I would need to copy and paste into a form on a 
website. Wouldn't it be easier if Python could copy the text to the clipboard directly and save me a click?

This will be done on a Windows 10 PC with Python 3 (3.8.1 specifically).

## Required Libraries ##

It seems that this is not nearly as straightforward as I thought it might be. This seems largely to do
with the fact that I want to do it on Windows as opposed to (possibly) Linux. The first result from Google
forwards me to a [big ol' list](https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python) of things I can try which seem somewhat involved. I don't really want to 
install TKinter in order to just get the clipboard.

The first result seems to have a straightforward [answer](https://stackoverflow.com/a/11063483/39492): use Pyperclip.

Hopefully this is something that pip can install for me. Let's try.

I did the following:

{% highlight console %}

C:\Users\sfrieder>pip3 install pyperclip
Collecting pyperclip
  Downloading https://files.pythonhosted.org/packages/f6/5b/55866e1cde0f86f5eec59dab5de8a66628cb0d53da74b8dbc15ad8dabda3/pyperclip-1.8.0.tar.gz
Installing collected packages: pyperclip
  Running setup.py install for pyperclip ... done
Successfully installed pyperclip-1.8.0
{% endhighlight %}

Whew! That was easy.

## Copying Text to the Clipboard ##

The SO answer from above has this code snippet:

{% highlight python %}

import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')
spam = pyperclip.paste()
{% endhighlight %}

I pasted that into a new Python script, ran it, and was able to paste the contents of the clipboard and
verify that it was the copied string. 

Bueno!

## Retrieving Text From the Clipboard ##

I'm guessing it's as easy as the 'paste' command seen in the previous script. I didn't check the result
of the paste command, so we'll add a print statement to see. Here's what the script looks like now:

{% highlight python %}

import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')
spam = pyperclip.paste()

print(str(spam))

{% endhighlight %}

And this script produces the following:

{% highlight console %}
The text to be copied to the clipboard.
{% endhighlight %}

Looks right to me!

## Resources ##

[Useful SO answer on how to copy text to the clipboard](https://stackoverflow.com/a/11063483/39492)
