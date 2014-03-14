Get Django model class from a string
####################################

:tags: django
:date: 2012-09-09 14:44:00

You could get a concrete model from a string provided that you know what model name (case insensitive) and the name of the apps.

.. code-block:: python

    from django.db.models.loading import get_model

    get_model(app_label, model_name)
