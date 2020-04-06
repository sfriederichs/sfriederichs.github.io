---
layout: post
title:  "How To Profile Python Scripts"
updated: 2017-08-25 9:27
date:   2017-08-25 9:27
categories: how-to Python profiling
---
Profling code is important - especially if you're me and you have a script you love that you just keep adding things on to and your only criteria for success is 'Eh, it works'.
'Eh, it works' is *marginally* okay, but once you do it three dozen times, you have a script that is less of an organized tool and more of a taped-together abomination. One of the main problems with this approach (other than the complete inability to work with the code after a while) is a loss in performance.  It's so subtle that you don't even notice it at first, but as you add more and more to the script the performance just gets worse and worse and worse....

Eventually, the time the script is supposed to be saving you is lost because of the sheer amount of time it takes to run. Profiling your script can help you identify where your 'Eh, it works' code is performing poorly and where your opportunities for improvement are.

## Generating the profile report

Turns out that profiling Python code is easy. You just have to run your script with a special command-line:

> python -m cProfile <script name> <options>

CProfile will profile your code and generate a confusing report that looks like this:

>     197 function calls (192 primitive calls) in 0.002 seconds
>
>Ordered by: standard name
>
>ncalls  tottime  percall  cumtime  percall filename:lineno(function)
>     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
>     1    0.000    0.000    0.001    0.001 re.py:212(compile)
>     1    0.000    0.000    0.001    0.001 re.py:268(_compile)
>     1    0.000    0.000    0.000    0.000 sre_compile.py:172(_compile_charset)
>     1    0.000    0.000    0.000    0.000 sre_compile.py:201(_optimize_charset)
>     4    0.000    0.000    0.000    0.000 sre_compile.py:25(_identityfunction)
>   3/1    0.000    0.000    0.000    0.000 sre_compile.py:33(_compile)

## Refining the report output

You can sort the report on the 'tottime' or 'cumtime' or 'ncalls' numbers by changing your command line:

> python -m cProfile -s <sort header> <script name> <options>

So, for example, you might have this for a command-line to sort by 'cumtime':

> python -m cProfile -s cumtime src\script.py

Then the report will be sorted in order of descending cumulative time.

## Reading the profile report

Now, this report isn't useful until you learn how to read it. Each row represents a function in your code or in a library somewhere. The columns are:

* ncalls - Number of calls made to this function (What about the 3/1? Dunno)
* tottime - This is the amount of time spent in that function *ONLY* - it does not include the time spent in functions called from this function
* percall (1) - This is the amount of time spent in the function per each call - i.e., 'tottime' divided by 'ncalls'
* cumtime - The amount of time spent in this function and all functions it calls
* percall (2) - The amount of cumulative time spent in this function and its called functions per each call - i.e., 'cumtime' divided by 'ncalls'

## Optimizing code with profiling results

This is going to vary a lot, but essentially, you want to approach this one of several ways:

1) Look at the highest first 'percall' (1) time. This will show you 

## Resources ##

* [Pertinent Stackoverflow link](https://stackoverflow.com/q/582336/39492)
* [Python Profiler Documentation](https://docs.python.org/3/library/profile.htm)