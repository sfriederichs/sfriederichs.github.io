---
layout: post
title:  "How To Add Logging to Python Scripts"
updated: 2017-12-08 10:58
date:   2017-12-08 10:58
categories: how-to python logging
---

Logging is one of the most useful capabilities to have in your script. A good logging framework lets you intelligently sift through the myriad different debugging, informational and error messages that come up in your application and it leaves the standard output (i.e., the destination for *print* statements) clean for actual programmatic output instead of debug information. Python has a good logging library that ships with it and it's easy to enable logging for your application. Below are several basic examples of logging.

## Logging to the Console ##

If you want your output to show up in the command prompt where you execute your script or program you can use the following code:

{% highlight python %}
#!/usr/bin/python

#Import the logging library
import logging

logFilePath = "logs/default.log"

#Set the default log level
#Options are (in order of increasing priority):
# * logging.DEBUG
# * logging.INFO
# * logging.WARNING
# * logging.ERROR
#Log levels allow all higher priority messages to go through, so if you set the level to DEBUG,
#you get every single log message, but if you set it to WARNING you only get WARNING and 
#ERROR

logLevel = logging.DEBUG 

#This call configures logging to a file at logFilePath with a level of logLevel
logging.basicConfig(level=logLevel)

#Basic logging - debug level
#Note: the logging functions do not support typical Python string concatenation
#E.g. logging.debug("Logging is configured - Log File " + str(logFilePath)) 
#The above example will produce an error
#You have to use printf-style casting as seeen below
#Note that when in doubt about data types and which cast you should use remember that you can just use %s 
#and use Python casts to make anything a string

logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 
logging.info("Informational... uh... *information*")
logging.warn("You have been put on notice")
logging.error("You done messed up")
{% endhighlight %}

Technically, this outputs all of the log data to the standard error output, so the standard output is clean for *print* statements and output redirection.
The log data that this produces is:

> DEBUG:root:Logging is configured - Log Level 10 , Log File: logs/default.log  
> INFO:root:Informational... uh... *information*  
> WARNING:root:You have been put on notice  
> ERROR:root:You done messed up  

## Logging to a File ##

This script directs the output to a file:

{% highlight python %}
#!/usr/bin/python

import logging

logFilePath = "logs/default.log"
logLevel = logging.DEBUG 

#The new thing here is the 'filemode' option - it determines how the data is written to the file
# 'a' - This will append the data to the end of the file. This behavior is the default if you 
# don't specify the option
# 'w' - This will overwrite the existing file every time the script is called
 
logging.basicConfig(filename=logFilePath,filemode='a',level=logLevel)

logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 
{% endhighlight %}

## Formatting Log Messages ## 

The default log format is pretty bland - it's just the log level, name of the logger and the message. One nice thing to add is the time. You can update the format for the log message by adding a 'format' option to the call to initialize the logger. The code looks like this:

{% highlight python %}
#!/usr/bin/python

import logging

logFilePath = "logs/default.log"
logLevel = logging.DEBUG 

# The 'format' option is new here:
logging.basicConfig(format='%(asctime)s - %(threadName)s - %(funcName)s  - %(levelname)-8s %(message)s',filename=logFilePath,filemode='a',level=logLevel)

logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 
{% endhighlight %}

That produces this output:

> 2017-12-08 14:06:27,731 - MainThread - \<module\>  - DEBUG    Logging is configured - Log Level 10 , Log File: logs/default.log

Valid fields/attributes to insert into the format string include:
* asctime
* thread
* levelname
* message
* funcName

And many others. See [here](https://docs.python.org/2/library/logging.html) in section 15.7.7


## Logging to a File and the Console Simultaneously ##

Very often you'll want a log file *and* to see the messages on the console. You can do this - it is a bit more complicated though. 

This code will do the trick:

{% highlight python %}
#!/usr/bin/python

import logging

logFilePath = "logs/default.log"
logLevel = logging.DEBUG 
formatStr = '%(asctime)s - %(threadName)s - %(funcName)s  - %(levelname)-8s %(message)s'

logging.basicConfig(format=formatStr,filename=logFilePath,filemode='a',level=logLevel)

#Here's all the new stuff to handle the configuration of the console output

#First, generate a formatter object with the common format
formatter = logging.Formatter(formatStr)

#Then, retrieve a StreamHandler - this outputs log data to the console
console = logging.StreamHandler()

#Now configure the stream handler to the same settings as the file handler
#Note, however that you don't need them both to be configured the same - it may be
#entirely appropriate to have different settings for console vs. file.

console.setLevel(logLevel)
console.setFormatter(formatter)

#And finally, attach the console handler to the logger so the output goes both places
logging.getLogger('').addHandler(console)

#This will now show up on the console and in the log file
logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 
{% endhighlight %}

## Logging to a Time/Date Stamped File ##

If you want to log to a new and unique file based on the current time and date, use this code example:

{% highlight python %}

import datetime

logFilePath = datetime.datetime.now().strftime('../logs/log_%H_%M_%d_%m_%Y.log')

{% endhighlight %}

Now, this won't work if the file doesn't exist - you'll get an error like this:
{% highlight console %}
Traceback (most recent call last):
  File "src\invoiceParser.py", line 110, in <module>
    main()
  File "src\invoiceParser.py", line 92, in main
    logging.basicConfig(filename=logFilePath,filemode='a',level=logLevel,format=formatStr)
  File "C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\lib\logging\__init__.py", line 1976, in basicConfig
    h = FileHandler(filename, mode)
  File "C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\lib\logging\__init__.py", line 1143, in __init__
    StreamHandler.__init__(self, self._open())
  File "C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\lib\logging\__init__.py", line 1172, in _open
    return open(self.baseFilename, self.mode, encoding=self.encoding)
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\sfrie\\Dropbox\\Projects\\logs\\alogfile_22_27_15_04_2020.log'
{% endhighlight %}


## Resources ##

* [StackOverflow answer on logging to files and console simultaneously](https://stackoverflow.com/a/23681578)
* [Python 2.7 logging documentation](https://docs.python.org/2/library/logging.html)





