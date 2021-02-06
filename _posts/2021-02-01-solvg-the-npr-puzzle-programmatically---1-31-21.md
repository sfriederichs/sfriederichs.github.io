---
layout: post
title: Solving the NPR Puzzle Programmatically - 1-31-21
date: 2021-02-01 19:46
categories: puzzle python
---

## Introduction ##

If you listen to NPR on Sundays you'll be familiar with 'The Puzzle'. 'The Puzzle' is wordplay game set up by NPR's puzzle master Will Shortz. Each week there's a 
qualifying puzzle question - answer it correctly, submit your answer, and if you get chosen from the correct answers you get to play a wordplay game with Will on 
Sunday.

I've long considered that many of these puzzles could be solved programmatically. This week's puzzle is one that I'm sure I can write a script to figure out.

This week's puzzle is this:

If you start in Montana, you could drive to South Dakota, then Iowa. If you take the postal abbreviations for these states (MT, SD, IA) and rearrange the letters, 
you can spell the word 'amidst'. 
If you drive through four states, there is at least one word that you can build in a similar way. What four states can you drive through, and what word can you 
make?

This should be doable with Python. So I'm going to try.

## Approach ##

First, I need some raw data. I need to know which states border other states and what their abbreviations are.

The second one is simple, in fact, there's a Python dictionary of states and their abbreviations on Gist [here](https://gist.github.com/rogerallen/1583593).

There's a list of states and which other states border them [here](https://thefactfile.org/u-s-states-and-their-border-states/)

I'm going to copy the table and use regex to parse it into a data structure.

In order to determine if the produced word is an English word, I'm going to use a spellchecker library as described [here](https://stackoverflow.com/a/3789057/39492)

To generate all possible permutations of the letters comprising the four abbreviations, apparently I can use Python's built-in itertools as
described [here](https://stackoverflow.com/a/8306692/39492).

So, what I'll do is parse the state border data from the website using regex to produce a dictionary with the keys being states and the values being a list
of other states that border them. I'll use the state abbreviation lookup to change all of the state names to abbreviations when I generate the dictionary.

Then, I'll generate a string of the letters of the abbreviations in each path through four states. I'll generate the paths by going through the dictionary key by
key and then going through each bordering state and finding its bordering states and so on until I've generated all of the paths through four states. Then I'll
generate all possible permutations of each path and check each against the dictionary to figure out if it's a word.

## Parsing State Border Data ##

So all I did was copy and paste the table from the website into a multi-line string in Python. The result looks like this:

{% highlight python %}

stateBorderData = """
1.	Alabama	Mississippi, Tennessee, Florida, Georgia	4
2.	Alaska	None	None
3.	Arizona	Nevada, New Mexico, Utah, California, Colorado	5
4.	Arkansas	Oklahoma, Tennessee, Texas, Louisiana, Mississippi, Missouri	6
5.	California	Oregon, Arizona, Nevada 3
6.	Colorado	New Mexico, Oklahoma, Utah, Wyoming, Arizona, Kansas, Nebraska	7
7.	Connecticut	New York, Rhode Island, Massachusetts	3
8.	Delaware	New Jersey, Pennsylvania, Maryland	3
9.	Florida	Georgia, Alabama	2
10.	Georgia	North Carolina, South Carolina, Tennessee, Alabama, Florida	5
11.	Hawaii	None	None
12.	Idaho	Utah, Washington, Wyoming, Montana, Nevada, Oregon	6
13.	Illinois	Kentucky, Missouri, Wisconsin, Indiana, Iowa, Michigan	6
14.	Indiana	Michigan, Ohio, Illinois, Kentucky	4
15.	Iowa	Nebraska, South Dakota, Wisconsin, Illinois, Minnesota, Missouri	6
16.	Kansas	Nebraska, Oklahoma, Colorado, Missouri	4
17.	Kentucky	Tennessee, Virginia, West Virginia, Illinois, Indiana, Missouri, Ohio	7
18.	Louisiana	Texas, Arkansas, Mississippi	3
19.	Maine
(The state which borders only one other U.S. state.)	New Hampshire	1
20.	Maryland	Virginia, West Virginia, Delaware, Pennsylvania	4
21.	Massachusetts	New York, Rhode Island, Vermont, Connecticut, New Hampshire	5
22.	Michigan	Ohio, Wisconsin, Illinois, Indiana, Minnesota (water border)	5
23.	Minnesota	North Dakota, South Dakota, Wisconsin, Iowa, Michigan (water border)	5
24.	Mississippi	Louisiana, Tennessee, Alabama, Arkansas	4
25.	Missouri (The state which touches the most other states.)	Nebraska, Oklahoma, Tennessee, Arkansas, Illinois, Iowa, Kansas, Kentucky	8
26.	Montana	South Dakota, Wyoming, Idaho, North Dakota	4
27.	Nebraska	Missouri, South Dakota, Wyoming, Colorado, Iowa, Kansas,	6
28.	Nevada	Idaho, Oregon, Utah, Arizona, California	5
29.	New Hampshire	Vermont, Maine, Massachusetts	3
30.	New Jersey	Pennsylvania, Delaware, New York	3
31.	New Mexico	Oklahoma, Texas, Utah, Arizona, Colorado	5
32.	New York	Pennsylvania, Rhode Island (water border), Vermont, Connecticut, Massachusetts, New Jersey	6
33.	North Carolina	Tennessee, Virginia, Georgia, South Carolina	4
34.	North Dakota	South Dakota, Minnesota, Montana	3
35.	Ohio	Michigan, Pennsylvania, West Virginia, Indiana, Kentucky	5
36.	Oklahoma	Missouri, New Mexico, Texas, Arkansas, Colorado, Kansas	6
37.	Oregon	Nevada, Washington, California, Idaho	4
38.	Pennsylvania	New York, Ohio, West Virginia, Delaware, Maryland, New Jersey	6
39.	Rhode Island	Massachusetts, New York (water border), Connecticut	3
40.	South Carolina	North Carolina, Georgia,	2
41.	South Dakota	Nebraska, North Dakota, Wyoming, Iowa, Minnesota, Montana	6
42.	Tennessee
(The state which touches the most other states.)	Mississippi, Missouri, North Carolina, Virginia, Alabama, Arkansas, Georgia, Kentucky	8
43.	Texas	New Mexico, Oklahoma, Arkansas, Louisiana	4
44.	Utah	Nevada, New Mexico, Wyoming, Arizona, Colorado, Idaho	6
45.	Vermont	New Hampshire, New York, Massachusetts	3
46.	Virginia	North Carolina, Tennessee, West Virginia, Kentucky, Maryland	5
47.	Washington	Oregon, Idaho	2
48.	West Virginia	Pennsylvania, Virginia, Kentucky, Maryland, Ohio	5
49.	Wisconsin	Michigan, Minnesota, Illinois, Iowa	4
50.	Wyoming	Nebraska, South Dakota, Utah, Colorado, Idaho, Montana	6"""
{% endhighlight %}

As you can see in this data, there's a number, a state, sometimes a parenthetical, a list of states, and a number. I need to develop a regex that will pick off 
all of the data that I'm looking for.

Whenever I'm working with regex in Python I use the [Python regex tester](https://pythex.org/) at pythex.org.  I'm going to use Tennessee's entry as the example
since it has the parenthetical reference. I'll have to use another entry without to proof the regex.

So, let's build a regex step by step.

The test string I'm using is this one:

> 42.     Tennessee  (The state which touches the most other states.)        Mississippi, Missouri, North Carolina, Virginia, Alabama, Arkansas, Georgia, Kentucky   8 
 
So, first, we match the number like this:

{% highlight python %}

[0-9]+.

{% endhighlight %}

That matches the '42.' by way of looking for one or more numeric characters followed by a '.'.

Next, we'll add in the state:

{% highlight python %}

[0-9]+.[\s]+([A-Za-z]+)[\s]+

{% endhighlight %}

The \s matches one or more whitespace characters (spaces in this case) and then it looks for one or more upper or lower case letters followed by one or more 
whitespace characters. The upper and lower case letter match is in parenthesis because it's a match group. The effect of that is that although Python will
use the whole regex to match the line, it will only return things that are match groups. You'll see in a bit.

Now is where it begins to get tricky because we have to match the parenthetical, but also allow for not having one at all.

If the parenthetical were always there, we could find it with this: 

{% highlight python %}

\([a-zA-Z. ]*\)

{% endhighlight %}

However, this regex always wants to see the parentheses, so it won't match correctly if the parenthetical isn't there. I need to make the parenthetical optional 
like this:

{% highlight python %}

[\(a-zA-Z .\)]*

{% endhighlight %}

That will match what's found in the parentheticals: alphabetical characters, spaces and a period. If the parenthetical isn't there, it will ignore it because
the star matches 0 or more occurances.

Now the full regex looks like this:

{% highlight python %}

[0-9]+.[\s]+([A-Za-z]+)[\s]*[\(a-zA-Z .\)]*

{% endhighlight %}

Next is more spaces followed by the list of bordering states. I was almost tempted to use regex to match every state within the list, but I'm going to be lazy
instead and just match the whole list itself. I'll use Python string parsing tools to split off all of the individual states separated by commas.
First, I'll need to match the whitespace, then the list of states. Here's the new regex:

{% highlight python %}

[0-9]+.[\s]+([A-Za-z]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z, ]+)

