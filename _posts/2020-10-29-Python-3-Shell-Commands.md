---
layout: post
title: How-To Execute Shell Commands in Python 3
date: 2020-10-29 10:38
categories: python3 shell
---

## Introduction ##

Shell automation (i.e., scripting/batching things on the command-line) is a heck of a time-saving practice.
While I'm great at making command-line scripts in Python, there are a bunch of other command-line tools
that I could be accessing from within Python to make my scripts even more effective. 

This article will detail how to execute command-line/shell commands from within Python scripts.

## Executing Shell Commands Within a Python Script ##

There are two main ways to execute shell commands: using os.system and using subprocesses.

Using os.system is quick and effective for some situations, but using subprocesses allows you much more control of the whole process.

### os.system Approach ###

The easiest way suggested by my one resource is to use the os.system module, like this:

{% highlight python %}

import os
os.system('ls -l')
{% endhighlight %}

You can't get the output of the script as a variable or anything else cool with this approach, but it's all I need for now.

### SubProcess Approach ###

When I need this approach, I'll document it. For now, you can just look at the site in Resources for all of the information.


## Resources ##

[How to Execute Shell Commands with Python](https://janakiev.com/blog/python-shell-commands/)