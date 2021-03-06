www_personalgenomes_org
=======================

This is the website for [www.personalgenomes.org](http://www.personalgenomes.org), implemented using Django. This enables our site to use IP address to display defaualt content based on the country a viewer is in, and to allow Austrian users to view a German version of their site. So far no database features have been used, although there's a chance we'll use such features in the future.

Submitting updates to the site
------------------------------
Personal Genome Project sites (e.g. Harvard, Canada, UK) each have a subsite within www_personalgenomes_org in the form of an app directory. This gives you a lot of flexibility to add features and content relevant to your PGP site.

By default we are giving developers "read only" access to the PersonalGenomesOrg repository. You can submit changes to the site in the form of pull requests.

To do this, you should:

1. [Fork the repository](https://help.github.com/articles/fork-a-repo) to create a copy in your own GitHub account.
2. Clone the repository to your local machine from the version in your Github account: `git clone git@github.com:YourUsername/www_personalgenomes_org`
3. Add the PersonalGenomesOrg as an "upstream" repository [as described here](https://help.github.com/articles/fork-a-repo).
4. Edit the site on the local machine and commit changes.
5. (Necessary before doing step 7.) Pull upstream changes from the PersonalGenomesOrg repository (and have these in your Github repository) before sending a pull request.
6. Push changes to your Github repository.
7. [Send a "pull request"](https://help.github.com/articles/creating-a-pull-request) to the PersonalGenomesOrg repository on Github.
8. Email madeleine@personalgenomes.org to notify Madeleine of the requested update.

Installation
------------
So far these instructions have been used for Ubuntu Linux 12.10 and OSX Mountain Lion. If you use
another system, please go ahead and submit modifications to this file to describe alternate
instructions. Thanks!

If you aren't familiar with pip and virtualenv: these are standard aspects of Python development,
greatly facilitating package management. Whenever working on this software you should do so within
the virtual environment.

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
7. run `brew install geoip postgresql` to install the GeoIP library and PostgreSQL if needed.
8. run `brew install python --with-brewed-openssl` to install Python from Homebrew.
9. run `pip install virtualenv virtualenvwrapper` to install virtualenv using pip, our Python package manager of choice.
10. Make a directory to store your virtual environments: `mkdir ~/.virtualenvs`
11. To make virtualenv and virtualenvwrapper commands work in future terminals, add the following
to your `~/.bashrc` (or create a `.bashrc` file in your home directory if one doesn't exist):
`export WORKON_HOME=$HOME/.virtualenvs` and
`source /usr/local/bin/virtualenvwrapper.sh`.

#### Linux ####

1. **(Root user action)** Install python/pip dependencies: `sudo apt-get install python-pip python-dev`
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

### Running locally (works immediately!) ###

You can run the site now by navigating to the top directory of the project and running
`python manage.py runserver --insecure`. You can then load the site by opening a web browser and
navigating to `http://localhost:8000`.

Because the development settings (which are default) use SQLite, no additional installation of
database software should be needed for local development. (SQLite is included in Python.)

### Running on AWS Elastic Beanstalk ###

[fill in later]
