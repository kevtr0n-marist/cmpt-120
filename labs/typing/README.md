# Lab 2 - Basics

## Exercise 1 - Data Types

In your `cmpt-120/labs/` folder, create a new folder called `typing`. You should now have two different folders in your labs folder:

- `cmpt-120/labs/setup`
- `cmpt-120/labs/typing`

Create a new __python__ file in the `typing` folder called `typing.py`.

### Step 1 - Assignment

There are four primitive data types in the Python programming language. The first thing I want you to do is to create a variable of each primitive type.

1. Create an integer variable called `my_int` and assign it an integer value.
2. Create a float variable called `my_float` and assign it a decimal value.
3. Create a boolean variable called `my_bool` and assign it true/false value.
4. Create a string variable called `my_str` and assign it a text value.

> __Tip:__ Remember the syntax for assignment is the following:
>
> ```
> <var> = <exr>
> ```
>
> Where `<var>` is your variable identifier, `=` is the assignment operator, and `<exr>` is the value.

After you create each variable, I then want you to print the value to the command line using the `print()` function. You can test this by running this file from the command line like so:

```sh
# while in your cmpt-120 folder
python labs/typing/typing.py
```

You should see the four values you assigned printed to the console.

### Step 2 - Type Checking

Sometimes the need to check the type of a variable may arise. In order to check the type of a variable, you must use the `type()` function which will return the type of whatever variable passed in as an argument. Check the type of each variable and print the result to the console like so:

> __Tip:__ Remember; you can pass a function call as an argument to another function, like so:
>
> ```py
> print(type(my_int))
>```

### Step 3 - Type Casting

One day, there may be a need to convert the data type of one variable to another. In order to do this you must make use of the following built-in Python functions:

- `int()` - converts a variable to an `int`.
- `float()` - converts a variable to a `float`.
- `bool()` - converts a variable to a `bool`.
- `str()` - converts a variable to a `str`.

It is important to note that there may times where you are unable to convert a variable into another data type. Consider the following scenario, you define a variable named `my_str` and you assign it a value of `"my text"`.

```py
my_float = float(my_str)
```

That line will cause an error because non-numerical text cannot be converted to a number. So it is important you are aware of the value you are trying to type cast.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'my text'
```

Please create the following variables and print out the values afterwards:

5. Create a variable called `int_to_float` and assign it the value of `float(my_int)`.
6. Create a variable called `float_to_int` and assign it the value of `int(my_float)`. You may notice something happen here that you may not have intended. By converting a float to an integer, we have effectively rounded the number down to nearest whole number by chopping off the decimal value. You must be careful when performing type conversions that you do not throw away data in this way unless intended.
7. Create a variable called `text` and assign it the value of `"123.456"`.
8. Create a variable called `str_to_float` and assign it the value of `float(text)`.
9. Create a variable called `float_to_str` and assign it the value of `str(my_float)`

### Step 4 - Erroneous Type Casing

I want you to demonstrate for yourself the consequences of invoking the `float` function on a non-numerical string value.

10. Create a variable called `error_var` and assign it the value of `float("hello")`. This should raise the `ValueError` I was explaining earlier. 

### Finishing Up

Once you have finished all of the steps, please run the execute the python and take a screenshot of the output (error included). Please submit that screenshot on Brightspace. 

```sh
# while in your cmpt-120 folder
python labs/typing/typing.py

```

You should see something like this:

```
1
41.2
False
some text
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'str'>
1.0
41
123.456
123.456
41.2
1
41.2
False
some text
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'str'>
1.0
41
123.456
123.456
41.2
Traceback (most recent call last):
  File "/home/kevtr0n/Repositories/marist/2023/fall/cmpt-120/labs/typing/typing.py", line 29, in <module>
    error_var = float("Hello")
                ^^^^^^^^^^^^^^
...
...
...
```
