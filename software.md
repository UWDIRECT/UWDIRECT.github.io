---
layout: page
title: Software
collection: main
---

The courses make use of a number of software packages that students
will install on their computers.  The software needs to be installed
before you show up for day 1 of class.

The following software are available for Windows, Mac, and Linux.


## Bash shell and git version control software
Part of learning advanced software development and data science is
becoming fluent with the bash shell and version control (git).
The bash shell provides a scripting environment that
is often used to manipulate files, install programs, and
basic data analysis.
The git version control system (along with the github website)
are widely used for sharing codes and collaborative development
of software.
Bash and git are part of Linux and Mac OSX. No installs are required.

### Mac OSX note: Some students reported an error with ``git``:
```
xcode-select: note: no developer tools were found at '/Applications/Xcode.app', requesting install. Choose an option in the dialog to download the command line developer tools.
```
To fix this, do the following:

* Start a new Terminal
* Run the following command: ``xcode-select --install``
* Click ``Install``
* Click ``Agree`` to agree to the terms
For more information see this [link](http://mac-how-to.wonderhowto.com/how-to/install-command-line-developer-tools-without-xcode-0168115/)

## Note for Windows 10 users.
There is a newish feature for Windows 10 that allows you to run Ubuntu apps natively inside of Windows called Windows Subsystem for Linux (WSL).  You can get it from the Microsoft Store for free here:
* [Installation instructions for Ubuntu under Windows 10](https://www.microsoft.com/en-us/store/p/ubuntu/9nblggh4msv6)<br>
Students from previous years and related courses (CSE 583 & DATA 515) have used this and it works great for `git` and other `bash` stuff. 
<br>**In addition** we strongly recommend installing the improved Windows Terminal from the Microsoft App Store.  This is considerably better than the standard windows shell window and works great with WSL.

These instructions show how to setup a really solid Windows development environment including Python and WSL: [https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd](https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd)

## Conda & Python
Python will be the primary programming language used in the courses.  It is recommended
that Python 3.7 be used.  Even if you have an existing installation of Python, it is
required that you install Python with Conda.  Conda is a system for installing and 
otherwise managing python packages and their dependenices.
We recommend students use Miniconda3.7.  If you have an older conda 3.5 or later install that will probably work fine.  Versions of conda that are based on Python 2 will be very problematic if not useless for the class.
See [http://conda.pydata.org/miniconda.html](http://conda.pydata.org/miniconda.html)
for instructions for downloading and installing miniconda. 
(You should use the instructions for your OS and Python 3.7.)
Below are detailed instructions after you have installed miniconda to verify it is working as intended:

1. Update conda's listing of packages for your system:
- $ conda update conda
2. Install IPython notebook and all its requirements
- $ conda install jupyter
3. Type ipython notebook in the terminal to start the notebook
- $ jupyter notebook

If everything has worked correctly, it should automatically launch your default browser.

## Text editor
Windows users will install the basic ```nano``` editor.  After a few classes, you may
decide that you want to try out more advanced editors.  Some options are
 - [Sublime](http://sublimetext.com)
 - [atom](http://atom.io)

Note that word processors, e.g. Microsoft Word, is _not_ a text editor.  Real text
editors for software development have syntax highlighting, and even integrate with
version control and style checkers.

