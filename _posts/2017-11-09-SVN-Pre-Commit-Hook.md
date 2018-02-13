---
layout: post
title:  "How To Create an SVN Pre-Commit Hook"
date:   2017-11-09 10:42
categories: how-to jenkins
---

I'd like to ensure that I always put a commit message in my SVN commits, but I can't do it with willpower alone because, well, that's just a bad idea. Therefore, I will use an SVN pre-commit hook script to ensure that the commit doesn't go through if there's no commit message. 

**NOTE: Pre-commit hooks must not modify the files being committed! This means validity checks only, but no code formatting, etc.**

Here's some steps:

1. Find the *hooks* directory for your repo. 
2. There should be a *pre-commit.tmpl* file there - rename it to *pre-commit* (no extension)
3. Restart the SVN server

Now, at this point if I try to commit and don't put in a message, it fails with this message (emphasis added):

> Commit failed (details follow):  
> Commit blocked by pre-commit hook (exit code 1) **with no output**.  
> If you want to break the lock, use the 'Check For Modifications' dialog or the repository browser.  

That's what I want but I don't like the 'with no output' part. I'd like there to be an indication of why the commit failed, but we'll get to that.

However, if I do put in a message and try to commit, it fails with this message:

> Commit failed (details follow):  
> Commit blocked by pre-commit hook (exit code 1) with output:  
> /cygdrive/c/svn/proj/hooks/pre-commit: line 88: commit-access-control.pl:  
>  command not found  
> If you want to break the lock, use the 'Check For Modifications' dialog or the repository browser.  

Seems like we have a misconfiguration. Let's do some searching.

Aaaaand... it seems that this isn't my fault. That script isn't included with the distribution I'm using, so I have to download it separately. You can do that from [here](http://svn.apache.org/viewvc/subversion/trunk/tools/hook-scripts/commit-access-control.pl.in?view=co). Save it in the *hooks* directory of your SVN repo.

And I did that... but it still doesn't work and I'm losing patience. So,I just commented out line 88 in the *hooks/pre-commit* file and now it works great! I'm sure I don't need that script anyway - right?

But how do we give a reasonable error message when there's no commit message? Turns out there's a [StackOverflow](https://stackoverflow.com/questions/16751653/unable-to-generate-output-from-svn-pre-commit-hook) question and answer for that. Essentially, any error messages must be output to *stderr* and then they'll show up in the right place. You can do that by modifying line 84 of *hooks/pre-commit* to this (emphasis shows added portions):
>    grep "[a-zA-Z0-9]" > /dev/null \|\| **echo "A commit message is required">&2  &&** exit 1

So now there's a valid error message. Great. That's the extent of what I wanted to do with this pre-commit script, but let's discuss how we can extend this.

We have a pre-commit script that runs. If we want to do more, we can either:
1. Add all of the pre-commit logic to the bash script, or
2. Call one or more separate scripts to do the dirty work

My preference is for the second option: we can call Python scripts from the pre-commit script to do all of the hard work. This keeps the pre-commit script simple and straightforward and allows complex behavior from the Python scripts.

More to come... maybe.


## Resources ##
* ['Official' pre-commit scripts](http://svn.apache.org/repos/asf/subversion/trunk/tools/hook-scripts/)
* [Commit-access-control error message resolution](https://subversion.open.collab.net/ds/viewMessage.do?dsForumId=3&dsMessageId=356435&orderBy=createDate&orderType=desc)
* [StackOverflow Q&A on outputing error messages from scripts](https://stackoverflow.com/questions/16751653/unable-to-generate-output-from-svn-pre-commit-hook)
