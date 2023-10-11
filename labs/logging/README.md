# Lab 3 - File Operations

The goal of this lab is for you familiarize yourself with creating variables, importing libraries, writing to a file, and reading from a file by creating a logger utility. A logger is an important tool for applications of all size and scope. If implemented and used properly it allows you to see what has happened and in what order.

## Step 1 - Setup

First create a new folder inside our `cmpt-120/labs` folder called `logging` and inside that folder, create two files called `logger.py` and `test_logger.py`. Copy the contents of the `test_logger.py` file from my logging folder on GitHub and paste it into yours.

## Step 2 - Naming our log file programmatically

When naming log files, it is customary to include the current date in the name of the log file. So for the first part of the assignment, I want you to programmatically include the current date in the log file name. The log file should have the format `log-file-yyyy-mm-dd.log`. Using the `datetime` package and string concatenation (or interpolation), I want you to reassign the value of `log_file` to include the date.

```py
# Change this to be log-file-yyyy-mm-dd.log
log_file = "log-file.log
```

Imports are typically done at the top of the file, like so:

```py
from datetime import datetime
```

In order to get the proper formatted version of the log file you would use the following function:

```py
log_file = "log-file-" + datetime.today().strftime('%Y-%m-%d') + ".log"
```

This would yield the log file name of "log-file-2023-10-11.log" which is the behavior that we want.

For help getting the proper date, you may use the [Python Docs](https://docs.python.org/3/library/datetime.html) online or review this [Stack Overflow](https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python) answer.

## Step 3 - Implement our log function

Next, we want to implement our `log` function in `logger.py`. Refer to our notes in chapter 5 on reading/writing to and from a file. We want to use the built in Python function `open` to open a file and use the proper mode to write to it. Some small caveats is that you will need to manually insert a newline character `\n` at the end of any text you want to log as that is not done for free using the `write` function. When you use this function you will notice a file is created with the text you passed in. However, there is a problem. We do not know when these logs were created!

> Hint: you will want to use the `open()` function with the "a" append option.

Next, we want to add a timestamp at the beginning of our logs. Using _string concatenation_ or _string interpolation_, I want you to insert the current date and time at the beginning of the log in the following format:

```sh
[yyyy-mm-dd hh:mm:ss] <message>\n
```

You may refer to the chapter 5 slides as well as same Python docs/Stack Overflow post from step 2 for help.

## Step 4 - Implement our dump function

Next, we want to implement our `dump` function in `logger.py`. Refer to our notes in chapter 5 or the online Python documentation on how to read a file's contexts into a variable. All this function is supposed to do is read the contents of the file into a variable and print that variable out to the user.

## Step 5 - Update our .gitignore

Finally, we are now going to want to update our `.gitignore` file so that our log files are not uploaded to Github every time we push. We can achieve this by adding `*.log` at the end of the file.

## Step 6 - Test our functions

Now let us manufally test our code. Create a new file in our `logging` folder called `main.py`. At the top of this file, I want you to import your logging functions from your `logger.py` file. You can do this like so:

```py
from logger import *
```

I want you to use the `log()` function to log the following messages:

1. Your name. (i.e., My name is Kevin)
2. Today's date. (i.e., Today's date is 10-11-2023)
3. What you ate for breakfast this morning. (i.e., I ate a bagel for breakfast)
4. Your favorite TV show. (i.e., My favorite show is Parks and Rec)
5. Your dream job. (i.e., I want to be a programmer!)

Open up the log file and take a screenshot. Submit that screenshot on Brightspace. It should look something like:

![Log File](/static/images/log-file.png)

Next, I want you to assign the return value of the `dump()` function to a string and print that out. It should print out exactly what is in the log file, line for line. Take a screenshot and submit that on Brightspace.

To test our function via unit tests we are going to run the `pytest` command which will run the new unit tests I have submitted with this assignment. The unit tests will test to make sure that your log file name is the correct format `log-file-yyyy-mm-dd.log`. 

## Final Step - Submitting your work

Once you have completed the work for the lab and you test down (all of your unit tests pass). I want you to submit all of the screenshots on Brightspace for full credit.