---
layout: post
title:  "How To Raise an Issue When a Jenkins Build Fails"

date:   2017-07-26 8:51
categories: how-to Jenkins
---
My adventure with Jenkins continues: today I had my first legitimate build failure after I updated a few input files. Unfortunately, the only way I knew that it had failed (because I don't watch Jenkins like a hawk) was to notice that the status reports hadn't been updated since yesterday. Sure enough, build failures. I wish it would tell me.

It turns out that this is a fairly common request, but there's no way to do it natively in Jenkins, so people rely on the [Post-Build Task Plugin](https://wiki.jenkins.io/display/JENKINS/Post+build+task) to do it. It allows you to read the log file for the build, look for specific words or phrases and then execute scripts conditionally based on the search. So, if your build fails, or even if it passes and you want to perform some additional steps, you can use this to handle the outcome intelligently.

I still need to install it and generate an example of its use.

## To-Do ##

* Install the plugin and document the steps
* Generate a Python script to raise issues or otherwise alert me to a build failure
* Document how to use the plugin

## Resources ##

* [Jenkins Post-Build Task Plugin](https://wiki.jenkins.io/display/JENKINS/Post+build+task)
* [Pertinent Stackoverflow Q&A](https://stackoverflow.com/q/11160363/39492)
