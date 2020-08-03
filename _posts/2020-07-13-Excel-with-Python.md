---
layout: post
title:  "How-to Use Python and Excel Together"
date:   2020-07-13 8:58

categories: how-to python3 excel
---


## Introduction ##

I have a tedious task to perform which involves reading information from SVN and updating a review checklist with the information. The 'hard' part of this whole process is the actual review.
The 'easy' part is looking up the revision information, paths, file names, etc and putting them into the spreadsheet. Despite the fact that this is the 'easy' part it's also very easy to 
mess up. This tedious copy and paste process has many steps, requires significant working memory and can be easily confusing. The worst part is that even if you do the 'hard' part well, you 
need to do the 'easy' part _perfectly_ because if you mess up a revision or a path there's no way to link the work you did to the actual artifact being reviewed.

So, why not create a script?

Python can read SVN and filesystem information. It can read Excel files. It can write excel files. So, why not automate it?

To do so, I will need to be able to write Excel files with Python 3. More specifically, I will need to modify an existing template with information I glean from SVN and other sources.

Thus, this post will contain information on how to read, write and modify Excel files with Python 3

## OpenPyXL ##

If you need a library that can read and write xlsx files (not just xls files), you want OpenPyXL. I don't think there's
any disagreemnt on that on Stack Overflow. As far as I can tell, it's the best way to write .xlsx 
files in Python.

### Installation ###

OpenPyXL installed just fine using pip:

{% highlight console %}

C:\users\sfrieder>pip3 install openpyxl
Collecting openpyxl
  Downloading https://files.pythonhosted.org/packages/f9/d8/be9dc2b17ba47f1db9032ed7e19915145b4c093f66bb36f0d919d2dc8ccf/openpyxl-3.0.4-py2.py3-none-any.whl (241kB)
     |████████████████████████████████| 245kB 172kB/s
Collecting jdcal (from openpyxl)
  Downloading https://files.pythonhosted.org/packages/f0/da/572cbc0bc582390480bbd7c4e93d14dc46079778ed915b505dc494b37c57/jdcal-1.4.1-py2.py3-none-any.whl
Collecting et-xmlfile (from openpyxl)
  Downloading https://files.pythonhosted.org/packages/22/28/a99c42aea746e18382ad9fb36f64c1c1f04216f41797f2f0fa567da11388/et_xmlfile-1.0.1.tar.gz
Installing collected packages: jdcal, et-xmlfile, openpyxl
  Running setup.py install for et-xmlfile ... done
Successfully installed et-xmlfile-1.0.1 jdcal-1.4.1 openpyxl-3.0.4
WARNING: You are using pip version 19.2.3, however version 20.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
{% endhighlight %}

### Reading Excel Files ###

I'm going to base all of this off of a tutorial I found [here](http://zetcode.com/python/openpyxl/).

It looks pretty simple for most things. Here's their simple code on how to read a cell:

{% highlight python %}

import openpyxl

book = openpyxl.load_workbook('sample.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']
a3 = sheet.cell(row=3, column=1)

print(a1.value)
print(a2.value) 
print(a3.value)
{% endhighlight %}

Except I don't see a good answer on how to select a sheet. I see the book.active thing and I don't think it's what I want. I want to select by name.

### Selecting a Sheet by Name ###

