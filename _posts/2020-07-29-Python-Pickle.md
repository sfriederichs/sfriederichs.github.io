---
layout: post
title:  "How-to Save Data in Python with Pickle"
date:   2020-07-29 8:58

categories: how-to python3 pickle serialization
---

## Introduction ##

There are times where you have some variable in Python that you need to persist between executions of the script. This data isn't being exported, it isn't being read by a human, 
it doesn't need to be portable, it just has to survive between executions and no one else needs it.

You seem to be in quite a pickle.

Haha, you see - that's what me and my countrymen call a joke. That's because there's a Python library called (for some reason) 'pickle' which lets you 
*serialize* and *deserialize* arbitrary data. Those super-serial words are just fancy talk for *save* and *load* for the purposes of this how-to.

So this article will show you how to use the pickle library to get yourself out of this... difficult situation.

This will be done on a Windows 10 PC with Python 3 (3.8.1 specifically).

## Required Libraries ##

*pickle* is the only required library and as far as I know, it comes standard with Python.

## Writing Serialized Data to a File ##

The basic examples from the website will work just fine:

{% highlight python %}

# Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }

pickle.dump( favorite_color, open( "save.p", "wb" ) )

{% endhighlight %}

## Reading Serialized Data from a File ##

Here's how they did it on the website:

{% highlight python %}

# Load the dictionary back from the pickle file.
import pickle

favorite_color = pickle.load( open( "save.p", "rb" ) )
# favorite_color is now { "lion": "yellow", "kitty": "red" }
{% endhighlight %}

## Pickling Multiple Variables at Once ##

It didn't take long before I figured out a wrinkle: I need to pickle multiple variables into one file and ensure that they get back into their proper variables when loaded. 
How do I do that?

[This](https://stackoverflow.com/a/34676949/39492) StackOverflow answer provides the answer: just dump them in order, then load them in order. Pickle will handle the rest.

Here's the code they wrote:

{% highlight python %}

>>> import pickle
>>> fruits = dict(banana=0, pear=2, apple=6)
>>> snakes = ['cobra', 'viper', 'rattler']
>>> with open('stuff.pkl', 'wb') as f:
...   pickle.dump(fruits, f)
...   pickle.dump(snakes, f)
... 
>>> with open('stuff.pkl', 'rb') as f:
...   food = pickle.load(f)
...   pets = pickle.load(f)
... 
>>> food
{'pear': 2, 'apple': 6, 'banana': 0}
>>> pets
['cobra', 'viper', 'rattler']
>>> 
{% endhighlight %}

## Resources ##

* [Pickle Library Documentation](https://docs.python.org/3/library/pickle.html)
* [Python - Using Pickle](https://wiki.python.org/moin/UsingPickle)
* [Pickling multiple objects at once](https://stackoverflow.com/a/34676949/39492)