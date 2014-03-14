Conventions Checklist
#####################

:date: 2013-12-04 01:00:00
:tags: ethics

In starting up a new project, the team has to establish a code conventions,
this is to minimize the inconsistency of the code throughout the project.

Once a convention has been decided, changing it requires a lot of efforts. 
So do put some time to discuss and agree on the convention 
that the team has to follow.

It doesn't matter if you didn't follow the following convention,
as long as you have to agreed on the convention that your team has set.

The following is my preference Conventions:

Javascript Convention
---------------------

- **Indentation**
  is 4 spaces instead of tab.
  2 spaces is harder to see so stick with 4 spaces.

.. code-block:: js

    // DO NOT
    if (true){
      return true; // 2 spaces or tab
    }

    // DO
    if (true){
        return true; // 4 spaces
    }
  

- **Curly Brace**
  is enforced even though it is optional

.. code-block:: js

    // DO NOT
    if (true)
        return true;

    // DO
    if (true){
        return true;
    }

- **Opening Braces Location**
  does not start on new line

.. code-block:: javascript

    // DO NOT
    function()
    {
        return
        {
            1:"hello"
        };
    }

    // DO
    function x(){
        return {
            1:"hello"
        };
    }

- **semicolon**
  is enforced even though it is optional

.. code-block:: js
    
    // DO NOT
    var x = function(){
        return 1
    }

    // DO
    var x = function(){
        return 1;
    };


- **White Space**
  is after semicolon, after operator, after comma, after colon,
  after ``for``, etc...

.. code-block:: js
    
    var i = 0,
        j = i + 1;

    if (i && j){
        i = i / j
    }


- **Capitalize function**
  is for constructor

.. code-block:: js

    function Person(){}
    var eugene = new Person();

- **Multiple Word**
  ``camelCase`` is for function.
  ``under_score`` is for variable.

- **_underscore prefixed**
  ``_private()`` is for private method.

- **API Docs**
  for documentation of functions

.. code-block:: js
    
    /**
     * Do Something
     *
     * @param  {int} number value to be parse to string 
     * @return {string} the done result
     */
    var result = function(number){
       return "" + number;
    };






