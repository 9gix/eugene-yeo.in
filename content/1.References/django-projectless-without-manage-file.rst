Django Projectless without manage.py
====================================

You don't actually need the manage.py.
If you look at the file, it is just a script to set your environment variable. 
You could actually set your environment variable manually by doing 
``export DJANGO_SETTINGS_MODULE=site.settings`` or If you already using 
virtualenvwrapper, then it would be a plus for you because you could 
set the environment variable automatically. Just add a hook 
on ``$VIRTUAL_ENV/bin/postactivate`` which contain some bash exports.

Example, here are my $VIRTUAL_ENV/dqbug/bin/postactivate script:

.. code-block:: bash

    export PYTHONPATH=/home/eugene/dqbug
    export DJANGO_SETTINGS_MODULE=dqbug.settings

In exchange to manage.py, you could use the django-admin.py. You could runserver, shell, etc..
