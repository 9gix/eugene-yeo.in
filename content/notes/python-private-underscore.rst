Python Private by Underscore?
=============================

:date: 2014-03-10 20:55:00
:tags: python

Based on PEP8, there is no private variable and methods in Python.
Most people claim that ``__this`` is actually private. Let's see:

.. code-block:: python

    class Car:
        petrol = 1
        _fuel = 10
        __gas = 20

    car = Car()
    print car.petrol     # Result: 1
    print car._fuel      # Result: 10
    print car._Car__gas  # Result: 20

In Python Nothing is really private. And there's no point of being private anyway.

Single leading Underscore Variable or methods in python convention is used 
for non public or only for internal use. But Of course you can call it 
directly from outside, It's just a convention.

And double underscore in python convention is used to avoid namespace conflict 
with its subclass. You can't call it directly, 
but to call it you have to use ``Class._Class__VarOrMethod``

So Summary: Nothing is Private in Python
