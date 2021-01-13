---
layout: post
title: How-To Package and Release a Python Program
date: 2021-01-11 21:31
categories: how-to python package
---

## Introduction ##

I write lots of Python scripts for my own use. Someday I'd love to write them for the use of other people: I'd love to have an installer that people could download
and install an executable version of my scripts for their own use. I'd love if it could work on Windows or Linux. I'd love it if I could figure out what licenses I would
need to cite to keep everything nice and legal and friendly.

So, what I'm going to do is kill two birds with one stone: I'm going to create a template command-line project that has all of the neat stuff I talked about and will serve
as the basis for whatever new script I dream up. Then, whenever I have an idea, I just have to export my generic project into a new folder, customize it and initialize a new 
git repo on top of it, then I'll have a nice command-line utility that does whatever I want that has all of the bells and whistles.


## Template Project ##

I've already started the template project [here](https://github.com/sfriederichs/pyCli).

## Executable Generation ##

I'm going to use PyInstaller to generate my executables. See my article on generating executables from Python scripts [here]({{site.baseurl}}{% post_url 2017-12-20-Python-Executables %}).

PyInstaller leaves me with one file for my output: pyCli.exe

That's muy bueno.

## Installation ##

Installation is going to follow a two-pronged path: Windows and Linux.

But first, what directory structure do we use for the installation folder?

The program itself will be just an executable file, but there will be lots of other things that I want to include (manuals, config files, etc.)

What I think I'm going to do is put the exe into the root of the install folder, then have multiple subdirectories. The ones I can 
think of at the moment are:

* logs - For any log files
* cfg - Configuration files
* res - Resources such as graphics, database files, etc.
* docs - For any documentation and license files

### Windows Installation ###

I'm going to use NSIS for generating a Windows installer.

#### Windows Installation Path ####

I need to figure out where to install the software so that I don't have to worry too much about admin privileges.

My first instinct is to install it somewhere in the user directory because that doesn't require admin privileges.
One issue with that is that no other users other than the one who installed it would be able to use the application.
The other is that there doesn't seem to be a standard location within the
user directory to install things. I know that Python did that on my work
machine when I didn't have admin privileges.

There's a question about it on [superuser.com](https://superuser.com/questions/532460/where-to-install-small-programs-without-installers-on-windows) with various answers:

* C:\Tools - I've seen some machines have permissions issues with placing anything in the root folder the same as they might with Program Files
* C:\Users\Steven - Given that this is just the user folder, so 
* C:\Users\Steven\AppData - This folder is supposed to be for *data*, not full program installs. Nevertheless, some applications install themselves here for one user
* C:\Users\Steven\AppData\Microsoft\Installer\<ProductId> - This is apparently where applications with MSI installers will install their application when installed for the current user only. I think I'll pass

Given all of these options I think I'm just going to use Program Files.

Of course, there's a rub - do I install in the x64 Program Files directory, or the x32 version?

I don't for sure know if my Python installation is x64. I don't know if all of my libraries that I use are. I also don't really know the difference between installing the program in either of those two locations: will the Microsoft Police come and arrest me if I put an x32 
program in the x64 Program Files directory?

I'm just going to use the x32 Program Files directory. Because I hate 
thinking too hard about decisions.

#### NSIS Script ####

I need an NSIS script to generate the installer. I had an article that 
I wrote about that [here]({{site.baseurl}}{% post_url 2018-05-16-NSIS %})

One of my first problems is where to put the install script. What subdirectory?

The issue is that NSIS usually puts the installer executable into the same
directory as the install script. You can change this configuration, but it 
still begs the question: Where does the script go and where do the installers go?

I'd like the installers to all go in one directory so I can .gitignore it, but the script?

I think I'll have an 'install' subdirectory where I can put the installers and an 'nsis' subdirectory which includes the script.

I'm going to copy the script that I started there and modify it below:

{% highlight nsis %}
#NSIS Example Install Script
#This file will be placed in the 'install' subdirectory in the project

#Basic definitions
!define APPNAME "Sample App"
!define COMPANYNAME "Steves Toolbox LLC"
!define DESCRIPTION "Basic Python Application"
!define APPSHORTNAME "pyCli"

#Ask for administrative rights
RequestExecutionLevel admin

#Other options include:
#none
#user
#highest

#Default installation location - Program Files or Program Files (x86)
InstallDir "$PROGRAMFILES\${APPSHORTNAME}"

#Text (or RTF) file with license information. The text file must be in DOS end line format (\r\n)
LicenseData "..\license.md"

#'Name' goes in the installer's title bar
Name "${COMPANYNAME}-${APPSHORTNAME}"

#Icon for the installer - this is the default icon
#Icon "logo.ico"

#The following lines replace the default icons
!include "MUI2.nsh"

#The name of the installer executable
outFile "${APPSHORTNAME}-inst.exe"

#...Not certain about this one
!include LogicLib.nsh

#Defines installation pages - these are known to NSIS
#Shows the license
Page license
#Allows user to pick install path
Page directory
#Installs the files
Page instfiles

#A macro to verify that administrator rights have been acquired
!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
        messageBox mb_iconstop "Administrator rights required!"
        setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
        quit
${EndIf}
!macroend

#This ensures the administrator check is performed at startup?
function .onInit
	setShellVarContext all
	!insertmacro VerifyUserIsAdmin
functionEnd

# Files for the install directory - to build the installer, these should be in the same directory as the install script (this file)
section "install"
    setOutPath $INSTDIR
	
	#Create directories
	
	#Logfiles
	CreateDirectory $INSTDIR\logs
	
	#Docs
	CreateDirectory $INSTDIR\docs
    
	#Config files
	CreateDirectory $INSTDIR\cfg
	
	#Resources
	CreateDirectory $INSTDIR\res
	
	# Files added here should be removed by the uninstaller (see section "uninstall")
    file /r ..\dist\*.*
	
	#Copy the license file to the docs directory
	file /oname=docs\LICENSE.md ..\LICENSE.md
	file /oname=docs\README.md ..\README.md

	
	# Add any other files for the install directory (license files, app data, etc) here
    
    #This creates a shortcut to the executable on the desktop - the second set of options in quotes are for command-line arguments
	CreateShortcut "$desktop\pyApp.lnk" "$instdir\pyCli.exe" 
 
sectionEnd
{% endhighlight %}


## Linux Installation ##

I'll probably use a makefile of some sort.

## Resources ##

* [Template CLI Project](https://github.com/sfriederichs/pyCli)
* [Rules for distributing Python with an application](https://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq#If_I_bundle_Python_with_my_application.2C_what_do_I_need_to_include_in_my_software_and.2For_printed_documentation.3F)

