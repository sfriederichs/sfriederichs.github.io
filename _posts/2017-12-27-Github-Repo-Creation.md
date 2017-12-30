---
layout: post
title:  "How To Create a Repository on Github"
date:   2017-12-27 21:55
categories: how-to git github cli
---

I've decided to create a repository of all the various code samples that I've created for my articles. This will save me the trouble of copying and pasting the snippets into Notepad++ every time I want to use them.

## Creating the Repository ##

There's probably a way of creating the repository on your local PC and then uploading it to Github, but I start by creating the repo on Github and then cloning it to my local PC. I follow these steps:

1. Log on to Github
2. In the toolbar in the upper right of the window there should be a '+' - click on it and select 'New Repository'
3. Set 'Repository Name' to something short but descriptive and memorable.
4. Add a description - any description. You'll thank yourself later.
5. Select your desired option for Public or Private for the repository visibility.
6. Check the box to generate a README.md file so that you can immediately clone the repository to your PC.
7. You can choose a pre-made .gitignore file customized for your programming language, but I prefer to leave it blank.
8. If you have a license in mind and Github has the license available, you can select it from the drop down. 
9. Click the 'Create repository' button to generate the repository.

The repository is now created and you should be taken to its page on Github.

## Cloning the Repository to Your Local PC - CLI##

These steps describe how to clone the repository to your PC via the command line. Luckily, these steps start right from the end of the repository creation steps. You should be on your repository's Github page. If not, navigate there.

1. Click the green 'Clone or Download' button just above the repository's file listing.
2. In the drop down, ensure the title 'Cloning with SSH' is shown at the top and click the 'Copy to Clipboard' button above the SSH URL for the repository.
3. Open your favorite command interpreter from which you can call *git*
4. Change the working directory to the directory where you'd like to check out the repository folder.
5. Now you'll type the command to clone the repository via its URL. I've included the URL to my code examples repository, but you can replace it with whatever is appropriate for you:
> git clone git@github.com:sfriederichs/code-examples.git
6. Enter the passphrase for the SSH key which is associated with your computer in your Github account (if necessary).
7. Wait for the repository to download.

Success! The repo should be checked out to its own folder under the current working directory.

## Setting Your Git Email and Name - CLI ##

Git (or maybe, Github?) requires that you provide it with an email address and a name so that a commit's author can be identified and thoroughly tongue-lashed via email for any infractions he or she may commit. Here's how you supply that information to Git:

1. Open a command interpreter from which you can call git
2. Provide Git your email and name with these command line:
> git config --global user.email "hahaha.no@waywillItellthis.fin"
> git config --global user.name "Stephen Friederichs"

You can optionally omit the --global option if you only want git to use the information you supply for a particular repository, but in the case you want to do that you'll need to change your current working directory to the repository directory first.

## Pushing Local Changes to Github - CLI ##

The whole purpose of this exercise is to work with your repository on your local PC, so you'll definitely want to push the changes you make locally back to Github. Here are the steps to do so from the command line:

1. In a command interpreter, change the current working directory to the repository directory.
2. Commit your changes and add any outstanding files to the local repo by typing:
> git commit -a -m "This is my commit message"
3. Push those changes to Github with this command:
> git push origin master
4. Provide the passphrase for your SSH key if necessary.

You can use a *git* commit command of your choice if the above options aren't to your liking, but those are the options that work well for me 80% of the time.

After this, you'll want to verify that your changes made it to Github. I saw my changes there within a minute or two after I committed and pushed.

## Resources ##

* [Clone the Repository Using the Command Line](https://services.github.com/on-demand/github-cli/clone-repo-cli)
* [The difference between git pull, git fetch and git clone and git rebase](https://blog.mikepearce.net/2010/05/18/the-difference-between-git-pull-git-fetch-and-git-clone-and-git-rebase/)


