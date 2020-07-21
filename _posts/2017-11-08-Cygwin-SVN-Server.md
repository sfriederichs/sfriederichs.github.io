---
layout: post
title:  "How To Run an SVN Server on Windows Through Cygwin"

date:   2017-11-08 11:54
categories: how-to svn cygwin
---

It's time to start from scratch: new job, new computer and no SVN server. So I'll have to make one if I'm to do things semi-properly. I'm running Cygwin on my Windows computer and I'd prefer to have as few things installed as possible, so I want to run the SVN server through Cygwin so I don't have to download the Windows SVN package. Getting the Cygwin SVN server to run as a service in Windows is not perfectly seamless, so here's the steps:

1. Select a location to store the SVN repository files. These are NOT the same as the files that will be IN the repo: they are the files that ARE the repo. There are several folders (conf, db, hooks, locks) and two files (format, README.txt). I prefer to put these in C:\SVN\<Project Name>
2. Open a Cygwin terminal and navigate to the location you chose to store the repo files. In this example, I will be using C:\SVN to store all of the repos I want to use and each project gets its own subdirectory. Type the following to generate the repo folder/file structure in the current working directory:
> mkdir newProject  
> cd newProject  
> svnadmin create .  
3. Now we need to modify several files in *conf* to configure the server. **It's important when you make these changes that the first character of the line is not a space.** In *svnserve.conf* line 27, remove the hash and space from the start of the line so it looks like this:
> password-db = passwd
4. In *svnserve.conf* change line 36 to remove the hash and space so it looks like this:
> authz-db = authz  
5. In *svnserve.conf* change line 66 to remove the hash and space so it looks like this:
> hooks-env = hooks-env
6. In the *conf* directory for the SVN repo, rename *hooks-env.tmpl* to *hooks-env*
5. Next, you need to give your Cygwin username a password. To find your Cygwin username, look at the prompt in Bash - it should look like *sfrieder@mycomputerID /~* - The part before the @ is your username (sfrieder) and that's what you need to add to the *passwd* file. Add the following line under *[users]*:
> username = password
6. In *authz* you need to modify the file to allow any user full access to the root folder. While this may not be advisable on, say, the internet it's fine for a single computer setup like this. Add the following lines to the bottom of the file:
> [/]  
> \* = rw
7. Start an SVN server for the new repo:
> svnserve -d -r /cydrive/c/svn
8. Now you need a directory to store all of your working copies. I use C:\Projects to store all of my working copies, so the WC for this example would be C:\Projects\newProject. You can check out the working copy by doing this:
> cd /cygdrive/c/Projects  
> svn co svn://127.0.0.1/newProject
9. Verify that everything worked correctly by creating the default directories and doing a test commit:
> cd newProject  
> mkdir trunk  
> mkdir tags  
> mkdir branches  
> svn add trunk  
> svn add branches  
> svn add tags  
> svn commit -m "Adding default top-level folders"
10. At this point it should ask for a password which is the same one that you put in the *passwd* file.

So now you've got a repo being served by *svnserve* and you can work with it - great. Except that *svnserve* wont' start up with Windows, so you'll have to start it up every time manually to serve your repo. You can start the server automatically by following these instructions:
1. Open a new Cygwin terminal as an administrator
2. Type this command:
> cygrunsrv --install svnserve --disp "CYGWIN svnserve" --path /bin/svnserve --args "--daemon --foreground --root=/cygdrive/c/svn"


## Resources ##

* [Damien's Site Guide](http://mc-kenna.com/windows/2006/12/subversion-on-windows-via-cygwin)
* [Cygwin Mailing List Message from Cygwin-SVN Author](https://cygwin.com/ml/cygwin/2010-10/msg00348.html)