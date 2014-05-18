#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

PROJECT_DIR = os.path.dirname(__file__)

AUTHOR = u'Eugene'
SITENAME = u"Eugene's Note"
SITEURL = 'http://blog.eugene-yeo.in'

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

PLUGIN_PATH = [
    os.path.join(PROJECT_DIR, 'plugins', 'pelican-plugins')
]
PLUGINS = [
    'pelican_youtube', 
    'assets',
    'sitemap',
]

STATIC_PATHS = ['images',]

PELICAN_THEME_DIR = os.path.join(PROJECT_DIR, 'themes', 'pelican-themes')
"""
# Compatible Pelican Themes
THEME = os.path.join(PELICAN_THEME_DIR, 'pelican-mockingbird')
THEME = os.path.join(PELICAN_THEME_DIR, 'dev-random')
THEME = os.path.join(PELICAN_THEME_DIR, 'chunk')
THEME = os.path.join(PELICAN_THEME_DIR, 'fresh')
THEME = os.path.join(PELICAN_THEME_DIR, 'elegant')
THEME = os.path.join(PELICAN_THEME_DIR, 'mnmlist')
THEME = os.path.join(PELICAN_THEME_DIR, 'monospace')
THEME = os.path.join(PELICAN_THEME_DIR, 'nmnlist')
"""
THEME = os.path.join(PELICAN_THEME_DIR, 'tuxlite_tbs')

GOOGLE_ANALYTICS = "UA-48871995-1"

ASSET_BUNDLES = (
    ('core', ['css/style.scss'], {'filters': 'scss', 'output': 'core.css'}),
)

PYGMENTS_RST_OPTIONS = {
    'linenos': 'table',
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.9,
        'pages': 0.6,
        'indexes': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'weekly',
        'indexes': 'daily'
    }
}
