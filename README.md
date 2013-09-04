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

1. **(Root user action)** Install python/pip/MySQL dependencies: `sudo apt-get install python-pip python-dev mysql-client libmysqlclient-dev`
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
4. Also while in the top directory in the project, run the following to add the directory to your
virtualenv's python path: `add2virtualenv $PWD`

In the future, you should run the `workon www_pg_org` command whenever you work on and run this code.

### Set up MySQL ###

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

### Running locally ###

You can run the site now by navigating to the top directory of the project and running
`python manage.py runserver`. You can then load the site by opening a web browser and
navigating to `http://localhost:8000`.

### Apache server with WSGI ###

You can use WSGI to run the site with an Apache server with the following steps:

1. **(Root user action)** Install Apache's WSGI mod with `sudo apt-get install libapache2-mod-wsgi`
2. **(Root user action)** Enable it with `sudo a2enmod wsgi`
3. **(Root user action)** Edit Apache's httpd.conf (`/etc/apache2/httpd.conf`) to contain lines
like the following:

```
WSGIScriptAlias / /path/to/project/www_personalgenomes_org/www_personalgenomes_org/wsgi.py
WSGIPythonPath /path/to/project/www_personalgenomes_org:/path/to/homedir/.virtualenvs/www_pg_org/lib/python2.7/site-packages
```
4. **(Root user action)** Edit Apache's default in sites-available (`/etc/apache2/sites-available/default`)
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
