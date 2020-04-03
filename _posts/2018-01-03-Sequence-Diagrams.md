---
layout: post
title:  "How To Generate Sequence Diagrams with Mscgen"
updated: 2018-1-3 7:00
date:   2018-1-3 7:00
categories: how-to mscgen dox
---

I am a huge fan of software documentation and one of my go-to means of documenting the behavior of software is through sequence diagrams. Sequence diagrams show communication between one or more endpoints in a system. For example, here's a sequence diagram of the TCP 3-way handshake:

![TCP 3-Way Handshake]({{site.basepath}}/img/tcp-example.png)

I use a program called [Mscgen](http://www.mcternan.me.uk/mscgen/) to generate sequence diagrams. It allows you to define the content of the sequence diagram with text markup which the Mscgen program then turns into a graphical file via the command-line. Here's an example of the markup that generates the above sequence diagram:

{% highlight mscgen %}
#Stephen Friederichs
#Mscgen sequence file example
#TCP 3-way handshake

# Command-line to generate output: mscgen -T png -i tcp-example.msc -o tcp-example.png

# See http://www.mcternan.me.uk/mscgen/ for complete markup details

# Comments start with a pound/hash

#This line begins the sequence diagram markup
msc {

    #This line definse the entities in the MSC diagram
    client,server;
    
    #These lines define the messages going back and forth between the entities
    client note server [label="TCP 3-Way Handshake Sequence Diagram"];
    client->server[label="SYN"];
    server->client[label="SYN-ACK"];
    client->server[label="ACK"];
    
    # Arrow options include:
    # '-> or <-' - Message
    # '=> or <=' - Method or function call
    # '>> or <<' - Method or function return value
    # '=>> or <<=' - Callback
    # ':> or <:' - Emphasized message
    # '-x or x-' - Lost message
    # '...' - Indicates detail ommitted or time passed
    # '---' - Comment block
    # '|||' - Adds extra space between rows
    # '->* or *<-' - Broadcast arcs, where the arc is extended to all but the source entity
    # 'box' - A box arc between two entities.
    # 'rbox' - A rounded box arc
    # 'abox' - An angular box arc
    # 'note' - Note box arc
    
}
{% endhighlight %}

As specified in the file, the command line:

> mscgen -T png -i tcp-example.msc -o tcp-example.png

will generate a PNG graphic of the sequence diagram. You can also generate EPS, PNG and something called 'ismap' which I doubt I will ever use. I prefer PNG for general use, but if I'm embedding the graphic in a LaTeX document then EPS is the best choice.


## Resources ##

* [Wikipedia Sequence Diagram Article](https://en.wikipedia.org/wiki/Sequence_diagram)
* [Mscgen Homepage](http://www.mcternan.me.uk/mscgen/)