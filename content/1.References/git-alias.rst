Git Alias
=========

:date: 2014-03-10 23:35:00
:tags: git

.. code-block:: bash

    # File: ~/.gitconfig

    [alias]
        co = checkout
        ci = commit
        st = status
        br = branch
        lg = log --graph --pretty=format:'%Cred%h%Creset %ad %s %C(yellow)%d%Creset %C(bold blue)<%an>%Creset' --date=short
        hist = log --graph --full-history --all --pretty=format:'%Cred%h%Creset %ad %s %C(yellow)%d%Creset %C(bold blue)<%an>%Creset' --date=short
        pick = cherry-pick
