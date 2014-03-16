Django Queryset multiple annotate
=================================

:date: 2014-03-10 23:15:00
:tags: django

.. code-block:: python

    # Wrong
    Publisher.objects.annotate(
            Count('book')
        ).filter(
            book__count__gt=100
        ).annotate(
            Count('author')
        ).filter(
            author__count__lt=5
        )

    # Correct
    Publisher.objects.annotate(
            Count('book', distinct=True)
        ).filter(
            book__count__gt=100
        ).annotate(
            Count('author', distinct=True)
        ).filter(
            author__count__lt=5
        )
