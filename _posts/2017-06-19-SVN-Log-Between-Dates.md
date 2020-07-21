---
layout: post
title:  "How to get a log of SVN activity between two dates"

date:   2017-06-19 11:01
categories: how-to
---

I wanted to get a list of all of the SVN commits I had made to a repo between certain dates. The best way is to use the command line using *svn log*, but I didn't know how to limit it to between two dates.

A bad way to do it would be to dump the whole log and then filter it - there's certain to be a way to do it from the command line directly.

(This)[https://stackoverflow.com/q/21822950/39492] Stackoverflow question poses the same problem. I used this command line to do the trick:

> svn log -v -r {2016-06-01}:{2017-06-01}

That works well, but then I need to find only the commits done by me. That can be done with grep. I updated the command line thusly:

> svn log -v -r {2016-06-01}:{2017-06-01} | grep sfriederichs

However, this only gives me the line with the username on it:

> r17796 | sfriederichs | 2017-05-23 13:53:49 -0400 (Tue, 23 May 2017) | 1 line

I want to see the log messages as well. The whole log entry I want looksl ike this:

> ------------------------------------------------------------------------
> r17796 | sfriederichs | 2017-05-23 13:53:49 -0400 (Tue, 23 May 2017) | 1 line
>
> Changed paths:
>
>    M --PATH--
>
>
>
> --

To get all of this, I need to add context with the -B (add lines before) and -A options ( add lines after), thusly:

> svn log -v -r {2016-06-01}:{2017-06-01} | grep -B1 -A4 sfriederichs

That produces the proper output IN MOST CASES! Note that not all entries will be the same length and you may be missing some entries. It doesn't matter to me very much for this application.