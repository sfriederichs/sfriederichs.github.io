---
layout: post
title:  "Git for Windows"
updated: 2020-03-24 21:47
date:   2020-03-24 21:47
categories: how-to git windows

---

## Introduction ##

I have a new computer.  It runs Windows 10. It doesn't have Git. I need Git to update this very website. That's a problem.

Let's remedy it.

## Downloading the Installer #

The installer for Git 2.26.0 can be found [here](https://github.com/git-for-windows/git/releases/download/v2.26.0.windows.1/Git-2.26.0-64-bit.exe). That was the latest version
at the time of writing of this article.

The latest version of the installer can be found at the Git for Windows website [here](https://gitforwindows.org).

## Installing Git for Windows ##

Start the installer and perform the following steps:

1. The first thing that came up for me was a UAC dialog asking if I wanted the installer to make changes. I agreed.
2. Agree to the license by clicking 'Next'
![License Agreement]({{site.basepath}}/img/2020-03-24 21_30_09-Git 2.26.0 Setup.png)
3. The default installation location is acceptable. Click 'Next'
![Installation Location]({{site.basepath}}/img/2020-03-24 21_40_31-Git 2.26.0 Setup.png)
4. I deselected the following components:
* Everything under Windows Explorer integration
* Associate .sh files to be run with Bash
Then click 'Next'.
![Component Selection]({{site.basepath}}/img/2020-03-24 21_43_32-Git 2.26.0 Setup.png)
5. The default options are acceptable on the next screen. Click 'Next'.
![Start Menu Folder]({{site.basepath}}/img/2020-03-24 21_44_26-Git 2.26.0 Setup.png)
6. I switched the default editor to Notepad++ and clicked 'Next'
![Default Editor]({{site.basepath}}/img/2020-03-24 21_48_03-Git 2.26.0 Setup.png)
7. I changed the PATH option to utilize Git and additional tools from the command line, then clicked 'Next'.  
![PATH Options]({{site.basepath}}/img/2020-03-24 21_48_50-Git 2.26.0 Setup.png)
8. I left the OpenSSL option for the HTTPS Transport Back End and clicked 'Next'.
![HTTPS Transport Backend]({{site.basepath}}/img/2020-03-24 21_49_49-Git 2.26.0 Setup.png)
9. I left the line ending options intact and clicked 'Next'
![Line Ending Options]({{site.basepath}}/img/2020-03-24 21_52_13-Git 2.26.0 Setup.png)
10. I left the terminal options as-is and clicked 'Next'
![Terminal Options]({{site.basepath}}/img/2020-03-24 21_54_26-Git 2.26.0 Setup.png)
11. I left the extra options at the defaults and clicked 'Install'.
![IExtra Options]({{site.basepath}}/img/2020-03-24 21_55_25-Git 2.26.0 Setup.png)
12. The installation commences.
13. When installation finishes, I de-selected 'View Release Notes' and clicked 'Next->', which, I guess should have been 'Finish'. 

Installation is done!

## Installation Verification ##

To verify the install, do the following:

1. Open a Command Prompt
2. Type 'git' - the output should be similar to below:

{% highlight console %}
Microsoft Windows [Version 10.0.18362.535]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\sfrie>git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
{% endhighlight %}

## Git Configuration ##

The following steps can be performed to configure Git with your name and email address:

1. Open a command interpreter from which you can call git
2. Provide Git your email and name with these command line:
> git config --global user.email "hahaha.no@waywillItellthis.fin"
> git config --global user.name "Stephen Friederichs"

## Git Commands ##

I just had an 'Oh crap' moment with Git that I was able to fix, so I decided I'd
add some common commands that I use here.

### Reverting Changes in a Working Copy ###

Alright, I'm sure someone is going to browbeat me about the fact that 'revert' and 'working copy' are Subversion concepts that Git doesn't have. I will accept this punishment because I understand that I'm a dinosaur who can't learn new things. I will have to subsist on likening my new knowledge to my old knowledge instead of  actually learning new concepts. 

So, in that spirit, let's discuss 'reverting' 'uncommitted' changes in git. If you've done something foolish in Git but haven't committed it yet, you can back out what you just did. With one simple command:

{% highlight console %}
C:\Users\sfrie\Dropbox\Projects\sfriederichs.github.io>git reset
{% endhighlight %}

That command will unstage all uncommitted changes in the local filesystem.

## Resources ##
* [Git for Windows Installer Download](https://github.com/git-for-windows/git/releases/download/v2.26.0.windows.1/Git-2.26.0-64-bit.exe)
* [Git for Windows Website](https://gitforwindows.org/)