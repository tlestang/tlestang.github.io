#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thibault Lestang'
SITENAME = 'Thibault Lestang'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./themes/mytheme"

# Both "templates" and "static" directories contain
# .hmtl file(s) ("homepage.html" "oxcrn_animation.html",
# respectively). by default Pelican will consider them as
# articles, but actually don't want them to be processes as such.
ARTICLE_EXCLUDES = ['templates', 'static']
# "static/oxcrn_animation.html" should just be copied to the
# output/ dir.
STATIC_PATHS = ['images', 'static']
INDEX_SAVE_AS = "blog/index.html"
ARTICLE_PATHS = ["blog"]

