#!/usr/bin/env  python

__license__   = 'GPL v3'
__copyright__ = '2010, Ismael Mejia <iemejia at gmail.com>'
'''
eltiempo.com
'''

from calibre import strftime
from calibre.web.feeds.news import BasicNewsRecipe

class ElTiempo(BasicNewsRecipe):
    title                 = u'El Tiempo'
    __author__            = 'Ismael Mejia'
    description           = 'El Tiempo'
    oldest_article        = 7
    max_articles_per_feed = 100
    feeds          = [
        (u'El Tiempo (colombia)', u'http://www.eltiempo.com/home/rss.xml')
        ]
