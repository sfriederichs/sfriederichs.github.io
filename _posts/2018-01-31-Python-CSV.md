---
layout: post
title:  "How To Work With CSV Data in Python"

date:   2018-01-31 7:07
categories: how-to python csv
---

Comma Separated Variable (CSV) is a useful and widely-supported format for storing spreadsheet-style data. Python has built-in libraries for making working with CSV files easy. This how-to will show you how to:

* Write data to CSV files
* Read data from CSV files (soon)

## Writing Data to CSV Files ##

Here's a (*very*) minimum example of writing data to a CSV file.

{% highlight python %}
import csv

with open('data.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow([1,2,3,4,5])
    csvWriter.writeRow([6,7,8])
{% endhighlight %}

This produces a file called 'data.csv' with the following content:

> 1,2,3,4,5  
> 6,7,8

It's fairly obvious from a high-level viewpoint what's going on here, but let's take a second to review some of the low-level aspects of what just happened.

1. We opened a file handle to 'data.csv' for writing and named it csvFile. The *with* keyword will automatically clean up the file handle when the indented section is left.
2. We initialized a CSV writer object by passing the file handle.
3. We wrote a single row via the writer. Despite appearances, we didn't write raw string data to the file. The value passed to *writerow* is a list of values and it's just a coincidence that it's also comma-separated. You can pass any list as a row.
4. Not all rows need the same number of elements in them. 
5. All data written in the CSV file is written as a string. It's the same data as if you used Python's built-in casting functions on whatever data you were writing.
6. Since the file format is *Comma* Separated Variable, all values will be separated by commas. Rows are separated by newlines. On Windows with Python 2.7 this was a two carriage returns (ASCII 0x0D) and then a linefeed (ASCII 0x0A). This seems excessive.

It's also worth noting that we're using a 'raw' CSV writer. There's an alternative: a dictionary writer. I'll investigate that later.

## Resources ##

* [Python CSV Library Documentation](https://docs.python.org/2/library/csv.html)
