---
layout: post
title:  "How To Archive and Retrieve Build Artifacts in Jenkins"

date:   2018-1-16 7:13
categories: how-to jenkins archive
---

I had a vision as I was lying in my bed last night, falling asleep. I saw a brave, beautiful future where Jenkins handled all of my builds, but also archived and served all of the build artifacts for me. In my dream, my builds ran by themselves, turned my Python scripts into executables and then packaged them into a self-extracting installer. Then, I simply typed a URL into my browser and downloaded the most recently-built installer directly from Jenkins.

I'm glad I remembered this vision, because it turns out that it's reality. You can configure Jenkins to retain the build artifacts, archive them and serve them up via a URL. I'll show you how.

## Archiving Build Artifacts ##

I'll create a simple build that doesn't really do anything and configure the build to archive the build artifacts.

1. Open [Jenkins](http://localhost:8080) in your browser (this link will work if you're configured the same way I am).
2. In the upper left corner click on 'New Item'
3. Name the item *Dummy Build*
4. Select *Freestyle Project* and click *OK* to continue.
5. You should now be in the configuration page for the build. Make the following changes:
* Add a description if you want
* Under *Build Environment* check *Delete workspace before build starts*
6. Under *Build* click on *Add build step* and select *Execute Windows batch command*
7. In the *Command* window write we'll write a command to generate a *buildArtifact.txt* file in the Jenkins workspace folder:  
> echo "Hello World!" > %WORKSPACE%\buildArtifact.txt  
8. Under *Post-build Actions* click *Add post-build action* and select *Archive the artifacts*
9. In the *Files to archive* text entry enter the path to the build artifact (Note: the path is relative to the workspace, so this only needs to be the file name):  
> buildArtifact.txt
10. Click *Save* to save the new build.
11. You should now be on the page for the dummy build project - click *Build Now* to execute the build. There should be no errors.

Note: if you want a full directory to be the build artifact, just put the path to the directory in the *Files to archive* entry with no file qualifiers or wildcards.

## Retrieving Build Artifacts via URL ##

If you completed the previous set of steps, you should be at the page for the dummy build you created and should have just executed the build. Follow these steps to retrieve the build artifact:

1. Refresh the page. There should be a new section in the dummy build page that says *Last Successful Artifacts* with one entry: *buildArtifact.txt*
2. Click on *buildArtifact.txt* and verify it says:  
> "Hello World!"
3. You can access the artifact directly via URL. The URL for this dummy build would be:  
> http://localhost:8080/job/Dummy%20Build/lastSuccessfulBuild/artifact/buildArtifact.txt

In general, the URL will be:  
> http://\<Jenkins Server URL\>/job/\<Job Name\>/lastSuccessfulBuild/artifact/\<Artifact File Name\>

If your build artifact is an entire directory or a non-safe file type (such as exe) you can automatically get a ZIP file of it with this URL:  
> http://\<Jenkins Server URL\>/job/\<Job Name\>/lastSuccessfulBuild/artifact/*zip*/archive.zip

## Shortcomings of This Approach ##

I plan to use this approach to retrieve the latest build of scripts and other software that I build, but it's strictly limited to 'latest build'. When I release something I usually like to put it in a zip file that indicates the SVN revision that it was generated from, but in this scheme, the artifact file name **must** be the same for every build. Thus, I have to generate a 'latest release' file (something along the lines of *latestRelease.zip*) instead of a specific release revision (something like *releaseRev8043.zip*).
