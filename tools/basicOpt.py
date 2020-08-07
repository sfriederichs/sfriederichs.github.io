""""
Blog Post Generator Script
Version 0.1
Author: Stephen Friederichs
License: Beerware License: If you find this program useful and you ever met me, buy me a beer. (I like Saisons)
This script demonstrates the use of the getopt library to parse command-line arguments passed to the Python script.
The following command-line parameters control the behavior of the script:
-h, --help - Shows this screen and exits
-v, --version - Display version information
-l, --license - Display author and license information
-f, -logfilepath=<PATH> - Set the log file path
"""

import textwrap
import logging
import getopt
import sys
import re
import os
import shutil
import datetime


logFilePath = "default.log"
logLevel = logging.DEBUG 

DEFAULT_POST_TEMPLATE_PATH = "./res/postTemplate.md"
DEFAULT_POSTS_DIR = "../_posts/"

def prettyPrint(uglyString):
    """This function properly formats docstrings for printing on the console"""
    
    #Remove all newlines
    uglyString = uglyString.replace('\n','').replace('\r','')
    #Use textwrap module to automatically wrap lines at 79 characters of text
    print(textwrap.fill(uglyString,width=79))
    

def license():
    for line in __doc__.splitlines()[3:5]:
        prettyPrint(line)
        
def help():
    for line in __doc__.splitlines()[5:]:
        prettyPrint(line)

def version():
    prettyPrint(__doc__.splitlines()[2])
 
def progId():
    prettyPrint(__doc__.splitlines()[1])

def reduceTitle(title):
    removeList = ["script","scripts","how","to","in","with"]
    shortTitle = title.lower()
    for x in removeList:
        shortTitle = shortTitle.strip().replace(x.lower(),"")
    shortTitle = shortTitle.strip().replace(" ","-").strip()
    return shortTitle
    
progId()

try: 
    opts, args = getopt.getopt(sys.argv[1:], 'hvlf:', ['help','version','license','logfile='])    
except getopt.GetoptError:
    print("Bad argument(s)"  )
    help()
    sys.exit(2)   
    
for opt, arg in opts:                 
    if opt in ('-h', '--help'):     
        help()                         
        sys.exit(2)                 
    elif opt in ('-l','--license'):    
        license()
    elif opt in ('-f','--logfilepath='):
        logFilePath=str(arg)
    elif opt in ('-v','--version'):
        version()
    else: 
        help()
        sys.exit(2)
        
logging.basicConfig(filename=logFilePath,filemode='a',level=logLevel)

logging.debug("Logging is configured - Log Level %s , Log File: %s",str(logLevel),logFilePath) 

#Get the post date string
postDateStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
fileDateStr = datetime.datetime.now().strftime("%Y-%m-%d")

#Ask the user for the post title
while True:
    postTitle = input("Please enter a title: " )
    if "y" in (input("Verify post title (y/n): ") or "y"):
        break

#Generate the reduced title for the file name
shortTitle = reduceTitle(postTitle)

#Load the template

with open(DEFAULT_POST_TEMPLATE_PATH,"rt") as templateHandle:
    postTemplate = templateHandle.read()
    
#Generate the regular expressions to replace date and title
dateRe = re.compile("date:")
titleRe = re.compile("title:")

#Replace the date line
postTemplate = dateRe.sub(str("date: " + postDateStr),postTemplate)

#Replace the title line
postTemplate = titleRe.sub(str("title: " + postTitle),postTemplate)

#Generate the file name
postFileName = fileDateStr + "-" + shortTitle + ".md"
postFilePath = os.path.join(DEFAULT_POSTS_DIR,postFileName)

#Save the modified buffer as the default post name
with open(postFilePath,"wt+") as postHandle:
    postHandle.write(postTemplate)
    
#Open the file up in nano
os.system("nano " + postFilePath)

while True:
    commitMsg = input("Enter a commit message: " )
    if "y" in (input("Accept message? ") or "y"):
        break
        
os.chdir("..")
os.system("git add _posts/*")
os.system("git commit -m \"" + str(commitMsg) + "\"")
os.system("git push origin master")


