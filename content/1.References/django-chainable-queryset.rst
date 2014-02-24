Django Chainable QuerySet
=========================

:tags: django
:date: 2014-02-25 03:00:00

In Django, you can create a long chain of query something like this.

.. code-block:: python

    Fruit.objects.seedless().sour().color("green")

First we have to define the :code:`seedless`, :code:`sour` and :code:`color`
queryset methods in our :code:`objects` manager class and its QuerySet class.

In Django 1.6 below, 
Because the manager class will have the same methods as its queryset class,
you could make use of :code:`__getattr__` method.

.. code-block:: python

    from django.db import models

    class FruitQuerySet(models.query.QuerySet):
        def seedless(self):
            return self.filter(seed_count=0)
        def sour(self):
            return self.filter(sour_index__gte=10)
        def color(self, col):
            return self.filter(color=col)

    class FruitManager(models.Manager):
        def get_queryset(self):
            return FruitQuerySet(self.model)
        def __getattr__(self, attr, *args):
            try:
                return getattr(self.__class__, attr, *args)
            except AttributeError:
                return getattr(self.get_queryset(), attr, *args)

    class Fruit(models.Model):
        # some fields
        # ...

        # manager
        objects = FruitManager()

In Django 1.7 and above,
Django create a helper methods :code:`QuerySet.as_manager()` to make your QuerySet class into a Manager,
because most of the time query methods from the QuerySet class more or less 
the same as the one in the Manager class.

.. code-block:: python

    from django.db import models

    class FruitQuerySet(models.query.QuerySet):
        def seedless(self):
            return self.filter(seed_count=0)
        def sour(self):
            return self.filter(sour_index__gte=10)
        def color(self, col):
            return self.filter(color=col)

    class Fruit(models.Model):
        # some fields
        # ...

        # manager
        objects = FruitQuerySet.as_manager()
