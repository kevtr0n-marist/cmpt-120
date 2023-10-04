# Lab 5 - DevOps

As you have probably heard me say multiple times in class, there is more to programming than just simply writing code. One of those things is learning how to use a __version control system__ (or simply __VCS__). 

> __Version control system__: In software engineering, version control is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. Version control is a component of software configuration management
>
> -[Wikipedia](https://en.wikipedia.org/wiki/Version_control)

We will be storing our code in this class in the __cloud__. Cloud-based is the standard nowadays for hosting repositories. The __cloud-based hosting service__ we will be used is called [__GitHub__](https://github.com). GitHub is a platform and cloud-based service for software development and version control using the [__Git__](https://git-scm.com) version control system, allowing developers to store and manage their code. Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 

## Setup

### Git Installation

Install the latest version of Git at https://git-scm.com. The reference manual can be found [here](https://git-scm.com/docs). Bookmark this very handy [cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)! You will need to learn how to use this version control tool.

### GitHub Registration

Please visit https://github.com and sign up for an account. If signing up for a student account, you may need to setup multifactor authentication. I created my account a long time ago so it may actually be required for all account types now. The multifactor-authentication may be SMS based or via an authenticator app.

### GitHub CLI

Now in order to connect our __Git__ VCS to our __GitHub__ account we will need to make use of the GitHub CLI (Command-Line Interface). Please visit https://cli.github.com and install the latest version. 

#### For Windows Users

For Windows users, visit https://github.com/cli/cli/releases/tag/v2.36.0 and download the appropriate Windows installer and run it.

To ensure it is installed, you can run the following command from the command prompt:

```sh
gh --version
```

#### For Mac Users

For Mac users, you can install GitHub CLI via __brew__ by running the following command:

```sh
brew install gh
```

If you do not have brew installed, you can install it by copying the command below and running it in the command line:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

It may prompt you to enter some commands in, if you need help with this let me know and I can help.

To ensure it is installed, you can run the following command from the terminal:

```sh
gh --version
```

### GitHub CLI Authentication

Next, we need to sign into our GitHub account using the GitHub CLI. Close and then reopen your command line application.

First `cd` into your `cmpt-120` folder. 

Next, authenticate yourself by running the following command:

```sh
gh auth login
```

When it asks you which account you want to log into select the __GitHub.com__ option. 

When it asks you what your preferred protocol for Git operations, select the __HTTPS__ option. 

When it asks how you would like to authenticate, select the __Login with a web browser__ option. 

Finally, copy the code, press the enter key, and input the code in the browser and _voila_! You are now authenticated and ready to use Git/GitHub!

### Creating Your First Repository

To create a new repository, visit https://github.com/new. 

For the field marked __Repository name__, please enter in `cmpt-120`. Add a description if you would like and be sure to select the __Private__ option. Ignore the rest of the options and press the green __Create repository__ button at the bottom.

Open up your command line and `cd` into your `cmpt-120` folder. Please run the following commands:

```sh
# Initializes a folder as a git repository.
git init

# Creates a .gitignore file which excludes any files in it from commits.
echo "__pycache__" >> .gitignore
echo ".pytest_cache" >> .gitignore

# Stages all files in your repository in your next commit.
git add .

# Commits your staged content as a new commit snapshot.
git commit -m "initial commit"

# Names your primary branch "main".
git branch -M main

# Connects the cmpt-120 folder on your computer with the remote repository.
git remote add origin https://github.com/USERNAME/cmpt-120.git 
# Replace USERNAME with your actual github username above.

# Transmits local branch commits to the remote repository branch.
git push -u origin main
```

Do not worry if you do not understand what is happening above. I will explain it in depth in lab.

If you did everything above correctly you should be able to see your code in https://github.com/USERNAME/cmpt-120 (be sure to replace USERNAME with your actual username).

### Updating your GitHub Repository

Next, lets push our first updates to our remote GitHub repository. If you update your code on your computer, that doesn't automatically update it in the cloud. In order to do that lets