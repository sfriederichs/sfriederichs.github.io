---
layout: post
title:  "How To Write Makefiles"

date:   2019-06-18 9:25
categories: how-to make
---

Makefiles are great for standardizing builds. 

## General Rules ##

Use only tab characters in makefiles. Otherwise, you get an error.

## Makefile Example ##

{% highlight makefile %}

{% endhighlight %}


## Tips ##

Add echos for key variables 

## Random How-Tos ##

### Basic Substitution ###

You can substitute text in variables very simply:

{% highlight makefile %}
VAR_SRC_FILE_NAME = test.c
VAR_OBJ_FILE_NAME = $(VAR_SRC_FILE_NAME:.c=.o)
{% endhighlight %}

### Automatic Variables ###

See [here](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html) as well.

| Variable  | Description                                                                                                                               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| $@        | Rule target                                                                                                                               |
| $<        | First dependency                                                                                                                          |
| $^        | All dependencies, space-separated                                                                                                         |
| $*        | The stem which an implicit rule matches. For example, if the rule is %.o: %.c and you want to build app.o from app.c, $* will be 'app'    |

### Source File List to Object File List ###

If you want to generate an object file for each source file and put them in a special object file directory, do this:

{% highlight makefile %}
SOURCES = src/a.cpp src/b.cpp src/c.cpp
OBJECTS = $(patsubst %.c, obj/%.o, $(notdir $(SOURCES)))

{% endhighlight %}


### Ignoring Errors in Commands ###

Sometimes a command will cause an error, but you kinda expect that and want to keep going. A [Stackoverflow answer](https://stackoverflow.com/a/2670143) shows you how to ignore errors in commands - you put a dash in front of the command like so:

{% highlight makefile %}
build_target: $(PRE_REQS) 
    -this_command_causes_an_error_but_is_ignored $(PRE_REQS)
{% endhighlight %}

### Source files in multiple subfolders ###

Sometimes you have source files in multiple subdirectories of a main directory and you don't
want to make a dozen rules for a dozen different subdirectories.

{% highlight makefile %}
SRC_DIRS = $(sort $(dir $(wildcard ../src/*/)))
vpath %.c $(SRC_DIRS)
{% endhighlight %}

This will:

1. Generate a list of subdirectories in the ../src
2. Set the VPATH to look for .c files in each of the src subdirectories

VPATH is a built-in makefile feature which assigns a list of search directories to look for
specific files or types. In this case, if you have a rule like this:

{% highlight makefile %}
obj/%.o: %.c
    $(CC) - $(CFLAGS) -c $< -o $@
{% endhighlight %}

make will now search for .c files in each of the vpath subdirectories and you get to have one rule like this instead of this:

{% highlight makefile %}
obj/%.o: subdir1/%.c:
    $(CC) - $(CFLAGS) -c $< -o $@
    
obj/%.o: subdir2/%.c:
    $(CC) - $(CFLAGS) -c $< -o $@    
{% endhighlight %}

### Filtering out an item from a list based on an implicit rule ###

Okay, so imagine you're creating unit tests and you have 20 different source files in your application and you want to test the functions in one source file at a time. You will mock out the remaining functions for testing purposes.
However, when you generate the mocks, you generate mocks for all source files. You can't link the mock object file in the same executable as the actual source object file because all of the functions in the source file are
repeated in the mock. So, you have to remove the mock object file from being linked into the unit test executable. Let's say you have a rule to generate the executable from object files - this is how you structure the rule
to remove the mock object file from being linked. Assume $(MOCK_OBJ_FILES) contains all of the mock object files and ut_%.o is the unit test object file for the source file you want to test.

{% highlight makefile %}

$(BIN_DIR)/test_%: $(OBJ_DIR)/ut_%.o $(MOCK_OBJ_FILES)
	$(LINKER) $(filter-out $(OBJ_DIR)/Mock$*.o,$^) $(LINKFLAGS) -o $@
    
{% endhighlight %}

The use of the $* variable matches the stem of the implicit rule. For the $(OBJ_DIR)/ut_%.o you can use the percent sign, but that won't work inside a function like filter-out, so you have to use the automatic variable $* instead.
Note: You CANNOT match the implicit stem in the dependencies for the rule - you have to put them all in and then filter the dependencies when executing the link command

### Getting a list of all subdirectories recursively ###

If you have need a list of all subdirectories all the way down starting from a root directory, try this:

{% highlight makefile %}
SUBDIRS = $(shell find $(ROOT_DIR) -type d)
{% endhighlight %}

### Getting a list of all source files recursively ###

If you have a bunch of source files all over a directory (maybe with subdirectories or whatnot)
and you want to find all of the, say, .c files in that directory recursively, you do this:

{% highlight makefile %}
SOURCES := $(shell find $(SOURCEDIR) -name '*.c')
{% endhighlight %}

This should find all .c files recursively under $(SOURCEDIR).

### foreach - Include Directories ###

If you have a list of include directories and want to turn that list into a list of flags you have to pass the compiler, use this:

{% highlight makefile %}
INCDIRS = ./include /lib/include
INCFLAGS = $(foreach d,$(INCDIRS),-I$d)

{% endhighlight %}

## Resources ##

* [Hello World and Makefiles](https://www.embeddedrelated.com/showarticle/740.php)
* [Makefile name functions](https://www.gnu.org/software/make/manual/html_node/File-Name-Functions.html)
* [Getting subdirectories in a makefile](https://stackoverflow.com/a/13898309)
* [Recursively finding source files in a directory](https://stackoverflow.com/a/3774731)
