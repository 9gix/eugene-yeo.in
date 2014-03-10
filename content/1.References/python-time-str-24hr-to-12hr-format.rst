Python convert time 24hr to 12hr format in string
=================================================

:date: 2014-03-10 23:10:00
:tags: python

.. code-block:: python

    import time

    my_time = "23:30"
    my_new_time = time.strftime("%I:%M %p", time.strptime(my_time, "%H:%M"))
    print my_new_time # 11:30 pm