{% endhighlight %}

The \s+ matches multiple whitespaces, then we start a match group for any alphabetical character (upper or lower case) as well as commas and spaces, and match one or more of those.

I could keep going and match the number of bordering states at the end, but there's no reason because I don't need that information, and even if I did, it could
be generated programmatically by getting the length of the list or bordering states.

To be sure everything worked, I pasted the full text into the regex tester and made sure it could find everything.

It can't. There's another wrinkle that I forgot about - look at the entry for New York:

> 32.	New York	Pennsylvania, Rhode Island (water border), Vermont, Connecticut, Massachusetts, New Jersey	6

That (water border) messed up my match. I'll need to add parentheses into the match for the list of border states.
Also, some states are two words, so I'll have to match that too.

Here's the new regex:

{% highlight python %}

[0-9]+.[\s]+([A-Za-z ]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z,\(\) ]+)[\s]+

{% endhighlight %}

After the first \s match, I added a space in the match for the state name, then I added parentheses to the characters to match in the comma-separated list of 
states.

It works like a charm - I get all of the states and the comma separated list of bordering states as matches.

Now I need to write a function that reads over the list and generates a dictionary of states with a list of their bordering states.

A note at this point: since the puzzles specifies that you *drive* to each state, I'm going to remove the water-bordering states from the list of bordering states.

Now, we start the function with a basic declaration:

{% highlight python %}

def parseStateBorderString(string= stateBorderData):
    pass
    
{% endhighlight %}

Earlier, I pasted the state border list as a multiline string named 'stateBorderData'. Our function takes in a parameter ('string') and its default value is 
specified as the 'stateBorderData' string. I could have just referenced the global 'stateBorderData' variable instead of passing it as a parameter, but 
I prefer to keep my functions independent of the rest of my program. By using a default parameter, I can override the default and use different data if I want,
but if I do nothing, it just uses the built-in table.

The 'pass' is something I always write in new functions before I create the body. It basically means do nothing. Your functions need a body or they're not proper
Python code, and the minimum body that you can have is a 'pass' command, so I always put it in to make sure I'm still able to run my script regardless if I have
finished writing the function yet.

This function is going to return a dictionary, so let's add that:

{% highlight python %}

def parseStateBorderString(string= stateBorderData):
    stateBorderDict = {}

    return borderDict

{% endhighlight %}

Now we still have a function that doesn't really *do* anything, but it will return a dictionary. An empty one, for now, but this function now essentially behaves
as it is supposed to from a strict viewpoint: You can call it and it returns an (empty) dictionary. Thus, if I wanted to stop working on this function, I could 
move on to writing other code and I could even incorporate this function into that code and it would run and produce (programmatically) valid output.

Our next task is to loop over all of the lines in the string and pick out the state and bordering states list.  You can loop over each line in the string like
this:

{% highlight python %}

def parseStateBorderString(string= stateBorderData):
    stateBorderDict = {}
    
    for line in stateBorderData.splitLines():
        logging.debug("Line is %s",line)
        pass
  
    return stateBorderDict

{% endhighlight %}

You'll notice that I used a logging framework to output the full text of the line. I really like to get visibility into the intermediate steps of my programs
by using debug statements. You'll see lots of them as we continue.

Next, we have to use regex to match the state and bordering state in the line. I'm going to use the *findall* function like this:

{% highlight python %}

def parseStateBorderString(string= stateBorderData):
    stateBorderDict = {}
    
    for line in stateBorderData.splitlines():
        logging.debug("Line is %s",line)

        matches = re.findall("[0-9]+.[\s]+([A-Za-z ]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z,\(\) ]+)[\s]+",line)
        
        if len(matches) >0:
            logging.debug("Found matches: %s",str(matches))
            (state,borderListStr) = matches[0]
            logging.debug("State is %s, borderList is %s",state,borderListStr)
        
    return stateBorderDict
    
{% endhighlight %}

A few things here: 

* The 'len(matches) >0' check is sort of a safety check. We assume there will always be matches, but if there aren't, we're going to cause an exception if
we just try to start playing with an empty list.
* The second line under the conditional (after the debug line) is *unpacking* the first match into two variables: the state and list of border state strings. Technically, I'm being risky by assuming that there's only one match and it's proper, but you've got to start trusting your program at some point. Plus, once I debug this it's always going to run perfectly every time since the data isn't changing

