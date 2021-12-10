---
layout: post
title: Solving the NPR Puzzle Programmatically - 1-31-21
date: 2021-02-01 19:46
categories: puzzle python
---

## Introduction ##

It's once again time to play the puzzle!

In case you're keeping score, I was NOT selected to play the puzzle on the air for my last
set of correct answers. There were a surprisingly large number of correct answers. I didn't
know there were so many Python programmers out there puzzling away /s.

This week's question is:

{% highlight text %}
Name a famous actor whose first name is a book of the Bible and
whose last name is an anagram of another book of the Bible. Who is it?
{% endhighlight %}

## Approach ##

I need to do a few things:

1. Get a list of famous actors
2. Split the name into first and last name
3. Generate all permutations of a last name
4. Check the first name and permutations of the last name against books of the Bible



### Generating Permutations of a Name ###

I know how to generate permutations of words from the last puzzle that I did. Here's the snippet:

{% highlight python %}
[''.join(p) for p in itertools.permutations(word)]
{% endhighlight %}

### Checking Names Against Books of the Bible ###

Now, I could be lame and just find a list of books of the Bible online and cut/paste it
into a string in my script.

Problem is, I spent a LOT of time last time reworking the regular expression to parse my
cut/pasted data, so I'm looking for any available data.

I found something: [python-scriptures](http://www.davisd.com/python-scriptures/). It's a library for identifying references to scripture within blocks of text. Looking through the 
documentation, I see something useful right away:

{% highlight text %}
book_re
~~~~~~~

Match a valid abbreviation or book name.

Examples:

    >>> import scriptures
    >>> import re
    >>> re.findall(scriptures.book_re, 'Matt test Ecclesiastes and 2 peter')
    ['Matt', 'Ecclesiastes', '2 peter'] 
{% endhighlight %}

So, all I have to do to find books of the Bible is run this regex against my string and see
if there are any matches. Perfect.

And it's so cool to have a Python library for this.

I installed python-scriptures by downloading the tar file from [here](https://pypi.org/project/python-scriptures/#files).

Then, I installed it like this:

{% highlight console %}
C:\Users\sfrie>cd Downloads

C:\Users\sfrie\Downloads>tar -zxf python-scriptures-3.0.0.tar.gz

C:\Users\sfrie\Downloads>cd python-scriptures-3.0.0

C:\Users\sfrie\Downloads\python-scriptures-3.0.0>python setup.py install
running install
running build
running build_py
creating build
creating build\lib
creating build\lib\scriptures
copying scriptures\bible_re.py -> build\lib\scriptures
copying scriptures\references.py -> build\lib\scriptures
copying scriptures\__init__.py -> build\lib\scriptures
creating build\lib\scriptures\texts
copying scriptures/texts\base.py -> build\lib\scriptures/texts
copying scriptures/texts\deuterocanon.py -> build\lib\scriptures/texts
copying scriptures/texts\kjv1611.py -> build\lib\scriptures/texts
copying scriptures/texts\protestant.py -> build\lib\scriptures/texts
copying scriptures/texts\__init__.py -> build\lib\scriptures/texts
running install_lib
creating C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures
copying build\lib\scriptures\bible_re.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures
copying build\lib\scriptures\references.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures
creating C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts
copying build\lib\scriptures\texts\base.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts
copying build\lib\scriptures\texts\deuterocanon.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts
copying build\lib\scriptures\texts\kjv1611.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts
copying build\lib\scriptures\texts\protestant.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts
copying build\lib\scriptures\texts\__init__.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts
copying build\lib\scriptures\__init__.py -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\bible_re.py to bible_re.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\references.py to references.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts\base.py to base.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts\deuterocanon.py to deuterocanon.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts\kjv1611.py to kjv1611.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts\protestant.py to protestant.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\texts\__init__.py to __init__.cpython-38.pyc
byte-compiling C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\scriptures\__init__.py to __init__.cpython-38.pyc
running install_data
copying LICENSE -> C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\.
running install_egg_info
Writing C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\python_scriptures-3.0.0-py3.8.egg-info

{% endhighlight %}

Next, I tested it by adding
{% highlight python %}
 'import scriptures' 
{% endhighlight %}
into my script and ran it to make sure it didn't error out. It didn't, so it's installed correctly. 

Then, I worked up this function:
{% highlight console %}
def getBibleBooksFromString(string):
    return re.findall(scriptures.book_re,string)
{% endhighlight %}

Pretty complicated huh? I tested it out like this:

{% highlight console %}
    string="Matt"
    books = getBibleBooksFromString(string)
    print(str(books))
{% endhighlight %}

And got this response:

{% highlight console %}
C:\Users\sfrie\Dropbox\Projects\pyPuzzle>python src\21-02-14.py
NPR Puzzle Script 2/14/21
2021-02-16 22:01:20,963 - MainThread - main  - DEBUG    Logging is configured - Log Level 10 , Log File: logs/log_22_01_16_02_2021.log
['Matt']
{% endhighlight %}

Seems to be working to me.

## Further Reading ##

## Resources ##

* [python-scriptures](https://pypi.org/project/python-scriptures/)
* [Generating all permutations of a string](https://stackoverflow.com/a/8306692/39492)
