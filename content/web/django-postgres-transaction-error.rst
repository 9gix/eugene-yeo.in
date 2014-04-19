Django Postgres Transaction Error Rollback
==========================================

:date: 2014-03-10 19:00:00
:tags: error, django, db

Every time there's an error in Django if using postgres, the connection somehow wasn't terminate properly. I have to manually rollback in my Django Shell. and rerun again

.. code-block:: python

    from django.db import connection
    connection._rollback()

Update: This bug has just been fixed in the latest release. `Ticket10813`_

.. _Ticket10813: https://code.djangoproject.com/ticket/10813
