#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Eugene'
SITENAME = u"Eugene's Note"
SITEURL = 'http://eugene-yeo.in'

TIMEZONE = 'Asia/Singapore'
DEFAULT_DATE = 'fs'

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

PROJECT_DIR = os.path.dirname(__file__)
THEME = os.path.join(PROJECT_DIR, 'themes/clean')

GOOGLE_ANALYTICS = "UA-48871995-1"
