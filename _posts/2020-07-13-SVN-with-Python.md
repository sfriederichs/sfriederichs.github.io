---
layout: post
title:  "How-to Access SVN with Python"
date:   2020-07-13 8:58

categories: how-to python3 svn
---


## Introduction ##

I have a tedious task to perform which involves reading information from SVN and updating a review checklist with the information. The 'hard' part of this whole process is the actual review.
The 'easy' part is looking up the revision information, paths, file names, etc and putting them into the spreadsheet. Despite the fact that this is the 'easy' part it's also very easy to 
mess up. This tedious copy and paste process has many steps, requires significant working memory and can be easily confusing. The worst part is that even if you do the 'hard' part well, you 
need to do the 'easy' part _perfectly_ because if you mess up a revision or a path there's no way to link the work you did to the actual artifact being reviewed.

So, why not create a script?

Python can read SVN and filesystem information. It can read Excel files. It can write excel files. So, let's just automate this whole thing.

This post will focus on the SVN aspects of the process. I have another that focuses on the Excel aspects.

## Background ##

There is a package called PySVN that handles the interface between Python and SVN. It's a bit of fun, so buckle up.

## PySVN Installation ##

On a Windows 10 PC using Python 3 (3.8.1) I did the following:

{% highlight console %}

C:\Users\sfrieder>pip3 install pysvn
Collecting pysvn
  ERROR: Could not find a version that satisfies the requirement pysvn (from versions: none)
ERROR: No matching distribution found for pysvn
{% endhighlight %}

Hmmm, odd. Usually that works...

It's really odd. I can't find a lot about why pip isn't working. That being said, it seems you just install it with an installer, from their website.

