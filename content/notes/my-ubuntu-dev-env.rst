Ubuntu Development Environment
==============================

The following is a personal notes for Setting up ubuntu for my dev machine.

Terminal Shortcut:

* CTRL+SHIFT+UP/DOWN
* SHIFT+PAGE UP/DOWN

Note: Execute with `sudo` command when needed

.. code-block:: bash

    # Update apt repository
    apt update
    apt upgrade
    apt dist-upgrade

    # text editor
    apt install vim

    # terminal workspace
    apt install yakuake

    # utilities
    apt install curl

    # revision control
    apt install git mercurial subversion

    # Append to ~/.bashrc
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

    # Python VirtualEnvironment 
    # http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Workspace
    export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
    source /usr/local/bin/virtualenvwrapper_lazy.sh

    # SSH & Git see: 
    # http://blog.eugene-yeo.in/setup-fedora-as-development-environment.html

    # NodeJS
    apt install nodejs npm nodejs-legacy
    npm config set prefix ~/.npm

    # Append to ~/.bashrc
    export PATH=$HOME/.npm/bin:$PATH 

    # Ruby Version Manager
    curl -L https://get.rvm.io | bash -s stable
    export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
    source $HOME/.rvm/scripts/rvm
    rvm autolibs packages
    rvm install ruby
    rvm use --default ruby
    gem install rails

    # https://help.ubuntu.com/community/PostgreSQL#Basic_Server_Setup
    sudo apt install postgresql postgresql-client postgresql-contrib pgadmin3

    # set root password
    sudo -u postgres psql postgres
    > \password postgres
    sudo -u postgres createdb mydb

    # alternative: set user as superuser
    sudo -u postgres createuser --superuser $USER
    sudo -u $USER psql
    > \password $USER
    sudo -u postgres createdb $USER

    