This produced the following output for a line:

{% highlight console %}
2021-02-01 22:18:39,501 - MainThread - parseStateBorderString  - DEBUG    Line is 50.   Wyoming Nebraska, South Dakota, Utah, Colorado, Idaho, Montana  6
2021-02-01 22:18:39,501 - MainThread - parseStateBorderString  - DEBUG    Found matches: [('Wyoming', 'Nebraska, South Dakota, Utah, Colorado, Idaho, Montana')]
2021-02-01 22:18:39,501 - MainThread - parseStateBorderString  - DEBUG    State is Wyoming, borderList is Nebraska, South Dakota, Utah, Colorado, Idaho, Montana
{% endhighlight %} 

Looks good to me.
Now I'm going to do some post-processing and split the string containing the list of border states into a list of states. Here's how:

{% highlight python %}
def parseStateBorderString(string= stateBorderData):
    stateBorderDict = {}
    
    for line in stateBorderData.splitlines():
        logging.debug("Line is %s",line)
        matches = re.findall("[0-9]+.[\s]+([A-Za-z ]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z,\(\) ]+)[\s]+",line)       
        
        if len(matches) >0:
            logging.debug("Found matches: %s",str(matches))
            (state,borderListStr) = matches[0]

            logging.debug("State is %s, borderList is %s",state,borderListStr)
            state=state.strip()
            borderStateList = [x.strip() for x in borderListStr.split(',')]
            logging.debug("Border state list is %s",str(borderStateList))

    return stateBorderDict
{% endhighlight %}

Two interesting things here:

List comprehension in generating the borderStateList. List comprehension is nifty shorthand in Python. Written longhand, that one line statement would be:

{% highlight python %}
borderStateList = []  #Create a new empty list
dirtySplitStringList = borderListStr.split(',') #Generate a list of entries by splitting the string at each comma
for entry in dirtySplitStringList:
    borderStateList.append(entry.strip())
{% endhighlight %}

This is a bit verbose compared to the list comprehension, and as long as you can understand the list comprehension, you don't lose any information. Indeed,
I find the list comprehension easier to read once you get used to it.

The other interesting aspect of this is the 'hygiene' aspect of stripping the whitespace from the strings via the *x.strip()* call. *strip* will remove all
leading and trailing whitespace from a string. This is useful because errant whitespace can mess up string comparisons, concatenation, really anything with 
strings. Sanitizing your data like this is a good habit to get into.

The borderStateList output produced by this looks like this for Wyoming:

{% highlight console %}
2021-02-01 22:37:03,128 - MainThread - parseStateBorderString  - DEBUG    Border state list is ['Nebraska', 'South Dakota', 'Utah', 'Colorado', 'Idaho', 'Montana']
{% endhighlight %}

That looks pretty clean to me. We almost have all of our data except for one wrinkle: I don't care about state names, I only care about their postal abbreviations.

To get the postal abbreviations, we'll have to use the name to postal abbreviation dictionary to look them up. That code looks like this:

{% highlight python %}

def parseStateBorderString(string= stateBorderData,pcList=us_state_abbrev):
    stateBorderDict = {}
    
    for line in stateBorderData.splitlines():
        logging.debug("Line is %s",line)
        matches = re.findall("[0-9]+.[\s]+([A-Za-z ]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z,\(\) ]+)[\s]+",line)       
        
        if len(matches) >0:
            logging.debug("Found matches: %s",str(matches))
            (state,borderListStr) = matches[0]

            logging.debug("State is %s, borderList is %s",state,borderListStr)
            state = state.strip()
            borderStateList = [x.strip() for x in borderListStr.split(',')]
            logging.debug("Border state list is %s",str(borderStateList))
            
            try:
                statePostalCode = pcList[state]
            except KeyError:
                print("State " + str(state) + " has no postal code abbreviation in the list")
                return {}
            logging.debug("State '"+str(state) + "' has abbreviation '"+str(statePostalCode) +"'")

            try:
                borderStatePcList = [pcList[state] for state in borderStateList]
            except KeyError:
                print("State '" + str(state) + "' has no postal code abbreviation in the list")
                return {}
            
    return stateBorderDict
{% endhighlight %}

I added a new parameter for the postal code abbreviation list and two try/catch blocks. If it can't find that state it's looking for in the list of abbreviations, it'll let me know with an error message that will help me
find the issue more quickly. It will then return an empty dictionary, which is a fair failure condition. Once again, since the data we're working with is hardcoded
and will never change, all of these potential errors will be worked out one way or another. None of this will ever happen 'in the wild'.

In fact, an error happened immediately:

{% highlight console %}
2021-02-01 22:48:17,132 - MainThread - parseStateBorderString  - DEBUG    Line is 2.    Alaska  None    None
2021-02-01 22:48:17,132 - MainThread - parseStateBorderString  - DEBUG    Found matches: [('Alaska', 'None')]
2021-02-01 22:48:17,132 - MainThread - parseStateBorderString  - DEBUG    State is Alaska, borderList is None
2021-02-01 22:48:17,133 - MainThread - parseStateBorderString  - DEBUG    Border state list is ['None']
2021-02-01 22:48:17,133 - MainThread - parseStateBorderString  - DEBUG    State 'Alaska' has abbreviation 'AK'
State 'Alaska' has no postal code abbreviation in the list
{% endhighlight %}

Now, here's two problems:

1. The *state* variable which I hoped would be distinct in the second try/catch block is, in fact, not distinct. The *state* variable inside the list comprehension is not visible outside of the list comprehension. It says it can't find 'Alaska' in the list, but it really can't find 'None'. 'Alaska' is just the value of the *state* variable from the first try/catch block
2. List comprehension and exceptions don't work very well together. If I looped over each list element and handled them individually, I could ignore the 'None' element and keep the rest. Sadly, I can't do that with list comprehension.

So, I'll change my list comprehension to a loop like this:

{% highlight python %}
def parseStateBorderString(string= stateBorderData,pcList=us_state_abbrev):
    stateBorderDict = {}
    
    for line in stateBorderData.splitlines():
        logging.debug("Line is %s",line)
        matches = re.findall("[0-9]+.[\s]+([A-Za-z ]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z,\(\) ]+)[\s]+",line)       
        
        if len(matches) >0:
            logging.debug("Found matches: %s",str(matches))
            (state,borderListStr) = matches[0]
            logging.debug("State is %s, borderList is %s",state,borderListStr)

            state = state.strip()
            borderStateList = [x.strip() for x in borderListStr.split(',')]
            logging.debug("Border state list is %s",str(borderStateList))
            
            try:
                statePostalCode = pcList[state]
            except KeyError:
                print("State " + str(state) + " has no postal code abbreviation in the list")
                return {}
            logging.debug("State '"+str(state) + "' has abbreviation '"+str(statePostalCode) +"'")

            borderStatePcList = []
            for borderState in borderStateList:
                try:
                    pcAbbrev = pcList[borderState]
                    logging.debug("Abbreviation for '%s' is '%s'",borderState,pcAbbrev)
                except KeyError:
                    logging.debug("Found invalid state in border list: %s",borderState)
                    continue
                borderStatePcList.append(pcAbbrev)    
            
    return stateBorderDict
{% endhighlight %}


