---
layout: post
title: How to Use Regular Expressions in Python
date: 2020-08-02 21:54
categories: how-to python regex
---

## Introduction ##

I've recently had to do a lot of string searching and replacement with Python. Regular expressions are the most
powerful tool available to find and replace data. 

Here's how I've been using them.

## Finding Matches to a Regular Expression ##

One of the most fundamental things to do with regular expressions is to find text that matches the regular 
expression. My favorite way to do that in Python with the regular expression library is *findall*. Here's an
example of looking for the string 'hello':

{% highlight python %}

import re

searchString = "Hello. My name is Inigo Montoya.You killed my father. Prepare to die. Say hello to my little friend."

matchList = re.findall("[Hh]ello", searchString)

print(str(matchList))

{% endhighlight %}

That produces this output:

{% highlight console %}

['Hello', 'hello']

{% endhighlight %}

So, it found the two hellos (one capitalized, one not). *findall* is great because it just returns a list of the 
matches and not any silly RE match object trickery.

## Replacing Text Matching a Regular Expression ##

Replacing text is accomplished via a function called *sub*. *sub* is great because it takes in the original string
and returns the modified string. It's not so awesome because it requires two steps to work, as we can see in this
example:

{% highlight python %}

import re

replaceString="Hello. My name is Inigo Montoya. You killed my father. Prepare to die. Say hello to my little friend."

helloRe = re.compile("[Hh]ello")
subbedString=helloRe.sub("Bonjour",replaceString)
print(subbedString)

{% endhighlight %}

That produces this output:
{% highlight console % }
Bonjour. My name is Inigo Montoya. You killed my father. Prepare to die. Say Bonjour to my little friend
{% endhighlight %}


