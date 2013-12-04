Setting up Django Server on EC2 Amazon AMI
##########################################

:tags: django, amazon, fedora, setup
:date: 2012-10-22 11:02:00

Install some extra kernel stuff which may be required.

.. code-block:: bash

    yum install kernel-headers kernel-devel gcc


Install Yakuake

.. code-block:: bash

    sudo yum install yakuake

Autostart Yakuake

.. code-block:: bash

    sudo cp /usr/share/applications/kde4/yakuake.desktop /etc/xdg/autostart/

Install VIM, SCM

.. code-block:: bash

    sudo yum install git hg svn
    sudo yum install vim

Install Python PIP (Package manager)

.. code-block:: bash

    sudo yum install python-pip

Install VirtualEnv

.. code-block:: bash

    sudo pip-python install virtualenvwrapper
    mkdir ~/.virtualenvs

Copy into ~/.bashrc file

.. code-block:: bash

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Workspace
    source /usr/local/bin/virtualenvwrapper.sh

`Install Eclipse <http://www.if-not-true-then-false.com/2010/linux-install-eclipse-on-fedora-centos-red-hat-rhel/>`_

.. code-block:: bash

    mkdir ~/.ssh
    cp aws-server.pem ~/.ssh

Create script to ssh production & staging server on your home directory

.. code-block:: bash

    ssh -t -i ~/.ssh/aws-server.pem ec2-user@ip-address screen -R YourName

Create and Copy the Key into Github Account

.. code-block:: bash

    ssh-keygen
    cat ~/.ssh/id_rsa.pub

Clone project

.. code-block:: bash

    git clone git@github.com:Account/project.git

Setup GitConfig File
`Alias <http://www.eugene-yeo.me/2012/09/9/my-favorite-git-alias-2012/>`_

.. code-block:: bash

    [user]
        name = YourName
        email = email@email.com

Make Virtual Environment

.. code-block:: bash

    mkvirtualenv project --distribute
    workon project

Setup Project

.. code-block:: bash

    sudo yum install mysql mysql-server mysql-devel python python-devel

Install Requirement

.. code-block:: bash

    pip install -r requirements.txt


`Install NodeJS <http://nodejs.tchol.org/>`_

This is to allow Sudo user to run execute node.

.. code-block:: bash

    sudo ln -s /usr/local/bin/node /usr/bin/node
    sudo ln -s /usr/local/lib/node /usr/lib/node
    sudo ln -s /usr/local/bin/npm /usr/bin/npm
    sudo ln -s /usr/local/bin/node-waf /usr/bin/node-waf


If you need PIL library:

.. code-block:: bash

    sudo yum install python-imaging

Extras:

.. code-block:: bash

    sudo rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm

I hope I didn't miss any step. If I do I'll update this post.
