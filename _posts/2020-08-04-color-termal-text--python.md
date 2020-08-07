---
layout: post
title: How to Color Terminal Text in Python
date: 2020-08-04 14:33
categories: python cli 
---

## Introduction ##

If you've ever worked with some fany command-line tools, you might have seen some colored 
text in there - maybe for a warning or error message or somesuch. It certainly can help
in reading comprehension in some situations, so how can we do it in Python?

Specifically, Python 3.8.5 on a Windows 10 machine.

## Coloring Terminal Text in Python ##

The library that is recommended (especially for cross-platform use) is [Colorama](https://pypi.python.org/pypi/colorama). [This](https://stackoverflow.com/a/3332860/39492) StackOverflow answer suggested its use.

### Installing Colorama ###

Colorama didn't come pre-installed, but pip saved me:

{% highlight console %}

C:\Users\sfrieder>pip3 install colorama
Collecting colorama
  Downloading https://files.pythonhosted.org/packages/c9/dc/45cdef1b4d119eb96316b3117e6d5708a08029992b2fee2c143c7a0a5cc5/colorama-0.4.3-py2.py3-none-any.whl
Installing collected packages: colorama
Successfully installed colorama-0.4.3
{% endhighlight %}


### Coloring 'print' Statements Example ###

This Python 3 snippet will color text for you:

{% highlight python %}
import colorama

colorama.init()

print(colorama.Fore.RED + "This is red text")
print("This is still red text")
print(colorama.Style.RESET_ALL) #This prints a newline FYI!
print("Now this is normal text")
print(colorama.Back.GREEN + "Now the background of this text is green")
print(colorama.Fore.RED + "And the text is red on a green background, this clashes so bad!")
print(colorama.Style.DIM + "It's now also... dimmed? What's that?")
print(colorama.Style.RESET_ALL)
print("Thank goodness, back to normal")
{% endhighlight %}

And it produces this output:
{% highlight console %}

This is red text
This is still red text

Now this is normal text
Now the background of this text is green
And the text is red on a green background, this clashes so bad!
It's now also... dimmed? What's that?

Thank goodness, back to normal
{% endhighlight %}

Eh... trust me. It's colored. I cannot figure out how to get that to come through here, but it is I swear!

### Coloring 'input' Statements Example ###

If you do something like this:

{% highlight python %}

import colorama

colorama.init()
answer=input(colorama.Fore.RED + "This is a dire question, so it is colored red. What is your name?" + colorama.Style.RESET_ALL)

{% endhighlight %}

You do NOT get a red colored question prompt. You get gobbledy-gook at the front and end of the line, but no colors.

The question is, how do you fix this?

Someone suggests this fix:

{% highlight python %}

import colorama

colorama.init(convert=True)
answer=input(colorama.Fore.RED + "This is a dire question, so it is colored red. What is your quest?" + colorama.Style.RESET_ALL)

{% endhighlight %}

Sadly, this does not work.

[This](https://stackoverflow.com/a/33532886/39492) SO answer suggests a truly confounding fix:

{% highlight python %}

import colorama
import sphinx.quickstart

colorama.init()
answer=input(colorama.Fore.RED + "This is a dire question, so it is colored red. What is your favorite color?" + colorama.Style.RESET_ALL)

{% endhighlight %}

I had to install sphinx with pip to even get it to run. It installed a LOT of stuff. Once that was done, the result was...

That it still couldn't find sphinx.quickstart.

Grumble grumble....

Okay, we can try something else:

{% highlight python %}

import colorama
import sphinx.quickstart

colorama.init()
print(colorama.Fore.RED, end='')
answer=input(This is a dire question, so it is colored red. What is the air speed velocity of an unladen swallow?" )
print(colorama.Style.RESET_ALL, end='')

{% endhighlight %}

And THAT has the intended effect!

What a silly workaround.

## Resources ##
* [Colorama](https://pypi.python.org/pypi/colorama)
* [StackOverflow Answer for print statements](https://stackoverflow.com/a/3332860/39492)
* [StackOverflow Question for 'input' not working with colors](https://stackoverflow.com/questions/32872612/python-colorama-not-working-with-input)