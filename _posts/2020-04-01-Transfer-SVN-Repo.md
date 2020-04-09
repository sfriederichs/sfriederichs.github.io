---
layout: post
title:  "Transferring SVN Repos Between Servers"
updated: 2020-04-01 21:47
date:   2020-04-01 21:47
categories: how-to svn

---

## Introduction ##

I started an SVN server on my work laptop for a project. Now, work wants me to move it to a 'real' server for 'safety' and 'availability'. Pfft. I've only
spilled water all over this laptop and nearly destroyed it ONCE!

But, an order is an order. So, I will figure out how to transfer SVN repos from one computer to another - via the command line. Because that's how I roll.

The intent of this is to transfer all files, version history, old version, pretty much everything to the new server.

## Steps ##

First, I need to backup my old repository. The command looks something like this:

{% highlight console %}

svnadmin dump /path/to/repository > repo_name.svn_dump

{% endhighlight %}

Gotta figure out what the path to the repository is...

Probably this, from one of my checkouts:

{% highlight console %}

svn://127.0.0.1/wagm

{% endhighlight %}

Okay, no, it's looking for a local file path.

That means I have to be where my repo is stored - which is c:\svn (I'm clever and unique aren't I?)
The repo is wagm, which is a subdirectory under this folder.

And... yeah, make sure you dump to a *file* and not just dump - it hanged my command prompt.

Here's the command line I used to dump the SVN repo:

{% highlight console %}

c:\svn>svnadmin dump wagm > wagm.svn_dump
* Dumped revision 0.
* Dumped revision 1.
* Dumped revision 2.
* Dumped revision 3.
* Dumped revision 4.
{% endhighlight %}

And it continues up to 750. That should be it.

So now I have the backup. On the new server-side, I must create a new repo into which I can 
restore the dump.

I have an SSH connection. Our repos are stored at /srv/svn/repos.

I do this:

{% highlight console %}

sfrieder@APWestSWTeamRed .../repos/svn$ sudo svnadmin create wagm

{% endhighlight %}

How do you like that? Not even an 'OK'!
Oh well, it did it.

Now I have to get the dump to the new server.

I used FTP.

Now, I load the dump into the newly-created repo:

{% highlight console %}

sfrieder@APWestSWTeamRed .../repos/svn$ sudo svnadmin load wagm < wagm.svn_dump

{% endhighlight %}

And after a bit, it has loaded everything in.  Fin.

Couldn't be easier!

Oh, but that wasn't all!

I had to change permissions on the folder that holds the repo I created. It needs to be owned by www-data user (or group?) for me to be able to check out the repo.

{% highlight console %}
sudo chown -R www-data wagm/
{% endhighlight %}

But... that didn't do it either. We're still trying - considering that this SVN server is tied to Redmine, we might have to make a Redmine project.

We did, in fact, have to make a Redmine project to allow my user to access it, but that was unique to our installation. It would not necessarily occur for anyone using a standalone SVN server.

## Resources ##

* [Instructions for transferring Repos](https://www.petefreitag.com/item/665.cfm)