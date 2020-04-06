---
layout: post
title:  "How To Return Errors from Windows Batchfiles"
date:   2017-07-24 8:06
categories: how-to Jenkins
---

I'm running a Jenkins server at work on a Windows machine. The only way I've found to effectively run scripts, lock files in SVN and check things back in is via Windows batch files. However, I'm seeing that when the script fails the task doesn't fail. This is not good: I need that visibility into it if it fails, especially as I expand my use of the server.

To that end I'm adding error checking and cleanup to the batch script.

Existing batch file:

> svn lock status_reports\Verification_Trace_Status_Brief.txt --username XXXX --password XXXX
>
> python tools\vTraceStatus\src\vtraceStatus.py -i "%WORKSPACE%" -r WARNING -b > status_reports\Verification_Trace_Status_Brief.txt
>
> svn commit status_reports\Verification_Trace_Status_Brief.txt -m "Jenkins automatic status update" --username XXXX --password XXXX

When the call to the Python script fails, the batch file will happily recommit a blank status report and return a passing status back to Jenkins. Jenkins has no idea that anything went wrong and neither do I - until I'm getting yelled at by a PM for a blank status report.

You can modify the script to look for errors,pass back status and clean up everything in case of an error:

> svn lock status_reports\Verification_Trace_Status_Brief.txt --username XXXX --password XXXX
>
> python tools\vTraceStatus\src\vtraceStatus.py -i "%WORKSPACE%" -r WARNING -b > status_reports\Verification_Trace_Status_Brief.txt \|\| goto :scriptError
>
> svn commit status_reports\Verification_Trace_Status_Brief.txt -m "Jenkins automatic status update" --username XXXX --password XXXX
>
> exit /b 0
>
> :scriptError
>
> svn revert status_reports\Verification_Trace_Status_Brief.txt --username XXXX --password XXXX
>
> svn unlock status_reports\Verification_Trace_Status_Brief.txt --username XXXX --password XXXX
>
> exit /b 2

There are several additions:

* The addition of the goto statement at the end of the line that calls the script sends the batch file to the error handling portion in case of an error in executing the script.
* The addition of the 'exit /b 0' statement tells the batch file to exit with no error (code of 0) if there were no script errors. The '/b' tells exit to only exit the batch file, not the command interpreter.
* The error handling under *scriptError* cleans everything up to th way it was before if the script fails and then returns an error code of 2 (non-zero values are errors).

## Resources ##

* [Relevant StackoverFlow Question](https://stackoverflow.com/q/734598/39492)