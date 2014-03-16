Django get model class from string
==================================


.. code-block:: python

    from django.db.models.loading import get_model
    get_model(app_label, model_name)
