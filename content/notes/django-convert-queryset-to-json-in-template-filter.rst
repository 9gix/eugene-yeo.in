Convert queryset into JSON from a template filter
=================================================

Before using my django template filters, you may want to consider using `JSONify`_ template filter snippets. The link is a simple template filter to encode a variable to JSON format. If the solution doesn't fit your requirement, you may then look at this.

Instead of serializing the queryset, you could jsondump a ``list()`` of ``queryset.values('fields')``.

.. code-block:: python

    from django.template import Library
    from django.utils import simplejson

    register = Library()

    @register.filter
    def jsonify_queryset(object,fields):
        return simplejson.dumps(list(object.values(*fields.split(','))))


    # Usage:
    # {{ book.objects.all | jsonify_queryset:"id,title" }}

.. _JSONify: http://djangosnippets.org/snippets/201/
