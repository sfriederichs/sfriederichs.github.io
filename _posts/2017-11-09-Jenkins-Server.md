---
layout: post
title:  "How To Install a Jenkins Server"
date:   2017-11-09 8:42
categories: how-to jenkins
---

Jenkins is one of my favorite tools for automating processes on files stored in SVN. I've used it in the past to automatically update status reports when new work items were committed to SVN and I've got all kinds of plans to use it for automatic code formatting, unit testing, documentation, etc. First I've got to install it though. I'm installing the Windows version of Jenkins (not any potential Cygwin version) 

## Download ##

You can download Jenkins from [here](https://jenkins.io/download/), but specifically for Windows it's [here](https://jenkins.io/download/thank-you-downloading-windows-installer-stable). 

## Install ##

You will need administrator privileges to install this. Unfortunately, I didn't save pictures or steps from the installation process, but it was completely straightforward: just keep clicking 'Next' and you'll be good.

## Configuration ##

### Unlocking Jenkins ###

Once installation is complete, point your browser to [localhost:8080](http://localhost:8080). You should see a 'Getting Started' page which will promt you to unlock Jenkins. You 'unlock' Jenkins by providing it a password saved on your local PC. For me, it was saved in:

> C:\Program Files (x86)\Jenkins\secrets\initialAdminPassword

It's seemingly a random, hexadecimal character string which I copied into the text box on the site. After it accepted the password it brought be to a customization page.

### Customizing Jenkins ###

On the next page you get the option to install plugins. I installed the suggested plugins which seem to be:

* Folders plugin
* Timestampper
* Pipeline
* Git plugin
* PAM Authentication
* OWASP Markup Formatter Plugin
* Workspace Cleanup Plugin
* GitHub Branch Source Plugin
* Subversion Plug-in
* LDAP Plugin
* Build Timeout
* Ant Plugin
* Pipeline: GitHub Groovy Libraries
* SSH Slaves plugin
* Email extension
* Credentials Binding Plugin
* Gradle Plugin
* Pipeline: Stage View Plugin
* Matrix Authorization Strategy Plugin
* Mailer Plugin

### Creating Admin User ###

Once the plugins are installed you'll have to enter information for an admin account. Since my setup is essentially a single-user setup I decided to keep it easy to remember, but if you need more security, adjust your setup. Once done, click Save and Finish. On the next screen, you'll be promted to start using Jenkins - click on it and you'll be at the main screen.

Done!

### Updating the SVN Workspace Version ###

By default, Jenkins uses an *old* version of the Subversion client and checks out its workspaces in that version. The version it uses is incompatible with the command-line client that would be used when you put SVN commands in the build instructions. To fix this, perform the following steps:

1. Open [Jenkins](http://localhost:8080) and log in
2. Click on *Manage Jenkins*
3. Find *Configure System* and click on it
4. Find *Subversion Workspace Version* and set it to the appropriate version. The maximum I have is 1.8 - I hope it's enough (it is!).
5. Click *Save*

### Moving the Default Workspace Location ###

The default workspace location (where SVN files used in builds are checked out) is located within the Program Files directory on your PC. This is less than ideal because you might not by default have write permissions to that when you execute scripts. Plus, it's going to put a lot of *stuff* in your Program Files directory which will make it huge and complicated. 

1. Create a folder where you want your workspace to be. I chose C:\Jenkins-Workspace
2. Open [Jenkins](http://localhost:8080) and log in
3. Click on *Manage Jenkins*
4. Under *Home Directory* click the *Advanced* button.
5. Set the *Workspace Root Directory* to the folder you created for this purpose.
6. Click *Save*

## Resources ##

* [Jenkins Download Page](https://jenkins.io/download/)
* [Jenkins Windows Download](https://jenkins.io/download/thank-you-downloading-windows-installer-stable)
* [Jenkins Post-Installer Page](https://wiki.jenkins.io/display/JENKINS/Thanks+for+using+Windows+Installer)
* [Jenkins SVN Workspace Update Stackoverflow answer](https://stackoverflow.com/a/15163931)