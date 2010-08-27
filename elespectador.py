#!/usr/bin/env  python

__license__   = 'GPL v3'
__copyright__ = '2010, Ismael Mejia <iemejia at gmail.com>'
'''
elespectador.com
'''

from calibre import strftime
from calibre.web.feeds.news import BasicNewsRecipe

class ElEspectador(BasicNewsRecipe):
    title                 = u'El Espectador'
    __author__            = 'Ismael Mejia'
    description           = 'El Espectador'
    oldest_article        = 7
    max_articles_per_feed = 100
    feeds          = [
        (u'El Espectador', u'http://www.elespectador.com/rss.xml'),
        (u'Pol\xeditica', u'http://www.elespectador.com/noticias/politica/feed'),
        (u'Judicial', u'http://www.elespectador.com/noticias/judicial/feed'),
        (u'Paz', u'http://www.elespectador.com/noticias/paz/feed'),
        (u'Investigaci\xf3n', u'http://www.elespectador.com/noticias/investigacion/feed'),
        (u'Soy periodista', u'http://www.elespectador.com/noticias/soyperiodista/feed'),
        (u'Educaci\xf3n', u'http://www.elespectador.com/noticias/educacion/feed'),
        (u'Salud', u'http://www.elespectador.com/noticias/salud/feed'),
        (u'El Mundo', u'http://www.elespectador.com/noticias/elmundo/feed'),
        (u'Nacional', u'http://www.elespectador.com/noticias/nacional/feed'),
        (u'Bogot\xe1', u'ahttp://www.elespectador.com/noticias/bogota/feed'),
        (u'Actualidad', u'http://www.elespectador.com/noticias/actualidad/feed'),
        (u'Opini\xf3n', u'http://www.elespectador.com/opinion/feed'),
        (u'Deportes', u'http://www.elespectador.com/deportes/feed')
        ]