This loop is a bit superior in that it can just ignore individual invalid elements in the list rather than throwing an exception for the whole thing if any one
is invalid. 

So now we have each state as an abbreviation and its bordering states as abbrevations. Now we just plop them into a dictionary and return it. Here's the finished 
function:

{% highlight python %}
def parseStateBorderString(string= stateBorderData,pcList=us_state_abbrev):
    stateBorderDict = {}
    
    for line in stateBorderData.splitlines():
        logging.debug("Line is %s",line)
        matches = re.findall("[0-9]+.[\s]+([A-Za-z ]+)[\s]*[\(a-zA-Z .\)]*[\s]+([A-Za-z,\(\) ]+)[\s]+",line)       
        
        if len(matches) >0:
            logging.debug("Found matches: %s",str(matches))
            (state,borderListStr) = matches[0]
            logging.debug("State is %s, borderList is %s",state,borderListStr)
            
            state = state.strip()
            borderStateList = [x.strip() for x in borderListStr.split(',')]
            logging.debug("Border state list is %s",str(borderStateList))
            
            try:
                statePostalCode = pcList[state]
            except KeyError:
                print("State " + str(state) + " has no postal code abbreviation in the list")
                return {}
            logging.debug("State '"+str(state) + "' has abbreviation '"+str(statePostalCode) +"'")

            borderStatePcList = []
            for borderState in borderStateList:
                try:
                    pcAbbrev = pcList[borderState]
                    logging.debug("Abbreviation for '%s' is '%s'",borderState,pcAbbrev)
                except KeyError:
                    logging.debug("Found invalid state in border list: %s",borderState)
                    continue
                borderStatePcList.append(pcAbbrev)

            stateBorderDict[statePostalCode]=borderStatePcList
                        
    return stateBorderDict
{% endhighlight %}

Now, we're going to call this in main, get the result and print it out to see if it looks good:

{% highlight python %}
    stateBorderDict = parseStateBorderString()
    logging.debug("State border dictionary is %s",str(stateBorderDict))
{% endhighlight %}

And the output looks like this:

{% highlight console %}
2021-02-01 23:05:01,359 - MainThread - main  - DEBUG    State border dictionary is {'AL': ['MS', 'TN', 'FL', 'GA'], 'AK': [], 'AZ': ['NV', 'NM', 'UT', 'CA', 'CO'], 'AR': ['OK', 'TN', 'TX', 'LA', 'MS', 'MO'], 'CA': ['OR', 'AZ', 'NV'], 'CO': ['OK', 'UT', 'WY', 'AZ', 'KS', 'NE'], 'CT': ['RI', 'MA'], 'DE': ['PA', 'MD'], 'FL': ['GA', 'AL'], 'GA': ['SC', 'TN', 'AL', 'FL'], 'HI': [], 'ID': ['UT', 'WA', 'WY', 'MT', 'NV', 'OR'], 'IL': ['KY', 'MO', 'WI', 'IN', 'IA', 'MI'], 'IN': ['MI', 'OH', 'IL', 'KY'], 'IA': ['NE', 'SD', 'WI', 'IL', 'MN', 'MO'], 'KS': ['NE', 'OK', 'CO', 'MO'], 'KY': ['TN', 'VA', 'WV', 'IL', 'IN', 'MO', 'OH'], 'LA': ['TX', 'AR', 'MS'], 'ME': ['NH'], 'MD': ['VA', 'WV', 'DE', 'PA'], 'MA': ['RI', 'VT', 'CT', 'NH'], 'MI': ['OH', 'WI', 'IL', 'IN'], 'MN': ['SD', 'WI', 'IA'], 'MS': ['LA', 'TN', 'AL', 'AR'], 'MO': ['NE', 'OK', 'TN', 'AR', 'IL', 'IA', 'KS', 'KY'], 'MT': ['WY', 'ID', 'ND'], 'NE': ['MO', 'SD', 'WY', 'CO', 'IA', 'KS'], 'NV': ['ID', 'OR', 'UT', 'AZ', 'CA'], 'NH': ['VT', 'ME', 'MA'], 'NJ': ['PA', 'DE', 'NY'], 'NM': ['OK', 'TX', 'UT', 'AZ', 'CO'], 'NY': ['PA', 'VT', 'CT', 'MA', 'NJ'], 'NC': ['TN', 'VA', 'GA', 'SC'], 'ND': ['MN', 'MT'], 'OH': ['MI', 'PA', 'WV', 'IN', 'KY'], 'OK': ['MO', 'NM', 'TX', 'AR', 'CO', 'KS'], 'OR': ['NV', 'WA', 'CA', 'ID'], 'PA': ['OH', 'WV', 'DE', 'MD', 'NJ'], 'RI': ['MA', 'CT'], 'SC': ['GA'], 'SD': ['NE', 'ND', 'WY', 'IA', 'MN', 'MT'], 'TN': ['MS', 'MO', 'NC', 'VA', 'AL', 'AR', 'GA', 'KY'], 'TX': ['OK', 'AR', 'LA'], 'UT': ['NV', 'NM', 'WY', 'AZ', 'CO', 'ID'], 'VT': ['NY', 'MA'], 'VA': ['TN', 'WV', 'KY', 'MD'], 'WA': ['OR', 'ID'], 'WV': ['PA', 'VA', 'KY', 'MD', 'OH'], 'WI': ['MI', 'MN', 'IL', 'IA'], 'WY': ['NE', 'SD', 'UT', 'CO', 'ID', 'MT']}
{% endhighlight %}

I see at least one issue with this data: If you look at Montana you'll see these connections:

{% highlight python %}
'MT': ['WY', 'ID', 'ND']
{% endhighlight %}

South Dakota is not in there. Why is that? Here's the entry from the text:

{% highlight console %}
26.	Montana	South Dakota, Wyoming, Idaho, North Dakota	4
{% endhighlight %}

First thing I notice is that South Dakota is there, but it has a space in it.
Let's test it in the online regex tester.

Indeed, that is certainly an issue. Here's the matches it finds:

{% highlight console %}
Match 1
1.	Montana
2.	Dakota, Wyoming, Idaho, North Dakota
{% endhighlight %}

Hmmm, just plain old Dakota eh? No bueno.

If I had to guess I'd say it's this aspect of the regex:

{% highlight python %}
[\(a-zA-Z .\)]*
{% endhighlight %}
The parentheses are optional, so it matches the 'South' portion of South Dakota and it gets ignored since it's not in a match group.

