# Lab 3 - Control Structures

Control structures are an essential part of programming that allow you to specify the flow of execution in your code. In Python, there are several types of control structures: sequential, selection, repetition, and error handling. In this lab we will focus on the first three only. Before we can do that, we must learn some things about __conditional operators__, __logical operators__, and the Python __keywords__ related to the topic. Do not write any code until you have read up until the first exercise.

## Conditional Operators

The operators below  are often used to check how two numbers stack up against one another. These operators also work with strings and other data types but for now we will just be using them

| Operator | Mathematics | Description              |
| -------- | ----------- | -------------------------|
| `<`      | <           | Less than                |
| `<=`     | ≤           | Less than or equal to    |
| `==`     | =           | Equal to                 |
| `>=`     | ≥           | Greater than or equal to |
| `>`      | >           | Greater than             |
| `!=`     | ≠           | Not equals               |

__Conditional Operator Examples__:

```py
print(1 < 2)          # 1 less than 2?               True
print(1 <= 2)         # 1 less than/equal to 2?      True
print(1 == 2)         # 1 equal to 2?                False
print(1 >= 2)         # 1 greater than/equal to 2?   False
print(1 > 2)          # 1 greater than 2?            False
print(1 != 2)         # 1 not equal to 2?            False
print("yes" == "yes") # True
print("yes" != "yes") # False
```


## Logical Operators

| Operator | Description                                                                  |
| -------- | ---------------------------------------------------------------------------- |
| `and`    | Both expressions must evaluate to `True`; otherwise evaluates to `False`.    |
| `or`     | Only one expression must evaluate to `True`; otherwise evaluates to `False`. |
| `not`    | Negates an expression.                                                       |

__Logical Operator Examples__:

```py
print(True and False)            # False
print(True or False)             # True
print(not True)                  # False
print((True or False) and True)  # True
print(not (True and True))       # False
```

## Control Structures

There are three different types of control structures in python:

- __Sequential__ - default mode.
- __Selection__ - used for decision making and branching.
- __Repetition__ - use for looping (i.e., repeating a code block multiple times).

---

### Sequential

Below is an example of the __sequential__ type. The code executes one line after the other.

```py
a = 20
b = 10
c = a - b
print("The difference is: ", c)
```

### Selection

Below are various examples of the __selection__ type. Using the keywords `if`, `elif`, `else`, `try`, and `except` we can execute various different bodies of code based on different scenarios. To use these keywords, we will make use of some __conditional operators__ to create our `bool` expressions. 

| Keywords | Description                             |
| -------- | --------------------------------------- |
| `if`     | To make a conditional statement.        |
| `elif`   | Used in conjunction with if-statements. |
| `else`   | Used in conjunction with if-statements. |

---

__Examples__:

- `if` statement:

    __Syntax__:

    ```
    if <boolean-expr>:
        <body>
    ```

    The way the `if` statement works is that it will evaluate the `boolean-expr` and if it evaluates to `True` then the body of the statement will execute. Here is an example. Imagine we have an _imaginary_ python library called `WeatherService` that connects to the internet and retrieves the weather in your location.

    ```py
    print("This program will tell you if the temperature is cold.")
    service = WeatherService()
    temperature = service.get_fahrenheit()
    print("The temperature is {0} degrees fahrenheit.".format(temperature))
    if temperature < 30.0:
        print("It is currently very cold.")
    ```

- `if-else` statement:

    __Syntax__:

    ```
    if <boolean-expr>:
        <body-1>
    else:
        <body-2>
    ```

    The way the `if-else` statement works is that it will evaluate the `boolean-expr` and if it evaluates to `True` then `body-1` will execute. If it evaluated to `False` then `body-2` will execute. Using the same imaginary service, here is another example below:

    ```py
    print("This program will tell you if the temperature is cold or not cold.")
    service = WeatherService()
    temperature = service.get_fahrenheit()
    print("The temperature is {0} degrees fahrenheit.".format(temperature))
    if temperature < 30.0:
        print("It is currently very cold.")
    else:
        print("It is not currently very cold.")
    ```

- `if-elif` statement:

    __Syntax__:

    ```
    if <boolean-expr-1>:
        <body-1>
    elif <boolean-expr-2>:
        <body-2>
    elif <boolean-expr-3>:
        <body-3>
    elif <boolean-expr-4>:
        <body-4>
    ```

    The way the `if-elif` statement works is that it will first evaluate `boolean-expr-1` and if it evaluates to `True` then `body-1` will execute and skip everything else. If it evaluates to `False` then it will skip `body-1` and evaluate `boolean-expr-2`. If that evaluates to `True` it will execute `body-2` and skip the rest. This will continue until there are no more `elif` clauses to evaluate. If none of the expressions evaluate to `True` then none of the bodies will execute. Here is an example:

    ```py
    print("This program will tell you if the temperature is cold or hot.")
    service = WeatherService()
    temperature = service.get_fahrenheit()
    print("The temperature is {0} degrees fahrenheit.".format(temperature))
    if temperature < 30.0:
        print("It is currently very cold.")
    elif temperature > 80.0:
        print("It is currently very hot.)
    ```

