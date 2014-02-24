#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eugene'
SITENAME = u'Reshaping the World Web Experience (WWE)'
SITEURL = 'http://eugene-yeo.in'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Eugene Legacy', 'http://eugene-yeo.me/'),)

# Social widget
SOCIAL = (('Facebook', 'http://www.facebook.com/yeo.eugene.oey'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGINS = ['pelican_youtube']

STATIC_PATHS = ['images',]

THEME = "/home/eugene/pelican-themes/elegant"
