# Tooling

* Text editor
  * VIM, neovim, bbedit, emacs
  * IDE: [vs code](https://code.visualstudio.com/)
    * Plugins - to come
* Debugger
  * pdb
  * vscode
* Package manager
  * *We have now deprecated the use of conda and anaconda.  We now prefer virtual environments.*
  * ~~conda, which is obtain with either~~
    * ~~[Miniconda](https://docs.conda.io/en/latest/miniconda.html) (preferred because it is minimalistic), or~~
    * ~~[Anaconda](https://docs.anaconda.com/)~~
  * venv - see [virtual-environments](virtual-environments.md)
* Source control
  * [Git](https://git-scm.com/)
    * [ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
    * 2FA
    * GitHub mobile as second factor
    * macOS only: May require installation of [Xcode command line tools](https://developer.apple.com/xcode/features/) prior to installation of Git.
  * [Git Desktop](https://desktop.github.com/)
* Code formatter
  * [Black](https://github.com/psf/black) and flake8

```bash
# after the local virtual environment is activated, install flake8 and black
# activate the venv with one of the following, depending on which shell is in use
source .venv/bin/activate # for bash shell
source .venv/bin/activate.csh # for c shell
source .venv/bin/activate.fish # for fish shell
source .venv/bin/Activate.fish # for powershell

pip install flake8
pip install black
```
