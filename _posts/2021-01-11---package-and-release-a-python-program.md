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

I'm going to use Py2Exe to generate my executables.

## Windows Installation ##

I'm going to use NSIS for generating a Windows installer.

### Windows Installation Path ###

I need to figure out where to install the software so that I don't have to worry too much about admin privileges.

## Linux Installation ##

I'll probably use a makefile of some sort.

## Resources ##

* [Template CLI Project](https://github.com/sfriederichs/pyCli)
* [Rules for distributing Python with an application](https://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq#If_I_bundle_Python_with_my_application.2C_what_do_I_need_to_include_in_my_software_and.2For_printed_documentation.3F)

