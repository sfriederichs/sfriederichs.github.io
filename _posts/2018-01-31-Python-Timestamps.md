---
layout: post
title:  "How To Work With Timestamps in Python"

date:   2018-01-31 9:07
categories: how-to python timestamps 
---
Timestamps for most UNIX systems are stored as the number of seconds since a given epoch (January 1st, 1970) plus or minus some nonsense with leap years.

This means they're an unsigned integer - but a LONG unsigned integer on some systems (8 bytes) and a shorter unsigned integer on others (4 bytes).

Each value has a definite representation as a time/date combination and getting there requires some simple code:

{% highlight python %}

import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1284101485")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

{% endhighlight %}

And this produces:

> 2010-09-10 00:51:25

Ta-da.

My particular implementation of this relies on an NTP server which is producing UTC timestamps. There's a note on the Stackoverflow answer regarding some non-portability or edge cases with this code and it recommends that you use a different *fromtimestamp* function to alleviate them: *utcfromtimestamp*. Since I'm working with UTC timestamps, I'll use that instead. Here's that code:

{% highlight python %}

import datetime
print(
    datetime.datetime.utcfromtimestamp(
        int("1284101485")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

{% endhighlight %}

And for this example, it produces the same output.

## Sub-Second Accuracy ##

The above approach is great if you only need one seconds'-worth of accuracy. If you're looking to include fractions of a second you have to do something different.

Here are the differences in the approach:

1. The first thing you have to do is to add the decimal portion of the timestamp to the number you pass to the conversion function.
2. Then, instead of converting to an integer, you convert to a float
3. And finally, you add the microsecond information to the output (the *.%f* portion of the *strftime* call

{% highlight python %}

import datetime
print(
    datetime.datetime.utcfromtimestamp(
        float("1284101485.01654")
    ).strftime('%Y-%m-%d %H:%M:%S.%f')
)

{% endhighlight %}

This code produces this output:

> 2010-09-10 06:51:25.016540  

## Resources ##

* [Stackoverflow - Converting UNIX Timestamp to Time/Date](https://stackoverflow.com/a/3682808)
* [Python strftime reference](http://strftime.org/)