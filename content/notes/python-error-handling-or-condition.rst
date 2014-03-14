Condition (LYBF) or Error Handling (EAFP)
=========================================

:date: 2014-03-10 18:10
:tags: python

The following are two different style of handling an case.

* ``if-else`` condition,
  (LBYL ~ Look before you leap)
* ``try-catch`` error handling. 
  (EAFP ~ It's easier to ask forgiveness than permission)

.. code-block:: python

    def x():
        return []

    # Condition
    def call_with_condition():
        if x:
            return x[0]
        else:
            return None
            
    # Try Catch
    def call_with_err_handling():
        try:
            return x[0]
        except IndexError:
            return None

Which of the above would you choose?

Taken from `Python EAFP-vs-LBYL`_, In general EAFP is preferred but not always. 

Both of the example above looks fine. But how if we expand the example above
to have a more complicated & nested cases,
which will be more readable & reliable after much iteration?

... To be continue
    

.. _Python EAFP-vs-LBYL: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#eafp-vs-lbyl
