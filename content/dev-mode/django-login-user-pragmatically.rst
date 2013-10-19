###############################
Django Login User Pragmatically
###############################

:date: 2013-03-15 16:37:33
:tags: login, django

Before you login user, this user has to be authenticated. It doesn't make sense if you allow someone to login without him authenticating (either by keying his password or something else) 

Usually, the right timing to know his password before being encrypted to database is when a user submit POST request whereby the password is still in plain text. This is the right time for you to authenticate the user. If plain text successfully authenticated, then you can login the user. or else it will fail.

Authentication user is straight forwards, just pass in the username and password. But if you have the email instead. You need to query the database for the username. If you don't have the password or the password is encrypted in the database, then you're a bit out of luck, because you will not be doing it the easy way in which you need to patch the user.backend.

Otherwise, Here's how you login the username and password the easy way.

.. code-block:: python

    from django.contrib.auth import authenticate, login

    user = authenticate(username=username, password=password)
    login(request, user)
    # Redirect the user or use ajax or whatever to refresh the page.

