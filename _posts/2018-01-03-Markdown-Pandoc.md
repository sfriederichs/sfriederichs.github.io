---
layout: post
title:  "How To Generate Fancy Documents with Markdown and Pandoc"

date:   2018-1-3 11:34
categories: how-to pandoc docx dox
---

Microsoft Word sucks - especially for generating engineering documents. I can't count the number of 'reviews' I've been in where the content of a document was largely ignored so that people could score easy points by critiquing font sizes, page breaks, table layouts, image formatting and whether or not something should be italicized or bolded. What's more frustrating is that those 'errors' only exist in the document because Word is so difficult to work with. How many times have spurious page breaks just *appeared* for no good reason in your Word document? How many times has one cell of a table gotten impossibly out of alignment with the rest of a table and you spend 10 minutes zoomed in on the cell trying to move the border *one pixel* so it lines up with the rest of the cells? How often have your images plopped themselves in the middle of a paragraph and refused to move above or below the text - instead opting to break onto another page, span between two pages or just disappear completely? The madness must end.

That's not to say that we need to get rid of Word. *That* will never happen: people expect Word documents and rightly throw fits when you try to give them a PDF or God forbid an ODF. Everyone has Word on their PC, people can edit Word documents easily, they can Track Changes for reviews, they can count words and paragraphs, they can spell check and grammar check. No one should be asked to give this up, but when I need to *generate* a new Word document I try to avoid using Word. Instead, I use a different approach that focuses on the content of the document first and puts the formatting second.

