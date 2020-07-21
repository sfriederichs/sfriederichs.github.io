---
layout: post
title:  "How to Replace With Regex Matches in Notepad++"
date:   2020-04-02 21:33

categories: how-to regex notepad-pp
---


## Introduction ##

Anyone who claims mastery over regular expressions is a witch. I don't claim mastery - I just know enough to be alternately useless and useful. I recently have figured out how to perform one new nifty trick with Notepad++ and regular expressions: replacing text with a regular expression match.

It came up when I wanted to do a mass-rename of a front-matter attribute in my blog posts. I needed to identify lines that matched "date: \<a sequence of characters that matches a date\>" and then change it to "updated: \<the same date from above\>".

Regular expressions can find things easily, but I'm also told by witches that it can store the things it finds for later use, and that this is a powerful tool at their disposal. I've cracked the code of how to do it in Notepad++.

It should be noted that this is *strictly* unique to Notepad++. The sad state of regular expressions is that expressions are not entirely portable between different implementations of regex searchers. Heck, grep even has a command-line options to control which implementation of regex it uses.

## Notepad++ Search and Replace with Regex Matches ##

First off, set the Search Mode to Regular Expression. Then you'll be in a good place to do the rest of these steps:

The Notepad++ regex that matched the 'date:' line I was looking for was this:

{% highlight text %}
date:   ([0-9\:\- ]*)
{% endhighlight %}

The dates were a complete timestamp in 24-hour time. The format was "YYYY-MM-DD HH:MM:SS", so the above regex found all that mess after 'date:' The important part are the parenthesis around the expression (i.e., the part in brackets). The parenthesis tells the regex interpreter that this match should be saved. 

Recovering that information and using it in the Replace function of Notepad++ looks like this:

{% highlight text %}
updated: (\1)
{% endhighlight %}

The magic here is the '(\1)' - that instructs the regex interpreter to recall the first saved match, which in this case is the date/timestamp. Essentially, this finds every instance of 'date: ' which has an actual date/timestamp after it, saves it, and replaces 'date:' with 'updated:'.