Turns out this is simple too. See [this](https://stackoverflow.com/questions/36814050/openpyxl-get-sheet-by-name/36814135) StackOverflow answer. There's a dictionary of sheets that you can index by name. Like this:

{% highlight python %}
from openpyxl import load_workbook
wb2 = load_workbook('test.xlsx')
ws4 = wb2["New Title"]  
{% endhighlight %}

### Getting a List of Sheet Names ###

This one's easy too. I'm beginning to think using OpenPyXL will be easy.

{% highlight python %}
from openpyxl import load_workbook
wb2 = load_workbook('test.xlsx')
print(wb2.sheetnames)
['Sheet2', 'New Title', 'Sheet1']
{% endhighlight %}

### Writing Data to Cells ###

Once again, easy.

From the tutorial I mentioned earlier:

{% highlight python %}

from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 1
sheet.cell(row=2, column=2).value = 2

book.save('write2cell.xlsx')
{% endhighlight %}

It's worth noting here that OpenPyXL uses 1-based indexing: the cell at row 2 column 2 is "B2", not "C3".

### Getting a Range of Cells ###

There are times when you want to pluck a range of cells and work with them. Here's how you can do that:

You can do it by rows. This code retrieves all rows between 3 and 10 (inclusive) and returns them as a list of lists :

{% highlight python %}
import openpyxl

wbPath = "test.xls"

wb = openpyxl.load_workbook(wbPath)

sheet = wb.sheets["Sheet1"]

rows = testSheet.iter_rows(min_row = 3, max_row=10)

for row in rows:
    for cell in row:
        print(str(cell.value))
    
{% endhighlight %}

And, to do the same thing with columns:

{% highlight python %}
import openpyxl

wbPath = "test.xls"

wb = openpyxl.load_workbook(wbPath)

sheet = wb.sheets["Sheet1"]

cols = testSheet.iter_cols(min_col = 3, max_col=10)

for col in cols:
    for cell in col:
        print(str(cell.value))
    
{% endhighlight %}

### Retrieving Just Data (Not Formulas) From a Workbook ###

I had a bit of a shock when I opened a workbook, specified a range of cells and tried to get values: I was getting formulas instead of the *result* of formulas. 
There's a way to avoid this: load the workbook as 'data only'. You do that like this:

{% highlight python %}

import openpyxl

wb = openpyxl.load_workbook(wbPath,data_only=True)

{% endhighlight %}

This way, when you acces the value of a cell, you get the result of the formula.

### OpenPyXL Notes ###


OpenPyXL uses 1-based indexing: the cell at row 2 column 2 is "B2", not "C3".


## xlrd, xlt and xlutils ##

There are multiple ways to read and write Excel files in Python. One way to do it is a collection of libraries that all work together:

* [xlrd](https://pypi.org/project/xlrd/)for reading
* [xlwt](https://pypi.org/project/xlwt/) for writing, and
* [xlutils](https://pypi.org/project/xlutils/) for miscellaneous functions

HOWEVER!!! MAJOR CAVEAT THAT BORKED MY ATTEMPT TO USE THESE LIBRARIES FOLLOWS!

*xlwt CANNOT write xlsx or xlsm files - only the older xls files*

I put a lot of effort into xlrd, xlwt and xlutils - all for nothing because my application
requires that I write .xlsx files. The information here will stay, because it's useful. How is it useful you ask? Well, if there's one thing I've found it's that you have to use the right tool for the job - and there's sadly many tools out there to read and write Excel files in Python.  It's not enough to just pick one and say 'this is the only one I'm going to use'. One big reason: speed. I've found that some libraries are much slower than others. Thus, if you only, for example, needed to _read_ Excel files, xlrd might be perfect for you over another, more comprhensive library that is much slower. You really have to watch out on large files sometimes - using a different, less featureful, but faster library may be useful.

### Installation ###

Here's what I did on a Windows 10 PC with Python 3.81 installed:

{% highlight console %}

pip3 install xlwt
pip3 install xlutils
pip3 install xlrd

{% endhighlight %}

I have both Python 2.7 and 3 installed, so in order to make sure that pip installed the libraries for Python 3 I had to use _pip3_ instead of _pip_.

## Example Code ##

Rather than write a lot of notes about how to use the libraries, I'll just show you an example program. It
does two things: reads specific data from an Excel file, and finds and modifies a specific incorrect value
within an Excel file.  

For reference, the Excel data being used looks like this:

| Name              | Telephone     | Address                           | Notes                                         |
|-------------------|---------------|-----------------------------------|-----------------------------------------------|
| Don Juan          | 1234567890    | 1121 Nowhere St. Tokyo Japan      | I like this guy                               |
| Jean-Luc Picard   | NA            | France, somewhere                 | Why does a Frenchman have an English accent?  |

The script will read the passed Excel file and print the data. Then, it will find and correct Jean-Luc's Address entry and save the result in a new Excel file.

{% highlight python %}


"""----------------------------------------------------------------------------
Excel Example
Author: Stephen Friederichs
Version 0.1

This script is an example of how to use Python to interact with Excel 
workbooks.

Example usage:

python xlExample.py -r <spreadsheet path>
 
Command-line switches:

-r, --read - Specify the path to an Excel file to read
-h, --help - Show this helpful information

"""

import xlwt
from xlutils.copy import copy as xlCopy   #I don't like just having a bare 'copy' around - make it specific
import textwrap
import getopt
import sys
import os
import logging
import xlrd
import shutil
import distutils.dir_util
import itertools

"""Global Variables"""
logFormatStr = '%(asctime)s -- %(funcName)s  - %(levelname)-8s %(message)s'
logLevel =  logging.DEBUG


"""Utility Functions - Common to all scripts"""

def prettyPrint(uglyString):
    """This function properly fomats docstrings for printing on the console"""
    
    #Remove all newlines
    uglyString = uglyString.replace('\n','').replace('\r','')
    #Use textwrap module to automatically wrap lines at 79 characters of text
    print(textwrap.fill(uglyString,width=79))
    
    
def help():
    for line in __doc__.splitlines()[4:]:
        prettyPrint(line)
    
def version():
    for line in __doc__.splitlines()[1:4]:
        prettyPrint(line)

"""Custom Functions"""

"""Return a list of tuples where each tuple is a row with the deata specified in the colHeaders list"""
def getSheetData(sheet,colHeaders):
    return zip(*[getColData(sheet,colHeader) for colHeader in colHeaders])
    
"""Return a column number for the column with the given colHeader"""
def getColNum(sheet,colHeader):
   
    headerRow=sheet.row(0)
                    
    for column,cell in enumerate(headerRow):
        if colHeader == str(cell.value):
            return int(column)
    
    raise ValueError("Cannot find " + str(colHeader) + " in sheet "+ str(sheet.name) +" among columns " + str(headerRow) )

"""Return a list of data values for the given header"""
def getColData(sheet,colHeader):
    return [str(cell.value) for cell in sheet.col(getColNum(sheet,colHeader))[1:]]
    
"""Return a list of sheet objects from the workbook object with the given sheetNames"""
def getWbSheets(xlWbPath,sheetNames):
    sheets = None
    xlWbPath = validatePath(xlWbPath)
    
    with xlrd.open_workbook(xlWbPath) as xlWbData:
        logging.debug("Reading spreadsheet @ %s",xlWbPath)
        sheets = {sheetName:sheet for (sheetName,sheet) in [(sheetName,xlWbData.sheet_by_name(sheetName)) for sheetName in sheetNames]}
    
    return sheets
        

"""Pass a list of sheet names to retrieve from an xlwt workbook object"""
def xlwtGetWbSheets(xlWbObj,sheets):
    retVal = {}
    try:
        for idx in itertools.count():
            sheet=xlWbObj.get_sheet(idx)
            if str(sheet.name) in sheets:
                retVal[sheet.name]=sheet
    except IndexError:
        pass
    return retVal
    
def formatPath(path):
    try:
        normPath = os.path.normpath(path)
        absPath = os.path.abspath(normPath)
    except ValueError as ex:
        logging.error("Couldn't format path %s : %s",str(path),str(ex))
        return None
    return absPath
        
def validatePath(path):
    formattedPath = formatPath(path)
    if not os.path.exists(path):
        raise ValueError("Path "+str(formattedPath)+" does not exist")
    else:
        return formattedPath
        
"""Main"""
        
def main():
    global logFormatStr
    global logLevel
    
    logging.basicConfig(format=logFormatStr,level=logLevel)
    
    """Main Function"""
    readPath=None
    
    version()

    try: 
        opts, args = getopt.getopt(sys.argv[1:], 'hr:', ['help','read'])    
    except getopt.GetoptError:
        print("Bad argument(s)")
        sys.exit(2)                 

    logging.debug("Opts/args: %s",str(opts))
    
    for opt, arg in opts:     
        logging.debug("Option %s, argument %s",str(opt),str(arg))
        if opt in ('-h', '--help'):     
            help()                         
            sys.exit(2)                 
        elif opt in ('-r','--read'):
            try:
                readPath = validatePath(formatPath(str(arg)))
            except ValueError:
                print("Specified path not found: "+str(arg))
                sys.exit(2)
        else: 
            print ("Invalid command-line option " + str(opt))
            help()
            sys.exit(2)

            
    #Validate command-line options
    
   
    if readPath is None:
        print("Must specify read path")
        help()
        sys.exit(2)
        
    try:
       
        if readPath is not None:
            #Approach one - not using any helper functions
            with xlrd.open_workbook(readPath) as xlWbData:
                print("Sheets in the workbook:")
                print(xlWbData.sheet_names())
                
                participantsSheet = xlWbData.sheet_by_name("Participants")
                print("\r\nHeader row data:")
                print(str(participantsSheet.row(0)))
                
                print("\r\nNumber of rows (total):")
                print(str(participantsSheet.nrows))
                
                print("\r\nNumber of data rows:")
                print(str(participantsSheet.nrows-1))
                
                print("\r\nData rows:")
                for i in range(1,participantsSheet.nrows):
                    print(str(participantsSheet.row(i)))
                
                print("\r\nNames only:")
                print(str(participantsSheet.col(0)[1:]))    #The indexing removes the header row
                
            #Approach two - using my helper functions
            #These functions help you read data from spreadsheets by names, not numbers
            sheets = getWbSheets(readPath,["Participants"])
            participants = getSheetData(sheets["Participants"],["Name","Telephone","Address","Notes"])
            
            for participant in participants:
                print(str(participant))
                
            #Step 2 - Modifying and saving in a new file
            
            print("Modifying " + str(readPath))
            #Open the original
            rb = xlrd.open_workbook(readPath)
            
            #Copy it to a new, writeable workbook object
            wb = xlCopy(rb)
            
            #Find the cell coordinates for Jean-Luc's address
            #Sadly, it doesn't appear that xlwt has the ability to read data - at least, not as well
            #as xlrd. Thus, you have to figure out where the data you want to change is located with xlrd
            #before changing it in the new workbook with xlwt
            
            #So, to do this, we'll find out which cell contains the data we want to change using xlrd
            
            participantsSheet = rb.sheet_by_name("Participants")
            
            colIdx = None
            rowIdx = None
            
            #Find the column number for 'Address'
            for idx,header in enumerate(participantsSheet.row(0)):
                if "Address" in str(header):
                    colIdx = idx
                    break
                    
            #Find the row that contains Jean-Luc        
            for idx in range(1,participantsSheet.nrows):
                if "Jean-Luc" in str(participantsSheet.row(idx)):
                    rowIdx = idx
                    break
            print("Jean-Luc's address cell is on the Participants sheet at "+str(rowIdx)+","+str(colIdx))
            
            #Find the participants sheet in the writeable object
            #Oops! xlwt doesn't have a sheet_by_name option, so you have to find the sheet manually
            #https://stackoverflow.com/questions/14587271/accessing-worksheets-using-xlwt-get-sheet-method
            participantsSheet = None
            try:
                for idx in itertools.count():
                    sheet=wb.get_sheet(idx)
                    if "Participants" in str(sheet.name):
                        participantsSheet=sheet
            except IndexError:
                pass
                
            if participantsSheet is None:
                raise ValueError("No Participants sheet in "+str(modifyPath))
                    
            participantsSheet.write(rowIdx,colIdx,"Le Barre, France")

            
            #Save the modified file
            wb.save("modified.xlsx")
            print("Saved modified file at "+str(formatPath("modified.xlsx")))
            
            pass 
    except Exception as e:
        raise

        
       
if __name__=="__main__":
    main()    
        


{% endhighlight %}




## Notes ##

I will document anything interesting or unique about specific workflows with xlrd, xlwt and xlutils here.

### Modifying Existing Excel Files With xlrd and xlwt ###

So, it seems, according to [this](https://stackoverflow.com/a/26958437/39492) answer, that the way to do this is to:

1. Use xlrd to read the excel file (i.e., 'workbook')
2. Copy the workbook with xlutils _copy_ function
3. Modify the workbook in memory
4. Save it to a new file.

The code snippet they used is here:

{% highlight python %}

#xlrd, xlutils and xlwt modules need to be installed.  
#Can be done via pip install <module>
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("names.xls")
wb = copy(rb)

s = wb.get_sheet(0)
s.write(0,0,'A1')
wb.save('names.xls')

{% endhighlight %}

I'll create a simple Excel file with some information in it, load it, modify it, and finally, save it in a new file.

### Writing to Excel Files ###

*xlwt CANNOT write .xlsx or .xlsm files, only .xls!!*

It's worth noting that xlwt and xlrd do not have equivalent APIs. I have no idea why this is, but the fact 
is that there's no easy way to iterate over the sheets in a workbook or to retrieve a sheet by name with
xlwt. xlrd has it just fine, but not xlwt. So you need a workaround, found [this](https://stackoverflow.com/questions/14587271/accessing-worksheets-using-xlwt-get-sheet-method). 

It's likely you or I will find more issues such as this while working with xlwt.

The upshot of most of this is that you'll have to do the heavy-duty reading using xlrd and then sparingly 
use xlwt to modify the data.

## Resources ##

[SO - Edit existing excel workbook and sheets with xlrd and xlwt](https://stackoverflow.com/questions/26957831/edit-existing-excel-workbooks-and-sheets-with-xlrd-and-xlwt)

[xkrd API Reference](https://xlrd.readthedocs.io/en/latest/api.html)

[SO - Workaround to get sheets by name with xlwt](https://stackoverflow.com/questions/14587271/accessing-worksheets-using-xlwt-get-sheet-method)

[OpenPyXL Examples](http://zetcode.com/python/openpyxl/)