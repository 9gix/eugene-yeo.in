Python Simple Thread
####################

:date: 2012-09-19 19:23:00
:tags: python

.. code-block:: python

    def do(arg1, arg2):
        print "Working"

        from threading import Thread
        Thread(target=do, args=("Starting Thread", "1")).start()
        Thread(target=do, args=("Nuke", "2")).start()
        Thread(target=do, args=("Ended", "3")).start()

