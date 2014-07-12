Ubuntu Development Environment
==============================

The following is a personal notes for Setting up ubuntu for my dev machine.

Terminal Shortcut:

* CTRL+SHIFT+UP/DOWN
* SHIFT+PAGE UP/DOWN

Terminology:

* `#` Comment
* `=#` Postgres console
* `>` Replace the specified file with the following lines
* `>>` Append to the specified file with the following lines

Note: 

#. Execute with `sudo` command when needed
#. `Fedora Setup`_

.. code-block:: bash

    # Update apt repository
    apt update
    apt upgrade
    apt dist-upgrade

    # text editor
    apt install vim

    # Vim Pathogen installation
    mkdir -p ~/.vim/autoload ~/.vim/bundle; \
    curl -LSso ~/.vim/autoload/pathogen.vim \
        https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim

    # >> ~/.bashrc
    execute pathogen#infect()
    syntax on
    filetype plugin indent on

    # Start Installing Vim Plugin inside the ~/.vim/bundle like this
    cd ~/.vim/bundle
    git clone git://github.com/tpope/vim-sensible.git

    # Ref: see my vimrc file below

    # terminal workspace
    apt install yakuake

    # utilities
    apt install curl

    # revision control
    apt install git mercurial subversion

    apt install python-pip
    pip install virtualenvwrapper

    # Python VirtualEnvironment
    # http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html
    # >> ~/.bashrc
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Workspace
    export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
    source /usr/local/bin/virtualenvwrapper_lazy.sh

    # SSH & Git see:
    # http://blog.eugene-yeo.in/setup-fedora-as-development-environment.html

    # NodeJS
    apt install nodejs nodejs-legacy
    curl https://www.npmjs.org/install.sh | sh
    npm config set prefix ~/.npm

    # >> ~/.bashrc
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
    =# \password postgres
    sudo -u postgres createdb mydb

    # alternative: set user as superuser
    sudo -u postgres createuser --superuser $USER
    sudo -u $USER createdb $USER
    sudo -u $USER psql
    =# \password <your-user-name>

    # Setup Java OpenJDK
    apt install openjdk-7-jdk

    # Setup Java Oracle JDK
    # https://www.digitalocean.com/community/articles/how-to-install-java-on-ubuntu-with-apt-get
    add-apt-repository ppa:webupd8team/java
    apt update
    apt install oracle-java8-installer

    # Java Environment
    # >> ~/.bashrc
    export PATH=$PATH:/usr/lib/jvm/java-<VERSION>-<VENDOR>/bin
    export JAVA_HOME=/usr/lib/jvm/java-<VERSION>-<VENDOR>

    # ElasticSearch Setup Guide
    # http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/setup-repositories.html
    # http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/setup-service.html

    # Bash Alias File: ~/.bash_aliases

Ref:

* `vimrc file`_

.. _Fedora Setup: /setup-fedora-as-development-environment.html
.. _vimrc file: /my-vimrc.html
