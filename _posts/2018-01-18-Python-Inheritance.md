---
layout: post
title:  "How To Inherit Classes in Python"
date:   2018-01-18 9:25
categories: how-to python classes oop
---

Who doesn't love object-oriented programming? Well, I'm ambivalent. However, as I learn more, I become more comfortable and more likely to use it. Hopefully, I become more likely to use it *well*. Here's another thing I need to learn with respect to Python classes: how to inherit them.

## Python Class Inheritance ##

A basic Python class looks like this:

{% highlight python %}

class Person:
    def __init__(self,name):
        self.name = str(name)
        
    def greet(self):
        print "Hi, my name is " + self.name
        

{% endhighlight %}

See? Easy. Now, let's extend this class:

{% highlight python %}

class Rapper(Person):
    def __init__(self,name,alterEgo):
        self.name = str(name)
        self.alterEgo = str(alterEgo)
        
    def greet(self):
        print "Hi, my name is " + self.alterEgo

{% endhighlight %}

So, in summary, a *Person* has a *name*, but a *Rapper* is a *Person* with an *alterEgo*. A *Person* will greet someone by saying their *name*, but a *Rapper* will greet someone with their *alterEgo*. 

Example:

{% highlight python %}

marshall = Person("Marshall Mathers")
slimShady = Rapper("Marshall Mathers","chicka chicka Slim Shady")

marshall.greet()
slimShady.greet()

{% endhighlight %}

This produces the output:

> Hi, my name is Marshall Mathers  
> Hi, my name is chicka chicka Slim Shady.

In this simple example, you can see how an inherited class (*Rapper*) overrides the built-in methods (*init* and *greet*) provided in the base class (*Person*). 


## Calling Base Class Methods in Inherited Classes ##

If you're a programmer, you may be crying foul at this simple example because the *Rapper* class inheriting from the *Person* class is essentially useless: the *Rapper* class completely overrides everything within the *Person* class. Why bother inheriting?

It's true: in the above example the inheritance does nothing. We can fix this though: there's one piece of functionality that's common between the two: setting *name* to the passed value. So, instead of completely reproducing this functionality in the inherited class, we can reuse the base class's constructor so that the inheritance isn't a complete waste of time. You do that like this (in Python 2.7):

{% highlight python %}
class Person:
    def __init__(self,name):
        self.name = str(name)
        
    def greet(self):
        print "Hi, my name is " + self.name
  
class Rapper(Person):
    def __init__(self,name,alterEgo):
        Person.__init__(self,name)
        self.alterEgo = str(alterEgo)
        
    def greet(self):
        print "Hi, my name is " + self.alterEgo
        
{% endhighlight %}

The addition here is the *Person* line in the *Rapper* initialization function. That line calls the initialization function for the base class of *Rapper* (*Person*). This will set the *name* attribute to the passed value of *name*, essentially reusing the code from the *Person* initialization function so it doesn't have to be completely reproduced in the *Rapper* class. You can reuse this approach for any built-in function in the base class, but mostly I use it for initialization functions.

## Resources ##

* [Stackoverflow - How to call parent class constructor](https://stackoverflow.com/q/12557612)
* [Stackoverflow - Two options for calling base class functions](https://stackoverflow.com/a/35215830)