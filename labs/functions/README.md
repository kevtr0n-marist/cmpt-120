# Lab 4 - Functions

This week our lab will consist of defining functions and their invocations.

__Function__: a function is a block of code that only runs when it is called. Think of it as a miniature program within your program that performs the same routine with different arguments.

__Syntax__: In order to define a function you must following the syntax below.
```py
def <identifier>(<parameter_list>):
   <body>
```

__Example__:

```py
def greet(name):
    print("Hello {0}!".format(name))
```

## Setup

Create a new folder in your `cmpt-120/labs` folder and call it `functions`. Inside that folder, create a new file and call it `functions.py`. 

## Exercises

Complete all of the exercises below. When you complete an exercise. Take a screenshot of the output in the terminal.

### Exercise 1

1. Inside the `functions.py` file, define a function named `get_value`. This function takes no arguments and the goal of this function is to simply __return__ a __str__ value back to the caller.
2. Define a variable called `value` and assign it the return value of the `get_value` function.
3. Print the `value` to the console.

### Exercise 2

1. Inside the `functions.py` file, define a function named `find_smallest`.This function takes a __list__ of numbers as an argument. The goal of this function is to iterate through the list and find the smallest number in the list and __return__ the number back to the caller.
2. Define a list variable called `numbers` and pass it as an argument to the function.
3. Define a variable named `value` and assign it the return value of the function.
4. Print the `value` to the console.


### Exercise 3

1. Inside the `functions.py` file, define a funtion named `square`. This function takes a __variable__ number of __int__ arguments. The goal of this function is to square each integer passed in and add it to a list. Once all of the integers have been processed, __return__ the list of squared numbers.
2. Pass any number of integer values as arguments to the function.
3. Define a variable named `values` and assign it the return value of the function.
4. Print the `values` to the console.

### Exercise 4

1. Inside the `functions.py` file, define a function named `average`. This function takes a __list__ of numbers as an argument. The goal of this functino is to iterate through the list and compute the average of all the numbers. If no numbers are passed in, it should return `None`.
2. Define a list variable called `numbers` and pass it as an argument to the function.
3. Define a variable named `value` and assign it the return value of the function.
4. Print the `value` to the console.

### Exercise 5

1. Inside the `functions.py` file, define a function named `count_vowels`. This function takes a single string as an argument. The goal of this function is to iterate through each character, count each vowel, and return the total number of vowels back to the caller.
2. Pass in `"Hello world!"` as an argument to the function. 
3. Define a variable named `value` and assign it the return value of the functions.
4. Print the `value` to the console. (It should be 3).

### Bonus 

Copy the code from the unittest file `test_functions` in this package on Github into your folder containing the `functions.py` file. Run `pytest` from the command line to test your code against my unittests. If written pro

> __NOTE__: your functions must be named ___exactly___ how they are written in the instructions for the unittests to work.

## Submission

Submit a screenshot of each of the exercises on Brightspace for full credit.