The download website is [here](https://pysvn.sourceforge.io/downloads.html).

I'm downloading the version for Python 3.8.1 and WIndows 1 x64, which is [here](https://sourceforge.net/projects/pysvn/files/pysvn/V1.9.12/Windows/py38-pysvn-svn1140-1.9.12-2041-Win64.exe/download). Note: it's the 1.14.0 version.

It brings me to SourceForge (ew) and the download starts.

Alright, downloaded. Now, starting the installer. 

Uh, where is it?

Oh look, Windows Defender says that it's scard of this download. I tell it 'no'. You will run it.

Anyway, on to the actual installation.

1. Select Start Menu Folder - The defaults are fine, I click 'Next'
2. Ready to Install - Everything looks good, I click 'Install'
3. Installation occurs...
4. And then, it finishes. So I click 'Finish'

Nothing major there!

## Hello World Script ##

The first thing I like to do with anything new is to do a 'Hello World' type script. In this case, my
workflow depends on several things:

1. Getting the full SVN URL of files checked out on to my PC
2. Getting the last few log entries of files check out on my PC
3. Finding the last user to commit a file check out on my PC

The first thing that shows up when I google for 'pysvn examples' is [this](https://tools.ietf.org/doc/python-svn/pysvn_prog_guide.html) page.

It has quite a few little snippets that look rather tasty. Let's see if I can find what I'm looking for.

Eh, no. I can't. Dang. What else do we have?

One thing I have noticed over the years of using PySVN is that it has curiously few examples running around out there. Few StackOverflow questions, few blog posts, etc.

### Getting a Login ###

One of the first things you'll need to do is specify a callback function to get a login to your SVN
server. Not much will work without it. [This](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_client_callback_get_login) is the documentation for implementing a callback, and below you'll see I've generated a simple function to suffice for the callback and register it to the SVN client.

{% highlight python %}
import pysvn

def get_login(realm,username,may_save):
    return True,"steve","password",True
    
client = pysvn.Client()
client.callback_get_login = get_login

{% endhighlight %}

That at least runs without error, so I'll move on to the next part.

FYI, none of those entries above are my real password to anything.

### Getting SVN Info for Working Copy Files ###

I think the function I need to use is the info2 function. Read more about it [here](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_client_info2).

I need to pick a file, point _info2_ towards it, then see what it returns. Here's the code I'm trying:

{% highlight python %}
        fileInfo = client.info2(filePath)
        print(str(fileInfo))
{% endhighlight %}

What the docs say will be returned is this:

{% highlight text %}
The info_dict contains:

URL - URL or path
rev - pysvn.Revision or None
kind - kind of path
repos_root_URL - string
repos_UUID - string
last_changed_rev - pysvn.Revision or None
last_changed_date - time or None
last_changed_author - string or None
lock - None or dictionary containing:
path - string
token - string or None
owner - string or None
comment - string or None
is_dav_comment - true if is DAV comment
creation_date - time or None
wc_info - None if url_or_path is a URL; otherwise a dictionary containing:
schedule - pysvn.wc_schedule or None
copyfrom_url - string or None
copyfrom_rev - pysvn.Revision or None
text_time - time or None
prop_time - time or None
checksum - string or None
conflict_old - string or None
conflict_new - string or None
conflict_wrk - string or None
prejfile - string or None
{% endhighlight %}

Historically, PySVN has a _very_ confusing way of storing useful information. Actually getting the information you want out of what it returns is complicated. Here's what comes out of the print statement:

{% highlight console %}

[('<local file path>', <PysvnInfo ''>)]
{% endhighlight %}

See? That's just kinda weird. A tuple inside a list? And the first item of the tuple is just the file path I passed to it? So, to access the PysvnInfo member, you have to do this:

{% highlight python %}

        fileInfo = client.info2(filePath)
        print(str(fileInfo))
        print(str(fileInfo[0][1]))
{% endhighlight %}

But the second print statement prints this out:

{% highlight console %}\
<PysvnInfo ''>
{% endhighlight %}

Brilliant. So, we start trying to figure out what's in there. Supposedly it's a dictionary, right? So 
we'll try accessing some of the named members from the website. Like this:

{% highlight console %}

        fileInfo = client.info2(filePath)
        print(str(fileInfo))
        print(str(fileInfo[0][1]))
        svnFileInfo = fileInfo[0][1]
        print(str(svnFileInfo["URL"]))
{% endhighlight %}

Which produces:

{% highlight console %}

[('<local file path>', <PysvnInfo ''>)]
<PysvnInfo ''>
<File URL>
{% endhighlight %}

Okay, so I didn't put the actual URL there, but take my word for it: it prints out the URL.

It should be easy to get the rest of the information that we want.

### Getting Revision Information ###

If you thought an SVN revision was just an integer number, raise your hand.

_Raises hand_

Turns out - I'm wrong. An SVN revision (as far as PySVN is concerned) is a _pysvn.Revision_ type.

Now what, pray tell, is *that*?

From [here](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_revision):

{% highlight text %}

The Revision object has three member variables:

kind - the kind of revision, its value is one of the opt_revision_kind enumerations.
date - date and time when kind is opt_revision_kind.date, as seconds since the epoch which is compatible with python's time module.
number - revision number when kind is opt_revision_kind.number
{% endhighlight %}

If you're interested in what the opt_revision_kind enumeration information is, look [here](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_opt_revision_kind):

{% highlight console %}

unspecified - No revision information given.
number - revision given as number
date - revision given as date
committed - rev of most recent change
previous - (rev of most recent change) - 1
base - .svn/entries current revision
working - current, plus local mods
head - repository youngest
{% endhighlight %}

Okay, so what will print out if we try to access the revision code? We try like this:

{% highlight console %}

        fileInfo = client.info2(filePath)
        svnFileInfo = fileInfo[0][1]
        print(str(svnFileInfo["rev"]))
{% endhighlight %}

That produces this:

{% highlight console %}
<Revision kind=number 2342>
{% endhighlight %}

Interesting, but supposedly tehre were three elements: kinda, date and number. Can we access them or am I misunderstanding things?

Trying this:

{% highlight console %}

        fileInfo = client.info2(filePath)

        svnFileInfo = fileInfo[0][1]

        print(str(svnFileInfo["rev"]))

        print(str(svnFileInfo["rev"].kind))
        print(str(svnFileInfo["rev"].date))
        print(str(svnFileInfo["rev"].number))

{% endhighlight %}

Which produces:

{% highlight console %}

<Revision kind=number 2342>
number
None
2342
{% endhighlight %}

Well, that at least bears out the part about having three elements. Now at least I can access the specific parts of the revision information that I'm looking for.

Not bad.

However, we must take into account a wrinkle with SVN: last-changed revision vs. current revision.

Current revision is basically the most recent revision of the working copy. Imagine if you did an update on the root of a working copy - when it finished you'd see something like "Updated to revision xxxx". Now, the working copy is considered to be at revision xxxx. However, many files within the working copy might not have been changed in revision xxxx - they have a 'last-changed' revision which will be lower than the working copy revision. When SVN says 'Updated to revision xxxx' what it's saying is 'all the files in this working copy are up-to-date as of revision xxxx'. If you pick a file that was last updated in say, revision 443 and tell SVN to check out that file at any revision later than 443, you'll get the most up-to-date file. If you choose to check out a revision earlier than 443, you will not have the most up-to-date file. 443 would be the 'last-changed revision', while xxxx would be the 'revision'.

Generally, the 'revision' isn't very useful when you're looking at individual files. Instead, you'll want to go with the 'last-changed revision'.

In order to print out the information for 'rev' vs. 'last-changed-rev', I would use this code:

{% highlight console %}

        svnFileInfo = client.info2(filePath)[0][1]
        curRev = svnFileInfo["rev"].number
        lastChangedRev = svnFileInfo["last_changed_rev"].number
        print("Current revision is " + str(curRev))
        print("Last-changed revision is +" str(lastChangedRev))
{% endhighlight %}

And you get this output:

{% highlight console %}
Current revision is 2342
Last-changed revision is 556
{% endhighlight %}

Not bad, now we can get all the revision information we want.


### Getting Author/Committer Information ###

I'm guessing that the author information is this one:

{% highlight console %}
last_changed_author - string or None
{% endhighlight %}

And luckily, it's just a string, so it should be easy to access like this:

{% highlight console %}

        fileInfo = client.info2(filePath)
        print("Last changed author is" + str(svnFileInfo["last_changed_author"]))
{% endhighlight %}

Which produces:

{% highlight console %}
Last changed author <author>
{% endhighlight %}

Keep in mind, the 'author' will be a username, not necessarily a full-fledged first and last name.

### Getting Log Entries ###

Now we're getting a bit farther. Most of the information I was looking for could be found with the _info2_ function, but I don't see anything about the log in the _info2_ documentation, so it must be elsewhere.

But where?

Look no further than [this](https://tools.ietf.org/doc/python-svn/pysvn_prog_ref.html#pysvn_client_log).

It's a single function call that returns this:

{% highlight text %}

log returns a list of log entries; each log entry is a dictionary. The dictionary contains:

author - string - the name of the author who committed the revision
date - float time - the date of the commit
message - string - the text of the log message for the commit
revision - pysvn.Revision - the revision of the commit
changed_paths - list of dictionaries. Each dictionary contains:
path - string - the path in the repository
action - string
copyfrom_path - string - if copied, the original path, else None
copyfrom_revision - pysvn.Revision - if copied, the revision of the original, else None
{% endhighlight %}

Alright, so what does this mean practically?

Here's the code I run:

{% highlight python %}

        logInfo = client.log(filePath)
        print(str(logInfo))
        
{% endhighlight %}
And the result:

{% highlight console %}
[<PysvnLog ''>, <PysvnLog ''>]
{% endhighlight %}

It's worth noting that retrieving the log takes a second - much more time than the _info2_ command took.

Okie.... this file has two entries in its log when I look at it, so that must be theese.  Let's assume those are dictionaries as specified above and see if we can print out the information we want for each entry. Here's the code I created:

{% highlight console %}

        logInfo = client.log(filePath)
        
        print(str(logInfo))
        for entry in logInfo:
            print(str(entry["revision"].number) + " - " +str(datetime.datetime.fromtimestamp(entry["date"]).strftime('%Y-%m-%d %H:%M:%S')) + os.linesep + str(entry["message"]) + " - "+ str(entry["author"]) )
            
{% endhighlight %}

And the output:

{% highlight console %}

[<PysvnLog ''>, <PysvnLog ''>]
<Revision> - <year>-<month>-<day> <hour>:<minute>:<seconds>
< Commit message 1 - 
Multiple Lines!> - <Committer>

<Revision> - <year>-<month>-<day> <hour>:<minute>:<seconds>
< Commit message 2 - 
Multiple Lines!> - <Committer>
{% endhighlight %}


I had to include the datetime library to get the correct formatting function since the timestamp comes back in a float format. But overall, not too bad!

### Listing the SVN Contents of a Directory ###

I have a situation where I need to get the SVN information (URL, last changed revision) for a few files
in a directory. This presents an interesting twist: in a working copy, not all files may be version
controlled. There could be uncommitted files hanging around there - this means it's important not to 
do a directory listing of files, but instead to do an SVN listing of files.

Turns out there's a useful command called 'ls'. Ha. Imagine that. Let's see what the [documentation](https://tools.ietf.org/doc/python-svn/pysvn_prog_ref.html#pysvn_client_ls) says about it.

{% highlight text %}
Use the list method in new code as it fixes performance and ambiguity problems with the ls method.
{% endhighlight %}

Oh. Okay. Where's that?

[Here](https://tools.ietf.org/doc/python-svn/pysvn_prog_ref.html#pysvn_client_list).

You pass it a path and it returns some information:

{% highlight text %}
Returns a list with a tuple of information for each file in the given path at the provided revision.

The tuple contains:

0 - PysvnList containing the dirent information
1 - PysvnLock containing the lock information or None
The PysvnList object contains the requested dirent fields:

created_rev - pysvn.Revision - the revision of the last change
has_props - bool - True if the node has properties
kind - node_kind - one of the pysvn.node_kind values
last_author - string - the author of the last change
repos_path - string - (always present) absolute path of file in the repository
size - long - size of file
time - float - the time of the last change
{% endhighlight %}

So, I whip this code up:

{% highlight python %}

        #Get directory from file path
        dirPath = os.path.dirname(filePath)
        print("Listing working copy path: " + str(dirPath))
        dirInfo = client.list(dirPath)
        for entry in dirInfo:
            print("Repository file: " + str(entry[0]["repos_path"]) )
            print("Last changed in revision " + str(entry[0]["created_rev"].number))
            print("By author: " + str(entry[0]["last_author"]))
{% endhighlight %}

Which produces this result:

{% highlight console %}

Listing working copy path: <WC Path>
Repository file: <Relative Repo Path>
Last changed in revision 556
By author: <Author>
Repository file: <Relative Repo Path>
Last changed in revision 340
By author: <Author>
Repository file: <Relative Repo Path>
Last changed in revision 556
By author: <Author>
Repository file: <Relative Repo Path>
Last changed in revision 340
By author: <Author>
{% endhighlight %}

Well, we've got a problem: the paths are relative repository paths, not complete URLs. The server name and protocol is not present, which is not what I want.

The question is: how do I get that?

I could use the list command to get a list of files and then use the info2 command to get their URLs.

Ah, but I've encountered a twist!

When you list a directory, the first entry returned is _the directory itself_!

Not really a problem, but if you're expecting just the files, you'll get in some trouble.

Anyway, here's the code to do get the full URL with the info2 command:

{% highlight python %}

        #Get directory from file path
        dirPath = os.path.dirname(filePath)
        print("Listing working copy path: " + str(dirPath))
        dirInfo = client.list(dirPath)
        for entry in dirInfo[1:]:   #Start at 1 to ignore the directory entry
            dir,fileName = os.path.split(entry[0]["repos_path"])
            wcFilePath = os.path.join(dirPath,fileName)
            fileInfo = client.info2(wcFilePath)[0][1]
            
            print("Repository file: " + str(fileInfo["URL"]) )
            print("Last changed in revision " + str(fileInfo["last_changed_rev"].number))
            print("By author: " + str(fileInfo["last_changed_author"]))
{% endhighlight %}

### Checking a Working Copy for Uncommitted Changes ###

One of the sanity checks I'll have to do is to make sure that I haven't failed to commit changes I've
made to my checklists before I close an issue.

[This](https://stackoverflow.com/a/45478994/39492) Stack Overflow answer suggests a method. 

Here's the code:

{% highlight console %}

    statuses = client.status(path_to_repository, ignore=True, recurse=True)
    statuses = [s for s in statuses if s.data['text_status'] != pysvn.wc_status_kind.normal]
    return len(statuses) == 0
    
{% endhighlight %}

I think I'd like to change it to something that returns a list of files with uncommitted changes.  Let's look up the _status_ function. Documentation is [here](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_client_status).

It returns a PysvnStatus object, what's that?

It's [this](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_status):

{% highlight text %}

Each status object has the following fields:

path - string - the path name
entry - PysvnEntry - entry information
is_versioned - Boolean - true if the path is versioned
is_locked - Boolean - true if the path is locked
is_copied - Boolean - true if the path is copied
is_switched - Boolean - true if the path has been switched
prop_status - wc_status_kind - the status of the properties of the path
text_status - wc_status_kind - the status of the text of the path
repos_prop_status - wc_status_kind - the repository status of the properties of the path
repos_text_status - wc_status_kind - the repository status of the text of the path
repos_lock - dict - the repository lock information

{% endhighlight %}

Alright, the big question is going to be what the _path_ returns - local? Repo? URL?

The other big issue is that the example code only looks for status NOT normal. That could include more things than just normal or uncommitted changes.

[This](https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_wc_status_kind) is the documentation for the _pysvn_wc_status_kind_ type, reproduced here:

{% highlight text %}

none - does not exist
unversioned - is not a versioned thing in this wc
normal - exists, but uninteresting.
added - is scheduled for addition
missing - under v.c., but is missing
deleted - scheduled for deletion
replaced - was deleted and then re-added
modified - text or props have been modified
merged - local mods received repos mods
conflicted - local mods received conflicting repos mods
ignored - a resource marked as ignored
obstructed - an unversioned resource is in the way of the versioned resource
external - an unversioned path populated by an svn:external property
incomplete - a directory doesn't contain a complete entries list
{% endhighlight %}

Okay, so we can check for a variety of non-ideal status. Honestly, at this point, if any status is not 
'normal' it pump the brakes, so I guess that guy was right....

Anyway, here's what I wrote for code:

{% highlight console %}

            statuses = client.status(dirPath, ignore=True, recurse=True)
            for entry in statuses:
                print (str(entry.data["path"]) + " has status " + str(entry.data["text_status"]))
                
{% endhighlight %}

And it produced this:

{% highlight console %}

<directory> has status normal
<file 1> has status normal
<file 2>  has status normal
<file 3>  has status normal
<file 4>  has status normal
{% endhighlight %}

And all of the file paths were local working directory paths. Doesn't really matter to me.

It's worth noting, again, that the first entry was the entry for the directory, not a file within the directory.

### Committing Changes in a Working Copy ###

Well, once you've ascertained there are uncommitted changes, you'll want to commit them. 

But PySVN doesn't use the verb 'commit' for this, it uses '[checkin](https://tools.ietf.org/doc/python-svn/pysvn_prog_ref.html#pysvn_client_checkin)'.

Only big question is how to get the log message. I know there can be a log message callback, but I think
I'll just use a text input to do this.

{% highlight python %}

        logMessage = input ("Enter a log message: ")

        try:
            newRev = client.checkin(dirPath,logMessage)
        except Exception as e:
            print ("Commit failed! " + str(e))
            sys.exit(2)

{% endhighlight %}

The try/catch is there because I know that it's possible that there will be circumstances the commit
will fail - one I know of for sure is a pre-commit hook failing. However, I don't know exactly what
the exception will be and the documentation isn't explicit on that, so I'm just catching a generic
exception.

Yes, I know - that's bad. But until that exception occurs I won't know what to look for specifically.
Or I could do more research. But I won't right now.

Also, I've had issues using os.linesep within log messages, as well as '\\r\\n'. The server I'm working on only wants the '\\n'.

## Adding Files to a Working Copy ##

If you have a newly-created file, you'll need to add it to your working copy and then commit
to get the file into SVN. Here's how you do it.

{% highlight python %}

client.add(filePath)
newRev = client.checkin(addressPath,"Added a new file")

{% endhighlight %}

## Notes ##

These are miscellaneous notes I'm keeping about using PySVN.

### Single-Threadedness ###

One of the interesting things about PySVN is that there's only one SVN client on your PC - _anywhere_.
That means if you're messing around with the command-line SVN client and you try to run a Python script
that uses the SVN client your Python script will have to wait for the command-line process to finish 
before it can start. 

One important upshot of this is that you really can't do multi-threaded access to the SVN client in Python. If you try, you're gonna have a confusing and frustrating time. 

*Only ever access the SVN client from _one_ Python thread*

## Resources ##

