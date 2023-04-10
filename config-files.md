# Configuration Files

This lesson introduces configuration files ("config files") through `.json` and 
`.yml` (also `.yaml`) file types.  

## Prerequisites

* A text editor.  We recommend Microsoft's [Visual Studio Code](https://code.visualstudio.com/) (aka "VS Code") because the following functionality is helpful:
  * Syntax highlighting
  * Error highlighting ("linting")
  * A command line editor
* Python 3.x.  Python 3.8 or higher compulsory, and Python 3.11, now available, is recommended.
  * Select the [installer](https://www.python.org/downloads/) that matches your local operating system, e.g., macos, Linux, or Windows.
  * After installation, from the command line, issue `$ python --version` and note the version you have installed.
* Local tools, see [tooling](tooling.md).
* A virtual environment, see [vitual-environment](virtual-environments.md).

## Introduction

Both `.json` and `.yml` are text files and encode a `key` $\mapsto$ `value` structure.

Advantages of a text file in general are

1. It is human-readable (e.g., not binary).
2. A proprietary application is not required to create/read/update/delete ("CRUD") the file.
3. Any application (e.g., Python, MATLAB, etc.) can operate (consume data from) the file.

The added advantages of `.json` and `.yml` are the structure that can be endowed in the file.
The structure is flat (or nested) key-value pairs.

## Examples with `.json`

*The `.json` examples are now largely historical, as now we prefer `.yml` to `.json`.*

* https://github.com/sandialabs/sibl/tree/master/geo/data/bezier
* https://github.com/sandialabs/sibl/tree/master/geo/data/bspline

## Examples with `.yml`

* https://github.com/autotwin/pixel/tree/main/tests/files
* https://github.com/autotwin/mesh/blob/main/tests/files/sphere.yml

## Exercise 1

Use a text editor to recreate the following `.yml` file:

```yml
# From the example of a mesh composed of two quadrilateral elements
# https://github.com/sandialabs/sibl/blob/master/geo/tests/test_mesh.py#L71
#
#      y
#      ^
#      |
#      4        105        6
#      *---------*---------*
#      |         |         |
#      |   (1)   |  (20)   |
#      |         |         |
#      *---------*---------*  --> x
#     101        2       103
#
version: 1.0
nodes:
  101: (0.0, 0.0),
  2: (1.0, 0.0),
  103: (2.0, 0.0),
  4: (0.0, 1.0),
  105: (1.0, 1.0),
  6: (2.0, 1.0),
elements:
  1: (101, 2, 105, 4),
  20: (2, 103, 6, 105),
```

The most up-to-date version of this file is found [here](files/two_quads.yml).

Read in the file and an echo the data to the command line:

```bash
$ python quad_reader.py

```

## Additional Reading

* [In Pursuit of Reproducibility: Declarative and Automated Post-Processing](present/2023-03-08-003-declarative-reproducible-figures-SAND2023-01369PE.pdf)
* [Quadrilateral Quality](present/quad_quality-2023-07-28.pdf) (Source `.tex` file at https://github.com/sandialabs/sibl/tree/master/geo/doc/mesh)
