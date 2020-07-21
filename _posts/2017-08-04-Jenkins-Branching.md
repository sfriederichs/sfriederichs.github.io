---
layout: post
title:  "Best Practices - Use SVN Branches With Jenkins"

date:   2017-08-04 9:40
categories: best-practices Jenkins
---

I've decided to add a new category to the site alongside How-To's: Best Practices. 

This is where I'll store my lessons for not stepping on my own two feet when doing engineering things.

Today's lesson: Use branches with Jenkins.

Issue: I use scripts to track the status of various aspects of our tracing effort for a customer, but I'm continually updating the scripts to add new features. In the process, I break the scripts and must fix them. This presents difficulties if I break a script that Jenkins is using to automatically generate status: the task fails and the loss of organization causes the team to go feral and eat each other. We've lost three interns this week and we're out of barbeque sauce.

Solution: Keep separate development and release branches for your scripts so Jenkins is always running the tested release branch and you can play in the development branch. 

Yes, I know: I'm waaaay late to the party in this respect. Software folks everywhere will scoff and say that should be standard practice, but let me tell you in the engineering world (at least, most places I've worked) it's NOT and it's something I've wrestled with my entire career.

