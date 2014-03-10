Restore Deleted File in Git
===========================

:date: 2014-03-10 20:40:00
:tags: git

.. code-block:: bash

    # Find the commit that you want to revert to. 
    # This commit is when the file exists. (usually the latest)
    git rev-list -n 1 HEAD -- file/you/want/to/restore

    # Checkout the file of that commit
    git checkout c0mm1t^ -- file/you/want/to/restore

    # add and commit back.
    git commit -a

