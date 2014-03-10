Python Split long text
======================

:date: 2014-03-10 23:30:00
:tags: python

In Python, there are a few ways of splitting a very long messages into small 
chunk. Here's one way that I like most because it does not store all 
the values in memory, but generate the values on the fly.

.. code-block:: python

    def splitter(text, amount):
        for i in range(0,len(text),amount):
            yield(text[i:i+amount])

    message = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nulla orci neque, Aliquam laoreet blandit nulla, 
    nec fermentum orci euismod vitae. 
    Vestibulum non nisi at leo rutrum imperdiet. """
    x = splitter(message,50)
    print x.next() # 1 - 50
    print x.next() # 51 - 100
