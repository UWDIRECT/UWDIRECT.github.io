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

Windows users should install the Software Carpentry recommended software:
Please follow these instructions on YouTube: [https://www.youtube.com/watch?v=339AEqk9c-8](https://www.youtube.com/watch?v=339AEqk9c-8).
Make sure you install gitbash _and_ the text editor (SWCarpentryInstaller).


## Python
We recommend that you use Python 3.5. Earlier versions of Python 3 work as well.
There are some differences between Python 2.7 (and earlier releases of Python 2)
and Python 3.
Details on installing Python can be found at https://www.python.org/downloads/.

## Conda & Python
Python will be the primary programming language used in the courses.  It is recommended
that Python 3.5 be used.  Even if you have an existing installation of Python, it is
required that you install Python with Conda.  Conda is a system for installing and 
otherwise managing python packages and their dependenices.
We recommend students use miniconda.
See [http://conda.pydata.org/miniconda.html](http://conda.pydata.org/miniconda.html)
for instructions for downloading and installing miniconda. 
(You should use the instructions for your OS and Python 3.5.)
Below are detailed instructions after you have installed miniconda:

1. Update conda's listing of packages for your system:
- $ conda update conda
2. Install IPython notebook and all its requirements
- $ conda install jupyter
3. Type ipython notebook in the terminal to start the notebook
- $ jupyter notebook

If everything has worked correctly, it should automatically launch your default browser

## Text editor
Windows users will install the basic ```nano``` editor.  After a few classes, you may
decide that you want to try out more advacned editors.  Some options are
 - [Sublime](http://sublimetext.com)
 - [atom](http://atom.io)

Note that word processors, e.g. Microsoft Word, is _not_ a text editor.  Real text
editors for software development have syntax highlighting, and even integrate with
version control and style checkers.
