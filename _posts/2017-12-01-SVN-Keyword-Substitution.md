---
layout: post
title:  "How To Use SVN Keyword Substitution with TortoiseSvn"

date:   2017-12-01 7:42
categories: how-to svn
---

SVN keyword substitution is a fun way to add metadata to your source files when you commit them. You might see something like this in a source file:

> /* Author: sfrieder  
>    Last commit date: 12-01-2017 12:43:00  
>    Last commit revision: 22837  
>    URL: http://localhost/svn/project/src/test.c  
> */

The reason people do things like this is usually Configuration Management requirements: process standards on a project or in a company will dictate that certain information must be in each tracked file, for example. I'm doing it so that I can track which revisions of files from CM are present on a target system (so I can save my sanity).

You could add this information to the file manually, but that's a sucker's game because SVN allows you do to automatic keyword substitution on files. SVN knows who the last author is, the last revision, etc., so it can automatically insert that information into files checked out into a working copy. All you have to do is enable it.

## TortoiseSVN Client Configuration ##

To enable keyword substitution you need to modify your client configuration to allow it. Right now I'm using TortoiseSVN as my SVN client on Windows. This is a popular client for Windows so I imagine these steps will be useful to many. If I have the need I may figure out how to add this feature to the command-line client.

So, for TortoiseSVN on Windows you need to modify the configuration file to enable auto-props. It's worth noting that these changes will only apply to files that are added AFTER these changes are made, not existing files in the repo. Follow these steps:

1. Open the Start Menu->TortoiseSVN->Settings
2. In the 'General' window in the 'Subversion' section of the right-hand side of the window there is a filed labeled 'Subversion Configuration File' with a button labeled 'Edit' next to it - click 'Edit.
3. Uncomment line 117 so it looks like this (your line number may vary, ensure there is NO WHITESPACE at the beginning of the line):
> enable-auto-props = yes
4. Down around line 138, there is an 'auto-props' section which has several lines which specify how auto-props for each different file extension should be applied. They look like this:
> \#*.h = svn:keywords=Author Date Id Rev URL;svn:eol-style=native
5. For each file type that you want to add keywords to you need to add the *svn:keywords=...* item to the line and uncomment it. I prefer to add them to every file, so I added this line under the *[auto-props]* section:
> \*.\* = svn:keywords=Author Date Id Rev URL

Now, every file you add will have the capability of supporting the following keywords:
* Author
* Date
* Id
* Rev
* URL

## File Example ##
Add the following into a new text file:

> $Date$  
> $URL$  
> $Author$  
> $Rev$  
> $Id$  

Then, add and commit the file. Once committed, the file will look something like this:

> $Date: 2017-12-01 09:04:09 -0700 (Fri, 01 Dec 2017) $  
> $URL: svn://127.0.0.1/prj/trunk/auto-prop.txt $  
> $Author: sfrieder $  
> $Rev: 36 $  
> $Id: auto-prop.txt 36 2017-12-01 16:04:09Z sfrieder $  

Fin.

## List of SVN Keywords ##

Here's a list of SVN keywords that I've seen. It's surprisingly difficult to find an exhaustive list, so I'm adding them as I encounter them here:

* Date - The last time the file was known to have been changed in the repository (date/time is in the local timezone)
* Revision - The last known revision in which this file changed in the repository 
* Author - Username of the last user to commit this file
* URL - Full URL to the file on the SVN server
* Id - An amalgamation of file name, revision, last commit time and user

## Resources ##

* [SVN Keyword Description](http://svnbook.red-bean.com/en/1.5/svn.advanced.props.special.keywords.html)
* [SVN Keywords Setup Guide](https://wiki.documentfoundation.org/Svn:keywords)
* [SVN Auto-props Setup Guide](https://www.mediawiki.org/wiki/Subversion/auto-props)



