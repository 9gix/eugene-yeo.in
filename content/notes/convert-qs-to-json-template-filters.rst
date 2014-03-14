Convert queryset into JSON with template filters
################################################

:tags: django
:date: 2012-09-09 14:47:00

Before using my django template filters, you may want to consider using `JSONify template filter snippets <http://djangosnippets.org/snippets/201/>`_ "JSONify"). The link is a simple template filter to encode a variable to JSON format. If the solution doesn't fit your requirement, you may then look at this. 

Instead of serializing the queryset, you could ``jsondump`` a ``list()`` of ``queryset.values('fields')``.

.. code-block:: python

    from django.template import Library
    from django.utils import simplejson

    register = Library()
    @register.filter
    def jsonify_queryset(object,fields):
        return simplejson.dumps(list(object.values(*fields.split(','))))

Such that you could do the following in your template.html

.. code-block:: python

    {{ book.objects.all | jsonify_queryset:"id,title" }}
