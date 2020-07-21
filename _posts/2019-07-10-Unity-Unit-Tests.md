---
layout: post
title:  "How To Write Unit Tests with Unity"

date:   2019-07-10 9:25
categories: how-to unity unit-test
---

I've written about the importance of unit tests before so it makes sense that I'd write a guide on how to implement them in your project. In the past I've used a unit test framework called Check which was useful and had lots of nice features, but the demands of the project I'm currently on has caused me to move towards a different framework.

That framework is called [Unity](http://www.throwtheswitch.org/unity) and it has a few advantages and disadvantages against check:

Advantages:

* Is distributed in source which can allow unit tests to run on-target
* Can be integrated with CMock to automatically generate mocks/stubs for tests (Big plus!)
* Straightforward and simple to use
* Comes with supplementary scripts to aid in test generation/automation

Disadvantages:

* Unit tests run in the same thread as the test executive which means bad code can fowl up the test execution instead of just producing a failure
* Doesn't include timeout functionality - infinite loop tests will cause a complete hangup of the test
* Mediocre test result options (when not using Ceedling)

Overall though, the inclusion of the supplementary scripts, automated generation of powerful mocks and the ability to execute tests on-target is what sets Unity apart from Check (which basically only performs pass/fail checking) and makes it a worthwhile choice to
use for unit testing

## Background/Directory Structure ##

For the purposes of this how-to we will assume you have the following contained within a top-level project folder:

* Target source code that you want to test - all contained in one directory, possibly with sub-directories (./src)
* A 'tools' directory in which the CMock and Unity files can be stored (./tools)
* A directory which contains unit test-related files (./test)
* A directory in which to store configuration files (./cfg)

Within the unit test directory, there are the following subdirectories:

* A directory for storing the unit test binaries (./test/bin)
* A directory for storing object code files (./test/obj)
* A directory for storing results (./test/results)
* A directory for storing unit test source files (./test/src)

There will also be several directories under ./test/src:

* A directory for storing automatically-generated mocks (./test/src/mocks)
* A directory for storing automatically-generated test runner files (./test/src/testRun)

In order to unit-test our target code, we will do the following things:

1. Pick one target source file to unit-test
2. Generate mocks for the functions in all the other target source files
3. Generate a unit-test source file named against the target source file being tested.
4. Create one or more test functions for each function within the target source file
5. Compile the mocks and test source into a object files, then link them into a binary
6. Pipe the output of the binary into a results file

Then, repeat this process for all the target source files and eventually all of your code will be tested!

## Acryonyms ##

| Acronym           | Meaning                               | Description                                                       |
|-------------------|---------------------------------------|-------------------------------------------------------------------|
| UT                | Unit Test                             | A test for a single software 'unit' - typically a function        |
| FUT               | Function Under Test                   | The target function which the Unit Test is testing                |

Table: Acronyms

## Generating Mocks ##

In the ./src directory (and/or its subdirectories) there are source files for your actual project. I'll call these 'target' source files (as opposed to 'test' source files which will come up in a bit). Inside these source files
are functions that we want to unit test. Here's the important part: these functions will call *other* functions from *other* target source files. In the actual target application you want to *actually* call those functions so that 
your code correctly implements its behaviors for your application, but when unit testing we don't want that to happen at all. All we want to confirm is that those external functions were called a certain number of times, that they
were called with specific parameters each time, and if applicable, we want to return specific values from those function calls back to the calling function. 

Mocks are what allow us to do all of this. When you generate a mock for an external function, you generate a special function which is named the same as the external function, but which contains test code which verifies passed
parameters, number of times the function is called, etc. In essence, it's a fake function which gets put into place of the real one when you're unit-testing so that you can verify the code you're testing behaves correctly.

Generating mocks manually would be a time-consuming and boring process. Luckily, the makers of Unity created another utility to make generation of mocks easy - CMock.

### Installing CMock and Unity ###

Before we can generate the mocks we need to install both Unity and CMock. These steps assume that you have Ruby installed already:

1. Download [CMock](https://github.com/ThrowTheSwitch/CMock/archive/master.zip)) and unzip it into ./tools/CMock
2. Download [Unity](https://github.com/ThrowTheSwitch/Unity/archive/master.zip) and unzip it into ./tools/CMock/vendor/unity
3. Open a command prompt/shell and change the working directory to the directory in which CMock was unzipped and type:
> bundle install

This should install CMock and Unity, though honestly I'm not sure what the 'install' is actually doing since I use the scripts and files in-place.

### Using CMock ###

CMock is interesting in that its inputs aren't the source files, but their headers. CMock will read a header file to see what functions are supposed to be available for other source files, and then will generate mocks for those functions without needing to look at the source file.
This makes sense: the behavior of the actual target function being mocked isn't necessary to know when mocking - all mocks do the same thing (count the number of times the function is called, verify passed parameters, etc.). 

To generate a mock using CMock, follow these steps:

1. Open a command prompt/shell and change the working directory to ./test/src
2. Pick the header file you want to mock the functions of - we'll say in this case we have a header called *uartSendBytes.h* which is located in ./src
3. Use the following command line to generate mock source files and header files from the *uartSendBytes.h* file:
> ruby ../../tools/CMock/lib/cmock.rb ../../src/uartSendBytes.h
4. This command generates the mock files in the default mock directory under the will generate two files in ./test/src/mocks:
* MockuartSendBytes.h
* MockuartSendBytes.c

These files contain mock functions for every function defined within *uartSendBytes.h*.

### CMock Configuration File ###

CMock can use a configuration file to specify options for generating mocks. Below is an example because I had a heck of a time figuring out the YAML format for the configuration file. The settings in this file are mainly the 
strippables which cause CMock to ignore some function-like macros that caused issues in the mocking. It also adds a default include to each of the C source files generated by CMock - *mockHeader.h*

{% highlight yaml %}
---
:cmock:
  :strippables: 
    - '(?:VALIDATE_SIZE\s*\(+.*?\)+)'
    - '(?:VX_MUTEX_SEMAPHORE\s*\(+.*?\)+)'
  :includes_c_pre_header: [mockHeader.h]


{% endhighlight %}

The following command line has been modified to use the configuration file:

> ruby ../../tools/CMock/lib/cmock.rb -o../../cfg/cmock.yml ../../src/uart.h

For a full discussion of the options in a CMock configuration file, see [here](https://github.com/ThrowTheSwitch/CMock/blob/master/docs/CMock_Summary.md).

## Creating Tests ##

Next, we will need to create a file which contains tests to test the various functions in the target source file we're testing. 

For the purposes of this example, let's assume that we have a function within *uart.c* called *uartSendString*. The purpose of this function is to transmit a string over the UART. The contents of the function are shown in the 
snippet below:

{% highlight c %}

int uartSendString(char const * strPtr) {
    int i;
    int retVal = 0;
    
    while(*strPtr) {
        retVal = uartSendByte(*(strPtr++));
        if(retVal)              //Check for transmission errors
            return retVal;
    }
    return retVal;
}

{% endhighlight %}

NOTE: In the real world, I would expect *uartSendByte* to be in the same source file as *uartSendString*. If that were the case, however, the approach presented here would *NOT* work
because we would be unable to mock the *uartSendByte* function. For the purposes of this example we will assume that the functions are in separate files.

We will need to create a test file containing a test for this function.

First, we need to know what this file will be called and where it will be placed. I've decided on the naming convention that the test file is named after the target source file being tested, according to the below standard:

> \<Target Source File\>.c -\> ut_\<Target Source File\>.c

Thus, since we're testing functions in *uart.c*, our test source file will be *ut_uart.c*. It will be located in ./tests/src.

For the purposes of this testing methodology, each function in the target source file being tested will have (at least) one function to test it. You can decide how you want to split things up - maybe the test function you create
can have multiple tests in it, maybe each test gets its own test function - it's all up to you. The only rule for this methodology is that every function which tests your target function *must* be named correctly:

> \<function under test\> -\> test_\<function under test\>

The *test_* prefix is important because it will allow some of our automation scripts to identify the test function when it generates a test runner (more on that later). For this example, the test function will be called *test_uartSendString*.

Test functions have no parameters are return nothing.

There are several important code items that must be present in the test source file - these are shown and explained in the code snippet below along with the test function for *uartSendString*.

{% highlight c %}

/** @ file ut_uart.c
    @brief This file contains tests for functions found in the target source file uart.c
*/

int uartSendByte(unsigned char x);
int uartSendString(char const * strPtr);

#include <unity.h>  //Required - Unity test framework include
#include <MockuartSendByte.h>


/** @fn test_uartSendString
    @brief Test function for target function uartSendString

    Basic test case
*/

void test_uartSendString(void) {

    char testString[] = "Test";             //Create a string for the function under test to ingest
    int retVal=-1;                          //Create a variable to store the return value of the function under test and set it to a value OTHER than what will be expected.
    
    //Set up the expectations for the mocked functions called by uartSendString - in this case, only uartSendByte
    
    uartSendByte_ExpectAndReturn('T',0);    //Mock function - on the first call, expect the character 'T' and return 0
    uartSendByte_ExpectAndReturn('e',0);    //Mock function - on the first call, expect the character 'e' and return 0
    uartSendByte_ExpectAndReturn('s',0);    //Mock function - on the first call, expect the character 's' and return 0
    uartSendByte_ExpectAndReturn('t',0);    //Mock function - on the first call, expect the character 't' and return 0
    
    //Call the function under test with the test string and capture the return value
    
    retVal = uartSendString(&testString);
    
    TEST_ASSERT_EQUAL_MESSAGE(0,retVal,"Return value from uartSendString is incorrect");    //Use the Unity framework to verify the return value from the function under test
}
    
{% endhighlight %}

This is a fairly minimal example of creating a test file for a single function. 

It should be noted that if you want to create multiple test cases for this function (i.e., you will call the function under test with multiple different strings) you will need to create *multiple test_ functions*, doing
this will *not* work:

{% highlight c %}
void test_uartSendString(void) {

    char testString1[] = "Test";             //Create a string for the function under test to ingest
    char testString2[] = "Food";            //Create a string for the second test
    
    int retVal=-1;                          //Create a variable to store the return value of the function under test and set it to a value OTHER than what will be expected.
    
    //Set up the expectations for the mocked functions called by uartSendString - in this case, only uartSendByte
    
    uartSendByte_ExpectAndReturn('T',0);    //Mock function - on the first call, expect the character 'T' and return 0
    uartSendByte_ExpectAndReturn('e',0);    //Mock function - on the first call, expect the character 'e' and return 0
    uartSendByte_ExpectAndReturn('s',0);    //Mock function - on the first call, expect the character 's' and return 0
    uartSendByte_ExpectAndReturn('t',0);    //Mock function - on the first call, expect the character 't' and return 0
    
    //Call the function under test with the test string and capture the return value
    
    retVal = uartSendString(&testString1);
    
    TEST_ASSERT_EQUAL_MESSAGE(0,retVal,"Return value from uartSendString is incorrect");    //Use the Unity framework to verify the return value from the function under test
    
    uartSendByte_ExpectAndReturn('F',0);    //Mock function - on the first call, expect the character 'F' and return 0
    uartSendByte_ExpectAndReturn('o',0);    //Mock function - on the first call, expect the character 'o' and return 0
    uartSendByte_ExpectAndReturn('o',0);    //Mock function - on the first call, expect the character 'o' and return 0
    uartSendByte_ExpectAndReturn('d',0);    //Mock function - on the first call, expect the character 'd' and return 0
    
    //Call the function under test with the test string and capture the return value
    
    retVal = uartSendString(&testString2);
    
    TEST_ASSERT_EQUAL_MESSAGE(0,retVal,"Return value from uartSendString is incorrect");    //Use the Unity framework to verify the return value from the function under test
    
}
{% endhighlight %}

This will cause a failure with the mocks - they will be looking for all 8 calls to be made at once instead of spread out over two calls to the function-under-test. To remedy this, you will need to write the tests like this:

{% highlight c %}
void test_uartSendString_Test(void) {

    char testString[] = "Test";             //Create a string for the function under test to ingest
  
    
    int retVal=-1;                          //Create a variable to store the return value of the function under test and set it to a value OTHER than what will be expected.
    
    //Set up the expectations for the mocked functions called by uartSendString - in this case, only uartSendByte
    
    uartSendByte_ExpectAndReturn('T',0);    //Mock function - on the first call, expect the character 'T' and return 0
    uartSendByte_ExpectAndReturn('e',0);    //Mock function - on the first call, expect the character 'e' and return 0
    uartSendByte_ExpectAndReturn('s',0);    //Mock function - on the first call, expect the character 's' and return 0
    uartSendByte_ExpectAndReturn('t',0);    //Mock function - on the first call, expect the character 't' and return 0
    
    //Call the function under test with the test string and capture the return value
    
    retVal = uartSendString(&testString);
    
    TEST_ASSERT_EQUAL_MESSAGE(0,retVal,"Return value from uartSendString is incorrect");    //Use the Unity framework to verify the return value from the function under test
    
  
    
}
void test_uartSendString_Food(void) {
    
    char testString[] = "Food";
    
    uartSendByte_ExpectAndReturn('F',0);    //Mock function - on the first call, expect the character 'F' and return 0
    uartSendByte_ExpectAndReturn('o',0);    //Mock function - on the first call, expect the character 'o' and return 0
    uartSendByte_ExpectAndReturn('o',0);    //Mock function - on the first call, expect the character 'o' and return 0
    uartSendByte_ExpectAndReturn('d',0);    //Mock function - on the first call, expect the character 'd' and return 0
    
    //Call the function under test with the test string and capture the return value
    
    retVal = uartSendString(&testString);
    
    TEST_ASSERT_EQUAL_MESSAGE(0,retVal,"Return value from uartSendString is incorrect");    //Use the Unity framework to verify the return value from the function under test
}

{% endhighlight %}

Each function will be executed if you follow the steps to create a test runner automatically.

Next, we need to create a source file to run this test.

## Creating a Test Runner ##

So far, we've written or generated mock functions and test functions to support unit testing our *uartSendString* function under test. There's only one more aspect of our unit test that we need to generate: a test runner.

The test runner is essentially a *main()* function that properly (according the rules of Unity) calls your test functions. It also has a bunch of setup and tear down to support the mock functions.
Theoretically you can write your own test runner by hand, but every time I tried the mocks didn't work correctly, so I decided to just use one of the scripts that came with Unity to
generate the test runner.

It's actually quite easy and interesting - you pass a test file to the script on the command line, it scans the file for *test_* functions and generates all the code needed to run them.

The script is invoked from the command line/shell thusly (when in the ./test/src directory):

> ruby ../../tools/CMock/vendor/unity/auto/generate_test_runner.rb ut_uart.c ./testRun/test_uart.c

This will generate ./testRun/test_uart.c which contains a lot of unintelligible code, but ultimately will execute the tests properly.

### Test Runner Configuration File ###

You can also create a YAML configuration file for the test runner generator. I've plased an example I've used below because I have troubles getting the YAML formatting correct. This should not 
be considered to be tailored to this specific application. This configuration file will add an include to the test runner files.

{% highlight yaml %}
:unity:
  :includes:
    - vxWorks.h
{% endhighlight %}

To use the configuration file, this would be the command line:

> ruby ../../tools/CMock/vendor/unity/auto/generate_test_runner.rb ut_uart.c ./testRun/test_uart.c ../../cfg/testRunner.yml

## Generating the Unit Test Binary ##

At this point we have:

* MockuartSendBytes.h - Contains function definition for mocked *uartSendBytes*
* MockuartSendBytes.c - Contains mock of *uartSendBytes*
* uart.c - Contains function under test - *uartSendString*
* uart.h - Contains funcion definition for *uartSendString*
* ut_uart.c - Contains tests for *uartSendString*
* test_uart.c - Contains *main()* function for running tests
* unity.c - Source code for the Unity test framework

We need to compile all of these into a binary file. We will do that wil GCC thusly (assuming we are currently working from the root of the project):

> gcc tools/CMock/vendor/unity/src/unity.c test/src/mocks/MockuartSendBytes.c test/src/testRun/test_uart.c test/src/ut_uart.c src/uart.c -o bin/test_uart

NOTE: There need to be -I include paths here as well.

This will generate *bin/test_uart* which will run the tests.

You can pipe the results to a results file like this:

> ./bin/test_uart > results/results.txt

## Makefile ##

I've created a makefile which handles the generation of all of the mocks, test runners, binaries, etc. The only things you need to provide are the configuration files, source files
and test files. This file should be placed in ./test.
This makefile should, if you simply call 'make', generate unit test binaries for every 'ut_*.c' file in your ./test/src folder, run them, and put the results in 
{% highlight makefile %}


PRJ_ROOT_DIR = ..

#Location for compiled object files
OBJ_DIR = obj
           
#Location for test binaries
BIN_DIR = bin
             
#Location for results
RESULTS_DIR = results

#Location for test source files
UT_SRC_DIR = src

#Location to store generated mocks
MOCK_DIR = $(UT_SRC_DIR)/mocks

#Location to store generated test runners
UT_RUNNER_DIR = $(UT_SRC_DIR)/testRun

#Root directory for target source files
TGT_SRC_ROOT = $(PRJ_ROOT_DIR)/src

#Gets a list of all subdirectories in the target source folder
TGT_SRC_DIRS = $(shell find $(TGT_SRC_ROOT) -type d)

#Generate a list of target source files...
TGT_SRC_FILES = $(shell find $(TGT_SRC_ROOT) -name '*.c')

#And their respective object files when compiled
TGT_OBJ_FILES = $(patsubst %.c,$(OBJ_DIR)/%.o,$(notdir $(TGT_SRC_FILES)))

#Finds all .h (header) files recursively in the target source directory
TGT_HEADER_FILES = $(shell find $(TGT_SRC_ROOT) -name '*.h')

#Generates a list of mock source file paths derived from the target header files
TGT_MOCK_FILES = $(patsubst %.h,$(MOCK_DIR)/Mock%.c, $(notdir $(TGT_HEADER_FILES)))

MOCK_OBJ_FILES = $(patsubst %.c, $(OBJ_DIR)/%.o,$(notdir $(TGT_MOCK_FILES)))

CMOCK_DIR = $(PRJ_ROOT_DIR)/tools/CMock
CMOCK_SRC_DIR = $(CMOCK_DIR)/src
CMOCK_OBJ_FILES = $(OBJ_DIR)/cmock.o

UNITY_SRC_DIR = $(CMOCK_DIR)/vendor/unity/src

#The path to where the object file of the compiled unity source will be  located              
UNITY_OBJ_FILES = $(OBJ_DIR)/unity.o                                       

#Generates a list of the test files 
UT_SRC_FILES:= $(shell find $(UT_SRC_DIR) -name 'ut_*.c')

#Generates a list of 
TEST_BIN_FILES = $(patsubst ut_%.c, $(BIN_DIR)/test_%, $(notdir $(UT_SRC_FILES)))

#Location of the overall results file
RESULTS_FILE = $(RESULTS_DIR)/results.txt

#VPaths specify paths on which to look for files of a specific type
vpath %.c $(TGT_SRC_DIRS) $(UT_SRC_DIR) $(MOCK_DIR) $(UT_RUNNER_DIR) $(UNITY_SRC_DIR) $(CMOCK_SRC_DIR)
vpath %.h $(TGT_SRC_DIRS) $(MOCK_INC_DIR) 

#Compiler command line
CC = gcc
#Non-include and non-define compiler flags                                
_CFLAGS = -g

#Linker command line
LINKER = g++

#Libraries to link against                            
LIB =

#Flags to be passed to linker                                   
LINKFLAGS = $(LIB)

#Definitions to be included in compiler command line
DEFS =                                  
DEFFLAGS = $(foreach d,$(DEFS),-D$(d))

#Include paths for compilation 
INC = $(TGT_SRC_ROOT) $(TGT_SRC_DIRS) $(CMOCK_SRC_DIR) $(MOCK_DIR) $(MOCK_INC_DIR) $(UNITY_SRC_DIR) 
INCFLAGS = $(foreach d,$(INC),-I$(d))

CFLAGS = $(_CFLAGS) $(INCFLAGS) $(DEFFLAGS) 

all: results

results: $(RESULTS_FILE)

#Note: the dash before 'for' below ignores errors - this allows all tests to run despite failures
$(RESULTS_FILE): $(TEST_BIN_FILES)
	-rm $(RESULTS_FILE)
	-for x in $(TEST_BIN_FILES); do ./$$x >> $(RESULTS_FILE); done
	
#Generic rule to generate an object file from a source file
$(OBJ_DIR)/%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

#This rule needs to be in place so that make knows it must generate a test_%.c file 
$(OBJ_DIR)/test_%.o: $(UT_RUNNER_DIR)/test_%.c
	$(CC) $(CFLAGS) -c $< -o $@

#Rule to generate test runner source files from unit test source files using Unity scripts
$(UT_RUNNER_DIR)/test_%.c: ut_%.c
	ruby $(CMOCK_DIR)/vendor/unity/auto/generate_test_runner.rb $< $@ 
    
#Rule to generate a mock source file from a target header file via CMock
$(MOCK_DIR)/Mock%.c: %.h
	ruby $(CMOCK_DIR)/lib/cmock.rb -o../cfg/unitTest.yml $<
    
#Rule to generate unit test binary from all relevant object files
#Note: the precedents for this step contain ALL mock object files and ALL target source files even though those get filtered in the actual linker set
#This is due to the fact that it may be impossible (i.e., I haven't figured out how) to filter the precendents correctly
$(BIN_DIR)/test_%: $(OBJ_DIR)/ut_%.o $(OBJ_DIR)/test_%.o $(UNITY_OBJ_FILES) $(CMOCK_OBJ_FILES) $(MOCK_OBJ_FILES) $(TGT_OBJ_FILES)
	$(LINKER) $(filter-out $(OBJ_DIR)/Mock$*.o,$(MOCK_OBJ_FILES)) $(filter $(OBJ_DIR)/$*.o,$(TGT_OBJ_FILES)) $(OBJ_DIR)/ut_$*.o $(OBJ_DIR)/test_$*.o $(UNITY_OBJ_FILES) $(CMOCK_OBJ_FILES) $(LINKFLAGS) -o $@

mocks: $(TGT_MOCK_FILES) 

tests: $(TEST_BIN_FILES)

.FORCE:

clean:
	@echo "Cleaning output directories..."
	@rm -rf $(BIN_DIR)/*
	@rm -rf $(OBJ_DIR)/*
	@rm -rf $(MOCK_DIR)/*
	@rm -rf $(UT_RUNNER_DIR)/*
	@rm -rf $(RESULTS_DIR)/*


{% endhighlight %}

## Jenkins Integration ##

It's worthwhile to create a Jenkins task to execute these unit tests. If you do this, Jenkins can alert you when the unit tests fail with an ~~annoying~~ helpful email.

The trick of the Jenkins integration is the script you use to execute the unit tests. The kicker is that since I ignored errors when executing unit test binaries, I need a way to gauge pass or fail from the command line so I can
mark the build as failed when a unit test fails. Here's how I did that:

{% highlight bash %}
cd F
make clean
make 
if [[ $(grep -c FAIL results/results.txt) -gt 0 ]]
then
	exit 1
fi
exit 0

{% endhighlight %}

This will let the tests run, then examing the results.txt file to see if the word 'FAIL' is in there, and exit with an error code if it is. This allows all the tests to run and the error status to be passed back to Jenkins
so the ~~annoying~~ helpful emails can be sent automatically when there's a failure.

It's also helpful to add a post-build step which archives the results so you can easily find them. To do that, add a post-build step to archive artifacts, and the path to the artifact you want to archive is here:

> test/results/results.txt

Then, you can find the results of the most recent build by going to http:\<Jenkins server IP\>/job/\<Job Name\>/lastBuild/artifact/test/results/results.txt

## Common Issues ##

### Returning Data Through Pointers ###

Many functions will use pointers to return data instead of return values (or in addition to return values).
You can use CMock to do this as well. Imagine we have a function that returns data through a pointer:

{% highlight c %}

int dummyFunction(unsigned char dataIn, unsigned char * dataOut);

{% endhighlight %}

You have to do four things to return data through dataOut:

* Configure CMock to include the plugins that enable return thru pointer functionality
* Give CMock at least one Expect or ExpectAndReturn call for the function
* Then, tell CMock to ignore the value of dataOut that is passed to the function
* Finally, instruct CMock to return a specific value through the pointer.


To configure CMock with the proper plugins we need to update the configuration file with the 'plugins' setting:


{% highlight yaml %}
---
:cmock:
  :strippables: 
    - '(?:VALIDATE_SIZE\s*\(+.*?\)+)'
    - '(?:VX_MUTEX_SEMAPHORE\s*\(+.*?\)+)'
  :includes_c_pre_header: [mockHeader.h]
  :plugins:
    - :ignore
    - :ignore_arg
    - :array
    - :callback
    - :return_thru_ptr
    - :expect_any_args

{% endhighlight %}

There are some extras there under plugins, but you'll probably want those too someday.

The next three steps are done within the test function that you're writing. In order to return the value 0xAB 
through the pointer, you'd use the following CMock calls in this order:

{% highlight c %}

    dummyFunction_ExpectAndReturn(0,NULL,0);    //Expect 0 for dataIn, NULL for dataOut and return 0
                                                //NULL for dataOut will be overridden shortly
    dummyFunction_IgnoreArg_dataOut();          //Instruct CMock to not fail the test if the value of dataOut isn't NULL
    dummyFunction_ReturnThruPtr_dataOut(0xAB);  //Instruct the mock to assign the value pointed to by dataOut to 0xAB
                                               
{% endhighlight %}

This sequence of calls will put the proper data into the address opinted to by dataOut and will not fail the
test because the value of dataOut doesn't match the expected value. It's worth noting that with pointers
like this many times we can't 'expect' a proper value for the value of the pointer since often the pointers
are instantiated within functions and will have random addresses from the stack instead of a known repeatable
value.

It is worth noting here that you can mess this whole process up very easily if, instead of an ExpectAndReturn
being the first call, you do an IgnoreAndReturn or Ignore. These Ignore calls apparently just wash their hands
of the whole function such that subsequent IgnoreArg and ReturnThruPtr calls will not work.

### Missing Mocks ###

Problem: I get linker errors trying to find \<function\>_Expect or \<function\>_ExpectAndReturn, help!

Solution: Ensure that you include the header files for the mocked functions and not only the source file for the actual function.

### Mocking Functions in the Same File as the FUT ###

Problem: The FUT calls functions in the same source file as itself - these files do not have mocks generated for them, so the function calls can't be directly verified using CMock and Unity.

Solution: Currently, the only solution I have is to analye the behavior of the called function and instruct Unity to 'expect' that behavior (i.e., mocked functions called, variables changed, etc.)

The problem with this approach is that sometimes the behavior of the called functions can be complex and writing the tests can be difficult. There is no workaround for this at the moment.

One potential future workaround is to follow these steps:

1. Generate mocks for *ALL* functions in your project - including your FUT. You now have mocks for every function within the file that contains the unit test (which your FUT calls) as well as the FUT.
2. Copy the source and header files containing the FUT and rename all of the functions within from \<function_)name\> to fut_\<function_name\>. This will create alternate versions of your code where the function name is changed.
3. In your test functions, instead of calling \<function_name\> for your FUT, call fut_\<function_name\>. This will ensure the original (not mocked) FUT is tested, but the function calls within your FUT will access the mocked versions of the functions in the same file as it instead of the actual ones (which have been renamed fut_\<function_name\>)
4. Compile the unit test project with all the mock source files, the test files, test runners and the *COPY* of the FUT source file where the function names are changed.

This will allow you to more easily test functions which call other functions in the same source file.

Ideally, there would be a way to automate this. Stay tuned.

## Resources ##
* [Handling Difficult Issues with CMock and Unity](https://spin.atomicobject.com/2012/01/15/using-cmock-when-c-is-oversensitive/)