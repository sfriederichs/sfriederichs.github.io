---
layout: post
title:  "How To Create a Repository on Github"
date:   2017-12-27 21:55

update-abstract: Added information on creating and adding SSH keys to Github
categories: how-to git github cli
---

I've decided to create a repository of all the various code samples that I've created for my articles. This will save me the trouble of copying and pasting the snippets into Notepad++ every time I want to use them.

## Creating the Repository on the Github Website ##

No matter what, if you want the repository to be on Github, you have to create it on there. An easy way to start is to create the repo on Github and then cloning it to my local PC. I follow these steps:

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

## Getting the Repository to Your Local PC - CLI ##

Getting the repository to your PC can be done one of two ways: either clone the remote (Github) repository to your PC, or initialize a repository on your PC, then add Github as a remote repository.
Realistically, there's no difference between these two steps. Initially, the Github repo is empty, so cloning the repo to your PC directly essentially performs the same steps. One approach may be preferable to another in different circumstances (e.g., within a scripting environment).

### Getting the SSH URL for Your Repository ###

No matter which approach you choose, you'll need the SSH URL for your repository. Here's how to get it:

1. Navigate to the Github page for your repository
2. Click the green 'Clone or Download' button just above the repository's file listing.
3. In the drop down, ensure the title 'Cloning with SSH' is shown at the top and click the 'Copy to Clipboard' button above the SSH URL for the repository.

### Cloning the Github Repository to Your PC ###

These steps describe how to clone the repository to your PC via the command line. Luckily, these steps start right from the end of the repository creation steps. 


1. Open Git Bash (or your favorite command interpreter from which you can call *git*)
2. Change the working directory to the directory where you'd like to check out the repository folder.
3. Now you'll type the command to clone the repository via its SSH URL. I've included the URL to my code examples repository, but you can replace it with whatever is appropriate for you:
> git clone git@github.com:sfriederichs/code-examples.git
4. Enter the passphrase for the SSH key which is associated with your computer in your Github account (if necessary).
5. Wait for the repository to download.

Success! The repo should be checked out to its own folder under the current working directory.

### Initializing the Repository Locally and Linking to Github ###

These instructions initialize a repository in an empty directory, generate a README file, add it, commit 
the changes, link the Github repository and push the changes there:

1. Create the directory where you want the repository
2. Open Git Bash or your favorite command interpreter and change the working directory to the new one you created
3. Create your first file with echo:
> echo # embedded_crc >> README.md
4. Initialize the git repo
> git init
5. Add the file:
> git add README.md
6. Commit the file to the repository:
> git commit -m "first commit"
7. Link the repository to Github:
> git remote add origin git@github.com:sfriederichs/code-examples.git
8. And finally, push the changes to Github
> git push -u origin master

At this point it should ask for your passphrase. Supply it and you're home free! Remember to replace the SSH URL with the one appropriate for your repository.

## Setting Your Git Email and Name - CLI ##

Git (or maybe, Github?) requires that you provide it with an email address and a name so that a commit's author can be identified and thoroughly tongue-lashed via email for any infractions he or she may commit. Here's how you supply that information to Git:

1. Open a command interpreter from which you can call git
2. Provide Git your email and name with these command line:

{% highlight console %}
git config --global user.email "hahaha.no@waywillItellthis.fin"
git config --global user.name "Stephen Friederichs"
{% endhighlight %}

You can optionally omit the --global option if you only want git to use the information you supply for a particular repository, but in the case you want to do that you'll need to change your current working directory to the repository directory first.

## Generating an SSH Key ##

