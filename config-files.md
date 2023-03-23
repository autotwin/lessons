# Configuration Files

This lesson introduces configuration files ("config files") through `.json` and 
`.yml` (also `.yaml`) file types.  

## Prerequisites

* A text editor.  I recommend Microsoft's [Visual Studio Code](https://code.visualstudio.com/) (aka "VS Code") because the following functionality is helpful:
  * Syntax highlighting
  * Error highlighting ("linting")
  * A command line editor
* Python 3.x.  Python 3.8 or higher compulsory, and Python 3.11, now available, is recommended.
  * Select the [installer](https://www.python.org/downloads/) that matches your local operating system, e.g., macos, Linux, or Windows.
  * After installation, from the command line, issue `$ python --version` and note the version you have installed.

## Introduction

Both `.json` and `.yml` are text files and encode a `key` $\mapsto$ `value` structure.

Advantages of a text file in general are

1. It is human-readable (e.g., not binary).
2. A proprietary application is not required to create/read/update/delete ("CRUD") the file.
3. Any application (e.g., Python, MATLAB, etc.) can operate (consume data from) the file.

The added advantages of `.json` and `.yml` are the structure that can be endowed in the file.
The structure is flat (or nested) key-value pairs.

## Exercise 1

Using a text, editor, recreate the following file:

2023-02-23: CBH paused for today.  

