www_personalgenomes_org
=======================

This is the website for [www.personalgenomes.org](http://www.personalgenomes.org), implemented using Django. So far no database features have been used, although there's a good chance we'll use such features in the future.

Installation
------------
These instructions were written for Ubuntu Linux (since that's what I use). If you use
another system, please go ahead and submit modifications to this file to describe alternate
instructions. Thanks!

### Clone the Git repository ###

* Navigate to the directory you want to have the code in, and clone the repository with:
* `git clone git@github.com:PersonalGenomeProject/www_personalgenomes_org`

### Set up standard python/django development tools ###

If you've already done work on Django or other Python packages, it's likely you already have pip
and virtualenv set up (and can skip these instructions).

If you aren't familiar with pip and virtualenv: these are standard aspects of Python development,
greatly facilitating package management. Whenever working on this software you should do so within
the virtual environment.

1. **(Root user action)** Install pip: `sudo apt-get install python-pip` 
2. **(Root user action)** Use pip to install virtualenv and virtualenvwrapper: `sudo pip install virtualenv virtualenvwrapper`
3. Make a directory to store your virtual environments: `mkdir ~/.virtualenvs`
4. To make virtualenv and virtualenvwrapper commands work in future terminals, add the 
following to your bashrc (or zshrc, as appropriate): 
`export WORKON_HOME=$HOME/.virtualenvs` and
`source /usr/local/bin/virtualenvwrapper.sh`.

### Set up virtualenv for www_personalgenomes_org ###

If you open a new terminal you should now be able to access the virtualenvwrapper commands listed below.

1. Create a new virtual environment for working on this code: `mkvirtualenv www_pg_org`
2. Start using this virtual environment: `workon www_pg_org`
3. Navigate to top directory in this project. Install the Python packages required for development with 
`pip install -r requirements.txt`

In the future, you should run the `workon www_pg_org` command whenever you work on and run this code.
