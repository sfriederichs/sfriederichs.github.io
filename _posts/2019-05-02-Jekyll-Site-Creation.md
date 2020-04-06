---
layout: post
title:  "How To Create Jekyll Website"
date:   2019-05-02 10:39
updated: 2019-05-02 10:39
categories: how-to jekyll
---

It's time to start a new project at work and I'm trying to do it *right*. One of the *right* things I plan to do is have a daily log. I will make this log on a Jekyll website because it's fast and easy to write posts.

I am running this on Cygwin64 on Windows 10.

Luckily I already have Jekyll installed, so I don't have to document that.

## Installing Jekyll on Windows 10 ##

I now have Windows 10 and haven't installed cygwin yet. Therefore, I'm going to figure out how to install Jekyll for Windows (10).

The instructions I used are [here](https://jekyllrb.com/docs/installation/windows/).

The download location for the Ruby+Devkit installer is [here](https://rubyinstaller.org/downloads/)

The actual file I downloaded is [here](https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.5-1/rubyinstaller-devkit-2.6.5-1-x64.exe).

Then I double clicked it.

I accepted the license and clicked Next.

I installed in the default directory and clicked 'Install'.

I used the preselected components and clicked 'Next'.

Ruby installed.

(As does a MinGW environment).

After installation, the checkbox for 'ridk install' to setup MSYS2 adn development toolchain was checked. I left it so and clicked 'Finish'.

A window came up with three options.

I pressed Enter to do all three options.

It does a bunch of stuff in a cmd.exe window.

It asks me to press Enter again. I do. It disappears.

I assume that is done.

Now I'm on to step 3 from the jekyll installation page.

 I open a command prompt.
 
 I type:
 
 > gem install jekyll bundler
 
 Something happens
 Lots of success.
 27 gems installed. Ok.
 
 Now I do:
 
 > jekyll -v
 
 and get:
 
 > jekyll 4.0.0
 
 That is fin.

## Creating the website ##

The command I need is:

> jekyll new /cygdrive/c/Users/sfrieder/Documents/notebook/<project-name>

It takes a while, but creates the site.

On my (corporate) PC, using C:\\notebooks\\<project-name> was a bad idea due to permissions

Then, update the gemfile in the site folder (C:\\Users\\sfrieder\\notebook\\<project>\\gemfile) with these lines:

> gem 'bigdecimal'
> gem 'wdm', '>= 0.1.0' if Gem.win_platform?

Open a Cygwin terminal and do the following from your home directory:

>  ~/bin/bundle install

This runs bundle which should... update packages? Not sure, but it seems to resolve dependencies.

## Starting the Server ##

Navigate to the directory where the site is stored.

> ~/bin/bundle exec ~/bin/jekyll serve

This should run the server and ensure that all dependencies are downloaded

### Running on a different port ###

I already have a jekyll running on one port so I can't run on that port. It doesn't automatically try a different port. How do I tell it to run on a different port?

Yes, use:

> ./jekyll serve --port 4001 --source <path>

## Resources ##
* [Jekyll Quickstart](https://jekyllrb.com/docs/)
* [Running Jekyll on a different port](https://stackoverflow.com/q/25650749)