How do I require the parentheses be part of the optional string?

I've come to this regex so far:

{% highlight python %}
[0-9]+.[\s]+([A-Za-z ]+)[\s]*[^\(a-zA-Z .\)$]?[\s]+([A-Za-z,\(\) ]+)[\s]+
{% endhighlight %}

The important part of this is this:

{% highlight python %}
[^\(a-zA-Z .\)$]?
{% endhighlight %}
This should match alphabetical characters, periods and spaces within two parentheses: the ^\( forces a match at the beginning of the string and the \)$ forces a match at the end of the string. The whole thing is placed within a character class that is optionally matched with the '?'.

However, when testing it with this text:

{% highlight console %}
25.	Missouri (The state which touches the most other states.)	Nebraska, Oklahoma, Tennessee, Arkansas, Illinois, Iowa, Kansas, Kentucky	8
{% endhighlight %}

I get this match:

{% highlight console %}
Match 2
1.	Missouri
2.	(The state which touches the most other
{% endhighlight %}

And I think that's because of this next part of the regex:

{% highlight python %}
[\s]+([A-Za-z,\(\) ]+)[\s]+
{% endhighlight %}

So it's looking for any number of spaces, and then alphabetical characters, spaces and commas *and parentheses* followed by one of more spaces.

I think this is matching the note in my match up there.

So the question is how can I match the comma separated list (which still contains parentheses and not the initial note in parentheses.

At this point I think I'm just going to edit the data to remove all of these pesky parentheses. It's the easiest thing at this point.

I'm going to leave the water border ones in because they're automatically
removed due to the fact they break the lookup of postal codes.

I changed the regex to this after removing all of the 'interesting' notes about the states and how many states they border:

{% highlight python %}
[0-9]+.[\s]+([A-Za-z ]+)[\s]+([A-Za-z,\(\) ]+)[\s]+
{% endhighlight %}

It's still not right though, and there's only one issue: the Maine entry.

Since it only borders one state, there are no commas. Plus, the state it 
borders is New Hampshire which has a space in it so it's doubly confusing.

I have one saving grace: The whitespace after the state name is not spaces, but a tab. So, instead of matching generic whitespace, I can match a tab like this:

{% highlight console %}
[0-9]+.[\s]+([A-Za-z ]+)[\t]+([A-Za-z,\(\) ]+)
{% endhighlight %}

Note the '\t' in there.

Okay, *now* it works.

Here's the updated list of states and border states:

{% highlight python %}
{'AL': ['MS', 'TN', 'FL', 'GA'], 'AK': [], 'AZ': ['NV', 'NM', 'UT', 'CA', 'CO'], 'AR': ['OK', 'TN', 'TX', 'LA', 'MS', 'MO'], 'CA': ['OR', 'AZ', 'NV'], 'CO': ['NM', 'OK', 'UT', 'WY', 'AZ', 'KS', 'NE'], 'CT': ['NY', 'RI', 'MA'], 'DE': ['NJ', 'PA', 'MD'], 'FL': ['GA', 'AL'], 'GA': ['NC', 'SC', 'TN', 'AL', 'FL'], 'HI': [], 'ID': ['UT', 'WA', 'WY', 'MT', 'NV', 'OR'], 'IL': ['KY', 'MO', 'WI', 'IN', 'IA', 'MI'], 'IN': ['MI', 'OH', 'IL', 'KY'], 'IA': ['NE', 'SD', 'WI', 'IL', 'MN', 'MO'], 'KS': ['NE', 'OK', 'CO', 'MO'], 'KY': ['TN', 'VA', 'WV', 'IL', 'IN', 'MO', 'OH'], 'LA': ['TX', 'AR', 'MS'], 'ME': ['NH'], 'MD': ['VA', 'WV', 'DE', 'PA'], 'MA': ['NY', 'RI', 'VT', 'CT', 'NH'], 'MI': ['OH', 'WI', 'IL', 'IN'], 'MN': ['ND', 'SD', 'WI', 'IA'], 'MS': ['LA', 'TN', 'AL', 'AR'], 'MO': ['NE', 'OK', 'TN', 'AR', 'IL', 'IA', 'KS', 'KY'], 'MT': ['SD', 'WY', 'ID', 'ND'], 'NE': ['MO', 'SD', 'WY', 'CO', 'IA', 'KS'], 'NV': ['ID', 'OR', 'UT', 'AZ', 'CA'], 'NH': ['VT', 'ME', 'MA'], 'NJ': ['PA', 'DE', 'NY'], 'NM': ['OK', 'TX', 'UT', 'AZ', 'CO'], 'NY': ['PA', 'VT', 'CT', 'MA', 'NJ'], 'NC': ['TN', 'VA', 'GA', 'SC'], 'ND': ['SD', 'MN', 'MT'], 'OH': ['MI', 'PA', 'WV', 'IN', 'KY'], 'OK': ['MO', 'NM', 'TX', 'AR', 'CO', 'KS'], 'OR': ['NV', 'WA', 'CA', 'ID'], 'PA': ['NY', 'OH', 'WV', 'DE', 'MD', 'NJ'], 'RI': ['MA', 'CT'], 'SC': ['NC', 'GA'], 'SD': ['NE', 'ND', 'WY', 'IA', 'MN', 'MT'], 'TN': ['MS', 'MO', 'NC', 'VA', 'AL', 'AR', 'GA', 'KY'], 'TX': ['NM', 'OK', 'AR', 'LA'], 'UT': ['NV', 'NM', 'WY', 'AZ', 'CO', 'ID'], 'VT': ['NH', 'NY', 'MA'], 'VA': ['NC', 'TN', 'WV', 'KY', 'MD'], 'WA': ['OR', 'ID'], 'WV': ['PA', 'VA', 'KY', 'MD', 'OH'], 'WI': ['MI', 'MN', 'IL', 'IA'], 'WY': ['NE', 'SD', 'UT', 'CO', 'ID', 'MT']}
{% endhighlight %}

## Generating All Permutations of a String ##

Another task we'll have to perform is generating all of the permutations of a string. I'm going to work with the 'MTSDIA' string as NPR already told me that 
'amidst' is in there.

Turns out, accoridng to the sources I looked up, it's a simple one-liner:

{% highlight python %}
stringPermutations = [''.join(p) for p in itertools.permutations("mtsdia")]
logging.debug("String permutations are: %s",stringPermutations)
{% endhighlight %}

I'm not even going to make a function for that one.

## Determining if a Permutation is an English Word ##

Now that we have a list of permutations, we can see if we can determine if any of those permutations are words.

The examples in Stackoverflow were very straightforward. Along with generating the permutations, my main function looks roughly like this:

{% highlight python %}
    stringPermutations = [''.join(p) for p in itertools.permutations("mtsdia")]
    logging.debug("String permutations are: %s",stringPermutations)
    
    d = enchant.Dict("en_US")
    
    for permutation in stringPermutations:
        if d.check(permutation):
            print("Found valid word: " +str(permutation))
{% endhighlight %}

This time I used *print* instead of logging. That's because this is a command-line application, and the actual output for a command line applications is always
done with a *print* statement rather than logging (which may only go into a logfile, not the console).

Interestingly, it found two words:

{% highlight console %}

Found valid word: amidst
Found valid word: admits

{% endhighlight %}

I don't know if that was known to the puzzle people at NPR, but there it is. Maybe we'll have more surprises when we finish this.

## Generating Strings for 4-State Travel ##

Now we come to the meat of the problem: generating a string comprised of the postal abbreviations of four states you can drive through, and doing that for every
combination of states you can drive through.

I need to do some figuring here to get this. I'm going to start with the 
'amidst' example.

So, starting with Montana, we have neighboring states:
'MT': ['SD', 'WY', 'ID', 'ND']

If you pick SD, you get:
'SD': ['NE', 'ND', 'WY', 'IA', 'MN', 'MT']

If you pick NE you're at the end.

So, this would return "MTSDNE".

Then, you would pick 'ND' from the 'NE' and get "MTSDND"
And the rest:

* NE - "MTSDNE" 
* ND - "MTSDND"
* WY - "MTSDWY"
* IA - "MTSDIA"
* MN - "MTSDMN"
* MT - "MTSDMT"

This is interesting because its path takes it back to Montana. As far as I 
know this is not disallowed, so I'll leave it.

So, if I make a function that recurses with itself to a given depth, it 
would start going through the list and the last invocation returns a list.

So, in this case, the last invocation would return a list like:

{% highlight PYTHON %}
["MTSDNE" ,"MTSDND","MTSDWY","MTSDIA","MTSDMN","MTSDMT"]
{% endhighlight %}

And then, for the Wyoming branch we have the following border states:

{% highlight console %}
'WY': ['NE', 'SD', 'UT', 'CO', 'ID', 'MT']
{% endhighlight %}

And it would return:

{% highlight python %}
["MTWYNE","MTWYSD","MTWYUT","MTWYCO","MYWYID","MYWYMT"]
{% endhighlight %}

And then you would combine the two lists to get this:

{% highlight python %}
["MTSDNE" ,"MTSDND","MTSDWY","MTSDIA","MTSDMN","MTSDMT""MTWYNE","MTWYSD","MTWYUT","MTWYCO","MYWYID","MYWYMT"]
{% endhighlight %}
Okay, I'm getting an idea.

We create a function with recursion. It has this sort of prototype:

{% highlight python %}
def createPathString(statePcAbbrev,borderStateDict,string="",depth=4)
{% endhighlight %}

So, on the first invocation, depth will be 4, the string will be empty and we'll pass the state we're starting
with along with the constant border state dictionary.

I'm going to start coding and then come back and explain.

Okay, took a bit but here it is:

{% highlight python %}

def generatePathString(startingStatePc,stateBorderDict,string="",depth=3):
    #Generate an empty list to return
    retPathList = []
	
    #We're going to use a list of border states twice so let's assign it to a variable
    borderStatesList = stateBorderDict[startingStatePc]
	
	#Add the current state to the string representing the path we're creating
    string += startingStatePc
	
	#If we're not at the endpoint of our journey, call this function again for all bordering states
    #The 'end' of the journey is 1, not 0 because we're going to add the border states to the string
	#and return it rather than going to 0 and returning a list with one string in it
	
	if depth > 1: 
        for borderState in borderStatesList:
            retPathList.extend(generatePathString(borderState,stateBorderDict,string,depth-1))
    #If we ARE at the endpoint of our journey, generate the list of strings representing the paths
	else:           
        retPathList = [string+statePcAbbrev for statePcAbbrev in borderStatesList]
    
    return retPathList
{% endhighlight %}

So, a couple of things with this:

* Depth is equal to the total number of states you want to travel through-1. Thus, since we want to travel through four states, it should be three, not four
* The 'extend' function for lists adds all of the elements of one list to another instead of making lists within lists. This will give us one big list of strings representing the paths through the states

I ran this function starting with Montana and with a depth of 2 - that should give us all the paths
through three states starting with Montana. Here's what I got:

{% highlight console %}
['MTSDNE', 'MTSDND', 'MTSDWY', 'MTSDIA', 'MTSDMN', 'MTSDMT', 'MTWYNE', 'MTWYSD', 'MTWYUT', 'MTWYCO', 'MTWYID', 'MTWYMT', 'MTIDUT', 'MTIDWA', 'MTIDWY', 'MTIDMT', 'MTIDNV', 'MTIDOR', 'MTNDSD', 'MTNDMN', 'MTNDMT']
{% endhighlight %}

And I can clearly see the 'MTSDIA' that will form 'amidst' so we're good there.


## Combining Everything ##

Now, I need to run it against all 50 states with a path four states long. That code looks like this:

{% highlight python %}
    #Generate an empty list of paths
	statePaths = []
    #Get the list of state abbreviations from the keys of the state border dictionary
	statePcAbbrevs = stateBorderDict.keys()
    
	#For each state, add the list of paths to the empty list
	for state in statePcAbbrevs:
        statePaths.extend(generatePathString(state,stateBorderDict))

{% endhighlight %}

I'm not going to paste the output here because there's 5646 such paths.

Now, to generate all of the permutations of those paths, we do this:

{% highlight python %}
    pathPermutations = []
    for path in statePaths:
        pathPermutations.extend([''.join(p) for p in itertools.permutations(path)])
{% endhighlight %}

And then when we try to run it....

We get a MemoryError.

I was afraid of that. There's just way too much stuff in there.

We can solve this by not storing all of this data: we can just process it as soon as we generate it and find any valid words without storing millions (billions?) of permutations and then doing it all at once.

So, we can check things as we generate them like this:

{% highlight console %}
    d = enchant.Dict("en_US")
    statePcAbbrevs = stateBorderDict.keys()
    for state in statePcAbbrevs:
        for path in generatePathString(state,stateBorderDict):
            print("Path is " + str(path))
            for permutation in [''.join(p) for p in itertools.permutations(path)]:
                if d.check(permutation):
                    print("Found valid word: " +str(permutation))
        
{% endhighlight %}

And this does not produce a MemoryError, however...

It's Slow. As. Molasses. I didn't even get through one state in the five minutes I let it run. No good.

Can we do better with list comprehension?

Here's how I would do it with list comprehension:

{% highlight python %}
    validWords = []
    d = enchant.Dict("en_US")
    statePcAbbrevs = stateBorderDict.keys()
    for state in statePcAbbrevs:
        for path in generatePathString(state,stateBorderDict):
            print("Path is " + str(path))
            validWords.extend([permutation for permutation in [''.join(p) for p in itertools.permutations(path)] if d.check(permutation)])
{% endhighlight %}

Nope, that's not better.

Looking at Task Manager, this is not breaking 6% processor. That's no good. We need threads!

We'll try running one thread for each path.

My worker thread function will look like this:

{% highlight python %}
def workerThread(path,validWords,d):
    validWords.extend([permutation for permutation in [''.join(p) for p in itertools.permutations(path)] if d.check(permutation)])
{% endhighlight %}

And the modified code to implement the search with threads looks like this:

{% highlight console %}
    threadHandles = []
    validWords = []
    d = enchant.Dict("en_US")
    statePcAbbrevs = stateBorderDict.keys()
    for state in statePcAbbrevs:
        for path in generatePathString(state,stateBorderDict):
            threadHandles.append(Thread(target=workerThread,args=(path,validWords,d,))  )
            threadHandles[-1].start() 
			
    for handle in threadHandles:
        handle.join()			
{% endhighlight %}

The -1 on the threadHandles index will always pull the last thread added. At the end, all threads will be joined and the program will end.

Haha, this is hilarious. My CPU usage is bumping up towards 100% and my memory usage is about 877MB.

I wonder how long it takes to do just one state?  I could profile the performance with just one state and then see if I have any major performance impediments.

Also, I've gotten at least one notification that I can't start a new thread because I've run out of thread handles. Hilarious.

{% highlight console %}
Traceback (most recent call last):
  File "src\pyPuzzle.py", line 317, in <module>
    main()
  File "src\pyPuzzle.py", line 296, in main
    threadHandles[-1].start()
  File "C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\lib\threading.py", line 852, in start
    _start_new_thread(self._bootstrap, ())
RuntimeError: can't start new thread
{% endhighlight %}

Well, running it on just Maine produced results in about a 30 seconds. There's only 9 paths through four states starting with Maine.

That's gonna be a lot.

I'm going to try to profile my code by 
calling it with this command line:

{% highlight console %}
C:\Users\sfrie\Dropbox\Projects\pyPuzzle>python -m cProfile -s cumtime src\pyPuzzle.py
{% endhighlight %}

Theoretically, this should tell me if something is taking too long.

However....

The threading really messes this up and makes it impossible to tell anything.
So, I'm going to remove the threading and do it all in one thread and then take a look at the report.

I'm going to break up my code as much as possible so that I can tell what's taking long.

The non-threaded code looks like this:

{% highlight python %}

    d = enchant.Dict("en_US")

    for path in generatePathString("ME",stateBorderDict):
        permutations = [''.join(p) for p in itertools.permutations(path)]
        for permutation in permutations:
            if d.check(permutation):
                print("Valid word " + str(permutation)
{% endhighlight %}

Interestingly, the non-threaded code is taking much longer than the threaded code. It's good so see that there's some benefit.

For reference, the threaded code took 36s for analyzing the paths through Maine.

It takes 91 seconds single-threaded.

That's a good gain, but not nearly good enough.

Here's the truncated output of the profiling:

{% highlight console %}
   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     33/1    0.000    0.000   91.265   91.265 {built-in method builtins.exec}
        1    0.002    0.002   91.265   91.265 pyPuzzle.py:2(<module>)
        1    0.396    0.396   90.974   90.974 pyPuzzle.py:222(main)
   362880    1.196    0.000   89.449    0.000 __init__.py:616(check)
   362880   86.759    0.000   86.847    0.000 _enchant.py:313(dict_check)
   362880    0.904    0.000    1.020    0.000 __init__.py:585(_check_this)
        1    0.004    0.004    0.637    0.637 pyPuzzle.py:162(parseStateBorderString)
{% endhighlight %}

In case you can't tell, we spend 86 or the total 91 seconds in the dictionary check.

That's bad. I need the dictionary check. That's the whole point.

Oh look, someone else has trouble with this too on Stackoverflow [here](https://stackoverflow.com/questions/3449968/large-scale-spell-checking-in-python).

Okay, we're going to try a different spell checker called pyspellchecker found [here](https://pypi.org/project/pyspellchecker/).

Using this library, I can check the paths for Maine like this:

{% highlight python %}
	validWords=[]
    spell = SpellChecker()
    for path in generatePathString("ME",stateBorderDict):
        validWords.extend(spell.known([''.join(p) for p in itertools.permutations(path)]))
        
    print(str(validWords))
{% endhighlight %}

MUCH BETTER! Total time is now 2 seconds!

But I'm not convinced: let's do this for the 'amidst' example to make sure it can find words that are valid.

Good news! It did indeed find 'amidst' and 'admits' which are the right answers.

And it only took a couple of seconds to do the search.

Now let's add the threads back in and see if we can do it all.

Another performance tip: Plug your laptop in so that your processor isn't stuck at 1.33GHz!

Okay, it finished! Took less than 10 minutes

What do we have?

{% highlight console %}
['galavant', 'tenorman', 'ornament', 'animator', 'flagrant', 'ransomed', 'mondares', 'cameroon', 'motorman', 'mailroom', 'molinari', 'dioramas', 'contemno', 'cameroon', 'condense', 'diocesan', 'condemns', 'diocesan', 'flagrant', 'magneton', 'galavant', 'duonetic', 'intoduce', 'emiliano', 'moleskin', 'amarillo', 'mailroom', 'emiliano', 'moleskin', 'emiliano', 'emiliano', 'molinari', 'nanomite', 'nominate', 'emiliano', 'diocesan', 'emiliano', 'animator', 'animator', 'moleskin', 'amarillo', 'condemns', 'emiliano', 'motorman', 'motorman', 'motorman', 'motorman', 'mailroom', 'mailroom', 'emiliano', 'maddison', 'diamonds', 'tenorman', 'ornament', 'magneton', 'tenorman', 'ornament', 'emiliano', 'emiliano', 'condense', 'duonetic', 'intoduce', 'condense', 'emiliano', 'nanomite', 'nominate', 'emiliano', 'moleskin', 'condemns', 'maddison', 'diamonds', 'ransomed', 'mondares', 'condemns', 'contused', 'condense', 'diocesan', 'dioramas', 'contemno', 'nanomite', 'nominate', 'motorman', 'nanomite', 'nominate', 'tenorman', 'ornament', 'animator', 'contused', 'galavant', 'galavant']
{% endhighlight %}

Well hell that's more than 1!

Also, I didn't mark down what paths these are.

I'll have to do it differently: a dictionary with the 
key being the path and the values being the words.

Alright, my worker function is now:

{% highlight console %}
def workerThread(path,validWords,d):
    knownWords = d.known([''.join(p) for p in itertools.permutations(path)])
    if len(knownWords) >0:
        validWords[path] = knownWords
{% endhighlight %}

And the code to generate the matches with threads is:

{% highlight python %}

    threadHandles = []
    validWords = {}    
    statePcAbbrevs = stateBorderDict.keys()
    threadsStarted = 0
    spell = SpellChecker()
    statePcAbbrevs = stateBorderDict.keys()
    for state in statePcAbbrevs:
        for path in generatePathString(state,stateBorderDict):
            threadHandles.append(Thread(target=workerThread,args=(path,validWords,spell,))  )
            threadHandles[-1].start()  
            threadsStarted += 1
            if threadsStarted % 25 == 0:
                print("Started " +str(threadsStarted) + " threads")
                
    print("Started all threads!")
    
    threadsComplete = 0
    for handle in threadHandles:
        handle.join()
        threadsComplete +=1
        if threadsComplete %25 == 0:
            print("Closed " +str(threadsComplete) + " threads out of 5646")
    print(str(validWords))
{% endhighlight %}

Okay, we did this and got the following:

{% highlight console %}
{'ALGATNVA': {'galavant'}, 
 'ARTNMONE': {'tenorman', 'ornament'}, 
 'ARTNMOIA': {'animator'}, 
 'ARTNGAFL': {'flagrant'}, 
 'ARMONESD': {'ransomed', 'mondares'}, 
 'ARMONECO': {'cameroon'}, 
 'ARMOTNMO': {'motorman'}, 
 'ARMOILMO': {'mailroom'}, 
 'ARMOILIN': {'molinari'}, 
 'ARMOIASD': {'dioramas'}, 
 'CONEMOTN': {'contemno'}, 
 'CONEMOAR': {'cameroon'}, 
 'CONESDNE': {'condense'}, 
 'CONESDIA': {'diocesan'}, 
 'CONESDMN': {'condemns'}, 
 'CONEIASD': {'diocesan'}, 
 'FLGATNAR': {'flagrant'}, 
 'GATNMONE': {'magneton'}, 
 'GAALTNVA': {'galavant'}, 
 'IDUTCONE': {'intoduce', 'duonetic'}, 
 'ILMONEIA': {'emiliano'}, 
 'ILMONEKS': {'moleskin'}, 
 'ILMOARLA': {'amarillo'}, 
 'ILMOARMO': {'mailroom'}, 
 'ILMOIANE': {'emiliano'}, 
 'ILMOKSNE': {'moleskin'}, 
 'ILIANEMO': {'emiliano'}, 
 'ILIAMONE': {'emiliano'}, 
 'INILMOAR': {'molinari'}, 
 'IANEMOTN': {'nominate', 'nanomite'}, 
 'IANEMOIL': {'emiliano'}, 
 'IASDNECO': {'diocesan'}, 
 'IAILMONE': {'emiliano'}, 
 'IAMOTNAR': {'animator'}, 
 'IAMOARTN': {'animator'}, 
 'KSNEMOIL': {'moleskin'}, 
 'LAARMOIL': {'amarillo'}, 
 'MNSDNECO': {'condemns'}, 
 'MONEIAIL': {'emiliano'}, 
 'MOTNMOAR': {'motorman'}, 
 'MOTNARMO': {'motorman'}, 
 'MOARTNMO': {'motorman'}, 
 'MOARMOTN': {'motorman'}, 
 'MOARMOIL': {'mailroom'}, 
 'MOILMOAR': {'mailroom'}, 
 'MOILIANE': {'emiliano'}, 
 'MOIASDND': {'maddison', 'diamonds'}, 
 'NEMOTNAR': {'tenorman', 'ornament'}, 
 'NEMOTNGA': {'magneton'}, 
 'NEMOARTN': {'tenorman', 'ornament'}, 
 'NEMOILIA': {'emiliano'}, 
 'NEMOIAIL': {'emiliano'}, 
 'NESDNECO': {'condense'}, 
 'NECOUTID': {'intoduce', 'duonetic'}, 
 'NECONESD': {'condense'}, 
 'NEIAILMO': {'emiliano'}, 
 'NEIAMOTN': {'nominate', 'nanomite'}, 
 'NEIAMOIL': {'emiliano'}, 
 'NEKSMOIL': {'moleskin'}, 
 'NMCONESD': {'condemns'}, 
 'NDSDIAMO': {'maddison', 'diamonds'}, 
 'SDNEMOAR': {'ransomed', 'mondares'}, 
 'SDNECONM': {'condemns'}, 
 'SDNECOUT': {'contused'}, 
 'SDNECONE': {'condense'}, 
 'SDIANECO': {'diocesan'}, 
 'SDIAMOAR': {'dioramas'}, 
 'TNMONECO': {'contemno'}, 
 'TNMONEIA': {'nominate', 'nanomite'}, 
 'TNMOARMO': {'motorman'}, 
 'TNMOIANE': {'nominate', 'nanomite'}, 
 'TNARMONE': {'tenorman', 'ornament'}, 
 'TNARMOIA': {'animator'}, 
 'UTCONESD': {'contused'}, 
 'VATNALGA': {'galavant'}, 
 'VATNGAAL': {'galavant'}}
{% endhighlight %}

Okay, a few things:
* There's some paths that are all the same states in different orders
* There's some... shall we say 'uncommon' words in here

I'm going to pare it down a bit and remove duplicates and just... odd words.

{% highlight console %}

{'AL->GA->TN->VA': {'galavant'}, 
 'AR->TN->MO->NE': {'ornament'}, 
 'AR->TN->MO->IA': {'animator'}, 
 'AR->TN->GA->FL': {'flagrant'}, 
 'AR->MO->NE->SD': {'ransomed'}, 
 'AR->MO->IL->MO': {'mailroom'}, 
 'AR->MO->IA->SD': {'dioramas'}, 
 'CO->NE->SD->NE': {'condense'}, 
 'CO->NE->SD->MN': {'condemns'}, 
 'IL->MO->NE->KS': {'moleskin'}, 
 'IL->MO->AR->LA': {'amarillo'}, 
 'IA->NE->MO->TN': {'nominate'}, 
 'MO->IA->SD->ND': {'diamonds'}, 
 'SD->NE->CO->UT': {'contused'},

{% endhighlight %}

Yeah, that's more than 1. And there's only two instances of revisiting a state already visited.

Alright. That's a wrap!

## Further Reading ##

If you like this sort of thing, turns out there's several people 
who do this sort of thing with Python. There's all sorts of tools,
libraries and approachs people use to gather the data they need, take
a look!

* [Basic Wordplay with Natural Language Toolkit](http://www.socouldanyone.com/2017/08/solving-sunday-puzzle-with-python-and.html)
* [Wikipedia APIs, a library of common tools, and more!](https://github.com/boisvert42/npr-puzzle-python)

## Resources ##

* [States and their bordering states](https://thefactfile.org/u-s-states-and-their-border-states/)
* [State Abbreviations Python Dictionary]( https://gist.github.com/rogerallen/1583593)
* [Checking if a string is an English word](https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python)
* [Generating all permutations of a string](https://stackoverflow.com/a/8306692/39492)
