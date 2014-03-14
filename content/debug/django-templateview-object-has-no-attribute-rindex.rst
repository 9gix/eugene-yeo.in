Django 'TemplateView' object has no attribute 'rindex'
######################################################

:tags: django, error
:date: 2012-09-09 14:56:40

Are you trying to make a Class Based Generic View? This error happened because None was sent to the parameters.

There's a lot of possibilities that may cause this error, for my case, I didn't to call the method ``.as_view()`` after the TemplateView

For your case may be different, so check out the proper syntax in Django Documentation:
``TemplateView.as_view(template_name="somepage.html")``