- `if-elif-else` statement:

    __Syntax__:

    ```
    if <boolean-expr-1>:
        <body-1>
    elif <boolean-expr-2>:
        <body-2>
    else:
        <body-3>
    ```

    The way the `if-elif-else` statement works is pretty much a combination of `if-else` and `if-elif`. It will evaluate each clause until one evaluates to `True` and if none evaluate to `True` then `body-3` in the `else` block will execute. Here is an example:

    ```py
    print("This program will tell you if the temperature is cold, hot, or comfortable.")
    service = WeatherService()
    temperature = service.get_fahrenheit()
    print("The temperature is {0} degrees fahrenheit.".format(temperature))
    if temperature < 30.0:
        print("It is currently very cold.")
    elif temperature > 80.0:
        print("It is currently very hot.)
    else:
        print("It is currently very comfortable.")
    ```

> __NOTE__: These various `if` statements can be nested in other `if` statements.

### Repetition

A __repetition statement__ is used to repeat a block of code. There are two different kinds of control loops: __definite__ and __indefinite__. __Definite__ loops, or __for-loops__ are used when you have a predefined number of times you want to repeat your code block. __Indefinite__ loops, or __while-loops__ are used when you __do not__ have a predefined number of times you want to repeat your code block.

| Keyword    | Description                                  |
| ---------- | -------------------------------------------- |
| `for`      | To create a for-loop.                        |
| `while`    | To create a while-loop.                      |
| `break`    | To break out of a loop.                      |
| `continue` | To continue to the next iteration of a loop. |

---

__Examples__:

- `for-loop` example:

    __Syntax__:

    ```
    for <iter> in <sequence>:
        <body>
    ```

    The `<sequence>` is any type of sequence in python that we want to iterate over (`list`, `set`, `dict`, `str`, etc.). The `<iter>` a reference to item in the sequence that we are iterating over whose scope is limited to the body of the loop. Here is an example:

    ```py
    # print the first 10 prime numbers.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes:
        print("{0} is a prime number.".format(prime))

    # print each letter in 'Hello world!'.
    for letter in "Hello world!":
        print(letter, end="")
    ```

- `while-loop` example:

    __Syntax__ example:

    ```
    while <boolean-expr>:
        <body>
    ```

    The `<boolean-expr>` is a boolean expression that gets evaluated before the body of the `while` loop gets executed. If the expression evaluates to `True` the body executes; otherwise the loop stops and relinquishes control back to the program. Picture a `while-loop` as an `if-statement` that executes indefinitely until it evaluates to `False.` Here is an example below of a `while-loop` where we play a guessing game and the body will execute indefinitely until either the user guesses correctly or quits.

    ```py
    answer = "elephant"
    guess = "":
    while guess != answer:
        guess = input("Guess the animal ('q' to quit): ").lower()
        if guess == "q":
            break
        elif (guess == answer):
            print("Correct!")
        else:
            print("Incorrect, try again!")
    ```

## Exercise 1 - Equilateral Triangle

The first thing to do is what we will always do to start a lab and that is to create a new module. Open up the `cmpt-120` folder with __vscode__ and create a new folder under the `labs` folder and call it `control`. In the `control` folder, create a new file and call it `equilateral.py`.

> __NOTE__: I am not sure if I mentioned this before, but a python file should end with the `.py` extension so your editor knows what type of file you are working on.

### Steps

__Problem__: 

Given three sides of a triangle, we don't know if is an equilateral or not. We want to create a program that calculates if a triangle is an equilateral and prints a message out to the user.

1. Print a message to the user stating what this program does.
2. Define a variable named `x` and prompt the user to enter the length of side 1.
3. Define a variable named `y` and prompt the user to enter the length of side 2.
4. Define a variable named `z` and prompt the user to enter the length of side 3.
5. Using a __SINGLE__ `if-statement`, check that all three sides are equal to one another and print out a message to the user telling them if the triangle is an equilateral or not. Defer to the sections above related to __conditional__ and __logical__ operators.

Once your program is working, execute the file using the __command line only__. Take a screenshot and upload it to Brightspace.

## Exercise 2 - Grade Point Average

__Problem__:

Given a stream of students grades, we want to calculate a student's grade point average and output the result.

1.  In the `control` folder, create a new file `grades.py`.
2.  Print a message to the user explaining what the program is designed to do.
3.  Define a empty list variable and call it `grades` like so: `grades = []`.
4.  Inside a `while-loop`, define a variable called `grade` and prompt the user enter in the value (don't forget to type-cast it to a float).
5.  Add the `grade` to the list of `grades` using the list's `append` function. Like so: `grades.append(grade)`
6.  We need an escape condition, `if` the user enters in a negative number; use the `break` keyword to exit out of the `while` loop.
7.  Next, use a `for-loop` to iterate through the list of grades to get the total sum of each grade.
8.  Determine the average by dividing `total` by the total number of grades input. (Hint: use the `len()` function.)
9.  Print a neatly formatted grade average back to the user rounded 2 decimal places. Example usage:
10. Using `if-elif-else` statements, print the student's letter grade.

__Example Usage:__ 

```
>> python grades.py
Enter grades to determine student's average.
Enter grade (negative to quit): 90
Enter grade (negative to quit): 89
Enter grade (negative to quit): 77
Enter grade (negative to quit): 72
Enter grade (negative to quit): 100
Enter grade (negative to quit): 34
Enter grade (negative to quit): 78
Enter grade (negative to quit): 98
Enter grade (negative to quit): 69
Enter grade (negative to quit): -1
Student average: 78.56
Student letter grade: C+
```

Once your program is working, execute the file using the __command line only__. Take a screenshot and upload it to Brightspace.
