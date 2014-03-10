Python List insert is slow
==========================

:date: 2014-03-10 23:45:00
:tags: python

.. code-block:: python
    
    nums = []
    for i in range(1000000):
        nums.append(i)
    nums.reverse()
    
    # Compare with 
    nums = []
    for i in range(200000):
        nums.insert(0,i)
        

When you do an insert, Python have to move all the elements after it. Appends didn't move all elements to its right immidiately, because they have a larger memory allocated. But when appends will move all the elements into a new memory allocation when its full. So using insert the memorry reallocation happen very often as it shift every insertion made, while append reallocate it when its full. That's the main difference. But there are some cases, if we're dealing with small amount of data, we may not feel the difference. So some cases I will still prefer insert over append, but mostly i would recommend use appends.