I start my documents in a text editor - Notepad++ and I write them in [Markdown](https://en.wikipedia.org/wiki/Markdown). The idea behind Markdown is twofold: 

1. It's entirely text-based and completely readable as text. If you open a Markdown file in a text editor you won't see gibberish that only becomes recognizable after running it through a filter and changing it into a different format.
2. It provides a basic set of markup (bulleted lists, tables, emphasis, links, etc.) that can be expressed in a variety of different formats. Markdown files can be converted to HTML, PDF, DOCX, ODF and [lots more](https://pandoc.org/MANUAL.html#description) but the most important part of this is that it *consistently* produces these outputs from its inputs. 

The upshot of this is that you can open up a text editor, start writing your content, add basic markup and then convert it to *anything*. This blog post is written in Markdown and run through Jekyll to create the web page from it but I can also someday take this same content and convert it to a PDF, EPUB, or DocBook for easy publishing in eBook or dead paper formats. Furthermore, you don't have to worry about messing around with formatting in Word (or whatever your final format is) because the conversion from Markdown to Word (or whatever) is automatic and consistent. If you don't like how something is done, you can define a template which produces the formatting you want. Never again will you have inconsistent formatting or need to play with a table for 10 minutes to get it to look right: just get it right once and you're done. Markdown is also [supported by Doxygen](https://www.stack.nl/~dimitri/doxygen/manual/markdown.html) which means that you can have just as much fun documenting your code as you do writing blog posts!

## Basic Markdown->DOCX with Pandoc ##

To perform these steps, you'll need to [install Pandoc](https://pandoc.org/installing.html). I didn't document that, sorry :(

FYI: there's nothing unique to these steps which allows them to produce DOCX output rather than, say, EPUB other than the command line options specified when you do the conversion. However, PDF output is a complete other thing which can't be done directly by changing the command line options seen in these steps. For PDF output you need some means of converting LaTeX to PDF which is not particularly straightforward. Hopefully I'll generate some steps to do that at some point.

These steps are for a Windows computer.

To convert Markdown to DOCX you will first need some Markdown to convert. Here's some:

{% highlight markdown%}

# Title: My Document #

This is my document. It is a good document. I love this document for the following reasons (in no particular order):

* It uses Markdown
* It has examples of basic Markdown
* There is no third bullet point

## Header Level 2 ## 

A subsection: subservient to the main section. Less than equal. Aspects of a subsection include (in this particular order):

1. It's beneath its parent
2. That's about it

And that needs some *emphasis*! Maybe even some **BOLDING**!

# A Table #

Here's a table:

| Column 1  | Column 2  |
|-----------|-----------|
| 1         | A         |
| 2         | B         |
| 3         | C         |

# Conversion #

If you save this as example.md, you can turn this file into a DOCX by typing this in the command line:

> pandoc -f markdown -t docx -o test.docx example.md

{% endhighlight %}

So if you save this text as 'example.md' in some directory, you can open a command prompt, navigate there and type the following to do the conversion:

> pandoc -f markdown -t docx -o test.docx example.md

Here's a breakdown of the command-line options:

* -f - Specifies the input format (Markdown, obviously)
* -t - Specifies the output format (docx)
* -o - Specifies the path to the output file

And then after all of those options you pass the input file and voila! You get a .docx file out!

## Directory Structure ##

One aspect of the Markdown methodology that's not immediately obvious is that you will need to store your resources (such as images) somewhere in your file system so they can be included. I tend to use the following directory structure when I generate documents from Markdown:

* *img* - Stores any images
* *gv* - Stores any GraphViz files (which are turned *into* images)
* *msc* - Stores any Mscgen files (again, these get turned into graphics)
* *txt* - Stores the Markdown text file

This list will get expanded as I develop more complex documents.

## Using Jenkins to Automatically Generate Documents ##

These steps assume that your Markdown file is stored in Subversion. Jenkins will poll Subversion for changes to the file and execute the commands to generate the document when its prerequisites change.

1. Open up Jenkins on your [local machine](http://localhost:8080)
2. In the upper left of Jenkins click on 'New Item'
3. Name the item 'DOCX Generation' or something else boring.
4. Select 'Freestyle project'
5. Click on 'OK' in th elower left corner
6. On next page, add a Description (you'll thank yourself later)
7. Under *Source Code Management* select *Subversion*
8. Now, you'll have to add a Module for every SVN location you want to monitor for updates to the resources needed to build the document. I'm going to write steps for each field that I needed to change. The first is the Repository URL. This needs to be the URL of the SVN folder where the resource that forces the document update is.
9. For *Credentials* I had to add them since I didn't have them added to Jenkins already. The credentials are the username/password for my local SVN server. Click on *Add* and then select *Jenkins*. Set the following options:  
* Domain: Global credentials (unrestricted)  
* Kind: Username with password  
* Scope: Global (Jenkins, nodes, items, all child items, etc)  
* Username: sfrieder  
* Password: ********  
* ID: Local SVN password
* Description: <None>  
10. Click on *Add*.
11. In the *Credentials* dropdown, select the newly-added credentials.
12. Leave the *Local module directory* as '.'
13. Leave *Repository Depth* as 'infinity'
14. Leave *Ignore externals* checked
15. Under *Build Triggers* check the *Poll SCM* box.
16. In the *Schedule* box that shows up enter '@hourly'
17. Under *Build* click on 'Add build step' and select 'Execute Windows Batch Command'
18. In the *Command* section write the command we used to generate the DOCX. There is one rub: apparently in whatever command interpreter Jenkins was running, the path to the *pandoc* executable was not set, so I had to supply the full path:  
> C:\Users\sfrieder\AppData\Local\Pandoc\pandoc -f markdown -t docx -o test.docx example.md
19. Click on 'Save'
20. You should now be at the page for the job that you just created. Click the *Build Now* link on the left-hand side of the page. 
21. The job should run (successfully I hope). The output can be found in the Jenkins a and you should find *test.docx* generated 

### Additions to the Jenkins Build ###

There are a few tricks I've learned to make generating documents a little easier. Most of these tricks should work directly in any document build.

#### Generating Images Automatically ####

At first, when I needed to generate an image from a .gv file or a .msc file I hardcoded the file name and build command line directly. In Windows batch files, it turns out that you can automate this. The following command line will take all .msc files in the *msc* subdirectory and generate images for them:

{% highlight batch %}

for %%i in (msc/*.msc) do mscgen -Tpng -i msc/%%i -o img/%%~ni.png

{% endhighlight %}

You can extend this to any *.gv* file or anything else that you can use a command-line to generate.

## Resources ##

* [Wikipedia Markdown Article](https://en.wikipedia.org/wiki/Markdown)
* [Pandoc Homepage](http://pandoc.org)
* [Stackoverflow - Batch iterating over files](https://stackoverflow.com/a/138538)
* [Stackoverflow - Removing extensions from files names in iteration](https://stackoverflow.com/a/3215539)
* [PP - A generic preprocessor for Pandoc](http://cdsoft.fr/pp/)