#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Leonardo Giordani'
SITENAME = 'The Babel Cat'
SITESUBTITLE = 'Avventure di un povero gatto in un mondo multilingue'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'it'
LOCALE = "it_IT.utf8"

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

DEFAULT_PAGINATION = 10

THEME = "../webmag"

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ['related_posts', 'assets']

STATIC_PATHS = [
    'images'
]


def index_category(categories, category):
    category_names = [c[0].name for c in categories]

    # Index in loops starts from 1 - Argh!
    return category_names.index(category) + 1


def articles_category(categories, category):
    d = dict((cat.name, len(articles)) for cat, articles in categories)
    return d[category]


JINJA_FILTERS = {
    'index_category': index_category,
    'articles_category': articles_category
}
