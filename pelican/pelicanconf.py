#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Leonardo Giordani"
SITENAME = "The Babel Cat"
SITESUBTITLE = "Avventure di un povero gatto in un mondo multilingue"
SITEURL = ""
DEBUG = True

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "it"
LOCALE = "it_IT.utf8"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

SITEMAP = {
    "format": "xml",
}

DEFAULT_PAGINATION = 10

THEME = "../webmag"

STATIC_PATHS = ["images"]


def index_category(categories, category):
    category_names = [c[0].name for c in categories]

    # Index in loops starts from 1 - Argh!
    return category_names.index(category) + 1


def articles_category(categories, category):
    d = dict((cat.name, len(articles)) for cat, articles in categories)
    return d[category]


JINJA_FILTERS = {
    "index_category": index_category,
    "articles_category": articles_category,
}

MAU = {
    "custom_templates": {
        "content_image.html": (
            "<figure>"
            '<img {% if alt_text %} alt="{{ alt_text }}"{% endif %} src="{{ uri }}">'
            "<figcaption>{% if title %}{{ title }}{% endif %}</figcaption>"
            "</figure>"
        ),
        "block-quote.html": (
            "<blockquote>"
            "{{ content }}"
            "{% if secondary_content %}<cite>{{ secondary_content }}</cite>{% endif %}"
            "</blockquote>"
        ),
    }
}
