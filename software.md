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
There is a newish feature for Windows 10 that allows you to run Ubuntu apps natively inside of Windows.  You can get it from the Microsoft Store for free here:
* [Installation instructions for Ubuntu under Windows 10](https://www.microsoft.com/en-us/store/p/ubuntu/9nblggh4msv6)<br>
Students from previous years and related courses (CSE 583 & DATA 515) have used this and it works great for `git` and other `bash` stuff. This is a viable option for Windows users but not as well tested at the `gitbash` tools described below.  Having said that, it is strongly recommended to try this option before `gitbash` below as that tool chain is on a deprecation roadmap.

### Alternate tools for Windows
Windows users should install the Software Carpentry recommended software:
Please follow these instructions on YouTube: [https://www.youtube.com/watch?v=339AEqk9c-8](https://www.youtube.com/watch?v=339AEqk9c-8).
Make sure you install gitbash _and_ the text editor (SWCarpentryInstaller).
Links to the installers for Windows:
* GitBASH: [https://git-for-windows.github.io](https://git-for-windows.github.io)
* Software Carpentry Installer: [https://github.com/swcarpentry/windows-installer/releases/](https://github.com/swcarpentry/windows-installer/releases/)

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

## Instructions for Running a Text Editor from Git Bash on Windows 10

These notes were contributed by a student in 2017:

***
These instructions assume that you already have already downloaded and installed Git Bash and Sublime for Windows 10. I have not attempted this with other text editors, but I hazard to guess the instructions are similar. These instructions are culled from Stack Overflow and Here.

In order to execute your text editor from Git Bash (not the default bash on Windows), open up Notepad and create the following file named Subl:
#!/bin/sh
"C:\Program Files\Sublime Text 3\sublime_text.exe" $1 &
In the above block of code, the line between “…” is the path where your text editor executable is installed. Save Subl wherever you want. I recommend to your desktop, so it is easy to find. Notice that Subl is likely saved as a text (Subl.txt) file. We want to get rid of the extension. However, the Windows gui doesn’t allow us to access the file extensions, so we have to do the following steps.

Next, run the Window’s command terminal (cmd) as an administrator. Navigate to where you saved Subl.txt (i.e. C:\Users\Andrew\Desktop). We want to get rid of that .txt extension. Use the copy command as follows:
C:\Users\…\Desktop>copy Subl.txt Subl
Now we have Subl with no extension. We now want to move it into our Git Bash bin directory, so that when we type Subl new_text_file.txt in Git Bash, it opens up new_text_file.txt using Sublime or your particular text editor. 

First, find the path of where your Git Bash bin directory is. The path is likely C:\Program Files\Git\usr\bin or “C:\Program Files (x86)\Git\bin” depending on if you did the 64 or 32-bit installation. Still in the Windows command terminal (running as an administrator), type the following: 
C:\Users\...\Desktop>move Subl “C:\Program Files\Git\usr\bin”
If you want, you can combine the above step with the previous step. This has now moved the script Subl to the specified bin directory. Now, in Git Bash you should be able to simply type Subl new_text_file.txt and it will create (if it doesn’t yet exist) or open up new_text_file.txt using Sublime. 

I have not tested this for any other text editor (i.e. nano/vim/atom/etc), but I imagine a similar script in similar directories should have similar results. 
***