You'lll need an SSH key  to be able to push data to a github repo. 
[Here](https://help.github.com/articles/generating-ssh-keys/) is a good resource from Github. The steps I followed are:

1. Start git bash from the start menu
2. Type:
> ls -al ~/.ssh

Your result should look something like this:

{% highlight console %}
total 12
drwxr-xr-x 1 sfrie 197609   0 Mar 24 21:59 ./
drwxr-xr-x 1 sfrie 197609   0 Mar 24 22:03 ../
-rw-r--r-- 1 sfrie 197609 799 Mar 24 22:02 known_hosts

{% endhighlight %}

You'll see no files of the form *.pub - this means there are no existing SSH keys. 
3. In the bash window, type:
> ssh-keygen -t rsa -b 4096 -C "\<your email address used on Github\>"
	
This is what happens:

{% highlight console %}
$ ssh-keygen -t rsa -b 4096 -C "sfriederichs@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/sfrie/.ssh/id_rsa):
{% endhighlight %}

4. Press Enter to use default - you should see this:

{% highlight console %}
Enter passphrase (empty for no passphrase):
{% endhighlight %}

5. Enter pass phrase:
	\<It's a secret\>

Get this result:

{% highlight console %}
Enter same passphrase again:
{% endhighlight %}

6. Enter passphrase again. Get this result
{% highlight console %}
Your identification has been saved in /c/Users/sfrie/.ssh/id_rsa
Your public key has been saved in /c/Users/sfrie/.ssh/id_rsa.pub
The key fingerprint is:
\<Redacted\>
The key's randomart image is:
\<Redacted\>

{% endhighlight %}

7. Type the following:
> eval "$(ssh-agent)"
	
Get this result:

{% highlight console %}
Agent pid 358
{% endhighlight %}

Any number is good!

8. Type the following:
> ssh-add ~/.ssh/id_rsa
Get this result:
{% highlight console %}
$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /c/Users/sfrie/.ssh/id_rsa:
Identity added: /c/Users/sfrie/.ssh/id_rsa (sfriederichs@gmail.com)
{% endhighlight %}

## Adding the SSH Key to Github ##

Once the SSH key is added to Github you can use it to push code. Here's how you do it:

1. Go to github.com and log in to your account
2. Go to https://github.com/settings/ssh
3. Click on 'New SSH key'
4. Set 'Title' to something descriptive for this particular PC
5. Obtain your SSH key by typing the following in git-bash:
> cat ~/.ssh/id_rsa.pub | clip
6. Paste into the 'Key' field - the previous command saved the key to the clipboard
7. Click 'Add Key'

Your key is now stored on Github - when you try to push to Github you'll have to put in your passphrase.

To verify the installation, do the following:

1. Open Git Bash
2. Type the following commadn:
> ssh -T git@github.com

You should see a message like this:

{% highlight console %}
sfrie@DESKTOP-NE76661 MINGW64 ~
$ ssh -T git@github.com
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
Hi sfriederichs! You've successfully authenticated, but GitHub does not provide shell access.
{% endhighlight %}

The 'no shell access' message means the SSH key installation was successful!

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



## Creating a .gitignore file ##

1. Create a file in the git repository folder called '.gitignore'
2. Add entries for files you with to ignore. For example:
> obj/* - Matches all files in the obj subfolder of the current directory

### .gitignore Entry Rules ###

These are the rules for .gitignore entries:

* Blank lines are ignored
* Lines starting with '#' are comments and are ignored
* Adding a leading slash to the entry will only match the current directory (/*.c matches all .c files in the current directory, but not subdirectories)
* Lines starting with ! are negated
* Regex is allowed: '[Tt]humbs.db' matches 'Thumbs.db' and 'thumbs.db'

### Typical .gitignore Entries ###

* obj/* - Ignores all object files as these can be regenerated by the makefile
* tmp/* - Ignores everything in the 'tmp' folder

## Resources ##

* [Clone the Repository Using the Command Line](https://services.github.com/on-demand/github-cli/clone-repo-cli)
* [The difference between git pull, git fetch and git clone and git rebase](https://blog.mikepearce.net/2010/05/18/the-difference-between-git-pull-git-fetch-and-git-clone-and-git-rebase/)
* [Github Guide to Generating SSH Keys](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

