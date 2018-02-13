---
layout: post
title:  "How To Develop GUI Applications in Python"
date:   2017-12-10 15:19
categories: how-to python gui tkinter
---

## GUI Hello World ##

If you want to try a basic 'Hello World' style application to ensure everything is working correctly this code will do the trick:

{% highlight python %}
#!/usr/bin/python

import Tkinter as tk

root = tk.Tk()
w=tk.Label(root,text="Hello World")
w.pack()
root.mainloop()

{% endhighlight %}


## GUIs with Threading ##

Currently, my approach to incorporating threads into GUI programs looks like this:

{% highlight python %}
#!/usr/bin/python

import Tkinter as tk
from threading import Thread
from time import sleep

exit = False

def myThread():
    global exit
    
    while not exit:
        sleep(1)

#GUI Setup        
root = tk.Tk()

#Set window size - NOTE: window is still resiazable
root.geometry("500x500")

#Set window title
root.title("My 1st GUI App")

w=tk.Label(root,text="Hello World")
w.pack()

#Threads setup
threads=[]

myHandle = Thread(target=myThread,args=())

threads.append(myHandle)

for handle in threads:
    handle.start()
    
#Main Loop
try:
    root.mainloop()
except KeyboardInterrupt:
    exit = True

exit = True

for handle in threads:
    handle.join()


{% endhighlight %}

## Resources ##

* [Python 2.7 Tkinter Documentation](https://docs.python.org/2/library/tkinter.html)





