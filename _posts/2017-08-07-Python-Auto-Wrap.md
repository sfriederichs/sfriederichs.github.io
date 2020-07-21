---
layout: post
title:  "How To Automatically Wrap Text in Python"
updated: 2017-08-07 9:05
date:   2017-08-07 9:05
categories: how-to Python
---

I'm doing a lot of work with command-line Python scripts, so I need to format my text all pretty-like. One particular example of this is the 'help' function for command-line tools which generally produces something like this:
{% highlight console %}
Generic Tool v0.1

Copyright Stephen Friederichs, 2017

All Rights Reserved

Unauthorized Duplication is prohibited

--------------------------------------

This script is a script that does things. Important things. USEFUL things. Don't 

it was made with love and hate in equal measure, but mostly with bits, bytes and 

This script will change your life for the better or end it completely, leaving you

useless husk of a person. Use at your own risk.

Command-line options:

-h, --help - Show this dialog

-l X, --log X - Set log file to X (default is logs/log.log)

-r X, --report X - Specify log report level: DEBUG, INFO, WARNING, ERROR, CRITICAL

-c X, --config X - Specify configuration file (Default is conf/settings.ini)

-i X, --input X - Specify path to input folder (Default is xxxxxxxx)

-o X, --outpath X - Specify path to output file (Default is xxxxxxxx)
{% endhighlight %}

Notice the part in the middle: four lines of text. If you wanted to write code to print that bit out, it would look something like this:

{% highlight python %}
print "This script is a script that does things. Important things. USEFUL things. Don't question this script -"

print "it was made with love and hate in equal measure, but mostly with bits, bytes and even some nibbles."

print "This script will change your life for the better or end it completely, leaving you a hollowed-out,"

print "useless husk of a person. Use at your own risk."
{% endhighlight %}

Now, suppose you wanted to add some text in the middle of one of those lines - maybe something about kittens? Then you'd do this:

{% highlight python %}
print "This script is a script that does things. Important things. USEFUL things. Don't question this script -"

print "it was made with love and hate in equal measure, but mostly with bits, bytes, nibbles and the souls of cute kittens - the orange ones are the tastiest don't you know? Oops this line is waaaay too long now isn't it?"

print "This script will change your life for the better or end it completely, leaving you a hollowed-out,"

print "useless husk of a person. Use at your own risk. "
{% endhighlight %}

Yes, that line is waaaaay too long now. If you write your code like this then you have to manually add line breaks in the right places to that mess. No! There must be a better way!

In Python, there is. There's a library called *textwrap*. With *textwrap* you can write your message as one long string which can then be auto-wrapped by *textwrap*, like this:

> import textwrap
>
> myMessage = "This script is a script that does things. Important things. USEFUL things. Don't question this script - it was made with love and hate in equal measure, but mostly with bits, bytes, nibbles and the souls of cute kittens - the orange ones are the tastiest don't you know? Oops this line is waaaay too long now isn't it? Doesn't matter, it will be auto-wrapped by *textwrap* - just you watch! This script will change your life for the better or end it completely, leaving you a hollowed-out, useless husk of a person. Use at your own risk."
>
> print(textwrap.fill(myMessage, width=50))

This produces a nice, well-wrapped output:

> This script is a script that does things.
>
> Important things. USEFUL things. Don't question
>
> this script - it was made with love and hate in
>
> equal measure, but mostly with bits, bytes,
>
> nibbles and the souls of cute kittens - the orange
>
> ones are the tastiest don't you know? Oops this
>
> line is waaaay too long now isn't it? Doesn't
>
> matter, it will be auto-wrapped by *textwrap* -
>
> just you watch! This script will change your life
>
> for the better or end it completely, leaving you a
>
> hollowed-out, useless husk of a person. Use at
>
> your own risk.

Ta da!

## Resources ##

* [Pertinent Stackoverflow link](https://stackoverflow.com/a/16430216/39492)