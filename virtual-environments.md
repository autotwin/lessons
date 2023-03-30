# Virtual Environments

Objective: Create a virtual environment for use with the lessons contained herein.

## Steps

* Locate the version of Python you wish to use to create the virtual environment; as there may be more than one Python installations on your local machine.  For example, I will use `/usr/local/bin/python3.11`
* Create the virtual environment

```bash
/Users/chovey/autotwin/lessons> $ /usr/local/bin/python3.11 -m venv .venv
# this is a call to the specific Python version, a flag to 'make' with the package 'venv' a
# virtual environment named '.venv'.
```

* Note: hereinafter, we dispense with the command line prompt indicator `/Users/chovey/autotwin/lessons> $`
* Active the newly created virutal environment (hereinafter, we dispense with the command line prompt

```bash
# activate the venv with one of the following, depending on which shell is in use
source .venv/bin/activate # for bash shell
source .venv/bin/activate.csh # for c shell
source .venv/bin/activate.fish # for fish shell
source .venv/bin/Activate.fish # for powershell
```

* Verify the Python version

```bash
python --version
Python 3.11.2
```

* Update `pip` and `setuptools` if a newer version is available:

```bash
pip list
Package    Version
---------- -------
pip        22.3.1
setuptools 65.5.0

[notice] A new release of pip available: 22.3.1 -> 23.0.1
[notice] To update, run: pip install --upgrade pip

pip install --upgrade pip setuptools

pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 67.6.1
```

* Let's include the PyYAML package, a YAML parser and emitter for Python.  See https://pypi.org/project/PyYAML/ for more details.

```bash
pip install PyYAML

# verify the version of PyYAML that was installed
pip list
Package    Version
---------- -------
pip        23.0.1
PyYAML     6.0
setuptools 67.6.1
```

Congratulations!  You have created and used a virtual environemnt named `.venv`, the customary name given to a local Python virtual environment.  This concludes this lesson.
