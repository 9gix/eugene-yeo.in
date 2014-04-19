###############################
Django Login User Pragmatically
###############################

:date: 2013-03-15 16:37:33
:tags: django

Before any user can login, one has to be authenticated.
Authentication usually required a password.

To get the user password in plaintext, you can intercept 
the request for the sign in or sign up form in the server
via the POST data attribute (e.g. ``request.POST['password']``)[*]_
By having this string of plaintext, you can then authenticate the user. 
Once authenticated, you can then login the user.

Authentication user is straight forwards, just pass in 
the username and password. But if you have the email instead, 
you need to query the database for the username or id.

.. code-block:: python

    from django.contrib.auth import authenticate, login

    user = authenticate(username=username, password=password)
    login(request, user)
    # Redirect the user or use ajax or whatever to refresh the page.

Unfortunately, If you don't have the password or 
the password is already hashed and stored in the database, 
then you're a bit out of luck, because you will not be do it the easy way.
But what you can do is to overwrite/patch your ``user.backend`` 
such that the login doesn't require password.

.. [*] You are not allowed to store the plain text password, you must hash it to protect your user confidential information and you should not know what their password either.

