#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marcos Dias'
SITENAME = 'Marcos Dias'
SITEURL = ''
ALT_NAME = "#! " + SITENAME
SITESUBTITLE = "Blog sobre tecnologias e afins"
DESCRIPTION = "Um blog sobre tecnologias, e afins."
# SITEURL = 'http://marcosdias.github.io/blog/'
#FAVICON = 'favicon.ico'
#FAVICON_TYPE = 'image/vnd.microsoft.icon'

#META_IMAGE = SITEURL + "/static/img/og_logo.jpg"
#META_IMAGE_TYPE = "image/jpeg"

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'
LOCALE = 'pt_br'

THEME = 'pelican-mg'

SHARE = True

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
SOCIAL = (
    ('github', 'https://github.com/marcosdias'),
    ('linkedin', 'https://br.linkedin.com/pub/marcos-dias/78/190/773'),
    ('envelope', 'mailto:marcos.a.melo.dias@gmail.com'),
)

DEFAULT_PAGINATION = 10

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
