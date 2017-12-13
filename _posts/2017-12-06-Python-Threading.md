---
layout: post
title:  "How To Create Threads in Python Scripts"
date:   2017-12-06 8:35
categories: how-to python multithreading
---

Multithreading is often the best way to prevent multiple different tasks in one application from stepping on each others' toes, blocking each other and making life difficult and annoying. It also improves the organization of the program and makes it easier to understand (hopefully anyway).


## Simple Thread Example ##

While it may be difficult to understand how threads are implemented behind the scenes, creating a thread is not much more difficult than calling a function. Here's example code that generates a single thread:

{% highlight python %}
import time  
from threading import Thread  
  
def myThread():  
	print "sleeping 5 sec myThread"  
	time.sleep(5)  
	print "finished sleeping from myThread"  
	  
myThreadHandle = Thread(target=myThread,args=())  
myThreadHandle.start()  
print "Waiting on thread(s) to finish..."  
myThreadHandle.join()  
print "All threads ended"  
{% endhighlight %}

Some notes on this example:
* The *myThread* function is the function that gets turned into its own thread
* The *Thread* returns a handle to the newly-created thread
* *myThreadHandle.start()* kicks off the thread in its own execution context
* *myThreadHandle.join()* blocks the main application until the thread represented by *myThreadHandle* exits

This script produces this output:

> Waiting on thread(s) to finishsleeping 5 sec myThread  
>   
> finished sleeping from myThread  
> All threads ended  

As you can see there are some synchronization issues regarding the use of *print* from within threads. Every time a python script prints something it is supposed to finish with a newline, so you'd expect the output to look like this:
 
> Waiting on thread(s) to finish  
> sleeping 5 sec myThread  
> finished sleeping from myThread  
> All threads ended  

This doesn't (necessarily) happen because both threads are trying to access the standard output (i.e., where *print* prints its text) at the same time with no synchronization between them. As a programmer, you have no control over which thread gets to *print* first unless you start adding in synchronization between the threads (such as mutex semaphores). That's a bit far afield for a simple thread example, but it's worth knowing why the output is munged in this case so that you can recognize this and similar problems with threading in more complex situations.

## Threads With Arguments Example ##

You can pass arguments to threads just the same like you would with functions. Here's what that looks like:

{% highlight python %}
import time  
from threading import Thread  
  
def myThread(i):  
	print "Argument for myThread is " + str(i)  
	print "sleeping 5 sec myThread"  
	time.sleep(5)  
	print "finished sleeping from myThread"  
	
myThreadHandle = Thread(target=myThread,args=(1,))  
myThreadHandle.start()  
print "Waiting on thread(s) to finish"  
myThreadHandle.join()  
print "All threads ended"  
{% endhighlight %}


## Threads as Superloop Example ##

Typically, threads don't just run straight through and exit: they continually loop and handle their business until it's time to exit the entire application. You can create a thread that loops until it's time to quit the application like this:

{% highlight python %}
import time  
from threading import Thread  
  
exit = False  
  
def myThread(i):  
    global exit  
    print "myThread: Argument for myThread is " + str(i)  
    while not exit:  
        print "myThread: sleeping 5 sec"  
        time.sleep(5)  
    print "myThread: Global exit flag set, exiting myThread..."  
	  
myThreadHandle = Thread(target=myThread,args=(1,))  
myThreadHandle.start()  
print "Main Thread: Started myThread...  Sleeping for 11s"  
time.sleep(11)  
print "Main Thread: Signaling exit..."  
exit = True  
myThreadHandle.join()  
print "Main Thread: All threads ended"  
{% endhighlight %}

And here's the output:

> myThread: Argument for myThread is 1Main Thread: Started myThread...  Sleeping for 11s  
>   
> myThread: sleeping 5 sec  
> myThread: sleeping 5 sec  
> myThread: sleeping 5 sec  
> Main Thread: Signaling exit...  
> myThread: Global exit flag set, exiting myThread...  
> Main Thread: All threads ended  

Now, apart from the difficulties with the order of what gets printed and when, you'll see something else interesting in this example. The main thread signals exit after its 11s wait, but *myThread* manages to sleep for 5 seconds three times for a total of 15 seconds instead of 11. This is because *myThread* can't exit while it's *sleep*ing because *sleep* is a blocking command - the thread will do no work while it's waiting for *sleep* to finish. That means that even though the main thread signals exit after 11 seconds, the whole application will only exit after *myThread* stops being blocked and recognizes the *exit* flag after 15 seconds. Thus, the *myThread.join()* call will cause the main thread to block for about 4 seconds - until *myThread* recognizes and acts on the flag. You'll see this behavior often in threads that involve blocking calls.

## Resources ##

* [Simplistic Python Thread Example](https://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/)




