www_personalgenomes_org
=======================

This is the website for [www.personalgenomes.org](http://www.personalgenomes.org), implemented using Django.
So far no database features have been used, although there's a good chance we'll use such features in the future.

Installation
------------
So far these instructions have been used for Ubuntu Linux 12.10 and OSX Mountain Lion. If you use
another system, please go ahead and submit modifications to this file to describe alternate
instructions. Thanks!

If you aren't familiar with pip and virtualenv: these are standard aspects of Python development,
greatly facilitating package management. Whenever working on this software you should do so within
the virtual environment.

### Clone the Git repository (OSX/Linux) ###

* Navigate to the directory you want to have the code in, and clone the repository with:
* `git clone git@github.com:PersonalGenomeProject/www_personalgenomes_org`

### Set up Python/Django developer tools ###

Skip if you already have these set up, of course.

#### OSX ###

You can use any plain text editing tool for editing various files (like .bashrc), [TextWrangler](http://www.barebones.com/products/textwrangler/) worked for us.

These instructions are adapted from [here](http://hackercodex.com/guide/mac-osx-mountain-lion-10.8-configuration/) and [here](http://hackercodex.com/guide/python-virtualenv-on-mac-osx-mountain-lion-10.8/).

1. To make sure compilers know what architecture your system is (64 bits), add the following to your `~/.bash_profile` (or create a `.bash_profile` in your home directory if it doesn't already exist).

```
# Set architecture flags
export ARCHFLAGS="-arch x86_64"
# Ensure user-installed binaries take precedence
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
# Load .bashrc if it exists
test -f ~/.bashrc && source ~/.bashrc
```

2. Close and open a new terminal (or tab) to have this configuration take effect.

3. Go to Apple's Developer Downloads area (Apple ID login will be required) and download the *Command Line Tools for Xcode* and install it.
4. Install Homebrew following the instructions on their site [http://brew.sh/](http://brew.sh/)
5. run `brew doctor` to check all is well.
6. run `brew update` to make sure it's up-to-date.
7. run `brew install python --with-brewed-openssl` to install Python from Homebrew.
8. run `brew install mysql` to install MySQL.
9. run `pip install virtualenv virtualenvwrapper` to install virtualenv using pip, our Python package manager of choice.
10. Make a directory to store your virtual environments: `mkdir ~/.virtualenvs`
11. To make virtualenv and virtualenvwrapper commands work in future terminals, add the following
to your `~/.bashrc` (or create a `.bashrc` file in your home directory if one doesn't exist):
`export WORKON_HOME=$HOME/.virtualenvs` and
`source /usr/local/bin/virtualenvwrapper.sh`.

#### Linux ####

1. **(Root user action)** Install python/pip/MySQL dependencies: `sudo apt-get install python-pip python-dev mysql-client libmysqlclient-dev`
2. **(Root user action)** Use pip to install virtualenv and virtualenvwrapper: `sudo pip install virtualenv virtualenvwrapper`
3. Make a directory to store your virtual environments: `mkdir ~/.virtualenvs`
4. To make virtualenv and virtualenvwrapper commands work in future terminals, add the 
following to your `~/.bashrc` (or zshrc, as appropriate): 
`export WORKON_HOME=$HOME/.virtualenvs` and
`source /usr/local/bin/virtualenvwrapper.sh`.

### Set up virtualenv for www_personalgenomes_org (OSX/Linux) ###

If you open a new terminal you should now be able to access the virtualenvwrapper commands listed below.

1. Create a new virtual environment for working on this code: `mkvirtualenv www_pg_org`
2. Start using this virtual environment: `workon www_pg_org`
3. Navigate to top directory in this project. Install the Python packages required for development with 
`pip install -r requirements.txt`
4. Also while in the top directory in the project, run the following to add the directory to your
virtualenv's python path: `add2virtualenv $PWD`

In the future, you should run the `workon www_pg_org` command whenever you work on and run this code.

### Set up MySQL (untested for Mac) ###

1. **(Root user action)** Install MySQL server: `sudo apt-get install mysql-server`
2. Log in to MySQL as root: `mysql -u root -p`
3. Within MySQL, create the new database: `CREATE DATABASE www_personalgenomes_org;`
4. Within MySQL, add the user to access the database:
`grant all privileges on www_personalgenomes_org.* to pgorg@localhost identified by 'glassworks';`
5. Edit `www_personalgenomes_org/settings.py` in the project tree: change the database password to the one you actually used in the previous step.
6. Navigate to the top directory in the project and initialize the database by running: `python manage.py syncdb`.
This will prompt you to create a superuser for Django's auth system, go ahead and do that too.

Running the site
----------------

### Running locally (works immediately!) ###

You can run the site now by navigating to the top directory of the project and running
`python manage.py runserver`. You can then load the site by opening a web browser and
navigating to `http://localhost:8000`.

### Apache server with WSGI ###

You can use WSGI to run the site with an Apache server with the following steps:

1. **(Root user action)** Install Apache's WSGI mod with `sudo apt-get install libapache2-mod-wsgi`
2. **(Root user action)** Enable it with `sudo a2enmod wsgi`
3. **(Root user action)** Edit Apache's default in sites-available (`/etc/apache2/sites-available/default`)
to contain lines like the following:

```
<VirtualHost *:80>

  <Directory /path/to/project/www_personalgenomes_org/www_personalgenomes_org>
    <Files wsgi.py>
      Order deny,allow 
      Allow from all
    </Files>
  </Directory>

  Alias /static/ /path/to/project/www_personalgenomes_org/static/

  WSGIDaemonProcess pgpsite python-path=/path/to/project/www_personalgenomes_org/path/to/homedir/.virtualenvs/www_pg_org/lib/python2.7/site-packages
  WSGIProcessGroup pgpsite
  WSGIScriptAlias / /path/to/project/www_personalgenomes_org-master/www_personalgenomes_org/wsgi.py/

  <Directory /path/to/project/www_personalgenomes_org/static>
    Order deny,allow
    Allow from all
  </Directory>
  
</VirtualHost>
```

**Notes:** 
* Check what your own path is for virtualenv's site-packages (step 3), you may have a different python version.
* Make sure permissions are set to give access to the files for the project.

### Running on AWS Elastic Beanstalk ###

[fill in later]
