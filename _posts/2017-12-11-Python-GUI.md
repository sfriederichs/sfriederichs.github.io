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

## Resources ##

* [Python 2.7 Tkinter Documentation](https://docs.python.org/2/library/tkinter.html)





