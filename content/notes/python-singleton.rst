Singleton in Python
===================

:date: 2014-03-10 23:25:00
:tags: python, design-pattern

.. code-block:: python
    
    # Borg Pattern
    class Earth:
        __dict = {}
        def __init__(self):
            self.__dict__ = self.__dict

    e1 = Earth()
    e2 = Earth()
    e1.population = 30000000
    print e2.population



    # or with Singleton decorator

    def singleton(cls):
        instances = {}
        def getinstance():
            if cls not in instances:
                instances[cls] = cls()
            return instances[cls]
        return getinstance

    @singleton
    class Earth:
        pass

    e1 = Earth()
    e2 = Earth()
    e1.population = 30000000
    print e2.population
