Email with Django
=================

:date: 2014-03-10 23:20:00
:tags: django

.. code-block:: python

    # File: settings.py

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'me@gmail.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_USE_TLS = True
    \# Optional
    DEFAULT_FROM_EMAIL = 'me@gmail.com'
    \# Temporarily show emails in the console during testing
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


    # To Send the Email, execute the following in separate file or console
    from django.core.mail import send_mail
    send_mail("subject", "message",'me@gmail.com', ['to@gmail.com'])

    # or
    from django.core.mail import EmailMessage
    email = EmailMessage("subject", "message", to=['to@gmail.com'])
    email.send()
