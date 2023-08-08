# Lab 1 - Environment Setup

10 points. Please complete each step.

**NOTES**: _At any time you are uncertain, ask for help rather than attempting to continue. I don't expect you to understand most of this stuff, but it is important for you to have this environment setup for ease of learning._

## Python Installation

The first thing we are going to do is install the latest version of _Python 3_. Some computers come with Python 2 by default and is used by the system. This version of Python is deprecated (no longer supported). We are going to want to use the feature-rich latest version of Python 3.

On your personal computer or laptop, visit https://www.python.org/downloads/ and install the latest version of Python 3.

Open up __Command Prompt__ on Windows or __Terminal__ on MacOS and run the following command:

```sh
python3 --version
```

You should see some output detailing the version of python that is being invoked.

```sh
Python 3.10.11
```

If you get an error, or the output doesn't say Python 3.xx.xx, raise your hand and I will help you out.

> NOTE: If at some point during the installation it asks you if you want to add it to PATH, check the box and continue. 

## Visual Studio Code Installation

The next thing we are going to do is install our _code editor_. This is application we are going to be using to create and edit our python files.

On your personal computer or laptop, visit https://code.visualstudio.com/ and install the latest version of Visual Studio Code.

## Visual Studio Code Configuration

Now that we have installed Visual Studio Code (or just simply __vscode__) we are going to want to configure it for Python development. On your personal computer or laptop, open up vscode and click the button on toolbar on the left labled "Extensions". 

1. In the "Extensions: Marketplace" searchbar, type in __"Python"__ and you should see an extension made by Microsoft. Press the green __Install__ button to install the extension. 
2. In the "Extensions: Marketplace" searchbar, type in __"Code Runner"__ and you should see an extension made by Jun Han. Press the green __Install__ button to install the extension.

This extension provides very useful tools to improve your development skills such as syntax highlighting, debugging, and more.

> NOTE: You may need to reload/restart the application for the extension to work.

## Project Hierarchy

Next, We are going to want to have a dedicated folder to store all of our python code for this class. 

1. On your personal computer or laptop, create a new folder called __cmpt-120__ somewhere you will remember.
2. Using __vscode__, open up that folder by pressing __File__ > __Open...__ and navigate to that __cmpt-120__ folder you just created and press __Open__.
3. Inside that folder create another folder called __labs__.
4. Inside that __labs__ folder create one last folder called __setup__. It is in here where we will create our first Python file.

## Running Your First Python File

Finally, we are going to want to make sure that we can execute Python code. 

1. Inside our __setup__ folder, create a file called `hello.py`. The `.py` file extension is very important as it lets the python interpreter and vscode editor know the file is Python source code. Copy and paste the code below into the file and ___be sure to save the file afterwards!___

    ```py
    def main():
        print("Hello, world!")

    if __name__ == '__main__':
        main()
    ```

2. Next, we are going to want to run the python file either using the command line or __Code Runner__ extension. 
    - To run it using the command prompt, run the following command:
        ```sh
        python3 path/to/cmpt-120/labs/setup/hello_world.py
        ```
    - To run it using code runner, simply press the __Run Code__ button (it is a triangle shaped button towards the top of vscode).

If you set up everything correctly, you should see the following code printed out to the command line:

```
Hello, world!
```

Take a screenshot of the output and submit it on Brightspace.
